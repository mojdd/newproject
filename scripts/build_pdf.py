#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""يبني نسخة PDF من القصة، مناسبة للقراءة على الموبايل (صفحة ضيّقة، خط كبير، RTL)."""
import re, markdown
from weasyprint import HTML

import sys
SRC = sys.argv[1] if len(sys.argv) > 1 else "/home/user/newproject/القصة.md"
OUT = sys.argv[2] if len(sys.argv) > 2 else SRC.rsplit(".", 1)[0] + ".pdf"

with open(SRC, encoding="utf-8") as f:
    md = f.read()

# نشيل أي تعليقات HTML مخبّأة
md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)

body_html = markdown.markdown(
    md,
    extensions=["tables", "fenced_code", "sane_lists"],
)

CSS = """
@page {
  size: 108mm 176mm;            /* صفحة ضيّقة بنسبة الموبايل تقريباً */
  margin: 11mm 9mm 13mm 9mm;
  @bottom-center {
    content: counter(page);
    font-family: "Noto Naskh Arabic";
    font-size: 9pt; color: #9a8c7a;
  }
}
html { direction: rtl; }
body {
  direction: rtl;
  font-family: "Noto Naskh Arabic", "Amiri", "Noto Color Emoji", sans-serif;
  font-size: 12.5pt;
  line-height: 1.95;
  color: #2b2b2b;
  text-align: right;
  hyphens: none;
  word-spacing: 0.02em;
}

/* العنوان الأول = غلاف الكتاب */
h1:first-of-type {
  break-before: avoid;
  break-after: page;
  margin-top: 34mm;
  text-align: center;
  font-family: "Noto Kufi Arabic", "Amiri", sans-serif;
  font-size: 27pt;
  line-height: 1.4;
  color: #6b4f9e;
  border: none;
}

/* بقية عناوين الفصول تبدأ بصفحة جديدة */
h1 {
  break-before: page;
  font-family: "Noto Kufi Arabic", "Amiri", sans-serif;
  font-size: 18pt;
  color: #6b4f9e;
  margin: 6mm 0 4mm 0;
  padding-bottom: 2mm;
  border-bottom: 2px solid #d9cdf0;
  line-height: 1.4;
}
h2 {
  font-family: "Noto Kufi Arabic", "Amiri", sans-serif;
  font-size: 14.5pt; color: #2e7d6b;
  margin: 5mm 0 2.5mm 0; line-height: 1.4;
}
h3 {
  font-size: 12.8pt; color: #b5651d; font-weight: 700;
  margin: 4mm 0 2mm 0; line-height: 1.4;
}
p { margin: 0 0 2.6mm 0; }

blockquote {
  margin: 3mm 0; padding: 2.5mm 4mm;
  border-right: 4px solid #c8b6ec;
  background: #f6f2fc;
  border-radius: 5px;
  color: #4a4458;
}
blockquote p { margin: 1mm 0; }

ul, ol { margin: 1mm 6mm 3mm 0; padding: 0 4mm 0 0; }
li { margin: 0.8mm 0; }

strong { color: #1f1f1f; font-weight: 700; }

hr {
  border: none; height: 0; margin: 5mm auto;
  border-top: 1.5px dashed #d3c7b6; width: 60%;
}

table {
  width: 100%; border-collapse: collapse; margin: 3mm 0;
  font-size: 10.5pt; line-height: 1.5;
}
th, td {
  border: 1px solid #d8cfc2; padding: 1.8mm 2mm; text-align: right;
  vertical-align: top;
}
th { background: #efe7da; color: #5a4a33; font-weight: 700; }
tr:nth-child(even) td { background: #faf7f1; }

code {
  font-family: "DejaVu Sans Mono", monospace;
  background: #f0eef4; padding: 0.3mm 1mm; border-radius: 3px;
  font-size: 9.5pt; direction: ltr; unicode-bidi: embed;
}
pre {
  background: #f4f2f7; border: 1px solid #e0dae9; border-radius: 6px;
  padding: 2.5mm 3mm; margin: 2.5mm 0;
  direction: ltr; text-align: left;
  white-space: pre-wrap;        /* لفّ الأسطر الطويلة بدل قطعها */
  word-break: break-word;
  overflow-wrap: anywhere;
}
pre code { background: none; font-size: 8.4pt; line-height: 1.5; }

a { color: #6b4f9e; text-decoration: none; }
"""

full_html = f"""<!DOCTYPE html><html lang="ar" dir="rtl"><head>
<meta charset="utf-8"><style>{CSS}</style></head>
<body>{body_html}</body></html>"""

HTML(string=full_html, base_url="/home/user/newproject/").write_pdf(OUT)

import os
size = os.path.getsize(OUT)
print(f"تمّ: {OUT}  ({size/1024:.0f} KB)")
