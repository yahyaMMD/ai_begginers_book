#!/usr/bin/env python3
"""Generate The Complete Beginner's Guide to Artificial Intelligence (HTML handbook)."""

from pathlib import Path

from expansions import CSS_FIXES, EXPANSIONS

OUT = Path("/workspace/book/ai-beginners-handbook.html")

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  --ink: #1a2332;
  --muted: #4a5568;
  --rule: #d0d7e2;
  --accent: #0d7377;
  --accent-dark: #095456;
  --accent-soft: #e6f4f4;
  --warm: #c45c26;
  --warm-soft: #fdf0e9;
  --warn: #9a3412;
  --warn-soft: #fff7ed;
  --tip: #0f766e;
  --tip-soft: #ecfdf5;
  --ex: #1e3a5f;
  --ex-soft: #eef4fb;
  --paper: #ffffff;
  --cover-bg: #0b2c2f;
  --cover-accent: #14b8a6;
  --font-sans: 'IBM Plex Sans', 'Segoe UI', sans-serif;
  --font-serif: 'IBM Plex Serif', Georgia, serif;
  --font-mono: 'IBM Plex Mono', Consolas, monospace;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { font-size: 10.5pt; }

body {
  font-family: var(--font-serif);
  color: var(--ink);
  background: #e8ecf1;
  line-height: 1.5;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

/* Screen preview */
@media screen {
  body { padding: 24px 0 60px; }
  .page-sheet {
    width: 160mm;
    min-height: 220mm;
    margin: 0 auto 18px;
    background: var(--paper);
    box-shadow: 0 8px 28px rgba(26, 35, 50, 0.12);
  }
  .book { width: 160mm; margin: 0 auto; background: var(--paper); box-shadow: 0 8px 28px rgba(26,35,50,.12); }
}

@page {
  size: 160mm 220mm;
  margin: 14mm 16mm 16mm 16mm;
  @bottom-center {
    content: counter(page);
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 8.5pt;
    color: #64748b;
  }
}

@page :first {
  margin: 0;
  @bottom-center { content: none; }
}

@media print {
  html, body { background: white; padding: 0; margin: 0; }
  .book { width: auto; box-shadow: none; margin: 0; }
  .no-print { display: none !important; }
  a { color: inherit; text-decoration: none; }
  /* Compact handbook: break on major sections, not every short chapter */
  .page-break, .part-opener, .cover, .toc-page, .front-matter { page-break-before: always; break-before: page; }
  .chapter { page-break-before: auto; break-before: auto; }
  .chapter { margin-top: 1.4em; padding-top: 0.6em; border-top: 1px solid var(--rule); }
  #ch-1, #ch-3, #ch-4, #ch-10, #ch-13, #ch-15, #ch-18, #ch-20, #ch-22, #ch-26, #ch-28, #ch-29 {
    page-break-before: always; break-before: page; border-top: none; margin-top: 0; padding-top: 0;
  }
  .cover { page-break-before: avoid; break-before: avoid; }
  h1, h2, h3 { page-break-after: avoid; break-after: avoid; }
  table, .callout, .box, .prompt, .workflow, figure { page-break-inside: avoid; break-inside: avoid; }
  tr { page-break-inside: avoid; }
}

/* Typography */
h1, h2, h3, h4, .part-label, .toc, .sans, .cover, nav, .callout-label, th, .badge, .kicker {
  font-family: var(--font-sans);
}

p { margin: 0 0 0.5em; orphans: 3; widows: 3; }

.lead { font-size: 1.02rem; color: var(--muted); margin-bottom: 0.75em; }

h1.chapter-title {
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--ink);
  line-height: 1.2;
  margin: 0 0 0.3em;
  padding-bottom: 0.28em;
  border-bottom: 2.5px solid var(--accent);
}

h2 {
  font-size: 1.05rem;
  font-weight: 650;
  color: var(--accent-dark);
  margin: 0.9em 0 0.3em;
  line-height: 1.25;
}

h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--ink);
  margin: 0.95em 0 0.3em;
}

h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--muted);
  margin: 0.8em 0 0.25em;
}

ul, ol { margin: 0 0 0.75em 1.15em; }
li { margin-bottom: 0.25em; }
li::marker { color: var(--accent); }

strong { font-weight: 600; }
em { font-style: italic; }

a { color: var(--accent-dark); }

code, .mono {
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: #f1f5f9;
  padding: 0.08em 0.28em;
  border-radius: 2px;
}

pre {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  line-height: 1.4;
  background: #0f172a;
  color: #e2e8f0;
  padding: 0.75em 0.9em;
  border-radius: 4px;
  margin: 0.6em 0 0.9em;
  white-space: pre-wrap;
  word-break: break-word;
  overflow-wrap: anywhere;
}

.prompt {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  line-height: 1.35;
  background: #0f172a;
  color: #e2e8f0;
  padding: 0.55em 0.7em;
  border-radius: 4px;
  margin: 0.35em 0 0.55em;
  border-left: 3px solid var(--cover-accent);
  white-space: pre-wrap;
}

/* Cover */
.cover {
  background: linear-gradient(165deg, #062426 0%, #0b2c2f 42%, #134e4a 100%);
  color: #f8fafc;
  min-height: 220mm;
  padding: 18mm 14mm 14mm;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.cover::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 80% 50% at 100% 0%, rgba(20,184,166,0.25), transparent 55%),
    radial-gradient(ellipse 60% 40% at 0% 100%, rgba(196,92,38,0.18), transparent 50%);
  pointer-events: none;
}

.cover-inner { position: relative; z-index: 1; display: flex; flex-direction: column; height: 100%; min-height: 192mm; }

.cover-kicker {
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--cover-accent);
  font-weight: 600;
  margin-bottom: 1.8em;
}

.cover h1 {
  font-size: 2.05rem;
  font-weight: 700;
  line-height: 1.12;
  letter-spacing: -0.03em;
  margin-bottom: 0.55em;
  max-width: 14ch;
}

.cover .subtitle {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  line-height: 1.45;
  color: #cbd5e1;
  max-width: 28ch;
  margin-bottom: 2.2em;
}

.cover-meta {
  margin-top: auto;
  border-top: 1px solid rgba(255,255,255,0.18);
  padding-top: 1.1em;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 1em;
}

.cover-meta .edition {
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #94a3b8;
}

.cover-meta .year {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--cover-accent);
}

.cover-band {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 8mm;
  background: var(--cover-accent);
}

/* Front matter */
.front-matter, .toc-page, .chapter, .part-opener {
  padding: 0;
}

.chapter-num {
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 600;
  margin-bottom: 0.35em;
}

.part-opener {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  min-height: 0;
  padding: 0.4em 0 0.8em;
  page-break-after: avoid;
}

.part-label {
  font-size: 0.75rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 600;
  margin-bottom: 0.8em;
}

.part-opener h1 {
  font-size: 1.85rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.6em;
  line-height: 1.15;
}

.part-opener p {
  color: var(--muted);
  max-width: 36ch;
  font-size: 1rem;
}

/* TOC */
.toc-page h1 {
  font-size: 1.5rem;
  margin-bottom: 1em;
  border-bottom: 2.5px solid var(--accent);
  padding-bottom: 0.35em;
}

.toc { list-style: none; margin: 0; padding: 0; }
.toc li {
  display: flex;
  align-items: baseline;
  gap: 0.4em;
  margin-bottom: 0.35em;
  font-size: 0.88rem;
  line-height: 1.3;
}
.toc .toc-part {
  margin-top: 0.85em;
  margin-bottom: 0.35em;
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent-dark);
  border-bottom: none;
}
.toc .dots {
  flex: 1;
  border-bottom: 1px dotted var(--rule);
  margin: 0 0.2em 0.2em;
  min-width: 1em;
}
.toc .pg { color: var(--muted); font-variant-numeric: tabular-nums; }

/* Boxes */
.callout, .box {
  border-radius: 4px;
  padding: 0.5em 0.7em;
  margin: 0.5em 0 0.65em;
  font-size: 0.9rem;
  line-height: 1.4;
}

.callout-label {
  display: block;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 0.25em;
}

.tip { background: var(--tip-soft); border-left: 3px solid var(--tip); }
.tip .callout-label { color: var(--tip); }

.note { background: var(--accent-soft); border-left: 3px solid var(--accent); }
.note .callout-label { color: var(--accent-dark); }

.warn { background: var(--warn-soft); border-left: 3px solid var(--warm); }
.warn .callout-label { color: var(--warn); }

.example { background: var(--ex-soft); border-left: 3px solid var(--ex); }
.example .callout-label { color: var(--ex); }

.mistake { background: #fef2f2; border-left: 3px solid #b91c1c; }
.mistake .callout-label { color: #b91c1c; }

.takeaway {
  background: linear-gradient(90deg, var(--accent-soft), #fff);
  border: 1px solid #b6e0e0;
  border-radius: 4px;
  padding: 0.7em 0.85em;
  margin: 1em 0;
}

.takeaway h3 { margin-top: 0; color: var(--accent-dark); font-size: 0.9rem; }

.action-steps {
  background: #f8fafc;
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 0.7em 0.85em 0.55em;
  margin: 0.8em 0 1em;
}
.action-steps h3 { margin-top: 0; font-size: 0.9rem; color: var(--ink); }
.action-steps ol { margin-bottom: 0.2em; }

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.6em 0 1em;
  font-family: var(--font-sans);
  font-size: 0.78rem;
  line-height: 1.35;
}

th, td {
  border: 1px solid var(--rule);
  padding: 0.4em 0.5em;
  text-align: left;
  vertical-align: top;
}

th {
  background: #0f3d40;
  color: #f8fafc;
  font-weight: 600;
}

tr:nth-child(even) td { background: #f7fafb; }

.small { font-size: 0.88rem; }
.muted { color: var(--muted); }

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75em;
  margin: 0.6em 0 0.9em;
}

.card-lite {
  border-top: 2px solid var(--accent);
  padding-top: 0.4em;
}
.card-lite h4 { margin-top: 0; color: var(--accent-dark); }

.workflow {
  font-family: var(--font-sans);
  font-size: 0.82rem;
  background: #f8fafc;
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 0.65em 0.75em;
  margin: 0.55em 0 0.85em;
}
.workflow .flow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.25em;
  margin-top: 0.35em;
}
.workflow .step {
  background: var(--accent-soft);
  color: var(--accent-dark);
  padding: 0.2em 0.45em;
  border-radius: 3px;
  font-weight: 500;
}
.workflow .arrow { color: var(--muted); }

.placeholder {
  border: 1.5px dashed #94a3b8;
  background: repeating-linear-gradient(-45deg, #f8fafc, #f8fafc 8px, #eef2f7 8px, #eef2f7 16px);
  color: var(--muted);
  font-family: var(--font-sans);
  font-size: 0.78rem;
  text-align: center;
  padding: 1.4em 0.8em;
  margin: 0.6em 0 0.9em;
  border-radius: 4px;
}

.project {
  border-left: 3px solid var(--accent);
  padding: 0.15em 0 0.15em 0.75em;
  margin: 0.7em 0 1em;
}
.project h3 { margin-top: 0; }
.project .meta {
  font-family: var(--font-sans);
  font-size: 0.78rem;
  color: var(--muted);
  margin-bottom: 0.35em;
}

.exercise {
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 0.65em 0.8em;
  margin: 0.7em 0 1em;
  background: #fff;
}
.exercise h4 {
  margin-top: 0;
  color: var(--warm);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hr { border: none; border-top: 1px solid var(--rule); margin: 1em 0; }

.colophon {
  font-size: 0.85rem;
  color: var(--muted);
  margin-top: 2em;
}

.badge {
  display: inline-block;
  font-size: 0.68rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  background: var(--accent-soft);
  color: var(--accent-dark);
  padding: 0.15em 0.45em;
  border-radius: 2px;
  font-weight: 600;
  margin-right: 0.25em;
}

.screen-toolbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: #0b2c2f;
  color: #e2e8f0;
  font-family: var(--font-sans);
  font-size: 13px;
  padding: 10px 16px;
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
}
.screen-toolbar button, .screen-toolbar a {
  background: var(--cover-accent);
  color: #042f2e;
  border: none;
  padding: 6px 12px;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  font-size: 12px;
}
""" + CSS_FIXES + """
.cover { overflow: hidden; }
.cover-inner { justify-content: space-between; padding-bottom: 10mm; }
.cover .subtitle { max-width: 32ch; }
@media print {
  .cover { height: 220mm; max-height: 220mm; padding: 16mm 14mm 12mm; }
  .cover-band { height: 6mm; }
  .part-opener { min-height: 0 !important; height: auto; padding: 2.2em 0 1.2em; }
}
"""


def box(kind: str, label: str, html: str) -> str:
    return f'<div class="callout {kind}"><span class="callout-label">{label}</span>{html}</div>'


def prompt(text: str) -> str:
    return f'<div class="prompt">{text.strip()}</div>'


def takeaways(items: list[str]) -> str:
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="takeaway"><h3>Key Takeaways</h3><ul>{lis}</ul></div>'


def actions(items: list[str]) -> str:
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="action-steps"><h3>Action Steps</h3><ol>{lis}</ol></div>'


def exercise(title: str, body: str) -> str:
    return f'<div class="exercise"><h4>Exercise — {title}</h4>{body}</div>'


def workflow(title: str, steps: list[str]) -> str:
    parts = []
    for i, s in enumerate(steps):
        if i:
            parts.append('<span class="arrow">→</span>')
        parts.append(f'<span class="step">{s}</span>')
    return f'<div class="workflow"><strong>{title}</strong><div class="flow">{"".join(parts)}</div></div>'


def part(num: str, title: str, blurb: str) -> str:
    return f"""
<section class="part-opener" id="part-{num}">
  <div class="part-label">Part {num}</div>
  <h1>{title}</h1>
  <p>{blurb}</p>
</section>
"""


def chapter(num: str, title: str, body: str) -> str:
    # Use a trimmed subset of expansions to stay within the 80-page print budget.
    priority = {"4", "6", "7", "8", "9", "10", "15", "22", "26", "27", "29"}
    extra = EXPANSIONS.get(str(num), "") if str(num) in priority else ""
    if extra and len(extra) > 2200:
        # Keep expansions useful but compact: cut after ~2200 chars at a tag boundary.
        cut = extra[:2200]
        last = max(cut.rfind("</p>"), cut.rfind("</ul>"), cut.rfind("</table>"), cut.rfind("</div>"))
        if last > 800:
            extra = cut[: last + cut[last:].find(">") + 1]
    if extra:
        markers = (
            '<div class="takeaway">',
            '<div class="action-steps">',
        )
        inserted = False
        for marker in markers:
            idx = body.find(marker)
            if idx != -1:
                body = body[:idx] + extra + body[idx:]
                inserted = True
                break
        if not inserted:
            body = body + extra
    return f"""
<section class="chapter" id="ch-{num}">
  <div class="chapter-num">Chapter {num}</div>
  <h1 class="chapter-title">{title}</h1>
  {body}
</section>
"""


def build() -> str:
    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="author" content="AI Handbook Editorial"/>
<meta name="description" content="The Complete Beginner's Guide to Artificial Intelligence — a practical print-ready handbook for 2026."/>
<title>The Complete Beginner's Guide to Artificial Intelligence</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="screen-toolbar no-print">
  <span><strong>AI Beginner's Handbook</strong> · Print preview (160×220 mm)</span>
  <span><button onclick="window.print()">Print / Save as PDF</button></span>
</div>
<article class="book">
""")

    # COVER
    parts.append("""
<section class="cover" id="cover">
  <div class="cover-inner">
    <div class="cover-kicker">Practical Handbook · 2026 Edition</div>
    <h1>The Complete Beginner's Guide to Artificial Intelligence</h1>
    <p class="subtitle">Learn AI Tools, ChatGPT, Prompt Engineering, Image Generation, Video Generation, AI Automation, AI Agents, and Productivity Workflows</p>
    <div class="cover-meta">
      <div class="edition">From zero to practical mastery<br/>No coding required</div>
      <div class="year">2026</div>
    </div>
  </div>
  <div class="cover-band"></div>
</section>
""")

    # FRONT MATTER
    parts.append("""
<section class="front-matter" id="how-to-use">
  <div class="chapter-num">Front Matter</div>
  <h1 class="chapter-title">How to Use This Book</h1>
  <p class="lead">This handbook is built for absolute beginners who want practical results—not academic theory. You will learn what AI is, which tools to use, how to write strong prompts, and how to apply AI to real work.</p>
  <h2>Who this book is for</h2>
  <p>Students, freelancers, entrepreneurs, marketers, creators, office workers, and anyone who wants to use AI confidently in daily work.</p>
  <h2>What you will be able to do</h2>
  <ul>
    <li>Explain AI in plain language and choose the right tool for a task</li>
    <li>Use ChatGPT, Claude, Gemini, Perplexity, and NotebookLM professionally</li>
    <li>Write powerful prompts for writing, research, marketing, and analysis</li>
    <li>Generate images, video, and audio with modern AI tools</li>
    <li>Build simple automations and understand AI agents</li>
    <li>Complete real projects you can reuse in business or freelancing</li>
  </ul>
  <h2>How to read it</h2>
  <p>Read Parts 1–4 in order. After that, jump to the sections you need—images, video, automation, or projects. Every chapter ends with action steps. Do them. Skill comes from practice, not passive reading.</p>
  """ + box("tip", "Tip", "<p>Keep a notes doc titled <em>AI Playbook</em>. After each chapter, save your best prompts and workflows. By the end you will own a personal operating system for AI.</p>") + """
  <h2>Print &amp; PDF notes</h2>
  <p>This file is sized for a <strong>160 × 220 mm</strong> handbook. Use your browser’s Print dialog → Save as PDF, enable backgrounds, and set margins to default (CSS already defines page size).</p>
</section>
""")

    # TOC
    parts.append("""
<section class="toc-page" id="toc">
  <h1>Contents</h1>
  <ul class="toc">
    <li class="toc-part">Part 1 — AI Fundamentals</li>
    <li><span>1. What Is Artificial Intelligence?</span><span class="dots"></span></li>
    <li><span>2. How Modern AI Works</span><span class="dots"></span></li>
    <li class="toc-part">Part 2 — The AI Ecosystem</li>
    <li><span>3. Understanding AI Tool Categories</span><span class="dots"></span></li>
    <li class="toc-part">Part 3 — Essential AI Tools</li>
    <li><span>4. Large Language Models</span><span class="dots"></span></li>
    <li><span>5. ChatGPT Complete Guide</span><span class="dots"></span></li>
    <li><span>6. Claude Complete Guide</span><span class="dots"></span></li>
    <li><span>7. Gemini Complete Guide</span><span class="dots"></span></li>
    <li><span>8. Perplexity Complete Guide</span><span class="dots"></span></li>
    <li><span>9. NotebookLM Complete Guide</span><span class="dots"></span></li>
    <li class="toc-part">Part 4 — Prompt Engineering</li>
    <li><span>10. Prompt Engineering Foundations</span><span class="dots"></span></li>
    <li><span>11. Prompt Frameworks</span><span class="dots"></span></li>
    <li><span>12. Professional Prompt Library</span><span class="dots"></span></li>
    <li class="toc-part">Part 5 — AI Image Generation</li>
    <li><span>13. Introduction to AI Images</span><span class="dots"></span></li>
    <li><span>14. Image Prompt Engineering</span><span class="dots"></span></li>
    <li class="toc-part">Part 6 — AI Video Generation</li>
    <li><span>15. Video AI Fundamentals</span><span class="dots"></span></li>
    <li><span>16. Veo Guide</span><span class="dots"></span></li>
    <li><span>17. Runway, Kling, Pika &amp; Sora</span><span class="dots"></span></li>
    <li class="toc-part">Part 7 — AI Audio</li>
    <li><span>18. Voice AI</span><span class="dots"></span></li>
    <li><span>19. Music AI</span><span class="dots"></span></li>
    <li class="toc-part">Part 8 — Productivity</li>
    <li><span>20. Personal Productivity with AI</span><span class="dots"></span></li>
    <li><span>21. Business Productivity</span><span class="dots"></span></li>
    <li class="toc-part">Part 9 — Automation</li>
    <li><span>22. Automation Fundamentals</span><span class="dots"></span></li>
    <li><span>23. n8n Complete Guide</span><span class="dots"></span></li>
    <li><span>24. Make Complete Guide</span><span class="dots"></span></li>
    <li><span>25. Zapier Complete Guide</span><span class="dots"></span></li>
    <li class="toc-part">Part 10 — AI Agents</li>
    <li><span>26. Understanding AI Agents</span><span class="dots"></span></li>
    <li><span>27. Building Agent Workflows</span><span class="dots"></span></li>
    <li class="toc-part">Part 11 — Projects</li>
    <li><span>28. 20 Complete AI Projects</span><span class="dots"></span></li>
    <li class="toc-part">Part 12 — Future &amp; Roadmap</li>
    <li><span>29. Future Trends</span><span class="dots"></span></li>
    <li><span>30. AI Career Roadmap</span><span class="dots"></span></li>
  </ul>
</section>
""")

    parts.append(part("1", "Understanding AI", "Start here. You will learn what artificial intelligence actually is, why it suddenly feels everywhere, and how modern systems produce useful answers from patterns in data."))

    # CH1
    parts.append(chapter("1", "What Is Artificial Intelligence?", f"""
<p class="lead">Artificial Intelligence (AI) is software that performs tasks that normally require human intelligence: understanding language, recognizing images, making recommendations, or generating new content.</p>

<h2>Definition</h2>
<p>Think of AI as a very fast pattern-matching engine. It studies huge amounts of examples, learns statistical relationships, and then applies those patterns to new situations. It does not “think” like a person—but it can produce outputs that look intelligent when used well.</p>

{box("example", "Real-world example", "<p>When Netflix suggests a show, YouTube ranks the next video, or Google Maps predicts traffic, an AI model is comparing your behavior to patterns learned from millions of other users.</p>")}

<h2>A short history (the useful version)</h2>
<ul>
  <li><strong>1950s–1980s:</strong> Rules and logic systems. Computers followed hand-written instructions.</li>
  <li><strong>1990s–2010s:</strong> Machine learning. Systems learned from data (spam filters, recommendations).</li>
  <li><strong>2012+:</strong> Deep learning. Neural networks made image and speech recognition practical.</li>
  <li><strong>2017+:</strong> Transformers. A new architecture unlocked modern language models.</li>
  <li><strong>2022–2026:</strong> Generative AI went mainstream—ChatGPT, image/video generators, agents, and workplace copilots.</li>
</ul>

<h2>Three types you must know</h2>
<table>
  <thead><tr><th>Type</th><th>Meaning</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td><strong>Narrow AI</strong></td><td>Good at one job or a narrow set of jobs</td><td>Spam filter, face unlock, translation</td></tr>
    <tr><td><strong>Generative AI</strong></td><td>Creates new text, images, audio, video, code</td><td>ChatGPT, Midjourney, Veo, Suno</td></tr>
    <tr><td><strong>General AI (AGI)</strong></td><td>Human-level flexible intelligence across domains</td><td>Not achieved yet</td></tr>
  </tbody>
</table>
<p>Everything you use today is Narrow AI—often generative. AGI is a research goal, not a product you can buy.</p>

<h2>Why AI matters now</h2>
<p>Three shifts happened at once: models got dramatically better, interfaces became chat-simple, and tools connected to everyday apps (Docs, email, browsers, design tools). That combination turned AI from a lab topic into a daily productivity layer.</p>

<h3>Where you already use AI</h3>
<table>
  <thead><tr><th>Product</th><th>What AI does</th></tr></thead>
  <tbody>
    <tr><td>Netflix / YouTube / TikTok</td><td>Ranks content likely to keep you watching</td></tr>
    <tr><td>Google Maps</td><td>Predicts routes, traffic, and arrival times</td></tr>
    <tr><td>Amazon</td><td>Recommends products and detects fraud patterns</td></tr>
    <tr><td>Banking apps</td><td>Flags unusual transactions</td></tr>
    <tr><td>Healthcare tools</td><td>Assists imaging review, triage, documentation</td></tr>
  </tbody>
</table>

<h2>Common myths</h2>
{box("mistake", "Myth → Reality", """
<ul>
<li><strong>“AI is conscious.”</strong> No. It predicts likely next words or pixels.</li>
<li><strong>“AI always tells the truth.”</strong> No. It can hallucinate confident wrong answers.</li>
<li><strong>“AI will replace all jobs overnight.”</strong> Unlikely. It changes tasks first; people who use AI replace people who don’t.</li>
<li><strong>“You need to code.”</strong> No. Chat interfaces are enough to start—and this book assumes zero coding.</li>
</ul>
""")}

<h2>The near future (practical view)</h2>
<p>Expect more multimodal tools (text + image + voice + video in one chat), more agents that take multi-step actions, and deeper workplace integration. Your advantage is not memorizing every product—it is learning transferable skills: prompting, verification, workflow design, and tool selection.</p>

{takeaways([
  "AI is pattern recognition and generation at scale—not human consciousness.",
  "Today’s tools are Narrow / Generative AI.",
  "You already use AI daily; the new skill is directing it deliberately.",
  "Always verify important facts; fluency ≠ accuracy."
])}
{actions([
  "List five apps you use daily and note where AI might already be helping.",
  "Open ChatGPT, Claude, or Gemini and ask: “Explain AI to me like I’m 14, with three everyday examples.”",
  "Create an AI Playbook document for prompts and notes."
])}
{exercise("Spot the AI", "<p>Pick one shopping site and one social app. Write three specific AI decisions each product is making for you (recommendations, ranking, moderation, search).</p>")}
"""))

    # CH2
    parts.append(chapter("2", "How Modern AI Works", f"""
<p class="lead">You do not need a computer science degree. You do need a mental model so AI stops feeling like magic—and so you know why prompts, context, and verification matter.</p>

<h2>The five-building-block model</h2>
<ol>
  <li><strong>Data:</strong> Text, images, audio, code, and other examples the system learns from.</li>
  <li><strong>Training:</strong> Adjusting millions/billions of internal knobs so predictions get better.</li>
  <li><strong>Model:</strong> The trained brain that can respond to new inputs.</li>
  <li><strong>Inference:</strong> Using the model to answer your prompt.</li>
  <li><strong>Tools &amp; retrieval:</strong> Optional extras—web search, your files, calculators, apps.</li>
</ol>

{box("note", "Analogy", "<p>Training is like studying for years. Inference is like taking an open exam in seconds. Retrieval is like being allowed to open a specific binder of your notes during the exam.</p>")}

<h2>Neural networks &amp; deep learning</h2>
<p>A neural network is a stack of simple math units (neurons) arranged in layers. “Deep” learning means many layers. Early layers catch simple patterns; later layers catch complex ones (edges → shapes → objects, or letters → words → ideas).</p>

<h2>Transformers (why ChatGPT exists)</h2>
<p>Transformers are the architecture behind modern large language models (LLMs). Their key trick is <strong>attention</strong>: the model learns which words in a passage matter for predicting the next word. That makes long-range context possible (“it” refers to which noun?) and scales extremely well.</p>

<h2>Tokens, not words</h2>
<p>Models read <strong>tokens</strong>—chunks of text that may be whole words or pieces (<code>ing</code>, <code>Chat</code>, <code>GPT</code>). Limits are measured in tokens. Rough rule: English ≈ 0.75 words per token (or ~100 tokens ≈ 75 words).</p>

<h2>Context windows</h2>
<p>The <strong>context window</strong> is how much text the model can consider at once (your prompt + conversation + uploaded material). Bigger windows help with long documents—but stuffing irrelevant text still hurts quality.</p>

<table>
  <thead><tr><th>Concept</th><th>Plain meaning</th><th>Why you care</th></tr></thead>
  <tbody>
    <tr><td>Parameters</td><td>Internal learned weights</td><td>Bigger ≠ always better; quality and training matter</td></tr>
    <tr><td>Context window</td><td>Short-term working memory</td><td>Limits how much you can paste at once</td></tr>
    <tr><td>Fine-tuning</td><td>Extra training for a specialty</td><td>Makes a model better at a narrow style/task</td></tr>
    <tr><td>RAG / Retrieval</td><td>Fetch relevant docs, then answer</td><td>Grounds answers in your files or the web</td></tr>
    <tr><td>Hallucination</td><td>Confident wrong output</td><td>Verify facts, citations, numbers, quotes</td></tr>
  </tbody>
</table>

<h2>Fine-tuning vs. prompting vs. retrieval</h2>
<ul>
  <li><strong>Prompting:</strong> Guide the base model with instructions and examples. Fastest for beginners.</li>
  <li><strong>Retrieval:</strong> Attach or search documents so answers cite your sources (NotebookLM, Perplexity, enterprise RAG).</li>
  <li><strong>Fine-tuning:</strong> Retrain on specialized data. Powerful but usually overkill for individuals.</li>
</ul>

{box("tip", "Practical implication", "<p>Most beginners get 80% of results from better prompts + better source material, not from switching models every week.</p>")}

{takeaways([
  "Models predict patterns learned from data; they do not look up a single ‘truth database’ by default.",
  "Tokens and context windows set hard limits on what fits in one go.",
  "Retrieval and tools reduce hallucinations when accuracy matters.",
  "Prompting is your primary control surface."
])}
{actions([
  "Ask an AI: “Explain transformers using a kitchen analogy.”",
  "Paste a 1-page article and ask for a summary—then ask which details it might have guessed.",
  "In your AI Playbook, note: Token ≈ word piece; Context = working memory; Verify = non-negotiable."
])}
"""))

    parts.append(part("2", "The AI Ecosystem", "AI is not one app. It is a landscape of tools. This part gives you a map so you can stop collecting random subscriptions and start choosing deliberately."))

    # CH3
    parts.append(chapter("3", "Understanding AI Tool Categories", f"""
<p class="lead">When someone says “I use AI,” ask: which category? Text, search, image, video, audio, coding, productivity, automation, or agents each solve different jobs.</p>

<h2>1. Text generation AI</h2>
<p><strong>Job:</strong> Draft, rewrite, brainstorm, analyze, tutor, plan.</p>
<p><strong>Examples:</strong> ChatGPT, Claude, Gemini, DeepSeek.</p>
<p><strong>Best for:</strong> Writing and thinking work. <strong>Watch out for:</strong> factual errors without sources.</p>

<h2>2. Search AI</h2>
<p><strong>Job:</strong> Answer questions with live web context.</p>
<p><strong>Examples:</strong> Perplexity, You.com.</p>
<p><strong>Best for:</strong> Current events, product comparisons, quick research with links.</p>

<h2>3. Research AI</h2>
<p><strong>Job:</strong> Go deeper—multi-source synthesis, long-document understanding.</p>
<p><strong>Examples:</strong> NotebookLM, Perplexity deep research modes, ChatGPT/Gemini research features.</p>
<p><strong>Best for:</strong> Reports, literature-style overviews, studying your own materials.</p>

<h2>4. Image generation AI</h2>
<p><strong>Examples:</strong> Midjourney, Flux, DALL·E, Ideogram, Leonardo.</p>
<p><strong>Best for:</strong> Concept art, ads, thumbnails, mockups. <strong>Weak at:</strong> perfect typography (except specialists like Ideogram), legal/likeness-sensitive work without care.</p>

<h2>5. Video generation AI</h2>
<p><strong>Examples:</strong> Google Veo, OpenAI Sora, Runway, Kling, Pika.</p>
<p><strong>Best for:</strong> Short clips, storyboards, social drafts. Still costly/limited for long-form cinema.</p>

<h2>6. Audio generation AI</h2>
<p><strong>Voice:</strong> ElevenLabs, PlayHT. <strong>Music:</strong> Suno, Udio.</p>
<p><strong>Best for:</strong> Voiceovers, podcasts drafts, placeholder scores. Check licensing before commercial use.</p>

<h2>7. Coding AI</h2>
<p><strong>Examples:</strong> Cursor, Windsurf, GitHub Copilot, Replit AI.</p>
<p><strong>Best for:</strong> Building software faster. Beginners can use them to learn—but always test code.</p>

<h2>8. Productivity AI</h2>
<p><strong>Examples:</strong> Notion AI, Grammarly, Motion, Fireflies.</p>
<p><strong>Best for:</strong> Meeting notes, grammar, scheduling, knowledge bases.</p>

<h2>9. Automation AI</h2>
<p><strong>Examples:</strong> Make, Zapier, n8n.</p>
<p><strong>Best for:</strong> Connecting apps: “When X happens, do Y with AI in the middle.”</p>

<h2>10. AI agents</h2>
<p><strong>Examples:</strong> OpenAI agent experiences, AutoGPT-style systems, custom agentic workflows.</p>
<p><strong>Best for:</strong> Multi-step goals with tools. <strong>Risk:</strong> errors compound—start supervised.</p>

<h2>Comparison at a glance</h2>
<table>
  <thead><tr><th>Category</th><th>Primary output</th><th>Start with</th><th>Pay when</th></tr></thead>
  <tbody>
    <tr><td>Text LLM</td><td>Writing / reasoning</td><td>ChatGPT or Claude</td><td>Daily heavy use</td></tr>
    <tr><td>Search AI</td><td>Cited answers</td><td>Perplexity</td><td>Research is your job</td></tr>
    <tr><td>Docs research</td><td>Source-grounded notes</td><td>NotebookLM</td><td>Large private corpora</td></tr>
    <tr><td>Images</td><td>Visuals</td><td>ChatGPT images or Flux</td><td>Brand/creative volume</td></tr>
    <tr><td>Video</td><td>Clips</td><td>Runway or Veo access</td><td>Content team needs</td></tr>
    <tr><td>Automation</td><td>Workflows</td><td>Zapier or Make</td><td>Repeatable processes</td></tr>
  </tbody>
</table>

{box("tip", "Starter stack (most people)", "<p><strong>ChatGPT or Claude</strong> (thinking/writing) + <strong>Perplexity</strong> (web research) + <strong>NotebookLM</strong> (your files) + one image tool. Add automation only after you repeat a task weekly.</p>")}

{takeaways([
  "Match the tool category to the job—don’t force ChatGPT to do everything.",
  "Search/research tools beat chatbots when citations and freshness matter.",
  "Automation pays off on repetition; agents need supervision.",
  "A small stack used deeply beats ten shallow subscriptions."
])}
{actions([
  "Write your top 10 recurring work tasks.",
  "Label each with a tool category from this chapter.",
  "Pick one gap and install only that missing tool this week."
])}
"""))

    parts.append(part("3", "Mastering Essential AI Tools", "These five tools cover most beginner-to-pro work: general LLMs, ChatGPT, Claude, Gemini, Perplexity, and NotebookLM. Learn them once; transfer the skills forever."))

    # CH4
    parts.append(chapter("4", "Large Language Models", f"""
<p class="lead">A Large Language Model (LLM) is an AI trained on vast text to predict and generate language. Chatbots are interfaces; the LLM is the engine underneath.</p>

<h2>What an LLM is good at</h2>
<ul>
  <li>Drafting and editing text in many tones</li>
  <li>Brainstorming structures, options, and angles</li>
  <li>Explaining concepts at different levels</li>
  <li>Transforming formats (bullets → email → script)</li>
  <li>Light reasoning and planning (with oversight)</li>
</ul>

<h2>Major model families (2026 landscape)</h2>
<table>
  <thead><tr><th>Family</th><th>Maker</th><th>Standing strength</th></tr></thead>
  <tbody>
    <tr><td><strong>GPT</strong></td><td>OpenAI</td><td>Generalist, tools, ecosystem, multimodal chat</td></tr>
    <tr><td><strong>Claude</strong></td><td>Anthropic</td><td>Long context, careful writing, coding/analysis</td></tr>
    <tr><td><strong>Gemini</strong></td><td>Google</td><td>Google Workspace + search ecosystem fit</td></tr>
    <tr><td><strong>DeepSeek</strong></td><td>DeepSeek</td><td>Strong value / reasoning-oriented options</td></tr>
    <tr><td><strong>Llama</strong></td><td>Meta</td><td>Open-weight ecosystem, local/self-host options</td></tr>
    <tr><td><strong>Mistral</strong></td><td>Mistral</td><td>Efficient open/European-cloud oriented models</td></tr>
  </tbody>
</table>
<p class="small muted">Model names and rankings change quickly. Judge by your tasks: writing quality, tool use, speed, price, privacy, and integrations.</p>

<h2>Parameters, memory, reasoning, multimodality</h2>
<ul>
  <li><strong>Parameters:</strong> Capacity of the model. Useful signal, not a scoreboard.</li>
  <li><strong>Chat memory:</strong> Product feature that stores preferences across chats (optional).</li>
  <li><strong>Reasoning modes:</strong> Some products spend more compute to plan before answering—better for hard problems, slower/costlier.</li>
  <li><strong>Multimodal:</strong> Accepts or produces more than text (images, audio, files).</li>
</ul>

{box("warn", "Privacy note", "<p>Don’t paste secrets, passwords, unpublished financials, or personal data of others into consumer AI tools unless your plan and policy explicitly allow it.</p>")}

{takeaways([
  "LLM = language engine; chatbot = product wrapper with tools and UI.",
  "Pick models by workflow fit, not hype cycles.",
  "Use specialized modes (search, reasoning, long context) when the task needs them."
])}
"""))

    # CH5 ChatGPT
    parts.append(chapter("5", "ChatGPT Complete Guide", f"""
<p class="lead">ChatGPT is many beginners’ first AI home base: conversation, drafting, analysis, images, voice, and custom tools in one place.</p>

<h2>Getting started</h2>
<ol>
  <li>Create an account at the official ChatGPT site.</li>
  <li>Start on the free tier to learn; upgrade if you hit limits or need advanced models/features.</li>
  <li>Set custom instructions: who you are, how you want answers (length, tone, format).</li>
</ol>

<div class="placeholder">[Screenshot placeholder: ChatGPT home — new chat, model picker, sidebar]</div>

<h2>Interface map</h2>
<ul>
  <li><strong>Sidebar:</strong> past chats, projects, GPTs</li>
  <li><strong>Composer:</strong> type prompts; attach files/images when available</li>
  <li><strong>Model picker:</strong> choose speed vs. capability</li>
  <li><strong>Tools:</strong> search, image generation, canvas/document editing, voice—depending on plan</li>
</ul>

<h2>Features that matter</h2>
<table>
  <thead><tr><th>Feature</th><th>Use it for</th></tr></thead>
  <tbody>
    <tr><td><strong>Projects</strong></td><td>Group chats + files for one client or course</td></tr>
    <tr><td><strong>Memory</strong></td><td>Remember preferences (review/delete regularly)</td></tr>
    <tr><td><strong>Canvas</strong></td><td>Side-by-side editing of long docs/code</td></tr>
    <tr><td><strong>Search</strong></td><td>Fresher answers with web context</td></tr>
    <tr><td><strong>Deep research</strong></td><td>Broader multi-step research reports</td></tr>
    <tr><td><strong>Image generation</strong></td><td>Concepts, thumbnails, simple marketing visuals</td></tr>
    <tr><td><strong>Voice mode</strong></td><td>Hands-free brainstorming and tutoring</td></tr>
    <tr><td><strong>Custom GPTs</strong></td><td>Reusable specialists with instructions + knowledge</td></tr>
  </tbody>
</table>

<h2>Professional workflow</h2>
{workflow("Client deliverable draft", ["Brief in Project", "Outline", "Draft sections", "Critique pass", "Final format"])}

{box("example", "Strong starter prompt", prompt("""You are a senior marketing editor.
Goal: Write a landing-page hero section for a budgeting app for freelancers.
Audience: US freelancers, 25–40, overwhelmed by taxes.
Tone: Clear, confident, no hype.
Deliver: 1 headline, 1 subhead, 3 bullet benefits, 1 CTA.
Constraints: Max 60 characters for headline; avoid buzzwords like "revolutionary."
"""))}

<h2>50 practical ChatGPT examples</h2>
<ol class="small">
  <li>Rewrite an email to be shorter and kinder</li>
  <li>Turn meeting notes into action items with owners</li>
  <li>Create a one-week meal plan from ingredients you have</li>
  <li>Explain a PDF contract in plain language (then verify legally)</li>
  <li>Generate interview questions for a role</li>
  <li>Draft a LinkedIn post from a bullet list</li>
  <li>Build a study plan for an exam date</li>
  <li>Compare two product options in a table</li>
  <li>Create a negotiation script for a raise</li>
  <li>Summarize a YouTube transcript into takeaways</li>
  <li>Produce SEO title options + meta description</li>
  <li>Design a customer survey (10 questions)</li>
  <li>Role-play an angry customer call</li>
  <li>Convert a blog post into a Twitter/X thread</li>
  <li>Create a project timeline from a vague goal</li>
  <li>Draft a product requirements outline</li>
  <li>Generate test cases from a feature description</li>
  <li>Simplify a technical paragraph for executives</li>
  <li>Create flashcards from lecture notes</li>
  <li>Brainstorm brand name candidates + domains angle</li>
  <li>Write a podcast show notes template</li>
  <li>Produce a swipe file of ad hooks</li>
  <li>Analyze a resume against a job description</li>
  <li>Create a content calendar for 30 days</li>
  <li>Draft SOPs from a messy process description</li>
  <li>Generate SQL-like logic in plain English for non-coders</li>
  <li>Plan a workshop agenda with timings</li>
  <li>Create objection-handling scripts for sales</li>
  <li>Turn analytics notes into an executive summary</li>
  <li>Build a personal weekly review checklist</li>
  <li>Rewrite a About page in three brand voices</li>
  <li>Extract FAQs from a help-center dump</li>
  <li>Create a competitive battlecard from notes</li>
  <li>Draft a webinar landing page outline</li>
  <li>Generate onboarding emails for a SaaS trial</li>
  <li>Turn a spreadsheet description into chart recommendations</li>
  <li>Create a risk list for a product launch</li>
  <li>Draft a partnership outreach message</li>
  <li>Build a glossary for a technical topic</li>
  <li>Write alt text for a set of marketing images</li>
  <li>Create a parenting / life admin weekly plan</li>
  <li>Produce a travel itinerary with constraints</li>
  <li>Draft a performance self-review from bullet wins</li>
  <li>Generate lesson warm-up activities for teachers</li>
  <li>Create a donation appeal for a nonprofit</li>
  <li>Rewrite jargon-heavy policy into plain language</li>
  <li>Plan an A/B test hypothesis list</li>
  <li>Draft community moderation decision notes</li>
  <li>Create a swipe file of subject lines for email</li>
  <li>Build a personal knowledge capture template</li>
</ol>

{box("mistake", "Common mistakes", "<ul><li>One-shot vague prompts (“write a marketing plan”).</li><li>Accepting citations without clicking them.</li><li>Putting confidential data in chats.</li><li>Never iterating—great output is usually draft 2–4.</li></ul>")}

{takeaways([
  "Custom instructions + Projects multiply consistency.",
  "Use search/research modes for time-sensitive facts.",
  "Custom GPTs encode repeatable expertise.",
  "Iterate: outline → draft → critique → polish."
])}
{actions([
  "Set custom instructions today (role, tone, format defaults).",
  "Create one Project for your main work area and upload 2–3 reference files.",
  "Save five prompts from this chapter into your AI Playbook."
])}
"""))

    # CH6 Claude
    parts.append(chapter("6", "Claude Complete Guide", f"""
<p class="lead">Claude (Anthropic) shines at long documents, careful analysis, thoughtful writing, and structured artifacts you can revise.</p>

<h2>Strengths to exploit</h2>
<ul>
  <li><strong>Long context:</strong> Large reports, book chapters, codebases summaries</li>
  <li><strong>Projects:</strong> Persistent instructions + knowledge for a workspace</li>
  <li><strong>Artifacts:</strong> Standalone documents, code, or mini-apps in a dedicated panel</li>
  <li><strong>Writing quality:</strong> Strong editorial sense when guided</li>
</ul>

<h2>Writing workflow</h2>
{workflow("Long-form article", ["Paste brief + sources", "Ask for outline", "Approve outline", "Draft by section", "Edit for voice"])}
{prompt("""Project instructions: You are my editorial partner for practical how-to content.
Always: ask clarifying questions if the brief is ambiguous; prefer concrete examples; flag unsupported claims.
Audience default: smart beginners.
""")}

<h2>Research workflow</h2>
<ol>
  <li>Upload PDFs or paste source notes.</li>
  <li>Ask for a source map: themes, agreements, contradictions.</li>
  <li>Request a brief with citations to your uploaded text (quotes + locations).</li>
  <li>Generate the deliverable only after the brief is solid.</li>
</ol>

{box("example", "Artifact use case", "<p>Ask Claude to produce a one-page competitive teardown as an artifact, then: “Tighten to 400 words and add a decision table.” Iterate in place instead of re-pasting everything.</p>")}

{box("tip", "When to choose Claude", "<p>Choose Claude when the input is long, the tone must feel human, or you need careful restructuring. Choose Search AI when you need live web citations first.</p>")}

{actions([
  "Create a Claude Project with a one-paragraph house style.",
  "Upload a 10+ page PDF and ask for a 1-page brief with quote-backed claims.",
  "Produce one artifact (checklist or one-pager) for work this week."
])}
"""))

    # CH7 Gemini
    parts.append(chapter("7", "Gemini Complete Guide", f"""
<p class="lead">Gemini is Google’s model family—most valuable when your work already lives in Gmail, Docs, Drive, and Workspace.</p>

<h2>Why Gemini is different for beginners</h2>
<p>Quality matters, but <strong>distribution</strong> matters more for daily habits. If AI appears beside the email you’re already writing, you will use it. Gemini’s edge is ecosystem gravity.</p>

<h2>Practical Workspace patterns</h2>
<table>
  <thead><tr><th>App</th><th>High-value use</th></tr></thead>
  <tbody>
    <tr><td>Gmail</td><td>Draft replies, shorten threads, extract action items</td></tr>
    <tr><td>Docs</td><td>Outline, rewrite, summarize comments</td></tr>
    <tr><td>Drive</td><td>Find themes across files; ask questions over documents you can access</td></tr>
    <tr><td>Sheets</td><td>Explain formulas, generate analysis steps, clean column plans</td></tr>
    <tr><td>Meet / notes</td><td>Summaries and follow-ups (where available)</td></tr>
  </tbody>
</table>

{workflow("From messy inbox to plan", ["Select thread", "Summarize decisions", "Draft reply", "Create Docs action list", "Schedule follow-ups"])}

{box("warn", "Grounding still required", "<p>Workspace AI can misread a thread. For commitments, money, or legal wording, read the final text yourself.</p>")}

{actions([
  "Enable Gemini features available on your Google account/plan.",
  "Pick one recurring email type and save a reply prompt template.",
  "Run a Docs rewrite on a past report: clearer title, sharper exec summary, shorter paragraphs."
])}
"""))

    # CH8 Perplexity
    parts.append(chapter("8", "Perplexity Complete Guide", f"""
<p class="lead">Perplexity is an answer engine: question in, cited synthesis out. Use it when freshness and sources matter more than creative drafting.</p>

<h2>Core habits</h2>
<ul>
  <li>Ask precise questions (“2025–2026”, “for freelancers in the EU”, “primary sources”).</li>
  <li>Open citations—don’t trust the summary alone.</li>
  <li>Use follow-ups to narrow: contradictions, costs, alternatives.</li>
  <li>Switch to deeper research modes for broader reports when available.</li>
</ul>

{prompt("""What are the main differences between Zapier, Make, and n8n for a 5-person marketing team in 2026?
Constraints: compare pricing model shape (not exact cents), learning curve, and best-fit use cases.
Output: table + recommendation. Prefer recent sources and cite them.""")}

{box("tip", "Research sandwich", "<p>Perplexity for sources → Claude/ChatGPT for structuring the narrative → human for conclusions and voice.</p>")}

{box("mistake", "Common mistake", "<p>Using Perplexity like a creative writer for brand storytelling. It’s a researcher first. Draft final copy in an LLM with your brand voice.</p>")}

{actions([
  "Run three work questions you usually Google; save the best cited answer.",
  "For one question, click every citation and rate trustworthiness.",
  "Add a ‘Research’ section to your AI Playbook with source-check steps."
])}
"""))

    # CH9 NotebookLM
    parts.append(chapter("9", "NotebookLM Complete Guide", f"""
<p class="lead">NotebookLM is Google’s source-grounded research assistant. You upload materials; it answers from those sources—ideal for studying, briefings, and knowledge bases.</p>

<h2>Core loop</h2>
{workflow("NotebookLM loop", ["Create notebook", "Add sources", "Ask grounded questions", "Generate study guide / FAQ / briefing", "Export insights to your docs"])}

<h2>Source types that work well</h2>
<ul>
  <li>PDFs, docs, pasted notes, transcripts</li>
  <li>Policy manuals, sales decks, course readings</li>
  <li>Competitor pages saved as documents (respect copyright/ToS)</li>
</ul>

<h2>Business use cases</h2>
<table>
  <thead><tr><th>Role</th><th>Notebook idea</th></tr></thead>
  <tbody>
    <tr><td>Founder</td><td>Investor Q&amp;A notebook from pitch + financial narrative docs</td></tr>
    <tr><td>Marketer</td><td>Brand voice + past campaigns → brief generator</td></tr>
    <tr><td>Support lead</td><td>Help center + policies → answer drafts with citations</td></tr>
    <tr><td>Student</td><td>Lecture PDFs → quizzes, timelines, podcast-style overviews</td></tr>
    <tr><td>Consultant</td><td>Client discovery notes → structured proposal outline</td></tr>
  </tbody>
</table>

{box("example", "Podcast / audio overview", "<p>Where available, NotebookLM can generate an audio overview of your sources—useful for commuting revision. Treat it as a study aid, not a citable academic authority.</p>")}

{box("tip", "Quality rule", "<p>Garbage sources → garbage notebooks. Curate. Split sprawling topics into multiple notebooks.</p>")}

{actions([
  "Create one notebook with 3–5 high-quality sources for a live project.",
  "Generate a FAQ and a one-page briefing.",
  "Ask: “What do my sources not cover that I still need?”"
])}
"""))

    parts.append(part("4", "Prompt Engineering", "Prompting is the universal skill. Same model, different prompt—completely different results. This part turns vague chatting into professional direction."))

    # CH10
    parts.append(chapter("10", "Prompt Engineering Foundations", f"""
<p class="lead">A prompt is the full instruction you give an AI: task, context, constraints, and desired format. Clear prompts produce clear work.</p>

<h2>Why prompts matter</h2>
<p>Models are general. Your prompt narrows the universe of possible answers. Professionals don’t “ask AI”—they brief it like a talented junior contractor.</p>

<h2>Components of a strong prompt</h2>
<ol>
  <li><strong>Role:</strong> who the AI should act as</li>
  <li><strong>Goal:</strong> what done looks like</li>
  <li><strong>Audience:</strong> who will read/use the output</li>
  <li><strong>Context:</strong> facts, product, constraints, examples</li>
  <li><strong>Process:</strong> steps (outline first, then draft)</li>
  <li><strong>Format:</strong> table, bullets, email, JSON, script</li>
  <li><strong>Quality bar:</strong> tone, length, must-include / must-avoid</li>
</ol>

{box("example", "Weak vs strong", """
<p><strong>Weak:</strong> “Write a business plan.”</p>
<p><strong>Strong:</strong> “Act as an SMB consultant. Create a 1-page lean plan for a home organizing service in Austin targeting busy parents. Include problem, offer, pricing hypothesis, 3 channels, 90-day milestones. No fluff. Table for milestones.”</p>
""")}

<h2>Iteration pattern</h2>
{workflow("Pro iteration", ["Brief", "Outline", "Draft", "Critique", "Tighten", "Final"])}
<p>Ask the model to critique its own draft against your checklist. Then apply fixes.</p>

{takeaways([
  "Prompts are briefs, not magic words.",
  "Format instructions dramatically improve usability.",
  "Iteration beats one giant mega-prompt for complex work."
])}
"""))

    # CH11
    parts.append(chapter("11", "Prompt Frameworks", f"""
<p class="lead">Frameworks are training wheels that become instincts. Memorize a few; remix freely.</p>

<h2>RTF — Role, Task, Format</h2>
{prompt("""Role: Career coach for career-switchers into UX.
Task: Create a 30-day learning plan.
Format: Week-by-week table with daily time estimates and deliverables.""")}

<h2>CRISPE</h2>
<p><strong>C</strong>apacity/Role · <strong>R</strong>equest · <strong>I</strong>nsight/Context · <strong>S</strong>tatement of goal · <strong>P</strong>ersonality/Tone · <strong>E</strong>xperiment/Evaluate</p>
{prompt("""Capacity: Senior B2B SaaS copywriter.
Request: Rewrite this homepage H1/H2.
Insight: Users fear complex setup; we offer 2-day onboarding.
Goal: Increase demo clicks.
Personality: Plain-spoken, confident, specific.
Evaluate: Give 3 variants and predict which converts best and why.""")}

<h2>APE — Action, Purpose, Expectation</h2>
{prompt("""Action: Summarize the transcript.
Purpose: Prep me for a 10-minute exec update.
Expectation: 5 bullets max, each with a decision needed.""")}

<h2>Chain of Thought (ask for steps)</h2>
<p>For logic, math, or tradeoffs: “Think step by step. List assumptions. Then conclude.”</p>

<h2>Tree of Thoughts</h2>
<p>Ask for 2–3 distinct approaches, evaluate each, then pick/merge a winner. Great for strategy and creative direction.</p>

<h2>Few-shot prompting</h2>
<p>Provide 2–3 examples of ideal input→output, then the new input. Best for consistent tone and structure.</p>

{box("tip", "Framework picker", "<p>RTF for speed · CRISPE for marketing · Few-shot for voice matching · Tree of Thoughts for strategy · CoT for analysis.</p>")}

{exercise("Upgrade a prompt", "<p>Take a vague prompt you used this month. Rewrite it with RTF and again with CRISPE. Compare outputs side by side.</p>")}
"""))

    # CH12 Prompt library - condensed but substantial
    parts.append(chapter("12", "Professional Prompt Library", f"""
<p class="lead">Copy, adapt, reuse. Replace bracketed fields. Keep winners in your AI Playbook.</p>

<h2>Marketing (12)</h2>
{prompt("Write 10 ad hooks for [product] targeting [audience]. Pain-focused, under 12 words each.")}
{prompt("Create a customer persona for [offer] with goals, fears, objections, and waterhole channels.")}
{prompt("Turn these features into benefits: [list]. Audience: [who]. Table format.")}
{prompt("Draft a launch email sequence (3 emails) for [product]. Goal: [trial/demo].")}
{prompt("Build a positioning statement: For [audience] who [problem], [brand] is [category] that [benefit]. Unlike [alt], we [difference].")}
{prompt("Generate 15 YouTube titles for [topic]—curiosity + clarity, no clickbait lies.")}
{prompt("Create a landing page outline with section goals and primary CTA.")}
{prompt("Write 5 retargeting ads based on objection: [objection].")}
{prompt("Produce a competitor teardown template, then fill it for [competitor] using provided notes.")}
{prompt("Suggest a 30-day content calendar for [brand] across LinkedIn + email.")}
{prompt("Rewrite this copy at an 8th-grade reading level without losing meaning: [paste].")}
{prompt("Give me a SWOT from these notes: [paste]. Be blunt.")}

<h2>Sales (8)</h2>
{prompt("Create a discovery-call script for [service] with qualifying questions and disqualifiers.")}
{prompt("Write objection responses for: price, timing, need to ask partner, already have vendor.")}
{prompt("Summarize this call transcript into next steps, risks, and a follow-up email.")}
{prompt("Draft a proposal one-pager from these notes: [paste].")}
{prompt("Role-play as a skeptical buyer. Interview me about [offer].")}
{prompt("Write a breakup email for stalled deals—polite, short, with an easy yes.")}
{prompt("Create a CRM note template fields for [sales motion].")}
{prompt("Map a 5-email nurture for cold leads interested in [topic].")}

<h2>Content &amp; social (10)</h2>
{prompt("Turn this outline into a 1,000-word blog post with examples and a checklist ending: [outline].")}
{prompt("Create a carousel outline (8 slides) teaching [topic].")}
{prompt("Repurpose this article into: LinkedIn post, X thread, newsletter blurb, short video script.")}
{prompt("Write 20 scroll-stopping first lines about [theme].")}
{prompt("Generate a content series plan: 6 parts, escalating difficulty.")}
{prompt("Create a brand voice chart: words we use / words we avoid for [brand].")}
{prompt("Draft community guidelines FAQ in friendly tone.")}
{prompt("Write a podcast episode outline with timestamps goals for [topic].")}
{prompt("Create thumbnail text options (3–4 words) for [video idea].")}
{prompt("Give me a hook-body-CTA template pack for short video.")}

<h2>Business &amp; ops (10)</h2>
{prompt("Draft an SOP for [process] with owner, trigger, steps, QA check, tools.")}
{prompt("Turn these messy notes into a decision log: [paste].")}
{prompt("Create a hiring scorecard for [role].")}
{prompt("Write a project kickoff agenda (45 min).")}
{prompt("Build a risk register from this plan: [paste].")}
{prompt("Draft a vendor evaluation rubric for [category].")}
{prompt("Create a weekly KPI review template for a small team.")}
{prompt("Write a customer apology email for [incident]—accountable, specific, no legalese fog.")}
{prompt("Generate onboarding checklist for new contractors.")}
{prompt("Summarize this policy into a 10-bullet employee cheat sheet: [paste].")}

<h2>Education &amp; research (8)</h2>
{prompt("Explain [concept] three ways: analogy, steps, common mistakes.")}
{prompt("Create a quiz (10 questions) from these notes with an answer key: [paste].")}
{prompt("Make a study schedule for [exam] on [date] with weak-area emphasis.")}
{prompt("Compare theories A and B in a table with practical implications.")}
{prompt("Extract definitions and key claims from this text; flag unsupported leaps.")}
{prompt("Create a lesson plan for 60 minutes on [topic] for beginners.")}
{prompt("Socratic tutor me on [topic]; ask one question at a time.")}
{prompt("Produce an annotated bibliography style summary from these abstracts: [paste].")}

<h2>Programming / technical (for beginners) (8)</h2>
{prompt("Explain this error like I’m new, then give fix steps: [error].")}
{prompt("Write pseudocode for [automation idea] before any real code.")}
{prompt("Review this script for security/privacy issues: [paste].")}
{prompt("Create a test plan for [feature].")}
{prompt("Translate this requirement into user stories + acceptance criteria.")}
{prompt("Suggest a simple architecture for [app idea] using no-code where possible.")}
{prompt("Document this function in plain language: [paste].")}
{prompt("Give a debugging checklist for [symptom].")}

<p class="small muted">That’s 56 ready prompts spanning the major work domains—extend each with your brand facts and examples (few-shot) for production quality.</p>

{actions([
  "Copy 15 prompts into your AI Playbook and fill brackets for your business.",
  "Create one few-shot block with 3 samples of your best writing.",
  "Run the same task with RTF and CRISPE; keep the better pattern."
])}
"""))

    parts.append(part("5", "AI Image Generation", "Images are now a language. Learn how diffusion models work at a practical level, then learn the prompt grammar that art directors use."))

    # CH13
    parts.append(chapter("13", "Introduction to AI Images", f"""
<p class="lead">Image models generate pictures from noise by gradually shaping random pixels toward your prompt. You steer with language—and increasingly with reference images.</p>

<h2>Diffusion in plain English</h2>
<p>Imagine reverse-blurring a messy TV signal until a clear photo appears—guided by your words. That’s the intuition behind diffusion models.</p>

<h2>Prompt structure that works</h2>
<ol>
  <li><strong>Subject:</strong> who/what</li>
  <li><strong>Action / pose:</strong> what’s happening</li>
  <li><strong>Setting:</strong> where / time</li>
  <li><strong>Style:</strong> photo, illustration, 3D, clay, editorial…</li>
  <li><strong>Lighting &amp; camera:</strong> softbox, golden hour, 35mm, top-down…</li>
  <li><strong>Quality cues:</strong> composition, texture, color grade</li>
  <li><strong>Negatives:</strong> what to avoid (when the tool supports it)</li>
</ol>

<table>
  <thead><tr><th>Tool</th><th>Best known for</th></tr></thead>
  <tbody>
    <tr><td>Midjourney</td><td>Aesthetic, artistic look</td></tr>
    <tr><td>Flux</td><td>Strong realism / controllable generation</td></tr>
    <tr><td>DALL·E (in ChatGPT)</td><td>Convenience + iterative chat edits</td></tr>
    <tr><td>Ideogram</td><td>Text in images</td></tr>
    <tr><td>Leonardo</td><td>Design workflows &amp; resources</td></tr>
  </tbody>
</table>

{box("warn", "Rights &amp; ethics", "<p>Avoid impersonating real private people, copying living artists’ names as a shortcut, and using generated marks that confuse brands. Check each tool’s commercial license.</p>")}
"""))

    # CH14
    parts.append(chapter("14", "Image Prompt Engineering", f"""
<p class="lead">Camera language upgrades results faster than adjective spam. Direct the shot like a brief to a photographer.</p>

<h2>Useful camera &amp; light vocabulary</h2>
<ul>
  <li><strong>Angles:</strong> eye-level, low angle, bird’s-eye, over-the-shoulder, Dutch angle</li>
  <li><strong>Lenses:</strong> 24mm environment, 35mm documentary, 85mm portrait, macro</li>
  <li><strong>Light:</strong> soft window light, hard noon sun, rim light, neon glow, overcast flat</li>
  <li><strong>Film/grade:</strong> Kodak Portra vibe, teal-orange grade, matte documentary</li>
</ul>

<h2>Character consistency tips</h2>
<ul>
  <li>Lock a written character sheet (age, face shape, hair, wardrobe).</li>
  <li>Use reference images / character features when the tool allows.</li>
  <li>Change one variable per revision (pose OR scene OR style).</li>
</ul>

<h2>80 image prompt starters</h2>
<p class="small">Copy and customize. Each line is a complete starter brief.</p>
<ol class="small">
  <li>Product photo of matte black water bottle on travertine, soft window light, 45° angle, subtle condensation, high-end catalog style</li>
  <li>Overhead flat lay of freelancer desk: laptop, notebook, coffee, plant, natural daylight, neat composition</li>
  <li>Founder portrait, 85mm, shallow depth of field, warm indoor ambient + soft key, confident smile, blurred office</li>
  <li>Isometric 3D illustration of tiny bakery shopfront, pastel clay materials, soft shadows</li>
  <li>Editorial photo of rainy Tokyo street at night, neon reflections, cinematic widescreen</li>
  <li>Kids’ picture-book illustration of a friendly fox reading a map, watercolor textures, cream paper</li>
  <li>UI mockup poster: fitness app dashboard on iPhone, soft gradient backdrop, clean modern marketing style</li>
  <li>Food photography: rustic sourdough loaf torn open, crumb detail, side light, dark moody backdrop</li>
  <li>Architecture exterior of small coastal cabin, dawn fog, 24mm, documentary realism</li>
  <li>Infographic-style illustration of AI workflow nodes connected by lines, minimal vector, teal accents on off-white</li>
  <li>Fashion lookbook shot, linen summer set, wind movement, golden hour beach path</li>
  <li>Macro photo of mechanical watch gears, specular highlights, black background</li>
  <li>Storyboard frame: courier handing package to customer, warm porch light, naturalistic</li>
  <li>Surreal collage poster: floating library rooms above a calm sea, paper-cut style</li>
  <li>Black-and-white street photo, decisive moment at crosswalk, high contrast</li>
  <li>3D render of eco detergent bottle, studio softbox, soft reflection on floor, commercial packshot</li>
  <li>Hand-drawn chalkboard menu style listing coffee drinks, charming imperfect lettering</li>
  <li>Fantasy concept art: mossy temple gate, volumetric god rays, wide establishing shot</li>
  <li>Medical explainer illustration of heart cross-section, clean textbook style, labeled areas blank</li>
  <li>Cozy café interior, morning light through blinds, empty table near window, lifestyle magazine</li>
  <li>Robot assistant gently watering plants in a home, friendly design, soft daylight, photoreal</li>
  <li>Vintage travel poster of Lisbon tram, limited color palette, mid-century graphic style</li>
  <li>YouTube thumbnail concept: shocked creator pointing at laptop chart, bold simple background, space for title text</li>
  <li>Transparent glass perfume bottle with botanical shadows, bright high-key studio</li>
  <li>Low-poly game art of mountain campsite at dusk</li>
  <li>Documentary portrait of artisan potter at wheel, dusty workshop, available light</li>
  <li>Abstract brand background: soft mesh gradients, grain, ample negative space for typography</li>
  <li>Kids STEM kit unboxing hero shot, bright even light, colorful components arranged neatly</li>
  <li>Cybersecurity concept: lock made of circuit traces, dark blue technical illustration</li>
  <li>Wedding invitation floral border, elegant line art, generous blank center</li>
  <li>Sports action still: amateur runner mid-stride, panning blur background, dawn road</li>
  <li>Interior design viz: small apartment living room, Scandinavian oak + olive textiles, photoreal</li>
  <li>Comic panel, 3-frame sequence of a barista learning an AI POS, clean ink, soft flat colors</li>
  <li>Satellite-style map illustration of a fictional walkable town, pastel legend-ready</li>
  <li>Luxury chocolate bar break reveal, shards and cocoa dust, dramatic side light</li>
  <li>Classroom scene redesign: collaborative tables, plants, natural light, architectural sketch overlay</li>
  <li>Podcast cover art: two hosts as bold vector portraits, limited palette, headphone motif</li>
  <li>Before/after cleaning service photo style: split composition of same kitchen, realistic</li>
  <li>Soft ceramic mug mockup floating on pastel backdrop for Shopify listing</li>
  <li>Cinematic still: solitary lighthouse, stormy sea, anamorphic lens flares subtle, film still</li>
  <li>Soft morning skincare shelfie, bathroom marble, gentle steam, lifestyle beauty ad</li>
  <li>Exploded-view illustration of a mechanical pencil, technical blueprint aesthetic</li>
  <li>Crowdfunding campaign hero: diverse makers around a workbench prototype, hopeful daylight</li>
  <li>Minimal logo mockup on craft paper bag, brand identity presentation style</li>
  <li>Night desk setup with dual monitors coding, practical RGB muted, cozy productivity mood</li>
  <li>Farm-to-table vegetable crate, outdoor market, crisp daylight, editorial food story</li>
  <li>App onboarding illustration set: three panels showing problem → tool → result, friendly flat design</li>
  <li>Historical museum exhibit photo style of ancient pottery, soft spotlight, dark gallery</li>
  <li>Electric bike on city street, motion blur background, lifestyle campaign, golden hour</li>
  <li>Handwritten journal open on linen, pen beside, soft top-down light, calm productivity aesthetic</li>
  <li>Paper craft diorama of a tiny office, miniature clay characters collaborating</li>
  <li>Glossy magazine cover mockup with bold typography space, fashion-tech theme</li>
  <li>Scientist and student collaborating at lab bench, hopeful documentary lighting</li>
  <li>Reusable packaging design flat lay: box, tissue, sticker, thank-you card</li>
  <li>Snowy cabin window view with steam mug foreground, cozy travel editorial</li>
  <li>Isometric map of online course journey milestones, clean infographic</li>
  <li>Vintage camera on wooden table, side window light, product lifestyle</li>
  <li>Community garden volunteers planting seedlings, authentic candid photo style</li>
  <li>Futuristic but grounded clinic reception, soft greens, human-centered design viz</li>
  <li>Stack of color-coded notebooks, overhead, stationery brand catalog</li>
  <li>Child building with blocks, shallow DOF, warm home interior, parenting brand</li>
  <li>Open laptop showing analytics dashboard, coffee and plant, creator workspace</li>
  <li>Hand-sewn leather wallet detail macro, artisan brand story</li>
  <li>City coworking space wide shot, natural light, inclusive modern workplace</li>
  <li>Illustrated recipe card layout with blank text areas, watercolor ingredients</li>
  <li>Drone-style still of coastal boardwalk, late afternoon haze, travel brochure</li>
  <li>Security professional reviewing wall of monitors, restrained cinematic teal grade</li>
  <li>Elegant dining table setting for two, candlelight, restaurant marketing</li>
  <li> Retro pixel-art scene of a tiny library interior</li>
  <li>Medical wearable on wrist, clean white product studio, clinical trustworthy</li>
  <li>Teachers’ lounge brainstorm wall with sticky notes, documentary candid</li>
  <li>Sustainable fashion rack of linen garments, airy boutique interior</li>
  <li>Board game night flat lay, colorful pieces, inviting social photo</li>
  <li>Architect model of courtyard housing, soft studio light, design presentation</li>
  <li>Close-up of violin bowing, concert hall bokeh, cultural arts poster</li>
  <li>Emergency go-bag contents organized on tarp, practical preparedness guide visual</li>
  <li>Soft clay character mascot waving, brand IP concept, studio softbox</li>
  <li>Rainy bus window portrait, reflective mood, indie film still</li>
  <li>Hydroponic indoor farm rows, clean tech-ag aesthetic, bright even light</li>
  <li>Thank-you card mockup with botanical border and empty center for message</li>
</ol>

{actions([
  "Build a one-page style card for your brand (palette, lighting, do/don’t).",
  "Generate the same subject in three styles; pick a house style.",
  "Save 10 winning prompts with the image filenames in your Playbook."
])}
"""))

    parts.append(part("6", "AI Video Generation", "Video models turn prompts—or still images—into motion. Treat them as pre-visualization and short-form engines, not overnight Hollywood."))

    # CH15-17
    parts.append(chapter("15", "Video AI Fundamentals", f"""
<p class="lead">Three input modes dominate: text-to-video, image-to-video, and video-to-video (restyle/extend). Pick based on control needs.</p>
<table>
  <thead><tr><th>Mode</th><th>You provide</th><th>Best when</th></tr></thead>
  <tbody>
    <tr><td>Text → video</td><td>Prompt only</td><td>Ideation, b-roll concepts</td></tr>
    <tr><td>Image → video</td><td>Key still + motion brief</td><td>You need visual consistency</td></tr>
    <tr><td>Video → video</td><td>Source clip</td><td>Style transfer, variations</td></tr>
  </tbody>
</table>
<p>Plan shots short (2–8 seconds). Write prompts like shot lists: subject, camera move, lighting, lens, pacing.</p>
{box("tip", "Production tip", "<p>Generate multiple takes, pick the best seconds, and edit traditionally. Hybrid workflows beat one-shot perfect clips.</p>")}
"""))

    parts.append(chapter("16", "Veo Guide", f"""
<p class="lead">Google Veo is a leading text/image-to-video model family. Prompt with cinematic language—camera, lens, motion, continuity.</p>

<h2>Prompt pattern</h2>
{prompt("""Shot type + subject + action + environment + camera movement + lighting + style + duration cue.
Example: "Medium shot of a ceramicist shaping clay on a wheel, slow dolly-in, soft morning window light, shallow depth of field, naturalistic documentary, subtle hand motion, 5 seconds."
""")}

<h2>Camera moves that read clearly</h2>
<ul>
  <li>Static tripod · slow push-in · pull-out · pan · tilt · orbit · tracking sideways · handheld subtle</li>
</ul>

<h2>40 Veo-ready examples</h2>
<ol class="small">
  <li>Product hero: bottle rotates on seamless infinity curve, soft studio lights, macro label detail</li>
  <li>Founder walks through bright studio, steadicam follow, candid confidence</li>
  <li>Coffee pour macro, steam rising, slow motion, warm café bokeh</li>
  <li>City dawn timelapse feel from rooftop, gentle pan across skyline</li>
  <li>Hands unboxing eco sneakers, top-down, crisp e-commerce lighting</li>
  <li>Teacher explains on whiteboard, locked-off camera, friendly classroom</li>
  <li>Drone-like rise over coastal path (keep motion physically plausible)</li>
  <li>Night market stalls, handheld wander, neon reflections on wet pavement</li>
  <li>Yoga flow silhouette at sunrise, side profile, calm pace</li>
  <li>Keyboard typing close-up for SaaS b-roll, shallow DOF</li>
  <li>Pet running through park toward camera, joyful, sunny</li>
  <li>Architect reviews blueprint on large table, overhead slow orbit</li>
  <li>EV charging at modern station, dusk, cinematic teal shadows</li>
  <li>Bread scoring and oven spring, rustic bakery documentary</li>
  <li>UI screen recording style recreation: cursor clicks through clean dashboard (abstracted)</li>
  <li>Rain on window with cozy room interior soft focus beyond</li>
  <li>Warehouse picker with handheld scanner, authentic logistics feel</li>
  <li>Kids STEM experiment volcano, playful, safe classroom energy</li>
  <li>Tailor pins a suit jacket, intimate workshop lamp light</li>
  <li>Farmers market vendor hands customer berries, warm sincerity</li>
  <li>Abstract particles forming a logo morph (keep simple geometry)</li>
  <li>Train window landscape sliding by, reflective mood</li>
  <li>Lab scientist pipettes sample, clinical bright lighting</li>
  <li>Street mural artist time-compressed painting strokes</li>
  <li>Quiet library aisle push-in toward sunlit desk</li>
  <li>Slow orbit around handmade ceramic bowl set, soft daylight studio</li>
  <li>Runner ties shoes at dawn trailhead, handheld intimate framing</li>
  <li>Chef plates pasta with tweezers, shallow DOF, restaurant kitchen glow</li>
  <li>Child’s hands planting a seed in soil, gentle educational tone</li>
  <li>Courier bike weaving carefully through quiet morning streets</li>
  <li>Open laptop on airplane tray, clouds beyond window, travel work mood</li>
  <li>Jewelry clasp close-up as necklace is fastened, luxury ad pacing</li>
  <li>Community volunteers painting a fence, documentary sunny afternoon</li>
  <li>Smart home thermostat interaction, clean modern interior, subtle push-in</li>
  <li>Bookstore aisle browse, warm practical light, cozy commerce feel</li>
  <li>Mechanic lowers EV hood, competent craftsmanship, natural garage light</li>
  <li>Waves wash over rocky shore, static tripod, meditative brand b-roll</li>
  <li>Makeup brush applies foundation, beauty macro, soft ring light</li>
  <li>Team huddle around whiteboard then disperse to desks, office energy</li>
  <li>Candle being lit in calm living room, slow and intimate evening mood</li>
</ol>

{actions(["Storyboard a 15-second ad as 3 shots.", "Generate each shot separately.", "Edit together with captions in a normal editor."])}
"""))

    parts.append(chapter("17", "Runway, Kling, Pika and Sora", f"""
<table>
  <thead><tr><th>Tool</th><th>Strengths</th><th>Watch-outs</th><th>Use when</th></tr></thead>
  <tbody>
    <tr><td><strong>Runway</strong></td><td>Creator suite, editing + gen tools</td><td>Credits; learning surface</td><td>Creative teams iterating clips</td></tr>
    <tr><td><strong>Kling</strong></td><td>Strong motion / cinematic clips</td><td>Access &amp; policy vary</td><td>Ambitious motion shots</td></tr>
    <tr><td><strong>Pika</strong></td><td>Fast social-style generation</td><td>Fine control limits</td><td>Quick ideation &amp; memes-to-motion</td></tr>
    <tr><td><strong>Sora</strong></td><td>High-end OpenAI video generation</td><td>Availability/limits</td><td>Premium text/image-to-video needs</td></tr>
    <tr><td><strong>Veo</strong></td><td>Google ecosystem video model</td><td>Access via Google products</td><td>Cinematic prompting + Google stack</td></tr>
  </tbody>
</table>
{box("tip", "Selection rule", "<p>Pick the tool you can actually access reliably, then master shot language. Prompt craft transfers; brand lock-in doesn’t have to.</p>")}
"""))

    parts.append(part("7", "AI Audio Generation", "Voice and music tools finish the content stack: narration, podcasts, explainers, and placeholder scores."))

    parts.append(chapter("18", "Voice AI", f"""
<p class="lead">Modern speech synthesis turns text into natural voiceovers. ElevenLabs and PlayHT are popular starting points.</p>
<h2>Workflow</h2>
{workflow("Voiceover", ["Write script", "Mark pauses", "Choose voice", "Generate", "Edit breaths/timing", "Mix under video"])}
<ul>
  <li>Write for the ear: shorter sentences, phonetic clarity, pronounceability.</li>
  <li>Add stage directions sparingly (“pause”, “warmer”).</li>
  <li>Keep a voice bible: voice ID, speed, stability settings.</li>
</ul>
{box("warn", "Consent &amp; cloning", "<p>Only clone voices you have rights and consent to use. Disclose synthetic voice when required by platform or law.</p>")}
{prompt("Script a 60-second product explainer for [product]. Friendly expert tone. Mark [PAUSE] where needed. Max 140 words.")}
"""))

    parts.append(chapter("19", "Music AI", f"""
<p class="lead">Suno and Udio generate songs from text prompts—useful for drafts, social beds, and creative exploration.</p>
{prompt("Upbeat indie-pop, 100 BPM, warm female vocals, song about learning AI without fear, clear chorus, radio-clean, no explicit content.")}
<ul>
  <li>Specify genre, tempo, mood, instruments, vocal type, and structure cues.</li>
  <li>Generate variants; treat outputs as drafts for licensing review.</li>
  <li>For client work, confirm commercial terms before publishing.</li>
</ul>
{box("tip", "Practical use", "<p>Use AI music for animatics and social tests; hire composers when brand identity and exclusivity matter.</p>")}
"""))

    parts.append(part("8", "AI Productivity", "The highest ROI is often boring: email, meetings, notes, and follow-ups. Make AI your operations intern."))

    parts.append(chapter("20", "Personal Productivity with AI", f"""
<h2>Meetings</h2>
<p>Record/transcribe (with permission) → summarize decisions, owners, deadlines → draft follow-up email.</p>
{prompt("From this transcript, produce: (1) 5-bullet summary, (2) decisions, (3) action table with owner + due date, (4) open questions. Flag anything unclear.")}

<h2>Email</h2>
<ul>
  <li>Paste the thread; ask for intent + draft reply options (short / detailed).</li>
  <li>Keep a tone pack: firm, warm, formal.</li>
</ul>

<h2>Research &amp; learning</h2>
{workflow("Learn a topic", ["Perplexity scan", "Save best sources", "NotebookLM notebook", "Teach-back to ChatGPT", "1-page cheat sheet"])}

<h2>Writing</h2>
<p>Outline with AI, draft yourself or co-draft, then ask for a critique against a checklist (clarity, specificity, claims).</p>

{takeaways(["Permission first on recordings.", "Summaries are drafts until you confirm owners/dates.", "Teach-back reveals what you didn’t learn."])}
"""))

    parts.append(chapter("21", "Business Productivity", f"""
<table>
  <thead><tr><th>Function</th><th>AI workflow</th></tr></thead>
  <tbody>
    <tr><td>Marketing</td><td>Brief → variants → critique → brand edit → schedule</td></tr>
    <tr><td>Support</td><td>Policy notebook → draft reply → human send for edge cases</td></tr>
    <tr><td>Sales</td><td>Call notes → CRM summary → personalized follow-up</td></tr>
    <tr><td>HR</td><td>Scorecards, JD drafts, onboarding checklists (watch bias)</td></tr>
    <tr><td>Operations</td><td>SOP drafting, incident timelines, vendor comparisons</td></tr>
  </tbody>
</table>
{box("mistake", "Business failure mode", "<p>Publishing unedited AI text that sounds generic—or worse, wrong—damages trust. AI accelerates drafts; humans own outcomes.</p>")}
{actions(["Pick one function above.", "Document a 5-step AI workflow.", "Run it for five real cases this week."])}
"""))

    parts.append(part("9", "AI Automation", "Automation connects apps so work happens without copy-paste. AI sits in the middle to classify, draft, or decide within guardrails."))

    parts.append(chapter("22", "Automation Fundamentals", f"""
<p class="lead">Every automation is: <strong>Trigger → (optional filters) → Actions</strong>. AI actions transform messy text into structured fields.</p>
<ul>
  <li><strong>Trigger:</strong> new email, form submit, schedule, webhook</li>
  <li><strong>Action:</strong> create task, send Slack, draft reply, update Sheet</li>
  <li><strong>API:</strong> how apps talk; no-code tools hide most of this</li>
</ul>
{box("tip", "Automation fitness test", "<p>Automate if you do it ≥3×/week, rules are clear, and mistakes are reversible or reviewed.</p>")}
{box("warn", "Guardrails", "<p>Start with drafts + human approval for anything external (customer email, social posts, payments).</p>")}
"""))

    parts.append(chapter("23", "n8n Complete Guide", f"""
<p class="lead">n8n is a flexible workflow automation tool, popular for builders who want control (self-host or cloud).</p>
<h2>Setup (conceptual)</h2>
<ol>
  <li>Choose cloud or self-hosted install.</li>
  <li>Connect credentials (OpenAI/Anthropic, Gmail, Slack, Sheets…).</li>
  <li>Build node-by-node; test with sample data.</li>
</ol>
<h2>10 workflow blueprints</h2>
<ol class="small">
  <li>Form → AI enrich lead → CRM row → Slack alert</li>
  <li>Support email → AI classify urgency → route mailbox/ticket</li>
  <li>RSS → AI summarize → newsletter draft Doc</li>
  <li>New Drive file → transcript/summary → Notion page</li>
  <li>Schedule: weekly metrics Sheet → AI narrative → email report</li>
  <li>Typeform feedback → sentiment tag → dashboard Sheet</li>
  <li>Twitter/X mention monitor → draft response queue</li>
  <li>Inbound invoice PDF → extract fields → accounting Sheet (review)</li>
  <li>Calendar end event → AI meeting notes template → task list</li>
  <li>Webhook from store → AI product blurb → Shopify draft (approval)</li>
</ol>
{workflow("n8n AI node pattern", ["Trigger", "Normalize text", "LLM extract JSON", "Validate fields", "Write to app", "Notify"])}
"""))

    parts.append(chapter("24", "Make Complete Guide", f"""
<p class="lead">Make (formerly Integromat) uses visual scenarios and modules—strong for marketers and ops teams.</p>
<h2>10 Make scenarios</h2>
<ol class="small">
  <li>Facebook Lead Ad → AI score → HubSpot + email nurture start</li>
  <li>Google Form job application → AI screen vs scorecard → Sheets + recruiter ping</li>
  <li>Instagram DM keyword → FAQ reply draft</li>
  <li>Shopify order → personalized thank-you email draft</li>
  <li>Intercom chat ended → summary to Notion QA log</li>
  <li>YouTube upload → AI chapters + description draft → notify editor</li>
  <li>Expense email receipt → extract → bookkeeping Sheet</li>
  <li>Webinar signup → AI segment → tailored sequence</li>
  <li>CSAT low score → create Zendesk ticket with context brief</li>
  <li>Content calendar row status=ready → generate social variants pack</li>
</ol>
{box("tip", "Make tip", "<p>Use routers and filters early. Keep AI modules deterministic with JSON schemas / strict formats.</p>")}
"""))

    parts.append(chapter("25", "Zapier Complete Guide", f"""
<p class="lead">Zapier is the friendliest entry point: Zaps connect thousands of apps quickly.</p>
<h2>10 Zaps to build</h2>
<ol class="small">
  <li>Gmail labeled “Speak” → AI draft reply → save to Drafts</li>
  <li>New Calendar event → prep brief from linked Doc</li>
  <li>Typeform → AI summary → Slack channel</li>
  <li>RSS → AI hook options → Buffer draft</li>
  <li>New CRM deal stage → generate kickoff checklist tasks</li>
  <li>Zoom recording ready → transcript summary → email attendees</li>
  <li>Airtable content idea → AI outline → Docs</li>
  <li>Shopify new product → AI SEO title/meta suggestions</li>
  <li>Help Scout tag “refund” → policy-aware draft (approval)</li>
  <li>Daily schedule Zap → AI prioritize task list from Todoist</li>
</ol>
{actions(["Build one Zap with a human approval step.", "Log failures for a week; tighten filters.", "Document the Zap in your Playbook."])}
"""))

    parts.append(part("10", "AI Agents", "Agents don’t just answer—they plan and use tools toward a goal. Powerful, but they need boundaries."))

    parts.append(chapter("26", "Understanding AI Agents", f"""
<p class="lead">An AI agent is a system that can set subgoals, call tools (browse, code, email, databases), remember state, and iterate until a stop condition.</p>
<h2>Architecture (beginner map)</h2>
<ul>
  <li><strong>Brain:</strong> LLM for planning and language</li>
  <li><strong>Tools:</strong> actions it may take</li>
  <li><strong>Memory:</strong> short-term thread + optional long-term store</li>
  <li><strong>Planner:</strong> break goal → steps → revisit</li>
  <li><strong>Guardrails:</strong> permissions, budgets, human approval</li>
</ul>
{box("warn", "Reality check", "<p>Unsupervised agents can loop, spend money, or message customers incorrectly. Start read-only or draft-only.</p>")}
"""))

    parts.append(chapter("27", "Building Agent Workflows", f"""
<h2>Practical examples</h2>
<ul>
  <li><strong>Research agent:</strong> gather sources → outline → brief (human publishes)</li>
  <li><strong>Support agent:</strong> retrieve policy → draft → escalate if confidence low</li>
  <li><strong>Marketing agent:</strong> pull product facts → generate campaign pack → Slack approval</li>
</ul>
{box("example", "Business pattern", "<p>Goal: “Prepare a weekly competitor brief.” Tools: web fetch, Drive write, email. Stop when a 1-page Doc exists. Human reviews every Friday.</p>")}
{workflow("Safe agent loop", ["Define goal", "Limit tools", "Require approval gates", "Log actions", "Review weekly"])}
{actions(["Write an agent spec: goal, tools, data access, success metric, kill switch.", "Implement as a Make/n8n flow before full autonomy."])}
"""))

    parts.append(part("11", "Real-World Projects", "Theory sticks when you ship. Twenty complete projects—steal the ones that match your goals."))

    # CH28 - 20 projects
    projects = [
        ("AI Content Creation Studio", "Publish 12 posts/month", "ChatGPT/Claude, Canva/Ideogram, Buffer", "Voice bible + calendar → batch drafts → image prompts → schedule", "Consistent pipeline; 4+ hours saved weekly"),
        ("Personal AI Research Desk", "Brief any topic in 45 minutes", "Perplexity, NotebookLM, Claude", "Search → save sources → notebook → 1-page brief", "Reusable research SOP"),
        ("Freelance Proposal Engine", "Faster, clearer proposals", "ChatGPT Projects, Notion", "Intake form → discovery summary → proposal draft → human price", "Higher close rate via clarity"),
        ("AI Customer Support Desk", "Faster first responses", "NotebookLM, Zendesk/Help Scout, Zapier", "Policy notebook → draft replies → approval → macros", "Lower first-response time"),
        ("Social Media Manager System", "Daily multi-platform presence", "Claude, Ideogram, scheduling tool", "Pillar content → atomize → visuals → schedule", "One idea → many assets"),
        ("YouTube / Shorts Factory", "Weekly video output", "ChatGPT, Veo/Runway, ElevenLabs, CapCut", "Script → voice → b-roll gen → edit → SEO package", "Faster packaging"),
        ("AI Marketing Offer Lab", "Test offers quickly", "ChatGPT, Perplexity, Sheets", "ICP research → offer variants → landing copy → ad hooks", "Structured experimentation"),
        ("Course Creator Companion", "Outline to lessons", "NotebookLM, Claude", "Source uploads → module map → lesson scripts → quizzes", "Complete curriculum skeleton"),
        ("Meeting OS", "Zero lost action items", "Fireflies/Zoom, ChatGPT, Todoist", "Transcript → actions → tasks → follow-up mail", "Accountability habit"),
        ("Sales Call Coach", "Improve discovery", "Claude, CRM", "Transcript critique vs scorecard → coaching notes", "Rep skill growth"),
        ("E-commerce Listing Booster", "Better PDPs", "ChatGPT, Ideogram, Shopify", "Feature list → benefits copy → image set → SEO fields", "Listing velocity"),
        ("HR Onboarding Kit", "Smoother new hires", "Gemini/Docs, Claude", "Role scorecard → 30-60-90 → FAQ notebook", "Less repeated questions"),
        ("Local Business Demo Package", "Sell AI services to SMBs", "Make/Zapier, ChatGPT", "Lead form automation + review response drafts + weekly report", "Productized freelance offer"),
        ("Investor Update Assistant", "Monthly updates in 30 min", "Sheets, Claude", "Metrics paste → narrative → risks → ask", "Consistent investor comms"),
        ("Podcast Production Pack", "Episode → assets", "Claude, ElevenLabs, Suno (optional)", "Outline → script → show notes → audiograms prompts", "Faster turnaround"),
        ("Grant / RFP Drafter", "Structured applications", "NotebookLM, Claude", "Requirements notebook → compliance matrix → draft answers", "Fewer missed criteria"),
        ("Personal Tutoring Bot", "Exam prep", "ChatGPT, NotebookLM", "Notes notebook → daily drills → weak-topic focus", "Measurable practice loop"),
        ("Brand Design Sprint", "Visual direction in a day", "Midjourney/Flux, Claude", "Mood prompts → select 3 directions → style card", "Aligned creative brief"),
        ("Ops SOP Library", "Document tribal knowledge", "Claude, Notion", "Interview transcript → SOP → checklist → quiz", "Trainable processes"),
        ("AI Automation Mini-Agency", "Retainers from workflows", "Make or n8n, LLM API", "Audit client tasks → 3 Zaps/scenarios → dashboard", "Recurring revenue offer"),
    ]

    proj_html = ['<p class="lead">Each project lists objective, tools, setup, workflow, and results. Adapt freely.</p>']
    for i, (name, obj, tools, wf, res) in enumerate(projects, 1):
        proj_html.append(f"""
<div class="project">
  <h3>Project {i}: {name}</h3>
  <p class="meta"><span class="badge">Objective</span> {obj} · <span class="badge">Tools</span> {tools}</p>
  <p><strong>Setup:</strong> Create a Project/folder, paste a one-paragraph brief, and add brand or policy sources.</p>
  <p><strong>Workflow:</strong> {wf}</p>
  <p><strong>Results:</strong> {res}</p>
</div>
""")

    proj_html.append(actions([
        "Pick one project and complete it in 7 days.",
        "Write a case study: before → after → hours saved.",
        "Productize your winning project as a freelance offer or internal SOP."
    ]))

    parts.append(chapter("28", "20 Complete AI Projects", "\n".join(proj_html)))

    parts.append(part("12", "The Future & Your Roadmap", "Tools will change. Your learning system shouldn’t. Finish with trends and a 12-month plan."))

    parts.append(chapter("29", "Future Trends", f"""
<ul>
  <li><strong>Agents:</strong> more tool-using assistants with workplace permissions</li>
  <li><strong>Multimodal:</strong> seamless text ↔ image ↔ audio ↔ video in one thread</li>
  <li><strong>Robotics:</strong> foundation models meeting physical hardware (slower, high impact)</li>
  <li><strong>AGI debate:</strong> progress continues; timelines uncertain—skills still compound</li>
  <li><strong>Careers:</strong> AI operators, automation specialists, AI product managers, domain experts who wield AI</li>
</ul>
{box("note", "Timeless skills", "<p>Problem framing, prompting, verification, workflow design, domain expertise, and ethics will outlast any single app.</p>")}
"""))

    parts.append(chapter("30", "AI Career Roadmap", f"""
<h2>Beginner (Months 1–3)</h2>
<ul>
  <li>Daily LLM practice; finish Parts 1–4 of this book</li>
  <li>Build Playbook with 30 prompts</li>
  <li>Ship 2 projects from Chapter 28</li>
</ul>
<h2>Intermediate (Months 4–8)</h2>
<ul>
  <li>Add image/video/audio for your niche</li>
  <li>Build 5 automations with approval gates</li>
  <li>Create a Custom GPT / Claude Project for your job</li>
  <li>Publish case studies</li>
</ul>
<h2>Advanced (Months 9–12)</h2>
<ul>
  <li>Design agentic workflows with logging and evals</li>
  <li>Specialize (support, marketing ops, research, education)</li>
  <li>Teach or consult; productize a service</li>
</ul>
<h2>12-month learning plan (summary)</h2>
<table>
  <thead><tr><th>Quarter</th><th>Focus</th><th>Proof</th></tr></thead>
  <tbody>
    <tr><td>Q1</td><td>LLM fluency + prompting</td><td>Playbook + 2 projects</td></tr>
    <tr><td>Q2</td><td>Multimodal content</td><td>Portfolio of assets</td></tr>
    <tr><td>Q3</td><td>Automation</td><td>5 live workflows</td></tr>
    <tr><td>Q4</td><td>Agents + specialization</td><td>Case study + offer</td></tr>
  </tbody>
</table>
{takeaways([
  "Practice daily in real work, not only demos.",
  "Proof beats certificates: projects, SOPs, metrics.",
  "Specialize after you have general fluency."
])}
{actions([
  "Block 30 minutes daily for AI practice this week.",
  "Choose your 12-month specialization hypothesis.",
  "Schedule a monthly review of your AI Playbook."
])}
<p class="colophon">You reached the end of <em>The Complete Beginner’s Guide to Artificial Intelligence</em> (2026 Handbook Edition). The tools will evolve—your ability to brief, verify, and build workflows is the durable advantage. Now open your AI Playbook and ship Project #1.</p>
"""))

    parts.append("""
</article>
</body>
</html>
""")
    return "".join(parts)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    html = build()
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html):,} bytes, ~{len(html.split()):,} words-ish)")


if __name__ == "__main__":
    main()
