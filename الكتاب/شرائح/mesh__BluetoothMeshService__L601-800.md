# شريحة — app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt (الأسطر 601–800)

```
601:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:601]

```
602:                // Verbose debug: device connected
```
> تعليق: تنقيح مُفصَّل: الجهاز متّصل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:602]

```
603:                try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:603]

```
604:                    val addr = device.address
```
> يُعرِّف متغيّراً ثابتاً اسمه العنوان (addr) ويضبطه بقيمة الخاصية address من الجهاز (device). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:604]

```
605:                    val peer = connectionManager.addressPeerMap[addr]
```
> يُعرِّف متغيّراً ثابتاً اسمه النظير (peer) ويضبطه بقيمة خريطة عنوان-نظير (addressPeerMap) من مدير الاتصال (connectionManager) عند المفتاح addr. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:605]

```
606:                    val nick = peer?.let { peerManager.getPeerNickname(it) } ?: "unknown"
```
> يُعرِّف متغيّراً ثابتاً اسمه الكُنية (nick) ويضبطه بنتيجة استدعاء getPeerNickname من مدير النظراء (peerManager) على peer إن لم يكن فارغاً، وإلا بالقيمة "unknown". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:606]

```
607:                    com.bitchat.android.ui.debug.DebugSettingsManager.getInstance()
```
> يستدعي getInstance من مدير إعدادات التنقيح (DebugSettingsManager) للحصول على نسخته الوحيدة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:607]

```
608:                        .logPeerConnection(peer ?: "unknown", nick, addr, isInbound = !connectionManager.isClientConnection(addr)!!)
```
> يستدعي logPeerConnection (تسجيل اتصال نظير) بالوسائط: peer أو "unknown"، وnick، وaddr، وisInbound مضبوطة بنفي نتيجة isClientConnection من connectionManager على addr (مع تأكيد عدم الفراغ بـ!!). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:608]

```
609:                } catch (_: Exception) { }
```
> يلتقط أي استثناء (Exception) ويتجاهله بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:609]

```
610:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:610]

```
611:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:611]

```
612:            override fun onDeviceDisconnected(device: android.bluetooth.BluetoothDevice) {
```
> يُعيد تعريف (override) الدالة onDeviceDisconnected (عند انفصال الجهاز) التي تأخذ وسيطاً device من نوع BluetoothDevice. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:612]

```
613:                Log.d(TAG, "Device disconnected: ${device.address}")
```
> يستدعي Log.d لتسجيل رسالة تنقيح نصّها "Device disconnected: " متبوعاً بقيمة device.address، تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:613]

```
614:                val addr = device.address
```
> يُعرِّف متغيّراً ثابتاً اسمه addr ويضبطه بقيمة device.address. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:614]

```
615:                // Remove mapping and, if that was the last direct path for the peer, clear direct flag
```
> تعليق: أزِل التعيين، وإن كان ذلك آخر مسار مباشر للنظير فامسح علم المباشرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:615]

```
616:                val peer = connectionManager.addressPeerMap[addr]
```
> يُعرِّف متغيّراً ثابتاً اسمه peer ويضبطه بقيمة addressPeerMap من connectionManager عند المفتاح addr. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:616]

```
617:                // ConnectionTracker has already removed the address mapping; be defensive either way
```
> تعليق: متتبّع الاتصال (ConnectionTracker) أزال تعيين العنوان بالفعل؛ توقَّ احتياطاً على أي حال. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:617]

```
618:                connectionManager.addressPeerMap.remove(addr)
```
> يستدعي remove على addressPeerMap من connectionManager لحذف المدخلة عند المفتاح addr. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:618]

```
619:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:619]

```
620:                // refresh peer list on disconnect. 
```
> تعليق: حدِّث قائمة النظراء عند الانفصال. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:620]

```
621:                try { peerManager.refreshPeerList() } catch (_: Exception) { }
```
> يحاول استدعاء refreshPeerList (تحديث قائمة النظراء) من peerManager، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:621]

```
622:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:622]

```
623:                if (peer != null) {
```
> يبدأ شرطاً يتحقق أن peer ليس فارغاً (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:623]

```
624:                    // Verbose debug: device disconnected
```
> تعليق: تنقيح مُفصَّل: الجهاز انفصل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:624]

```
625:                    try {
```
> يبدأ كتلة محاولة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:625]

```
626:                        val nick = peerManager.getPeerNickname(peer) ?: "unknown"
```
> يُعرِّف متغيّراً ثابتاً اسمه nick ويضبطه بنتيجة getPeerNickname من peerManager على peer، وإلا بالقيمة "unknown". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:626]

```
627:                        com.bitchat.android.ui.debug.DebugSettingsManager.getInstance()
```
> يستدعي getInstance من DebugSettingsManager للحصول على نسخته الوحيدة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:627]

```
628:                            .logPeerDisconnection(peer, nick, addr)
```
> يستدعي logPeerDisconnection (تسجيل انفصال نظير) بالوسائط peer وnick وaddr. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:628]

```
629:                    } catch (_: Exception) { }
```
> يلتقط أي استثناء ويتجاهله بجسم فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:629]

```
630:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:630]

```
631:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:631]

```
632:            
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:632]

```
633:            override fun onRSSIUpdated(deviceAddress: String, rssi: Int) {
```
> يُعيد تعريف الدالة onRSSIUpdated (عند تحديث قوة الإشارة RSSI) التي تأخذ وسيطاً deviceAddress من نوع نص (String) وrssi من نوع عدد صحيح (Int). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:633]

```
634:                // Find the peer ID for this device address and update RSSI in PeerManager
```
> تعليق: اعثر على معرّف النظير لعنوان الجهاز هذا وحدِّث قوة الإشارة في مدير النظراء. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:634]

```
635:                connectionManager.addressPeerMap[deviceAddress]?.let { peerID ->
```
> يجلب قيمة addressPeerMap من connectionManager عند المفتاح deviceAddress، وإن لم تكن فارغة ينفّذ كتلة let مع تسميتها peerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:635]

```
636:                    peerManager.updatePeerRSSI(peerID, rssi)
```
> يستدعي updatePeerRSSI (تحديث قوة إشارة النظير) من peerManager بالوسيطين peerID وrssi. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:636]

```
637:                }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:637]

```
638:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:638]

```
639:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:639]

```
640:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:640]

```
641:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:641]

```
642:    /**
```
> يبدأ تعليقاً توثيقياً (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:642]

```
643:     * Start the mesh service
```
> تعليق: ابدأ خدمة الشبكة المتشابكة (mesh). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:643]

```
644:     */
```
> يُغلق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:644]

```
645:    fun startServices() {
```
> يُعرِّف الدالة startServices (بدء الخدمات) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:645]

```
646:        // Prevent double starts (defensive programming)
```
> تعليق: امنع البدء المزدوج (برمجة احتياطية). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:646]

```
647:        if (isActive) {
```
> يبدأ شرطاً يتحقق أن العلم isActive (نشط) صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:647]

```
648:            Log.w(TAG, "Mesh service already active, ignoring duplicate start request")
```
> يستدعي Log.w لتسجيل تحذير نصّه "Mesh service already active, ignoring duplicate start request" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:648]

```
649:            return
```
> يُعيد (خروج) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:649]

```
650:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:650]

```
651:        if (!isBleTransportEnabled()) {
```
> يبدأ شرطاً يتحقق أن نتيجة isBleTransportEnabled (هل نقل BLE مُفعَّل) غير صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:651]

```
652:            Log.i(TAG, "BLE transport disabled by debug settings; not starting mesh service")
```
> يستدعي Log.i لتسجيل معلومة نصّها "BLE transport disabled by debug settings; not starting mesh service" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:652]

```
653:            connectionManager.disableTransport()
```
> يستدعي disableTransport (تعطيل النقل) من connectionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:653]

```
654:            TransportBridgeService.unregister("BLE")
```
> يستدعي unregister (إلغاء التسجيل) من خدمة جسر النقل (TransportBridgeService) بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:654]

```
655:            com.bitchat.android.service.MeshServiceHolder.stopSharedGossip("BLE")
```
> يستدعي stopSharedGossip (إيقاف الإشاعة المشتركة) من حامل خدمة الشبكة (MeshServiceHolder) بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:655]

```
656:            try { com.bitchat.android.services.AppStateStore.clearTransportPeers("BLE") } catch (_: Exception) { }
```
> يحاول استدعاء clearTransportPeers (مسح نظراء النقل) من مخزن حالة التطبيق (AppStateStore) بالوسيط "BLE"، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:656]

```
657:            try { com.bitchat.android.services.AppStateStore.clearTransportDirectPeers("BLE") } catch (_: Exception) { }
```
> يحاول استدعاء clearTransportDirectPeers (مسح نظراء النقل المباشرين) من AppStateStore بالوسيط "BLE"، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:657]

```
658:            return
```
> يُعيد (خروج) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:658]

```
659:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:659]

```
660:        if (terminated) {
```
> يبدأ شرطاً يتحقق أن العلم terminated (مُنهًى) صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:660]

```
661:            // This instance's scope was cancelled previously; refuse to start to avoid using dead scopes.
```
> تعليق: نطاق هذه النسخة أُلغي سابقاً؛ ارفض البدء لتجنّب استخدام نطاقات ميتة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:661]

```
662:            Log.e(TAG, "Mesh service instance was terminated; create a new instance instead of restarting")
```
> يستدعي Log.e لتسجيل خطأ نصّه "Mesh service instance was terminated; create a new instance instead of restarting" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:662]

```
663:            return
```
> يُعيد (خروج) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:663]

```
664:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:664]

```
665:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:665]

```
666:        Log.i(TAG, "Starting Bluetooth mesh service with peer ID: $myPeerID")
```
> يستدعي Log.i لتسجيل معلومة نصّها "Starting Bluetooth mesh service with peer ID: " متبوعاً بقيمة myPeerID (معرّفي كنظير) تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:666]

```
667:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:667]

```
668:        if (connectionManager.startServices()) {
```
> يبدأ شرطاً يتحقق أن نتيجة startServices من connectionManager صحيحة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:668]

```
669:            isActive = true
```
> يضبط العلم isActive بالقيمة صحيح (true). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:669]

```
670:            TransportBridgeService.register("BLE", this)
```
> يستدعي register (تسجيل) من TransportBridgeService بالوسيطين "BLE" وthis (هذه النسخة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:670]

```
671:            
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:671]

```
672:            // Start periodic announcements for peer discovery and connectivity
```
> تعليق: ابدأ إعلانات دورية لاكتشاف النظراء والاتصالية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:672]

```
673:            sendPeriodicBroadcastAnnounce()
```
> يستدعي sendPeriodicBroadcastAnnounce (إرسال إعلان بثّي دوري). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:673]

```
674:            Log.d(TAG, "Started periodic broadcast announcements (every 30 seconds)")
```
> يستدعي Log.d لتسجيل رسالة تنقيح نصّها "Started periodic broadcast announcements (every 30 seconds)" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:674]

```
675:            // Start periodic syncs
```
> تعليق: ابدأ مزامنات دورية. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:675]

```
676:            com.bitchat.android.service.MeshServiceHolder.startSharedGossip("BLE")
```
> يستدعي startSharedGossip (بدء الإشاعة المشتركة) من MeshServiceHolder بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:676]

```
677:            Log.d(TAG, "GossipSyncManager started")
```
> يستدعي Log.d لتسجيل رسالة تنقيح نصّها "GossipSyncManager started" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:677]

```
678:        } else {
```
> يبدأ فرع وإلا (else). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:678]

```
679:            Log.e(TAG, "Failed to start Bluetooth services")
```
> يستدعي Log.e لتسجيل خطأ نصّه "Failed to start Bluetooth services" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:679]

```
680:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:680]

```
681:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:681]

```
682:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:682]

```
683:    /**
```
> يبدأ تعليقاً توثيقياً (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:683]

```
684:     * Apply the debug master transport toggle without destroying this mesh instance.
```
> تعليق: طبّق مفتاح تبديل النقل الرئيسي للتنقيح دون تدمير نسخة الشبكة هذه. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:684]

```
685:     */
```
> يُغلق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:685]

```
686:    fun setBleTransportEnabled(enabled: Boolean) {
```
> يُعرِّف الدالة setBleTransportEnabled (ضبط تفعيل نقل BLE) التي تأخذ وسيطاً enabled من نوع منطقي (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:686]

```
687:        if (enabled) {
```
> يبدأ شرطاً يتحقق أن enabled صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:687]

```
688:            startServices()
```
> يستدعي startServices. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:688]

```
689:        } else {
```
> يبدأ فرع وإلا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:689]

```
690:            pauseServicesForTransportDisable()
```
> يستدعي pauseServicesForTransportDisable (إيقاف الخدمات مؤقتاً لتعطيل النقل). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:690]

```
691:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:691]

```
692:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:692]

```
693:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:693]

```
694:    private fun pauseServicesForTransportDisable() {
```
> يُعرِّف دالة خاصة (private) اسمها pauseServicesForTransportDisable بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:694]

```
695:        Log.i(TAG, "Disabling BLE mesh transport")
```
> يستدعي Log.i لتسجيل معلومة نصّها "Disabling BLE mesh transport" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:695]

```
696:        isActive = false
```
> يضبط العلم isActive بالقيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:696]

```
697:        announceJob?.cancel()
```
> يستدعي cancel (إلغاء) على مهمّة الإعلان (announceJob) إن لم تكن فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:697]

```
698:        announceJob = null
```
> يضبط announceJob بالقيمة فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:698]

```
699:        com.bitchat.android.service.MeshServiceHolder.stopSharedGossip("BLE")
```
> يستدعي stopSharedGossip من MeshServiceHolder بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:699]

```
700:        TransportBridgeService.unregister("BLE")
```
> يستدعي unregister من TransportBridgeService بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:700]

```
701:        try { com.bitchat.android.services.AppStateStore.clearTransportPeers("BLE") } catch (_: Exception) { }
```
> يحاول استدعاء clearTransportPeers من AppStateStore بالوسيط "BLE"، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:701]

```
702:        try { com.bitchat.android.services.AppStateStore.clearTransportDirectPeers("BLE") } catch (_: Exception) { }
```
> يحاول استدعاء clearTransportDirectPeers من AppStateStore بالوسيط "BLE"، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:702]

```
703:        connectionManager.disableTransport()
```
> يستدعي disableTransport من connectionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:703]

```
704:        try { peerManager.refreshPeerList() } catch (_: Exception) { }
```
> يحاول استدعاء refreshPeerList من peerManager، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:704]

```
705:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:705]

```
706:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:706]

```
707:    /**
```
> يبدأ تعليقاً توثيقياً (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:707]

```
708:     * Stop all mesh services
```
> تعليق: أوقِف كل خدمات الشبكة المتشابكة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:708]

```
709:     */
```
> يُغلق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:709]

```
710:    fun stopServices() {
```
> يُعرِّف الدالة stopServices (إيقاف الخدمات) بلا وسائط. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:710]

```
711:        if (!isActive) {
```
> يبدأ شرطاً يتحقق أن isActive غير صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:711]

```
712:            Log.w(TAG, "Mesh service not active, ignoring stop request")
```
> يستدعي Log.w لتسجيل تحذير نصّه "Mesh service not active, ignoring stop request" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:712]

```
713:            return
```
> يُعيد (خروج) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:713]

```
714:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:714]

```
715:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:715]

```
716:        Log.i(TAG, "Stopping Bluetooth mesh service")
```
> يستدعي Log.i لتسجيل معلومة نصّها "Stopping Bluetooth mesh service" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:716]

```
717:        isActive = false
```
> يضبط العلم isActive بالقيمة خطأ (false). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:717]

```
718:        announceJob?.cancel()
```
> يستدعي cancel على announceJob إن لم تكن فارغة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:718]

```
719:        announceJob = null
```
> يضبط announceJob بالقيمة فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:719]

```
720:        TransportBridgeService.unregister("BLE")
```
> يستدعي unregister من TransportBridgeService بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:720]

```
721:        try { com.bitchat.android.services.AppStateStore.clearTransportPeers("BLE") } catch (_: Exception) { }
```
> يحاول استدعاء clearTransportPeers من AppStateStore بالوسيط "BLE"، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:721]

```
722:        try { com.bitchat.android.services.AppStateStore.clearTransportDirectPeers("BLE") } catch (_: Exception) { }
```
> يحاول استدعاء clearTransportDirectPeers من AppStateStore بالوسيط "BLE"، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:722]

```
723:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:723]

```
724:        // Send leave announcement
```
> تعليق: أرسِل إعلان مغادرة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:724]

```
725:        sendLeaveAnnouncement()
```
> يستدعي sendLeaveAnnouncement (إرسال إعلان المغادرة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:725]

```
726:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:726]

```
727:        serviceScope.launch {
```
> يطلق متعاوناً (coroutine) على نطاق الخدمة (serviceScope) عبر launch. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:727]

```
728:            Log.d(TAG, "Stopping subcomponents and cancelling scope...")
```
> يستدعي Log.d لتسجيل رسالة تنقيح نصّها "Stopping subcomponents and cancelling scope..." تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:728]

```
729:            delay(200) // Give leave message time to send
```
> يستدعي delay (تأخير) بمقدار 200 (ملّي ثانية)، مع تعليق: أعطِ رسالة المغادرة وقتاً لتُرسَل. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:729]

```
730:            
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:730]

```
731:            // Stop all components
```
> تعليق: أوقِف كل المكوّنات. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:731]

```
732:            com.bitchat.android.service.MeshServiceHolder.stopSharedGossip("BLE")
```
> يستدعي stopSharedGossip من MeshServiceHolder بالوسيط "BLE". [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:732]

```
733:            Log.d(TAG, "GossipSyncManager stopped")
```
> يستدعي Log.d لتسجيل رسالة تنقيح نصّها "GossipSyncManager stopped" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:733]

```
734:            connectionManager.stopServices()
```
> يستدعي stopServices (إيقاف الخدمات) من connectionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:734]

```
735:            Log.d(TAG, "BluetoothConnectionManager stop requested")
```
> يستدعي Log.d لتسجيل رسالة تنقيح نصّها "BluetoothConnectionManager stop requested" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:735]

```
736:            peerManager.shutdown()
```
> يستدعي shutdown (إغلاق) من peerManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:736]

```
737:            fragmentManager.shutdown()
```
> يستدعي shutdown من مدير التجزئة (fragmentManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:737]

```
738:            securityManager.shutdown()
```
> يستدعي shutdown من مدير الأمان (securityManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:738]

```
739:            storeForwardManager.shutdown()
```
> يستدعي shutdown من مدير التخزين والتمرير (storeForwardManager). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:739]

```
740:            messageHandler.shutdown()
```
> يستدعي shutdown من معالج الرسائل (messageHandler). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:740]

```
741:            packetProcessor.shutdown()
```
> يستدعي shutdown من معالج الحزم (packetProcessor). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:741]

```
742:            
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:742]

```
743:            // Mark this instance as terminated and cancel its scope so it won't be reused
```
> تعليق: علِّم هذه النسخة كمُنهاة وألغِ نطاقها لئلّا يُعاد استخدامها. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:743]

```
744:            terminated = true
```
> يضبط العلم terminated بالقيمة صحيح (true). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:744]

```
745:            serviceScope.cancel()
```
> يستدعي cancel (إلغاء) على serviceScope. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:745]

```
746:            Log.i(TAG, "BluetoothMeshService terminated and scope cancelled")
```
> يستدعي Log.i لتسجيل معلومة نصّها "BluetoothMeshService terminated and scope cancelled" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:746]

```
747:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:747]

```
748:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:748]

```
749:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:749]

```
750:    /**
```
> يبدأ تعليقاً توثيقياً (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:750]

```
751:     * Whether this instance can be safely reused. Returns false after stopServices() or if
```
> تعليق: هل يمكن إعادة استخدام هذه النسخة بأمان. يُعيد خطأ بعد stopServices() أو إذا. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:751]

```
752:     * any critical internal scope has been cancelled.
```
> تعليق: أُلغي أي نطاق داخلي حرِج. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:752]

```
753:     */
```
> يُغلق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:753]

```
754:    fun isReusable(): Boolean {
```
> يُعرِّف الدالة isReusable (هل قابلة لإعادة الاستخدام) التي تُعيد قيمة منطقية (Boolean). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:754]

```
755:        val reusable = !terminated && serviceScope.isActive && connectionManager.isReusable()
```
> يُعرِّف متغيّراً ثابتاً اسمه reusable (قابلة للإعادة) ويضبطه بالتقارن المنطقي: نفي terminated، وكون serviceScope نشطاً (isActive)، ونتيجة isReusable من connectionManager. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:755]

```
756:        if (!reusable) {
```
> يبدأ شرطاً يتحقق أن reusable غير صحيح. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:756]

```
757:            Log.d(TAG, "isReusable=false (terminated=$terminated, scopeActive=${serviceScope.isActive}, connReusable=${connectionManager.isReusable()})")
```
> يستدعي Log.d لتسجيل رسالة تنقيح تعرض قيم terminated وserviceScope.isActive ونتيجة connectionManager.isReusable() تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:757]

```
758:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:758]

```
759:        return reusable
```
> يُعيد قيمة المتغيّر reusable. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:759]

```
760:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:760]

```
761:    
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:761]

```
762:    /**
```
> يبدأ تعليقاً توثيقياً (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:762]

```
763:     * Send public message
```
> تعليق: أرسِل رسالة عامّة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:763]

```
764:     */
```
> يُغلق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:764]

```
765:    fun sendMessage(content: String, mentions: List<String> = emptyList(), channel: String? = null) {
```
> يُعرِّف الدالة sendMessage (إرسال رسالة) التي تأخذ content من نوع نص (String)، وmentions (إشارات) من نوع قائمة نصوص بقيمة افتراضية قائمة فارغة، وchannel (قناة) من نوع نص قابل للفراغ بقيمة افتراضية فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:765]

```
766:        if (content.isEmpty()) return
```
> إذا كان content فارغاً (isEmpty) يُعيد (خروج) من الدالة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:766]

```
767:        
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:767]

```
768:        serviceScope.launch {
```
> يطلق متعاوناً على serviceScope عبر launch. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:768]

```
769:            val packet = BitchatPacket(
```
> يُعرِّف متغيّراً ثابتاً اسمه packet (حزمة) ويضبطه بإنشاء كائن BitchatPacket (حزمة بِتشات). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:769]

```
770:                version = 1u,
```
> يضبط الوسيط version (الإصدار) بالقيمة 1 غير مُوقَّعة (1u). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:770]

```
771:                type = MessageType.MESSAGE.value,
```
> يضبط الوسيط type (النوع) بقيمة value من نوع الرسالة MessageType.MESSAGE. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:771]

```
772:                senderID = hexStringToByteArray(myPeerID),
```
> يضبط الوسيط senderID (معرّف المُرسِل) بنتيجة hexStringToByteArray (تحويل النص السّتعشري إلى مصفوفة بايتات) على myPeerID. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:772]

```
773:                recipientID = SpecialRecipients.BROADCAST,
```
> يضبط الوسيط recipientID (معرّف المُستقبِل) بقيمة BROADCAST (بثّ) من المستقبِلين الخاصّين (SpecialRecipients). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:773]

```
774:                timestamp = System.currentTimeMillis().toULong(),
```
> يضبط الوسيط timestamp (الطابع الزمني) بقيمة الوقت الحالي بالملّي ثانية (System.currentTimeMillis) محوّلة إلى عدد طويل غير مُوقَّع (toULong). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:774]

```
775:                payload = content.toByteArray(Charsets.UTF_8),
```
> يضبط الوسيط payload (الحمولة) بتحويل content إلى مصفوفة بايتات (toByteArray) بترميز UTF-8. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:775]

```
776:                signature = null,
```
> يضبط الوسيط signature (التوقيع) بالقيمة فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:776]

```
777:                ttl = MAX_TTL
```
> يضبط الوسيط ttl (مدّة البقاء) بالقيمة MAX_TTL (أقصى مدّة بقاء). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:777]

```
778:            )
```
> إغلاق نطاق استدعاء المُنشئ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:778]

```
779:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:779]

```
780:            // Sign the packet before broadcasting
```
> تعليق: وقِّع الحزمة قبل البثّ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:780]

```
781:            val signedPacket = signPacketBeforeBroadcast(packet)
```
> يُعرِّف متغيّراً ثابتاً اسمه signedPacket (الحزمة المُوقَّعة) ويضبطه بنتيجة signPacketBeforeBroadcast (توقيع الحزمة قبل البثّ) على packet. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:781]

```
782:            broadcastRoutedPacket(RoutedPacket(signedPacket))
```
> يستدعي broadcastRoutedPacket (بثّ حزمة مُوجَّهة) بوسيط كائن RoutedPacket (حزمة مُوجَّهة) مُنشأ من signedPacket. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:782]

```
783:            // Track our own broadcast message for sync
```
> تعليق: تتبَّع رسالتنا البثّية الخاصّة للمزامنة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:783]

```
784:            try { gossipSyncManager.onPublicPacketSeen(signedPacket) } catch (_: Exception) { }
```
> يحاول استدعاء onPublicPacketSeen (عند رؤية حزمة عامّة) من مدير مزامنة الإشاعة (gossipSyncManager) على signedPacket، ويلتقط أي استثناء ويتجاهله. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:784]

```
785:        }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:785]

```
786:    }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:786]

```
787:
```
> سطر فارغ. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:787]

```
788:    /**
```
> يبدأ تعليقاً توثيقياً (KDoc). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:788]

```
789:     * Send a file over mesh as a broadcast MESSAGE (public mesh timeline/channels).
```
> تعليق: أرسِل ملفاً عبر الشبكة كرسالة بثّية MESSAGE (خط زمن/قنوات الشبكة العامّة). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:789]

```
790:     */
```
> يُغلق التعليق التوثيقي. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:790]

```
791:    fun sendFileBroadcast(file: com.bitchat.android.model.BitchatFilePacket) {
```
> يُعرِّف الدالة sendFileBroadcast (إرسال بثّ ملف) التي تأخذ وسيطاً file من نوع BitchatFilePacket (حزمة ملف بِتشات). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:791]

```
792:        try {
```
> يبدأ كتلة محاولة (try). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:792]

```
793:            Log.d(TAG, "📤 sendFileBroadcast: name=${file.fileName}, size=${file.fileSize}")
```
> يستدعي Log.d لتسجيل رسالة تنقيح تعرض اسم الملف (file.fileName) وحجمه (file.fileSize) تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:793]

```
794:            val payload = file.encode()
```
> يُعرِّف متغيّراً ثابتاً اسمه payload (الحمولة) ويضبطه بنتيجة encode (ترميز) من file. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:794]

```
795:            if (payload == null) {
```
> يبدأ شرطاً يتحقق أن payload فارغ (null). [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:795]

```
796:                Log.e(TAG, "❌ Failed to encode file packet in sendFileBroadcast")
```
> يستدعي Log.e لتسجيل خطأ نصّه "❌ Failed to encode file packet in sendFileBroadcast" تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:796]

```
797:                return
```
> يُعيد (خروج) من الدالة بلا قيمة. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:797]

```
798:            }
```
> إغلاق نطاق. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:798]

```
799:            Log.d(TAG, "📦 Encoded payload: ${payload.size} bytes")
```
> يستدعي Log.d لتسجيل رسالة تنقيح تعرض حجم الحمولة المُرمَّزة (payload.size) بالبايتات تحت الوسم TAG. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:799]

```
800:        serviceScope.launch {
```
> يطلق متعاوناً على serviceScope عبر launch. [app/src/main/java/com/bitchat/android/mesh/BluetoothMeshService.kt:800]
