# الذكاء الاصطناعي للأطفال — SCHOOLERX

كتاب عربي بسيط جداً للأطفال (حوالي 8 سنوات).

## الملفات

- `ai-beginners-handbook.html` — الكتاب
- `ai-beginners-handbook.pdf` — PDF للطباعة (160×220 مم)
- `assets/cover.png` — الغلاف
- `assets/kids/` — صور تعليمية

## إعادة التوليد

```bash
cd scripts && python3 generate_book_kids.py
```

## المعاينة

```bash
cd book && python3 -m http.server 8765 --bind 0.0.0.0
```
