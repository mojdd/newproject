# 08 — نموذج البيانات (Data Model)

البنية المنطقية للكيانات وعلاقاتها. التنفيذ الفعلي عبر Room + SQLCipher
([وحش ٧](07-wolf-storage.md)).

## العلاقات

```
Identity (1) ────── يملك ──────> TrustedContact (N)
Message  (N) ────── له ────────> DeliveryReceipt (0..1)
Message  (N) ────── يُفهرَس في ─> SeenMessageCache
AggregateRecord (N) ── يُرفَع عبر ─> Gateway → Server
```

## الكيانات

### `Identity` (سجل واحد)
| الحقل | النوع | ملاحظة |
|-------|------|--------|
| `nodeId` | String (PK) | مشتق من المفتاح العام للتوقيع |
| `signPubKey` | ByteArray | Ed25519 عام |
| `signPrivEnc` | ByteArray | Ed25519 خاص **مشفّر** بمفتاح Keystore |
| `boxPubKey` | ByteArray | X25519 عام |
| `boxPrivEnc` | ByteArray | X25519 خاص **مشفّر** |
| `displayName` | String? | للموثوقين فقط |

### `TrustedContact`
| الحقل | النوع | ملاحظة |
|-------|------|--------|
| `nodeId` | String (PK) | معرّف الموثوق |
| `signPubKey` | ByteArray | للتحقق من توقيعه |
| `boxPubKey` | ByteArray | للتشفير إله (sealed box) |
| `displayName` | String | اسم ظاهر (من QR) |
| `addedAt` | Long | وقت الإضافة |

### `Message`
| الحقل | النوع | ملاحظة |
|-------|------|--------|
| `id` | String (PK) | `MessageId` (هاش فريد) |
| `type` | Int | BROADCAST / UNICAST / RECEIPT |
| `priority` | Int | NORMAL / EMERGENCY |
| `originNodeId` | String | المصدر |
| `destNodeId` | String? | الهدف (unicast) |
| `payload` | ByteArray | **مشفّر** للـ unicast |
| `signature` | ByteArray | Ed25519 للمصدر |
| `ttlHops` | Int | قفزات متبقية |
| `state` | Int | آلة الحالة ([وحش ٣](03-wolf-store-and-forward.md)) |
| `createdAt` | Long | |
| `expiresAt` | Long | 24–48h أو عند ACK |
| `lastRebroadcastAt` | Long | لجدولة إعادة البث |

### `SeenMessageCache`
| الحقل | النوع | ملاحظة |
|-------|------|--------|
| `messageId` | String (PK) | للـ dedup |
| `firstSeenAt` | Long | للتقليم حسب `SEEN_SET_TTL` |

> عملياً يُكمَّل بـ Bloom filter بالذاكرة للكفاءة ([وحش ٢](02-wolf-routing.md))؛
> الجدول للصمود عبر إعادة التشغيل.

### `AggregateRecord`
| الحقل | النوع | ملاحظة |
|-------|------|--------|
| `id` | String (PK) | MessageId (idempotency بالرفع) |
| `category` | Int | MEALS / WATER / TOILETS / MEDICAL / DENSITY / PROCESSION / SUPPLIER / FINANCE / HEALTH … |
| `axis` | String? | المحور/الموقع التقريبي (مكان، **مو شخص**) |
| `payload` | ByteArray | الحقول التجميعية (أرقام عن مكان/خدمة) |
| `uploadState` | Int | PENDING / UPLOADED |
| `createdAt` | Long | |

> ⚠️ `AggregateRecord` **عن مكان/خدمة/موكب فقط** — لا حقول تعرّف فرداً بالاسم.
> انظر [الخطوط الحمراء](10-red-lines.md).

### `DeliveryReceipt`
| الحقل | النوع | ملاحظة |
|-------|------|--------|
| `messageId` | String (PK) | الرزمة المؤكَّدة |
| `ackedBy` | String | nodeId الهدف أو السيرفر |
| `signature` | ByteArray | توقيع المؤكِّد |
| `kind` | Int | DELIVERED_PEER / UPLOADED_SERVER |
| `receivedAt` | Long | |

## ملاحظات

- كل البايتات الحساسة (المفاتيح الخاصة، payloads) **مشفّرة عند الراحة** عبر
  SQLCipher، والمفاتيح الخاصة **مشفّرة مرتين** (طبقة Keystore فوق).
- الـ enums تُخزَّن كـ Int للاستقرار عبر الإصدارات (مع توثيق القيم).
