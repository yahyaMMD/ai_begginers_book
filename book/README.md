# The Complete Beginner's Guide to Artificial Intelligence

A print-ready HTML/CSS handbook (160 × 220 mm trim) for absolute beginners.

## Files

| File | Description |
|------|-------------|
| `book/ai-beginners-handbook.html` | Full book — open in a browser and Print → Save as PDF |
| `book/ai-beginners-handbook.pdf` | Exported sample PDF (≈60–80 pages) |
| `scripts/generate_book.py` | Generator for the HTML handbook |
| `scripts/expansions.py` | Extra chapter content modules |

## Print settings

- **Trim size:** 160 mm × 220 mm
- **Margins:** 14 mm top/bottom, 16 mm left/right (CSS `@page`)
- **Target length:** 60–80 pages (never exceed 80)

### Export PDF from the browser

1. Open `book/ai-beginners-handbook.html` in Chrome.
2. Print → Destination: Save as PDF.
3. Enable **Background graphics**.
4. Margins: Default (CSS defines page size).
5. Paper size: custom 160×220 mm if offered; otherwise CSS `@page` size applies in Chromium.

### Regenerate

```bash
cd scripts && python3 generate_book.py
```

## Contents (30 chapters)

1. AI fundamentals & how modern AI works  
2. Tool categories across the ecosystem  
3. ChatGPT, Claude, Gemini, Perplexity, NotebookLM  
4. Prompt engineering + professional prompt library  
5. Image, video, and audio generation  
6. Productivity, automation (n8n / Make / Zapier), agents  
7. 20 real-world projects + career roadmap  

## Design

Teal professional handbook styling with IBM Plex typography, callout boxes, tables, workflows, exercises, and print-optimized layout.
