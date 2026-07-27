#!/bin/bash
set -euo pipefail
OUT=/workspace/book/ai-beginners-handbook.pdf
PREVIEW=/workspace/book/preview.pdf
HTML=file:///workspace/book/ai-beginners-handbook.html
rm -f "$OUT" "$PREVIEW"
google-chrome --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$OUT" "$HTML"
cp "$OUT" "$PREVIEW"
python3 - <<'PY'
from pypdf import PdfReader
r = PdfReader('/workspace/book/ai-beginners-handbook.pdf')
print('pages', len(r.pages))
print('size', r.pages[0].mediabox)
for i in [0, 1, 2, 3, 10, 30]:
    if i < len(r.pages):
        t = (r.pages[i].extract_text() or '').strip().replace('\n', ' | ')
        print(f'p{i+1} ({len(t)}c):', t[:240])
PY
