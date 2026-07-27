#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Arabic RTL AI Beginner's Handbook — SCHOOLERX edition."""

from pathlib import Path

from expansions_ar import inject as inject_ar

OUT = Path("/workspace/book/ai-beginners-handbook.html")

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

:root {
  --ink: #1A2744;
  --navy: #1A2A40;
  --purple: #5B2C8B;
  --purple-deep: #3D1A6E;
  --orange: #FF7A00;
  --orange-hot: #FF4D00;
  --gold: #FFB800;
  --magenta: #E91E8C;
  --cyan: #00B4D8;
  --paper: #ffffff;
  --bg-soft: #F5F5F7;
  --rule: #E2E5EC;
  --muted: #5A6478;
  --font-ar: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
  --font-en: 'IBM Plex Sans', sans-serif;
  --font-mono: 'IBM Plex Mono', Consolas, monospace;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html {
  font-size: 11pt;
  direction: rtl;
}

body {
  font-family: var(--font-ar);
  color: var(--ink);
  background: #e8e9ef;
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
}

.en, .mono, code, .tool {
  font-family: var(--font-en);
  direction: ltr;
  unicode-bidi: isolate;
}

code, .mono {
  font-family: var(--font-mono);
  font-size: 0.86em;
  background: #f1f0f7;
  padding: 0.05em 0.28em;
  border-radius: 3px;
}

@media screen {
  body { padding: 20px 0 50px; }
  .book {
    width: 160mm;
    margin: 0 auto;
    background: var(--paper);
    box-shadow: 0 12px 40px rgba(26, 39, 68, 0.15);
  }
}

@page {
  size: 160mm 220mm;
  margin: 13mm 15mm 15mm 15mm;
  @bottom-center {
    content: counter(page);
    font-family: 'Cairo', sans-serif;
    font-size: 8.5pt;
    color: #7a8499;
  }
}

@page :first {
  margin: 0;
  @bottom-center { content: none; }
}

@media print {
  html, body { background: white; padding: 0; }
  .book { box-shadow: none; width: auto; margin: 0; }
  .no-print { display: none !important; }
  .part-opener, .cover, .toc-page, .front-matter { break-before: page; page-break-before: always; }
  .chapter { break-before: auto; margin-top: 1.1em; padding-top: 0.55em; border-top: 1px solid var(--rule); }
  #ch-1, #ch-3, #ch-4, #ch-10, #ch-13, #ch-15, #ch-18, #ch-20, #ch-22, #ch-26, #ch-28, #ch-29 {
    break-before: page; page-break-before: always; border-top: none; margin-top: 0; padding-top: 0;
  }
  .cover { break-before: avoid; page-break-before: avoid; }
  h1, h2, h3 { break-after: avoid; }
  .callout, .prompt, .workflow, .takeaway, .action-steps, .exercise { break-inside: avoid; }
}

.screen-toolbar {
  position: sticky; top: 0; z-index: 30;
  background: linear-gradient(90deg, var(--purple-deep), var(--navy));
  color: #fff;
  font-family: var(--font-ar);
  font-size: 13px;
  padding: 10px 16px;
  display: flex; justify-content: space-between; align-items: center; gap: 12px;
}
.screen-toolbar button {
  background: linear-gradient(90deg, var(--orange), var(--gold));
  color: #1a1030; border: none; padding: 7px 14px; border-radius: 6px;
  font-weight: 700; cursor: pointer; font-family: var(--font-ar); font-size: 12px;
}

/* Cover */
.cover {
  position: relative;
  width: 100%;
  height: 220mm;
  overflow: hidden;
  background: var(--bg-soft);
  break-after: page;
  page-break-after: always;
}
.cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  display: block;
}

/* Typography */
p { margin: 0 0 0.5em; orphans: 3; widows: 3; }
.lead { font-size: 1.02rem; color: var(--muted); margin-bottom: 0.75em; font-weight: 500; }

h1.chapter-title {
  font-size: 1.35rem; font-weight: 800; color: var(--navy);
  line-height: 1.25; margin: 0 0 0.35em; padding-bottom: 0.3em;
  border-bottom: 3px solid transparent;
  border-image: linear-gradient(270deg, var(--orange), var(--gold), var(--purple)) 1;
}
h2 {
  font-size: 1.05rem; font-weight: 700; color: var(--purple);
  margin: 0.9em 0 0.3em; line-height: 1.3;
}
h3 { font-size: 0.98rem; font-weight: 700; color: var(--navy); margin: 0.75em 0 0.25em; }
h4 { font-size: 0.9rem; font-weight: 700; color: var(--muted); margin: 0.6em 0 0.2em; }

ul, ol { margin: 0 0 0.7em 0; padding-inline-start: 1.2em; }
li { margin-bottom: 0.22em; }
li::marker { color: var(--orange); }

.chapter-num {
  font-size: 0.72rem; letter-spacing: 0.04em; color: var(--orange);
  font-weight: 700; margin-bottom: 0.2em;
}

.part-opener {
  padding: 0.5em 0 0.8em;
  background:
    radial-gradient(ellipse 70% 50% at 100% 0%, rgba(91,44,139,0.08), transparent 55%),
    radial-gradient(ellipse 50% 40% at 0% 100%, rgba(255,122,0,0.07), transparent 50%);
  border-radius: 8px;
  margin-bottom: 0.4em;
}
.part-label {
  font-size: 0.78rem; font-weight: 800; color: var(--purple);
  margin-bottom: 0.35em;
}
.part-opener h1 {
  font-size: 1.55rem; font-weight: 800; color: var(--navy);
  margin-bottom: 0.35em; line-height: 1.2;
}
.part-opener p { color: var(--muted); max-width: 36em; }

.toc-page h1, .front-matter .chapter-title {
  font-size: 1.4rem; font-weight: 800; color: var(--navy);
  margin-bottom: 0.8em; padding-bottom: 0.3em;
  border-bottom: 3px solid var(--orange);
}
.toc { list-style: none; margin: 0; padding: 0; }
.toc li {
  display: flex; align-items: baseline; gap: 0.35em;
  margin-bottom: 0.28em; font-size: 0.86rem;
}
.toc .toc-part {
  margin-top: 0.75em; margin-bottom: 0.3em;
  font-weight: 800; font-size: 0.78rem; color: var(--purple);
}
.toc .dots {
  flex: 1; border-bottom: 1px dotted var(--rule); margin: 0 0.15em 0.15em; min-width: 0.8em;
}

.callout {
  border-radius: 8px; padding: 0.55em 0.75em; margin: 0.55em 0 0.7em;
  font-size: 0.9rem; line-height: 1.5;
  border-inline-start: 4px solid;
  background: var(--bg-soft);
}
.callout-label {
  display: block; font-size: 0.68rem; font-weight: 800;
  letter-spacing: 0.02em; margin-bottom: 0.2em;
}
.tip { background: #FFF6EB; border-color: var(--orange); }
.tip .callout-label { color: var(--orange-hot); }
.note { background: #F4EEFA; border-color: var(--purple); }
.note .callout-label { color: var(--purple); }
.warn { background: #FDEBF4; border-color: var(--magenta); }
.warn .callout-label { color: var(--magenta); }
.example { background: #E8F8FC; border-color: var(--cyan); }
.example .callout-label { color: #087990; }
.mistake { background: #FFF0F0; border-color: #D32F2F; }
.mistake .callout-label { color: #C62828; }

.takeaway {
  background: linear-gradient(270deg, #F4EEFA, #fff);
  border: 1px solid #d9c8ec; border-radius: 8px;
  padding: 0.65em 0.8em; margin: 0.85em 0;
}
.takeaway h3 { margin-top: 0; color: var(--purple); font-size: 0.92rem; }

.action-steps {
  background: var(--bg-soft); border: 1px solid var(--rule);
  border-radius: 8px; padding: 0.65em 0.8em; margin: 0.7em 0 0.9em;
}
.action-steps h3 { margin-top: 0; font-size: 0.92rem; color: var(--navy); }

.prompt {
  font-family: var(--font-ar);
  font-size: 0.78rem; line-height: 1.45;
  background: var(--navy); color: #F0F4FA;
  padding: 0.6em 0.75em; border-radius: 8px;
  margin: 0.35em 0 0.6em;
  border-inline-start: 4px solid var(--orange);
  white-space: pre-wrap;
}
.prompt .en { color: #FFE0A3; }

table {
  width: 100%; border-collapse: collapse; margin: 0.5em 0 0.85em;
  font-size: 0.78rem; line-height: 1.4;
}
th, td {
  border: 1px solid var(--rule); padding: 0.38em 0.48em;
  text-align: right; vertical-align: top;
}
th {
  background: linear-gradient(90deg, var(--purple-deep), var(--purple));
  color: #fff; font-weight: 700;
}
tr:nth-child(even) td { background: #FAF8FC; }

.workflow {
  font-size: 0.82rem; background: #FAF8FC;
  border: 1px solid #e0d4f0; border-radius: 8px;
  padding: 0.55em 0.7em; margin: 0.5em 0 0.75em;
}
.workflow .flow {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.25em; margin-top: 0.35em;
}
.workflow .step {
  background: linear-gradient(90deg, #FFF1DE, #F4EEFA);
  color: var(--navy); padding: 0.18em 0.45em; border-radius: 4px; font-weight: 600;
}
.workflow .arrow { color: var(--orange); font-weight: 700; }

.exercise {
  border: 1px dashed var(--orange); border-radius: 8px;
  padding: 0.55em 0.75em; margin: 0.6em 0 0.85em; background: #FFFCFA;
}
.exercise h4 {
  margin-top: 0; color: var(--orange-hot); font-size: 0.78rem;
}

.project {
  border-inline-start: 4px solid var(--purple);
  padding: 0.1em 0 0.1em 0.7em; margin: 0.55em 0 0.85em;
}
.project h3 { margin-top: 0; }
.project .meta { font-size: 0.78rem; color: var(--muted); margin-bottom: 0.3em; }

.badge {
  display: inline-block; font-size: 0.68rem; font-weight: 800;
  background: #F4EEFA; color: var(--purple);
  padding: 0.12em 0.4em; border-radius: 4px; margin-inline-start: 0.2em;
}

.small { font-size: 0.86rem; }
.muted { color: var(--muted); }
.colophon { font-size: 0.88rem; color: var(--muted); margin-top: 1.4em; }

.hero-band {
  display: flex; gap: 0.4em; flex-wrap: wrap; margin: 0.6em 0 0.9em;
}
.hero-band span {
  background: var(--bg-soft); border: 1px solid var(--rule);
  border-radius: 999px; padding: 0.2em 0.65em;
  font-size: 0.72rem; font-weight: 700; color: var(--purple);
}
"""


def box(kind, label, html):
    return f'<div class="callout {kind}"><span class="callout-label">{label}</span>{html}</div>'


def prompt(text):
    return f'<div class="prompt">{text.strip()}</div>'


def takeaways(items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="takeaway"><h3>الخلاصة</h3><ul>{lis}</ul></div>'


def actions(items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="action-steps"><h3>خطوات عملية</h3><ol>{lis}</ol></div>'


def exercise(title, body):
    return f'<div class="exercise"><h4>تمرين — {title}</h4>{body}</div>'


def workflow(title, steps):
    parts = []
    for i, s in enumerate(steps):
        if i:
            parts.append('<span class="arrow">←</span>')
        parts.append(f'<span class="step">{s}</span>')
    return f'<div class="workflow"><strong>{title}</strong><div class="flow">{"".join(parts)}</div></div>'


def part(num, title, blurb):
    return f"""
<section class="part-opener" id="part-{num}">
  <div class="part-label">الجزء {num}</div>
  <h1>{title}</h1>
  <p>{blurb}</p>
</section>
"""


def chapter(num, title, body):
    body = inject_ar(str(num), body)
    return f"""
<section class="chapter" id="ch-{num}">
  <div class="chapter-num">الفصل {num}</div>
  <h1 class="chapter-title">{title}</h1>
  {body}
</section>
"""


def build():
    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="author" content="SCHOOLERX"/>
<title>الذكاء الاصطناعي — الدليل الشامل للمبتدئين | SCHOOLERX</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="screen-toolbar no-print">
  <span><strong>الذكاء الاصطناعي</strong> · دليل SCHOOLERX · معاينة الطباعة (160×220 مم)</span>
  <button onclick="window.print()">طباعة / حفظ PDF</button>
</div>
<article class="book">
""")

    # COVER with image
    parts.append("""
<section class="cover" id="cover">
  <img src="assets/cover.png" alt="غلاف كتاب الذكاء الاصطناعي — الدليل الشامل للمبتدئين — SCHOOLERX"/>
</section>
""")

    # FRONT MATTER
    parts.append("""
<section class="front-matter" id="how-to-use">
  <div class="chapter-num">مقدمة</div>
  <h1 class="chapter-title">كيف تستخدم هذا الكتاب؟</h1>
  <p class="lead">هذا الدليل صُمم للمبتدئين تماماً. ستتعلم ما هو الذكاء الاصطناعي، وكيف تختار الأداة المناسبة، وكيف تكتب أوامر قوية، وكيف تطبق <span class="en">AI</span> في عملك اليومي — دون الحاجة لأي خلفية تقنية.</p>
  <div class="hero-band">
    <span>ChatGPT</span><span>Claude</span><span>Gemini</span><span>Perplexity</span>
    <span>NotebookLM</span><span>Veo</span><span>n8n</span><span>Make</span><span>Zapier</span>
  </div>
  <h2>لمن هذا الكتاب؟</h2>
  <p>الطلاب، المستقلون، رواد الأعمال، أصحاب المشاريع، المسوّقون، صنّاع المحتوى، موظفو المكاتب، وكل من يريد استخدام الذكاء الاصطناعي بثقة.</p>
  <h2>ماذا ستستطيع أن تفعل؟</h2>
  <ul>
    <li>تشرح مفاهيم الذكاء الاصطناعي بلغة بسيطة وتختار الأداة المناسبة لكل مهمة</li>
    <li>تستخدم ChatGPT و Claude و Gemini و Perplexity و NotebookLM باحتراف</li>
    <li>تكتب أوامر (Prompts) قوية للكتابة والبحث والتسويق والتحليل</li>
    <li>تولّد صوراً وفيديوهات وصوتيات بأدوات حديثة</li>
    <li>تبني أتمتة بسيطة وتفهم وكلاء الذكاء الاصطناعي (Agents)</li>
    <li>تنفّذ مشاريع عملية يمكنك بيعها أو استخدامها فوراً</li>
  </ul>
  """ + box("tip", "نصيحة SCHOOLERX", "<p>أنشئ ملفاً اسمه <strong>دفتر أوامر الذكاء الاصطناعي</strong>. بعد كل فصل احفظ أفضل الأوامر وسير العمل. في نهاية الكتاب ستمتلك نظام تشغيل شخصياً للذكاء الاصطناعي.</p>") + """
  <h2>ملاحظات الطباعة</h2>
  <p>الملف مُحسَّن لحجم <strong>160 × 220 مم</strong>. من المتصفح: طباعة ← حفظ كـ PDF ← فعّل خلفيات الرسومات.</p>
  <p class="muted small">من إعداد <strong class="en">SCHOOLERX</strong> · إصدار 2026</p>
</section>
""")

    # TOC
    parts.append("""
<section class="toc-page" id="toc">
  <h1>المحتويات</h1>
  <ul class="toc">
    <li class="toc-part">الجزء 1 — فهم الذكاء الاصطناعي</li>
    <li><span>1. ما هو الذكاء الاصطناعي؟</span><span class="dots"></span></li>
    <li><span>2. كيف يعمل الذكاء الاصطناعي الحديث؟</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 2 — منظومة الأدوات</li>
    <li><span>3. فهم فئات أدوات الذكاء الاصطناعي</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 3 — الأدوات الأساسية</li>
    <li><span>4. نماذج اللغة الكبيرة (LLM)</span><span class="dots"></span></li>
    <li><span>5. دليل ChatGPT الشامل</span><span class="dots"></span></li>
    <li><span>6. دليل Claude الشامل</span><span class="dots"></span></li>
    <li><span>7. دليل Gemini الشامل</span><span class="dots"></span></li>
    <li><span>8. دليل Perplexity الشامل</span><span class="dots"></span></li>
    <li><span>9. دليل NotebookLM الشامل</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 4 — هندسة الأوامر</li>
    <li><span>10. أساسيات هندسة الأوامر</span><span class="dots"></span></li>
    <li><span>11. أُطر كتابة الأوامر</span><span class="dots"></span></li>
    <li><span>12. مكتبة أوامر احترافية</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 5 — توليد الصور</li>
    <li><span>13. مقدمة إلى صور الذكاء الاصطناعي</span><span class="dots"></span></li>
    <li><span>14. هندسة أوامر الصور</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 6 — توليد الفيديو</li>
    <li><span>15. أساسيات فيديو الذكاء الاصطناعي</span><span class="dots"></span></li>
    <li><span>16. دليل Veo</span><span class="dots"></span></li>
    <li><span>17. Runway و Kling و Pika و Sora</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 7 — الصوت</li>
    <li><span>18. الذكاء الاصطناعي الصوتي</span><span class="dots"></span></li>
    <li><span>19. موسيقى الذكاء الاصطناعي</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 8 — الإنتاجية</li>
    <li><span>20. الإنتاجية الشخصية</span><span class="dots"></span></li>
    <li><span>21. إنتاجية الأعمال</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 9 — الأتمتة</li>
    <li><span>22. أساسيات الأتمتة</span><span class="dots"></span></li>
    <li><span>23. دليل n8n</span><span class="dots"></span></li>
    <li><span>24. دليل Make</span><span class="dots"></span></li>
    <li><span>25. دليل Zapier</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 10 — الوكلاء</li>
    <li><span>26. فهم وكلاء الذكاء الاصطناعي</span><span class="dots"></span></li>
    <li><span>27. بناء سير عمل الوكلاء</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 11 — المشاريع</li>
    <li><span>28. عشرون مشروعاً كاملاً</span><span class="dots"></span></li>
    <li class="toc-part">الجزء 12 — المستقبل</li>
    <li><span>29. توجهات المستقبل</span><span class="dots"></span></li>
    <li><span>30. خارطة طريق مهنية</span><span class="dots"></span></li>
  </ul>
</section>
""")

    parts.append(part("1", "فهم الذكاء الاصطناعي", "ابدأ من هنا. ستفهم ما هو الذكاء الاصطناعي فعلاً، ولماذا أصبح في كل مكان، وكيف تنتج الأنظمة الحديثة إجابات مفيدة من أنماط البيانات."))

    parts.append(chapter("1", "ما هو الذكاء الاصطناعي؟", f"""
<p class="lead">الذكاء الاصطناعي (<span class="en">Artificial Intelligence — AI</span>) هو برمجيات تؤدي مهاماً كانت تتطلب ذكاءً بشرياً: فهم اللغة، التعرف على الصور، تقديم التوصيات، أو إنشاء محتوى جديد.</p>
<h2>التعريف</h2>
<p>فكّر في الذكاء الاصطناعي كمحرك سريع جداً لمطابقة الأنماط. يدرس كميات هائلة من الأمثلة، يتعلم علاقات إحصائية، ثم يطبقها على مواقف جديدة. هو لا «يفكر» كالإنسان — لكنه ينتج مخرجات تبدو ذكية عند توجيهه جيداً.</p>
{box("example", "مثال واقعي", "<p>عندما يقترح Netflix فيلماً، أو يرتّب YouTube الفيديو التالي، أو يتوقع Google Maps الزحام — فإن نموذج ذكاء اصطناعي يقارن سلوكك بأنماط تعلمها من ملايين المستخدمين.</p>")}
<h2>تاريخ مختصر (النسخة المفيدة)</h2>
<ul>
  <li><strong>الخمسينات–الثمانينات:</strong> أنظمة قواعد ومنطق مكتوبة يدوياً.</li>
  <li><strong>التسعينات–2010:</strong> تعلّم آلي من البيانات (فلاتر البريد، التوصيات).</li>
  <li><strong>2012+:</strong> التعلّم العميق جعل التعرف على الصور والصوت عملياً.</li>
  <li><strong>2017+:</strong> معماريات Transformers فتحت باب نماذج اللغة الحديثة.</li>
  <li><strong>2022–2026:</strong> الذكاء الاصطناعي التوليدي أصبح يومياً — ChatGPT والصور والفيديو والوكلاء.</li>
</ul>
<h2>ثلاثة أنواع يجب أن تعرفها</h2>
<table>
<thead><tr><th>النوع</th><th>المعنى</th><th>مثال</th></tr></thead>
<tbody>
<tr><td><strong>ذكاء ضيق</strong></td><td>ممتاز في مهمة محددة</td><td>فلتر سبام، فتح بالوجه</td></tr>
<tr><td><strong>توليدي</strong></td><td>ينشئ نصاً/صوراً/صوتاً/فيديو</td><td>ChatGPT، Midjourney، Veo</td></tr>
<tr><td><strong>عام (AGI)</strong></td><td>ذكاء مرن بمستوى بشري</td><td>غير موجود بعد كمنتج</td></tr>
</tbody>
</table>
<h2>لماذا يهم الآن؟</h2>
<p>تحسّنت النماذج، وأصبحت الواجهات بمحادثة بسيطة، واتصلت بالبريد والمستندات والمتصفح. النتيجة: طبقة إنتاجية يومية وليس موضوع مختبر فقط.</p>
<h3>أين تستخدمه بالفعل؟</h3>
<table>
<thead><tr><th>المنتج</th><th>ماذا يفعل الذكاء الاصطناعي؟</th></tr></thead>
<tbody>
<tr><td>Netflix / YouTube / TikTok</td><td>يرتب المحتوى ليبقيك متابعاً</td></tr>
<tr><td>Google Maps</td><td>يتوقع المسارات والازدحام</td></tr>
<tr><td>Amazon</td><td>يوصي بالمنتجات ويكشف الاحتيال</td></tr>
<tr><td>التطبيقات البنكية</td><td>يرصد عمليات غير معتادة</td></tr>
<tr><td>الرعاية الصحية</td><td>يساعد في التصوير والتوثيق</td></tr>
</tbody>
</table>
{box("mistake", "خرافة ← حقيقة", """
<ul>
<li><strong>«الذكاء الاصطناعي واعٍ.»</strong> لا. هو يتنبأ بالكلمات أو البكسلات التالية.</li>
<li><strong>«دائماً يقول الحقيقة.»</strong> لا. قد يخترع إجابات بثقة (هلوسة).</li>
<li><strong>«سيستبدل كل الوظائف فوراً.»</strong> يغيّر المهام أولاً؛ من يستخدمه يتفوق على من يتجاهله.</li>
<li><strong>«تحتاج للبرمجة.»</strong> لا. واجهة المحادثة كافية للبداية.</li>
</ul>
""")}
{takeaways([
  "الذكاء الاصطناعي مطابقة أنماط وتوليد على نطاق واسع — ليس وعياً بشرياً.",
  "أدوات اليوم ذكاء ضيق / توليدي.",
  "أنت تستخدمه يومياً؛ المهارة الجديدة هي توجيهه بوعي.",
  "تحقق دائماً من الحقائق المهمة."
])}
{actions([
  "اكتب خمسة تطبيقات تستخدمها يومياً وحدد أين يساعد الذكاء الاصطناعي.",
  "افتح ChatGPT أو Claude أو Gemini واسأل: «اشرح لي الذكاء الاصطناعي كأنني في الـ14 مع 3 أمثلة يومية.»",
  "أنشئ دفتر أوامرك الشخصي."
])}
{exercise("اكتشف الذكاء الاصطناعي من حولك", "<p>اختر موقعاً للتسوق وتطبيقاً اجتماعياً. اكتب ثلاثة قرارات ذكية يتخذها كل منتج لأجلك (توصيات، ترتيب، بحث).</p>")}
"""))

    parts.append(chapter("2", "كيف يعمل الذكاء الاصطناعي الحديث؟", f"""
<p class="lead">لا تحتاج شهادة علوم حاسوب. تحتاج نموذجاً ذهنياً بسيطاً حتى يتوقف السحر ويبدأ التحكم.</p>
<h2>خمسة أركان</h2>
<ol>
  <li><strong>البيانات:</strong> نصوص، صور، صوت، أمثلة يتعلم منها النظام.</li>
  <li><strong>التدريب:</strong> ضبط ملايين/مليارات المعاملات الداخلية لتحسين التنبؤ.</li>
  <li><strong>النموذج:</strong> «العقل» المدرَّب الذي يستجيب لمدخلات جديدة.</li>
  <li><strong>الاستدلال:</strong> استخدام النموذج للإجابة على أمرك.</li>
  <li><strong>الأدوات والاسترجاع:</strong> بحث ويب، ملفاتك، حاسبات، تطبيقات.</li>
</ol>
{box("note", "تشبيه", "<p>التدريب كالدراسة لسنوات. الاستدلال كأداء امتحان مفتوح في ثوانٍ. الاسترجاع كأن يُسمح لك بفتح ملف ملاحظات محدد أثناء الامتحان.</p>")}
<h2>الشبكات العصبية والتعلم العميق</h2>
<p>طبقات من وحدات حسابية بسيطة. الطبقات الأولى تلتقط أنماطاً بسيطة، واللاحقة أنماطاً أعقد (حروف ← كلمات ← أفكار).</p>
<h2>Transformers والرموز Context</h2>
<p>معمارية Transformers خلف نماذج اللغة الكبيرة. حيلتها الأساسية هي <strong>الانتباه</strong>: معرفة أي كلمات مهمة للتنبؤ. النماذج تقرأ <strong>Tokens</strong> (قطع نص) وليس كلمات فقط. <strong>نافذة السياق</strong> هي حجم الذاكرة القصيرة لما يمكن أن يراه النموذج دفعة واحدة.</p>
<table>
<thead><tr><th>المفهوم</th><th>ببساطة</th><th>لماذا يهمك؟</th></tr></thead>
<tbody>
<tr><td>Parameters</td><td>أوزان داخلية متعلَّمة</td><td>الأكبر ليس دائماً الأفضل</td></tr>
<tr><td>Context window</td><td>الذاكرة العاملة</td><td>تحدد كم يمكنك لصقه مرة واحدة</td></tr>
<tr><td>Fine-tuning</td><td>تدريب إضافي لتخصص</td><td>يحسّن أسلوباً أو مهمة ضيقة</td></tr>
<tr><td>RAG / استرجاع</td><td>جلب مصادر ثم الإجابة</td><td>يربط الإجابات بملفاتك أو الويب</td></tr>
<tr><td>هلوسة</td><td>خطأ بثقة عالية</td><td>تحقق من الأرقام والاقتباسات</td></tr>
</tbody>
</table>
{box("tip", "تطبيق عملي", "<p>80٪ من نتائج المبتدئين تأتي من أوامر أفضل + مصادر أفضل — لا من تبديل النماذج كل أسبوع.</p>")}
{takeaways([
  "النماذج تتنبأ بأنماط؛ ليست قاعدة بيانات حقيقة واحدة افتراضياً.",
  "الرموز ونوافذ السياق تضع حدوداً صلبة.",
  "الاسترجاع والأدوات يقللان الهلوسة عند الحاجة للدقة.",
  "الأمر (Prompt) هو سطح التحكم الأساسي لديك."
])}
"""))

    parts.append(part("2", "منظومة أدوات الذكاء الاصطناعي", "الذكاء الاصطناعي ليس تطبيقاً واحداً. هذه خريطة تساعدك على الاختيار بدل جمع الاشتراكات عشوائياً."))

    parts.append(chapter("3", "فهم فئات أدوات الذكاء الاصطناعي", f"""
<p class="lead">عندما يقول أحدهم «أستخدم الذكاء الاصطناعي» اسأله: أي فئة؟ النص، البحث، الصور، الفيديو، الصوت، البرمجة، الإنتاجية، الأتمتة، أم الوكلاء؟</p>
<table>
<thead><tr><th>الفئة</th><th>أمثلة</th><th>أفضل استخدام</th></tr></thead>
<tbody>
<tr><td>توليد النص</td><td>ChatGPT، Claude، Gemini، DeepSeek</td><td>الكتابة والتفكير والتخطيط</td></tr>
<tr><td>بحث ذكي</td><td>Perplexity، You.com</td><td>أسئلة حديثة مع مصادر</td></tr>
<tr><td>بحث عميق / ملفات</td><td>NotebookLM، أوضاع Research</td><td>تقارير ودراسة مصادرك</td></tr>
<tr><td>صور</td><td>Midjourney، Flux، DALL·E، Ideogram</td><td>إعلانات، ثمنيلز، مفاهيم</td></tr>
<tr><td>فيديو</td><td>Veo، Sora، Runway، Kling، Pika</td><td>مقاطع قصيرة وستوري بورد</td></tr>
<tr><td>صوت</td><td>ElevenLabs، Suno، Udio</td><td>تعليق صوتي وموسيقى مسودة</td></tr>
<tr><td>برمجة</td><td>Cursor، Copilot، Replit AI</td><td>بناء برمجيات أسرع</td></tr>
<tr><td>إنتاجية</td><td>Notion AI، Grammarly، Fireflies</td><td>اجتماعات وبريد وملاحظات</td></tr>
<tr><td>أتمتة</td><td>Make، Zapier، n8n</td><td>ربط التطبيقات بسير عمل</td></tr>
<tr><td>وكلاء</td><td>OpenAI Agents، Autogen workflows</td><td>أهداف متعددة الخطوات (بإشراف)</td></tr>
</tbody>
</table>
{box("tip", "حزمة البداية لمعظم الناس", "<p><strong>ChatGPT أو Claude</strong> (تفكير/كتابة) + <strong>Perplexity</strong> (بحث ويب) + <strong>NotebookLM</strong> (ملفاتك) + أداة صور واحدة. أضف الأتمتة فقط عندما تتكرر مهمة أسبوعياً.</p>")}
{actions([
  "اكتب أهم 10 مهام متكررة في عملك.",
  "صنّف كل مهمة ضمن فئة من هذا الفصل.",
  "اختر فجوة واحدة وثبّت الأداة الناقصة هذا الأسبوع فقط."
])}
"""))

    parts.append(part("3", "الأدوات الأساسية", "خمس أدوات تغطي معظم العمل من مبتدئ إلى محترف. أتقنها مرة؛ وستنقل المهارة إلى أي أداة لاحقة."))

    parts.append(chapter("4", "نماذج اللغة الكبيرة (LLM)", f"""
<p class="lead">نموذج اللغة الكبير هو محرك مدرَّب على نصوص هائلة للتنبؤ باللغة وتوليدها. الشات بوت واجهة؛ و<span class="en">LLM</span> هو المحرك.</p>
<table>
<thead><tr><th>العائلة</th><th>الشركة</th><th>نقطة القوة</th></tr></thead>
<tbody>
<tr><td><strong>GPT</strong></td><td>OpenAI</td><td>شامل، أدوات، منظومة واسعة</td></tr>
<tr><td><strong>Claude</strong></td><td>Anthropic</td><td>سياق طويل وكتابة دقيقة</td></tr>
<tr><td><strong>Gemini</strong></td><td>Google</td><td>اندماج مع Google Workspace</td></tr>
<tr><td><strong>DeepSeek / Llama / Mistral</strong></td><td>متعددة</td><td>قيمة، أوزان مفتوحة، كفاءة</td></tr>
</tbody>
</table>
{box("warn", "خصوصية", "<p>لا تلصق أسراراً أو كلمات مرور أو بيانات مالية غير منشورة أو بيانات أشخاص آخرين في أدوات استهلاكية إلا إذا سمحت خطتك وسياستك بذلك.</p>")}
{takeaways(["LLM = محرك لغة؛ الشات = منتج بأدوات وواجهة.", "اختر حسب سير عملك لا حسب الضجيج.", "استخدم أوضاع البحث/التفكير عند الحاجة."])}
"""))

    parts.append(chapter("5", "دليل ChatGPT الشامل", f"""
<p class="lead">ChatGPT هو المنزل الأول لكثير من المبتدئين: محادثة، صياغة، تحليل، صور، صوت، وأدوات مخصصة.</p>
<h2>البداية</h2>
<ol>
  <li>أنشئ حساباً من الموقع الرسمي.</li>
  <li>ابدأ بالمجان لتتعلم؛ رقِّ خطتك عند الحاجة لحدود أعلى أو نماذج أقوى.</li>
  <li>اضبط التعليمات المخصصة: من أنت؟ وكيف تريد الإجابات؟</li>
</ol>
<h2>ميزات مهمة</h2>
<table>
<thead><tr><th>الميزة</th><th>استخدمها لـ</th></tr></thead>
<tbody>
<tr><td>Projects</td><td>تجميع محادثات وملفات لمشروع واحد</td></tr>
<tr><td>Memory</td><td>تذكر تفضيلاتك (راجعها دورياً)</td></tr>
<tr><td>Canvas</td><td>تحرير مستندات طويلة جنباً إلى جنب</td></tr>
<tr><td>Search / Deep Research</td><td>معلومات أحدث وتقارير أوسع</td></tr>
<tr><td>Images / Voice / Custom GPTs</td><td>صور، صوت، متخصصون قابلون لإعادة الاستخدام</td></tr>
</tbody>
</table>
{workflow("تسليم للعميل", ["موجز في Project", "هيكل", "مسودة", "نقد", "صيغة نهائية"])}
{prompt("""أنت محرر تسويق أول.
الهدف: كتابة قسم Hero لصفحة هبوط لتطبيق ميزانية للمستقلين.
الجمهور: مستقلون 25–40 يشعرون بإرهاق الضرائب.
النبرة: واضحة وواثقة بلا مبالغة.
المطلوب: عنوان + عنوان فرعي + 3 فوائد + زر CTA.
قيود: العنوان أقل من 60 حرفاً؛ تجنب كلمات مثل «ثوري».
""")}
<h2>30 مثالاً عملياً</h2>
<ol class="small">
<li>إعادة كتابة بريد ليصبح أقصر وألطف</li>
<li>تحويل ملاحظات اجتماع إلى مهام بمالكين</li>
<li>خطة دراسة لامتحان بتاريخ محدد</li>
<li>مقارنة منتجين في جدول</li>
<li>أسئلة مقابلة لوظيفة</li>
<li>منشور LinkedIn من نقاط</li>
<li>تلخيص عقد بلغة بسيطة (ثم مراجعة قانونية)</li>
<li>تقويم محتوى لـ 30 يوماً</li>
<li>سيناريو تفاوض لزيادة راتب</li>
<li>بطاقات مراجعة من ملاحظات محاضرة</li>
<li>عناوين SEO ووصف Meta</li>
<li>استبيان عملاء من 10 أسئلة</li>
<li>تمثيل دور عميل غاضب</li>
<li>تحويل مقال إلى سلسلة تغريدات</li>
<li>خط زمني لمشروع غامض</li>
<li>مسودة متطلبات منتج</li>
<li>تبسيط فقرة تقنية للمدراء</li>
<li>أسماء علامة تجارية مقترحة</li>
<li>ملاحظات بودكاست جاهزة</li>
<li>ردود على اعتراضات المبيعات</li>
<li>تحليل سيرة ذاتية مقابل وظيفة</li>
<li>إجراءات تشغيلية من وصف فوضوي</li>
<li>أجندة ورشة عمل بتوقيتات</li>
<li>ملخص تنفيذي من ملاحظات تحليلات</li>
<li>قائمة مراجعة أسبوعية شخصية</li>
<li>إعادة كتابة صفحة «من نحن» بثلاث نبرات</li>
<li>استخراج أسئلة شائعة من مركز مساعدة</li>
<li>بطاقة منافسة من ملاحظات</li>
<li>رسائل ترحيب لتجربة SaaS</li>
<li>قالب التقاط معرفة شخصية</li>
</ol>
{box("mistake", "أخطاء شائعة", "<ul><li>أمر غامض لمرة واحدة («اكتب خطة تسويق»).</li><li>تصديق مصادر دون فتحها.</li><li>وضع بيانات سرية في المحادثة.</li><li>عدم التكرار — الجودة غالباً في المسودة 2–4.</li></ul>")}
{actions(["اضبط التعليمات المخصصة اليوم.", "أنشئ Project لمجال عملك الرئيسي.", "احفظ خمسة أوامر في دفترك."])}
"""))

    parts.append(chapter("6", "دليل Claude الشامل", f"""
<p class="lead">يتفوق Claude في المستندات الطويلة، التحليل الحذر، الكتابة المتأنية، و<span class="en">Artifacts</span> القابلة للمراجعة.</p>
<ul>
<li><strong>سياق طويل:</strong> تقارير وفصول وملخصات كود</li>
<li><strong>Projects:</strong> تعليمات ومعرفة ثابتة لمساحة عمل</li>
<li><strong>Artifacts:</strong> مستند أو كود أو أداة صغيرة في لوحة جانبية</li>
</ul>
{workflow("مقال طويل", ["الصق الموجز والمصادر", "اطلب هيكلاً", "وافق عليه", "اكتب قسماً بقسم", "حرر للصوت"])}
{prompt("""تعليمات المشروع: أنت شريكي التحريري لمحتوى عملي.
دائماً: اسأل إن كان الموجز غامضاً؛ فضّل أمثلة ملموسة؛ أشر إلى الادعاءات غير المدعومة.
الجمهور الافتراضي: مبتدئون أذكياء.
""")}
{box("tip", "متى تختار Claude؟", "<p>عندما يكون المدخل طويلاً أو يجب أن يبدو النص بشرياً ودقيقاً. اختر بحثاً ذكياً أولاً إن احتجت مصادر ويب حية.</p>")}
"""))

    parts.append(chapter("7", "دليل Gemini الشامل", f"""
<p class="lead">قيمة Gemini تظهر بقوة إن كان عملك يعيش في Gmail و Docs و Drive و Workspace.</p>
<table>
<thead><tr><th>التطبيق</th><th>استخدام عالي القيمة</th></tr></thead>
<tbody>
<tr><td>Gmail</td><td>مسودات ردود، اختصار خيوط، استخراج مهام</td></tr>
<tr><td>Docs</td><td>هيكلة، إعادة كتابة، تلخيص تعليقات</td></tr>
<tr><td>Drive</td><td>أسئلة عبر ملفاتك المتاحة</td></tr>
<tr><td>Sheets</td><td>شرح صيغ وخطط تنظيف أعمدة</td></tr>
</tbody>
</table>
{workflow("من بريد فوضوي إلى خطة", ["اختر الخيط", "لخّص القرارات", "صغ رداً", "أنشئ قائمة مهام", "جدول المتابعات"])}
{box("warn", "تحقق دائماً", "<p>قد يخطئ في قراءة خيط بريد. للالتزامات والمال والصياغة القانونية راجع النص بنفسك.</p>")}
"""))

    parts.append(chapter("8", "دليل Perplexity الشامل", f"""
<p class="lead">محرك إجابات: سؤال ← توليف مع استشهادات. استخدمه عندما تهم الحداثة والمصادر أكثر من الإبداع الأدبي.</p>
<ul>
<li>اسأل بدقة (سنة، منطقة، جمهور، مصادر أولية).</li>
<li>افتح الاستشهادات — لا تثق بالملخص وحده.</li>
<li>ضيّق بالمتابعات: تناقضات، تكاليف، بدائل.</li>
</ul>
{prompt("""ما أبرز الفروقات بين Zapier و Make و n8n لفريق تسويق من 5 أشخاص في 2026؟
القيود: قارن شكل التسعير ومنحنى التعلم وأفضل حالات الاستخدام.
المخرجات: جدول + توصية. فضّل مصادر حديثة مع ذكرها.""")}
{box("tip", "ساندويتش البحث", "<p>Perplexity للمصادر → Claude/ChatGPT لصياغة السرد → أنت للاستنتاج والصوت.</p>")}
"""))

    parts.append(chapter("9", "دليل NotebookLM الشامل", f"""
<p class="lead">مساعد بحث مربوط بمصادرك. ترفع المواد فيجيب منها — مثالي للدراسة والإحاطات وقواعد المعرفة.</p>
{workflow("حلقة NotebookLM", ["أنشئ دفترًا", "أضف مصادر", "اسأل أسئلة مربوطة", "ولّد دليل دراسة / FAQ", "صدّر إلى مستنداتك"])}
<table>
<thead><tr><th>الدور</th><th>فكرة دفتر</th></tr></thead>
<tbody>
<tr><td>مؤسس</td><td>أسئلة مستثمرين من العرض والسرد المالي</td></tr>
<tr><td>مسوّق</td><td>صوت العلامة + حملات سابقة → مولّد موجزات</td></tr>
<tr><td>دعم</td><td>مركز مساعدة + سياسات → مسودات بإسناد</td></tr>
<tr><td>طالب</td><td>محاضرات PDF → اختبارات وملخصات صوتية</td></tr>
</tbody>
</table>
{box("tip", "قاعدة الجودة", "<p>مصادر رديئة = دفتر رديء. انتقِ المصادر. قسّم المواضيع المتشعبة على دفاتر متعددة.</p>")}
"""))

    parts.append(part("4", "هندسة الأوامر", "مهارة عالمية. نفس النموذج + أمر مختلف = نتيجة مختلفة تماماً. حوّل الدردشة العشوائية إلى توجيه احترافي."))

    parts.append(chapter("10", "أساسيات هندسة الأوامر", f"""
<p class="lead">الأمر (Prompt) هو التعليمات الكاملة: المهمة، السياق، القيود، والصيغة المطلوبة.</p>
<ol>
<li><strong>الدور:</strong> من يتقمص الذكاء الاصطناعي؟</li>
<li><strong>الهدف:</strong> ما شكل الإنجاز؟</li>
<li><strong>الجمهور:</strong> من سيقرأ؟</li>
<li><strong>السياق:</strong> حقائق وقيود وأمثلة</li>
<li><strong>العملية:</strong> هيكل أولاً ثم مسودة</li>
<li><strong>الصيغة:</strong> جدول، نقاط، بريد، سكربت</li>
<li><strong>معيار الجودة:</strong> نبرة وطول وما يُمنع</li>
</ol>
{box("example", "ضعيف مقابل قوي", """
<p><strong>ضعيف:</strong> «اكتب خطة عمل.»</p>
<p><strong>قوي:</strong> «تصرف كمستشار للشركات الصغيرة. أنشئ خطة من صفحة واحدة لخدمة تنظيم منازل في الرياض تستهدف آباء مشغولين. تضمّن المشكلة والعرض وفرضية التسعير و3 قنوات ومعالم 90 يوماً. بلا حشو. جدول للمعالم.»</p>
""")}
{workflow("تكرار المحترفين", ["موجز", "هيكل", "مسودة", "نقد", "ضغط", "نهائي"])}
"""))

    parts.append(chapter("11", "أُطر كتابة الأوامر", f"""
<h2>RTF — Role · Task · Format</h2>
{prompt("""الدور: مدرب مهني للتحول إلى UX.
المهمة: خطة تعلم 30 يوماً.
الصيغة: جدول أسبوعي مع تقدير وقت يومي ومخرجات.""")}
<h2>CRISPE</h2>
{prompt("""القدرة: كاتب SaaS B2B أول.
الطلب: أعد كتابة H1/H2 للصفحة الرئيسية.
السياق: المستخدمون يخافون الإعداد المعقد؛ نقدم تجهيزاً خلال يومين.
الهدف: زيادة طلبات العرض التجريبي.
الشخصية: مباشرة وواثقة ومحددة.
التقييم: 3 نسخ وتوقع الأفضل ولماذا.""")}
<h2>APE و Chain of Thought و Few-shot</h2>
<p><strong>APE:</strong> إجراء + غرض + توقع. <strong>CoT:</strong> «فكّر خطوة بخطوة.» <strong>Few-shot:</strong> أعطِ 2–3 أمثلة للنمط المطلوب ثم المدخل الجديد.</p>
{box("tip", "اختيار سريع", "<p>RTF للسرعة · CRISPE للتسويق · Few-shot لمطابقة الصوت · Tree of Thoughts للاستراتيجية.</p>")}
"""))

    parts.append(chapter("12", "مكتبة أوامر احترافية", f"""
<p class="lead">انسخ وعدّل. استبدل الحقول بين قوسين. احفظ الفائزين في دفترك.</p>
<h2>تسويق</h2>
{prompt("اكتب 10 خطافات إعلان لـ [منتج] تستهدف [جمهور]. ركّز على الألم، أقل من 12 كلمة.")}
{prompt("ابنِ شخصية عميل لـ [عرض] مع أهداف ومخاوف واعتراضات وقنوات تواجد.")}
{prompt("حوّل هذه الميزات إلى فوائد: [قائمة]. الجمهور: [من]. بصيغة جدول.")}
{prompt("سلسلة إطلاق من 3 رسائل بريد لـ [منتج]. الهدف: [تجربة/عرض].")}
{prompt("بيان تموضع: لـ [جمهور] الذين [مشكلة]، [علامة] هي [فئة] التي [فائدة]. بخلاف [بديل]، نحن [فرق].")}
{prompt("15 عنوان يوتيوب عن [موضوع] — فضول + وضوح بلا كذب.")}
<h2>مبيعات ومحتوى</h2>
{prompt("سكربت مكالمة اكتشاف لـ [خدمة] مع أسئلة تأهيل واستبعاد.")}
{prompt("ردود على اعتراضات: السعر، التوقيت، أحتاج موافقة شريك، لدينا مزود.")}
{prompt("لخّص نص المكالمة إلى خطوات تالية ومخاطر وبريد متابعة.")}
{prompt("حوّل هذا المخطط إلى مقال 1000 كلمة مع أمثلة وقائمة تحقق.")}
{prompt("أعد توظيف المقال إلى: LinkedIn + سلسلة X + نشرة + سكربت قصير.")}
{prompt("20 سطر افتتاحي يوقف التمرير عن [ثيمة].")}
<h2>أعمال وتعليم وبرمجة للمبتدئين</h2>
{prompt("اكتب إجراءً تشغيلياً لـ [عملية] مع المالك والمحفز والخطوات وفحص الجودة.")}
{prompt("بطاقة توظيف لـ [دور] مع معايير تقييم.")}
{prompt("اشرح [مفهوم] بثلاث طرق: تشبيه، خطوات، أخطاء شائعة.")}
{prompt("اختبار من 10 أسئلة من هذه الملاحظات مع مفتاح إجابة: [الصق].")}
{prompt("اشرح هذا الخطأ كأنني مبتدئ ثم أعطِ خطوات الإصلاح: [خطأ].")}
{prompt("اكتب قصص مستخدم ومعايير قبول من هذا المتطلب.")}
{actions(["انسخ 15 أمراً واملأها لعملك.", "أنشئ كتلة Few-shot من 3 نماذج كتابتك الأفضل.", "جرّب نفس المهمة بـ RTF و CRISPE واحتفظ بالأفضل."])}
"""))

    parts.append(part("5", "توليد الصور", "الصور أصبحت لغة. تعلّم كيف تعمل نماذج الانتشار، ثم قواعد الأوامر التي يستخدمها المخرجون."))

    parts.append(chapter("13", "مقدمة إلى صور الذكاء الاصطناعي", f"""
<p class="lead">تولّد نماذج الصور صوراً من ضوضاء بإرشاد كلماتك — وأحياناً صور مرجعية.</p>
<ol>
<li>الموضوع · 2) الحركة/الوضعية · 3) المكان · 4) الأسلوب · 5) الإضاءة والكاميرا · 6) إشارات الجودة · 7) ما يجب تجنبه</li>
</ol>
<table>
<thead><tr><th>الأداة</th><th>تشتهر بـ</th></tr></thead>
<tbody>
<tr><td>Midjourney</td><td>جمالية فنية قوية</td></tr>
<tr><td>Flux</td><td>واقعية وتحكم</td></tr>
<tr><td>DALL·E داخل ChatGPT</td><td>سهولة وتعديل بالمحادثة</td></tr>
<tr><td>Ideogram</td><td>نص داخل الصورة</td></tr>
</tbody>
</table>
{box("warn", "حقوق وأخلاقيات", "<p>تجنب انتحال أشخاص حقيقيين أو نسخ أسماء فنانين أحياء كاختصار. راجع رخصة الاستخدام التجاري لكل أداة.</p>")}
"""))

    parts.append(chapter("14", "هندسة أوامر الصور", f"""
<p class="lead">لغة الكاميرا ترفع النتائج أسرع من حشو الصفات.</p>
<ul>
<li><strong>زوايا:</strong> مستوى العين، زاوية منخفضة، عين طائر، فوق الكتف</li>
<li><strong>عدسات:</strong> 24mm بيئة، 35mm وثائقي، 85mm بورتريه، ماكرو</li>
<li><strong>إضاءة:</strong> نافذة ناعمة، شمس قاسية، Rim light، ساعة ذهبية</li>
</ul>
<h2>40 أمراً جاهزاً (بالإنجليزية للأدوات)</h2>
<ol class="small en">
<li>Matte black water bottle on travertine, soft window light, catalog style</li>
<li>Overhead freelancer desk flat lay, laptop notebook coffee plant</li>
<li>Founder portrait 85mm shallow DOF warm indoor light</li>
<li>Isometric clay bakery shopfront pastel soft shadows</li>
<li>Rainy Tokyo street night neon reflections cinematic</li>
<li>Watercolor kids book fox reading a map cream paper</li>
<li>Fitness app iPhone mockup soft gradient backdrop</li>
<li>Rustic sourdough crumb detail side light dark mood</li>
<li>Coastal cabin dawn fog 24mm documentary</li>
<li>Minimal vector AI workflow nodes teal on off-white</li>
<li>Linen fashion lookbook golden hour beach path</li>
<li>Macro watch gears specular highlights black bg</li>
<li>Courier handing package warm porch light</li>
<li>Paper-cut surreal floating library above sea</li>
<li>B&amp;W street crosswalk decisive moment</li>
<li>Eco detergent packshot softbox reflection</li>
<li>Chalkboard coffee menu charming lettering</li>
<li>Mossy temple gate volumetric rays establishing</li>
<li>Textbook heart cross-section clean labels blank</li>
<li>Cozy cafe morning blinds lifestyle magazine</li>
<li>Friendly home robot watering plants photoreal</li>
<li>Vintage Lisbon tram poster limited palette</li>
<li>YouTube thumbnail shocked creator chart space for title</li>
<li>Perfume bottle botanical shadows high-key</li>
<li>Low-poly mountain campsite dusk</li>
<li>Potter at wheel dusty workshop available light</li>
<li>Soft mesh brand background grain negative space</li>
<li>STEM kit unboxing bright even colorful</li>
<li>Circuit-trace lock cybersecurity illustration</li>
<li>Wedding floral border elegant blank center</li>
<li>Runner mid-stride dawn road panning blur</li>
<li>Scandi apartment living room photoreal viz</li>
<li>3-panel comic barista learning AI POS</li>
<li>Pastel walkable town map illustration</li>
<li>Luxury chocolate break cocoa dust side light</li>
<li>Podcast cover two vector hosts headphones</li>
<li>Before/after kitchen cleaning split realistic</li>
<li>Ceramic mug mockup pastel Shopify hero</li>
<li>Stormy lighthouse film still subtle flares</li>
<li>Soft morning skincare shelfie marble steam</li>
</ol>
"""))

    parts.append(part("6", "توليد الفيديو", "النص أو الصورة يتحولان إلى حركة. اعتبرها محركات تصوّر ومحتوى قصير — لا هوليوود فورية."))

    parts.append(chapter("15", "أساسيات فيديو الذكاء الاصطناعي", f"""
<table>
<thead><tr><th>الوضع</th><th>ماذا تعطي؟</th><th>متى؟</th></tr></thead>
<tbody>
<tr><td>نص ← فيديو</td><td>أمر فقط</td><td>أفكار و B-roll</td></tr>
<tr><td>صورة ← فيديو</td><td>لقطة ثابتة + حركة</td><td>ثبات بصري</td></tr>
<tr><td>فيديو ← فيديو</td><td>مقطع مصدر</td><td>أسلوب وتنويعات</td></tr>
</tbody>
</table>
{box("tip", "إنتاج", "<p>ولّد لقطات قصيرة (2–8 ثوانٍ)، اختر الأفضل، ثم حرر تقليدياً. الهجين يتفوق على لقطة واحدة كاملة.</p>")}
"""))

    parts.append(chapter("16", "دليل Veo", f"""
<p class="lead">اكتب بلغة سينمائية: نوع اللقطة، الموضوع، الحركة، البيئة، حركة الكاميرا، الإضاءة، الأسلوب.</p>
{prompt("""Medium shot of a ceramicist shaping clay on a wheel, slow dolly-in, soft morning window light, shallow depth of field, naturalistic documentary, 5 seconds.""")}
<h2>25 مثالاً</h2>
<ol class="small en">
<li>Product bottle rotate infinity curve soft studio</li>
<li>Founder walk-through studio steadicam</li>
<li>Coffee pour macro steam slow-mo</li>
<li>Rooftop dawn pan across skyline</li>
<li>Top-down eco sneakers unboxing</li>
<li>Teacher at whiteboard locked-off friendly</li>
<li>Coastal path gentle rise plausible motion</li>
<li>Night market handheld neon wet pavement</li>
<li>Yoga silhouette sunrise calm pace</li>
<li>Keyboard typing SaaS b-roll shallow DOF</li>
<li>Pet running toward camera sunny park</li>
<li>Architect blueprint table slow orbit</li>
<li>EV charging dusk cinematic</li>
<li>Bread scoring oven spring bakery doc</li>
<li>Abstract clean dashboard cursor clicks</li>
<li>Rain on window cozy interior soft focus</li>
<li>Warehouse picker scanner authentic</li>
<li>Kids STEM volcano playful safe</li>
<li>Tailor pins jacket workshop lamp</li>
<li>Farmers market berries warm sincerity</li>
<li>Simple particles logo morph</li>
<li>Train window landscape reflective</li>
<li>Scientist pipette clinical bright</li>
<li>Mural artist painting strokes</li>
<li>Library aisle push-in sunlit desk</li>
</ol>
"""))

    parts.append(chapter("17", "Runway و Kling و Pika و Sora", f"""
<table>
<thead><tr><th>الأداة</th><th>القوة</th><th>متى؟</th></tr></thead>
<tbody>
<tr><td>Runway</td><td>جناح إبداعي وتحرير</td><td>فرق محتوى تتكرر</td></tr>
<tr><td>Kling</td><td>حركة سينمائية</td><td>لقطات طموحة</td></tr>
<tr><td>Pika</td><td>سرعة لأسلوب سوشيال</td><td>أفكار سريعة</td></tr>
<tr><td>Sora / Veo</td><td>جودة عالية حسب التوفر</td><td>احتياج فيديو مميز</td></tr>
</tbody>
</table>
{box("tip", "قاعدة الاختيار", "<p>اختر ما تستطيع الوصول إليه بثبات، ثم أتقن لغة اللقطة. الحرفة تنتقل بين الأدوات.</p>")}
"""))

    parts.append(part("7", "الصوت", "التعليق الصوتي والموسيقى يكمّلان حزمة المحتوى."))

    parts.append(chapter("18", "الذكاء الاصطناعي الصوتي", f"""
{workflow("تعليق صوتي", ["اكتب السكربت", "علّم الوقفات", "اختر صوتاً", "ولّد", "حرر", "امزج تحت الفيديو"])}
{prompt("اكتب سكربت شرح منتج 60 ثانية لـ [منتج]. نبرة خبير ودود. ضع [PAUSE] عند الحاجة. بحد أقصى 140 كلمة.")}
{box("warn", "موافقة", "<p>استنسخ الأصوات فقط بحقوق وموافقة. افصح عن الصوت الاصطناعي عند اللزوم.</p>")}
"""))

    parts.append(chapter("19", "موسيقى الذكاء الاصطناعي", f"""
<p>Suno و Udio يولّدان أغاني من نص — مفيد للمسودات وخلفيات السوشيال.</p>
{prompt("Upbeat indie-pop, 100 BPM, warm female vocals, song about learning AI without fear, clear chorus, radio-clean.")}
{box("tip", "استخدام عملي", "<p>استخدم موسيقى الذكاء الاصطناعي للاختبارات والأنيماتيك؛ استعن بملحنين عندما تهم الهوية الحصرية للعلامة.</p>")}
"""))

    parts.append(part("8", "الإنتاجية", "أعلى عائد غالباً في البريد والاجتماعات والمتابعات. اجعل الذكاء الاصطناعي متدرب عملياتك."))

    parts.append(chapter("20", "الإنتاجية الشخصية مع الذكاء الاصطناعي", f"""
{prompt("من هذا النص: (1) ملخص 5 نقاط (2) قرارات (3) جدول مهام بمالك وموعد (4) أسئلة مفتوحة. أشر لأي غموض.")}
{workflow("تعلّم موضوعاً", ["مسح Perplexity", "حفظ أفضل المصادر", "دفتر NotebookLM", "علّم ChatGPT ما فهمت", "ورقة غش بصفحة"])}
{takeaways(["استأذن قبل التسجيل.", "الملخص مسودة حتى تؤكد الملاك والمواعيد.", "الشرح العكسي يكشف ما لم تتعلمه."])}
"""))

    parts.append(chapter("21", "إنتاجية الأعمال", f"""
<table>
<thead><tr><th>الوظيفة</th><th>سير عمل بالذكاء الاصطناعي</th></tr></thead>
<tbody>
<tr><td>تسويق</td><td>موجز → نسخ → نقد → تحرير علامة → جدولة</td></tr>
<tr><td>دعم</td><td>دفتر سياسات → مسودة → إرسال بشري للحالات الحدية</td></tr>
<tr><td>مبيعات</td><td>ملاحظات مكالمة → ملخص CRM → متابعة مخصصة</td></tr>
<tr><td>موارد بشرية</td><td>بطاقات أدوار وخطط 30-60-90 (راقب التحيز)</td></tr>
<tr><td>عمليات</td><td>صياغة إجراءات وجداول حوادث</td></tr>
</tbody>
</table>
{box("mistake", "فشل شائع", "<p>نشر نص ذكاء اصطناعي دون تحرير يضر بالثقة. الذكاء الاصطناعي يسرّع المسودات؛ الإنسان يملك النتيجة.</p>")}
"""))

    parts.append(part("9", "الأتمتة", "اربط التطبيقات ليتوقف النسخ واللصق. ضع الذكاء الاصطناعي في الوسط للتصنيف أو الصياغة ضمن حدود."))

    parts.append(chapter("22", "أساسيات الأتمتة", f"""
<p class="lead">كل أتمتة: <strong>محفّز → (فلاتر) → إجراءات</strong>.</p>
{box("tip", "اختبار الصلاحية", "<p>أتمت إن تكررت المهمة ≥3 مرات/أسبوع، والقواعد واضحة، والأخطاء قابلة للمراجعة.</p>")}
{box("warn", "حواجز أمان", "<p>ابدأ بمسودات + موافقة بشرية لأي شيء خارجي (بريد عملاء، منشورات، مدفوعات).</p>")}
"""))

    parts.append(chapter("23", "دليل n8n الشامل", f"""
<p>أداة مرنة للأتمتة (سحابة أو استضافة ذاتية).</p>
<ol class="small">
<li>نموذج → إثراء بالذكاء الاصطناعي → صف CRM → تنبيه Slack</li>
<li>بريد دعم → تصنيف استعجال → توجيه</li>
<li>RSS → تلخيص → مسودة نشرة</li>
<li>ملف Drive جديد → ملخص → صفحة Notion</li>
<li>أسبوعي: مقاييس Sheet → سرد → بريد تقرير</li>
<li>تغذية راجعة → وسم مشاعر → لوحة</li>
<li>إشارة على X → طابور ردود مسودة</li>
<li>فاتورة PDF → استخراج حقول → Sheet (مراجعة)</li>
<li>نهاية اجتماع تقويم → قالب ملاحظات → مهام</li>
<li>Webhook متجر → وصف منتج → مسودة Shopify</li>
</ol>
"""))

    parts.append(chapter("24", "دليل Make الشامل", f"""
<p>سيناريوهات بصرية قوية للتسويق والعمليات.</p>
<ol class="small">
<li>Lead Ad → تقييم → HubSpot + تسلسل</li>
<li>طلب وظيفة → فحص مقابل بطاقة → Sheets + تنبيه</li>
<li>كلمة مفتاح في DM → مسودة FAQ</li>
<li>طلب Shopify → شكر مخصص مسودة</li>
<li>انتهاء محادثة → ملخص إلى Notion</li>
<li>رفع يوتيوب → فصول + وصف → تنبيه محرر</li>
<li>إيصال مصروف → استخراج → محاسبة</li>
<li>تسجيل ويبينار → تقسيم → تسلسل مخصص</li>
<li>CSAT منخفض → تذكرة مع ملخص سياق</li>
<li>صف تقويم جاهز → حزمة منشورات</li>
</ol>
"""))

    parts.append(chapter("25", "دليل Zapier الشامل", f"""
<p>أسهل مدخل: آلاف التكاملات بسرعة.</p>
<ol class="small">
<li>Gmail بوسم → مسودة رد → Drafts</li>
<li>حدث تقويم → موجز تحضير من Doc</li>
<li>Typeform → ملخص → Slack</li>
<li>RSS → خطافات → مسودة Buffer</li>
<li>مرحلة صفقة CRM → قائمة kickoff</li>
<li>تسجيل Zoom جاهز → ملخص للحضور</li>
<li>فكرة Airtable → مخطط → Docs</li>
<li>منتج Shopify → عناوين SEO مقترحة</li>
<li>وسم استرداد → مسودة سياسة (موافقة)</li>
<li>يومياً: ترتيب مهام Todoist بالذكاء الاصطناعي</li>
</ol>
{actions(["ابنِ Zap واحداً بخطوة موافقة بشرية.", "راقب الأخطاء أسبوعاً.", "وثّقه في دفترك."])}
"""))

    parts.append(part("10", "وكلاء الذكاء الاصطناعي", "الوكيل لا يجيب فقط — يخطّط ويستخدم أدوات نحو هدف. قوي… ويحتاج حدوداً."))

    parts.append(chapter("26", "فهم وكلاء الذكاء الاصطناعي", f"""
<ul>
<li><strong>العقل:</strong> LLM للتخطيط واللغة</li>
<li><strong>الأدوات:</strong> إجراءات مسموحة</li>
<li><strong>الذاكرة:</strong> قصيرة وطويلة اختيارياً</li>
<li><strong>المخطّط:</strong> هدف ← خطوات ← مراجعة</li>
<li><strong>الحواجز:</strong> صلاحيات، ميزانية، موافقة بشرية</li>
</ul>
{box("warn", "واقع", "<p>الوكلاء بلا إشراف قد يدخلون حلقات أو يراسلون عملاء خطأ. ابدأ للقراءة فقط أو المسودات فقط.</p>")}
"""))

    parts.append(chapter("27", "بناء سير عمل الوكلاء", f"""
<ul>
<li><strong>بحث:</strong> مصادر → هيكل → إحاطة (إنسان ينشر)</li>
<li><strong>دعم:</strong> استرجاع سياسة → مسودة → تصعيد إن انخفضت الثقة</li>
<li><strong>تسويق:</strong> حقائق منتج → حزمة حملة → موافقة Slack</li>
</ul>
{workflow("حلقة وكيل آمنة", ["عرّف الهدف", "حدّد الأدوات", "بوابات موافقة", "سجّل الأفعال", "راجع أسبوعياً"])}
"""))

    parts.append(part("11", "مشاريع عملية", "النظرية تثبت عندما تنشر. عشرون مشروعاً — اختر ما يناسب هدفك."))

    projects = [
        ("استوديو محتوى بالذكاء الاصطناعي", "12 منشوراً/شهر", "ChatGPT/Claude + Ideogram + جدولة", "دليل صوت + تقويم → دفعات → صور → نشر", "توفير ساعات أسبوعياً"),
        ("مكتب بحث شخصي", "إحاطة بأي موضوع خلال 45 دقيقة", "Perplexity + NotebookLM + Claude", "بحث → مصادر → دفتر → صفحة واحدة", "SOP بحث قابل لإعادة الاستخدام"),
        ("محرك عروض المستقل", "عروض أوضح وأسرع", "ChatGPT Projects + Notion", "نموذج استقبال → ملخص → عرض → تسعير بشري", "رفع وضوح الإغلاق"),
        ("مكتب دعم عملاء", "رد أول أسرع", "NotebookLM + Helpdesk + Zapier", "دفتر سياسات → مسودة → موافقة → قوالب", "خفض زمن الرد"),
        ("نظام إدارة سوشيال", "حضور يومي متعدد المنصات", "Claude + Ideogram + جدولة", "عمود محتوى → تفتيت → بصريات → جدول", "فكرة واحدة ← أصول كثيرة"),
        ("مصنع فيديو قصير", "مخرجات أسبوعية", "ChatGPT + Veo/Runway + ElevenLabs", "سكربت → صوت → B-roll → مونتاج → SEO", "تغليف أسرع"),
        ("مختبر عروض تسويقية", "اختبار عروض بسرعة", "ChatGPT + Perplexity + Sheets", "ICP → عروض → نسخة هبوط → خطافات", "تجريب منظم"),
        ("رفيق صانع الدورات", "من مخطط إلى دروس", "NotebookLM + Claude", "مصادر → وحدات → سكربتات → اختبارات", "هيكل منهج كامل"),
        ("نظام اجتماعات", "صفر مهام ضائعة", "Fireflies/Zoom + ChatGPT + Todoist", "نص → مهام → متابعة", "عادة مساءلة"),
        ("مدرب مكالمات مبيعات", "تحسين الاكتشاف", "Claude + CRM", "نقد النص مقابل بطاقة → ملاحظات تدريب", "نمو مهارة المندوب"),
        ("محسّن قوائم تجارة", "صفحات منتج أفضل", "ChatGPT + Ideogram + Shopify", "ميزات → فوائد → صور → SEO", "سرعة إدراج"),
        ("حقيبة تأهيل موظفين", "انضمام أسلس", "Gemini/Docs + Claude", "بطاقة دور → 30-60-90 → FAQ", "أسئلة أقل تكراراً"),
        ("باقة عرض للأعمال المحلية", "بيع خدمات ذكاء اصطناعي", "Make/Zapier + ChatGPT", "أتمتة نماذج + ردود تقييمات + تقرير أسبوعي", "عرض مستقل منتجي"),
        ("مساعد تحديث المستثمرين", "تحديث شهري بـ 30 دقيقة", "Sheets + Claude", "لصق مقاييس → سرد → مخاطر → طلب", "تواصل منتظم"),
        ("حزمة إنتاج بودكاست", "من حلقة إلى أصول", "Claude + ElevenLabs", "مخطط → سكربت → ملاحظات → أوامر أغلفة", "دورة أسرع"),
        ("صائغ منح / RFP", "طلبات منظمة", "NotebookLM + Claude", "دفتر متطلبات → مصفوفة امتثال → إجابات", "معايير أقل ضياعاً"),
        ("مدرس خاص شخصي", "تحضير امتحان", "ChatGPT + NotebookLM", "دفتر ملاحظات → تدريبات يومية → نقاط ضعف", "حلقة ممارسة قابلة للقياس"),
        ("سبرينت هوية بصرية", "اتجاه بصري في يوم", "Midjourney/Flux + Claude", "مزاج → 3 اتجاهات → بطاقة أسلوب", "موجز إبداعي متوافق"),
        ("مكتبة إجراءات تشغيل", "توثيق المعرفة الضمنية", "Claude + Notion", "مقابلة → SOP → قائمة تحقق → اختبار", "عمليات قابلة للتدريب"),
        ("وكالة أتمتة مصغرة", "عقود من سير العمل", "Make أو n8n + LLM", "تدقيق مهام عميل → 3 أتمتات → لوحة", "إيراد متكرر"),
    ]
    proj_html = ['<p class="lead">كل مشروع: هدف، أدوات، إعداد، سير عمل، نتيجة. عدّل بحرية.</p>']
    for i, (name, obj, tools, wf, res) in enumerate(projects, 1):
        proj_html.append(f"""
<div class="project">
  <h3>مشروع {i}: {name}</h3>
  <p class="meta"><span class="badge">الهدف</span> {obj} · <span class="badge">أدوات</span> <span class="en">{tools}</span></p>
  <p><strong>الإعداد:</strong> أنشئ مجلداً/مشروعاً، الصق موجزاً من فقرة، وأضف مصادر العلامة أو السياسات.</p>
  <p><strong>سير العمل:</strong> {wf}</p>
  <p><strong>النتيجة:</strong> {res}</p>
</div>
""")
    proj_html.append(actions([
        "اختر مشروعاً واحداً وأكمله خلال 7 أيام.",
        "اكتب دراسة حالة: قبل → بعد → ساعات موفرة.",
        "حوّل مشروعك الفائز إلى عرض خدمة أو إجراء داخلي."
    ]))
    parts.append(chapter("28", "عشرون مشروعاً كاملاً بالذكاء الاصطناعي", "\n".join(proj_html)))

    parts.append(part("12", "المستقبل وخارطة الطريق", "الأدوات تتغير. نظام تعلّمك لا يجب أن يتغير. اختم بالتوجهات وخطة 12 شهراً."))

    parts.append(chapter("29", "توجهات المستقبل", f"""
<ul>
<li><strong>وكلاء:</strong> مساعدون يستخدمون أدوات بصلاحيات عمل</li>
<li><strong>متعدد الوسائط:</strong> نص ↔ صورة ↔ صوت ↔ فيديو في خيط واحد</li>
<li><strong>روبوتات:</strong> نماذج أساس تلتقي العتاد (أبطأ وأعمق أثراً)</li>
<li><strong>وظائف:</strong> مشغّلو ذكاء اصطناعي، متخصصو أتمتة، مديرو منتجات AI، خبراء مجال يستخدمون AI</li>
</ul>
{box("note", "مهارات خالدة", "<p>تأطير المشكلة، كتابة الأوامر، التحقق، تصميم سير العمل، خبرة المجال، والأخلاقيات — تبقى بعد زوال أي تطبيق.</p>")}
"""))

    parts.append(chapter("30", "خارطة طريق مهنية لتعلّم الذكاء الاصطناعي", f"""
<h2>مبتدئ (الأشهر 1–3)</h2>
<ul>
<li>تمرين يومي على نماذج اللغة؛ أنهِ الأجزاء 1–4</li>
<li>دفتر بـ 30 أمراً</li>
<li>نفّذ مشروعين من الفصل 28</li>
</ul>
<h2>متوسط (4–8)</h2>
<ul>
<li>أضف صوراً/فيديو/صوتاً لتخصصك</li>
<li>ابنِ 5 أتمتات ببوابات موافقة</li>
<li>أنشئ Custom GPT أو Claude Project لوظيفتك</li>
<li>انشر دراسات حالة</li>
</ul>
<h2>متقدم (9–12)</h2>
<ul>
<li>صمّم سير عمل وكلاء مع سجلات وتقييم</li>
<li>تخصص (دعم، تسويق تشغيلي، بحث، تعليم)</li>
<li>علّم أو استشر؛ حوّل خبرتك إلى عرض</li>
</ul>
<table>
<thead><tr><th>الربع</th><th>التركيز</th><th>الإثبات</th></tr></thead>
<tbody>
<tr><td>Q1</td><td>طلاقة النماذج والأوامر</td><td>دفتر + مشروعان</td></tr>
<tr><td>Q2</td><td>محتوى متعدد الوسائط</td><td>محفظة أصول</td></tr>
<tr><td>Q3</td><td>أتمتة</td><td>5 سير عمل حية</td></tr>
<tr><td>Q4</td><td>وكلاء + تخصص</td><td>دراسة حالة + عرض</td></tr>
</tbody>
</table>
{takeaways([
  "تمرّن يومياً على عمل حقيقي لا استعراضات فقط.",
  "الإثبات يتفوق على الشهادات: مشاريع وإجراءات ومقاييس.",
  "تخصص بعد أن تمتلك طلاقة عامة."
])}
{actions([
  "احجز 30 دقيقة يومياً هذا الأسبوع للتمرين.",
  "اختر فرضية تخصص لـ 12 شهراً.",
  "جدول مراجعة شهرية لدفتر أوامرك."
])}
<p class="colophon">وصلت إلى نهاية <em>الذكاء الاصطناعي — الدليل الشامل للمبتدئين</em>. الأدوات ستتغير — قدرتك على التوجيه والتحقق وبناء سير العمل هي ميزتك الدائمة.<br/>من إعداد <strong class="en">SCHOOLERX</strong> · 2026<br/>الآن افتح دفترك ونفّذ المشروع رقم 1.</p>
"""))

    # Glossary
    parts.append("""
<section class="chapter" id="glossary">
  <div class="chapter-num">ملحق</div>
  <h1 class="chapter-title">مسرد سريع (عربي / English)</h1>
  <table>
    <thead><tr><th>المصطلح</th><th>المعنى للمبتدئ</th></tr></thead>
    <tbody>
      <tr><td><span class="en">Prompt</span> / أمر</td><td>التعليمات التي تعطيها للنموذج</td></tr>
      <tr><td><span class="en">LLM</span></td><td>نموذج لغة كبير يولّد نصاً ويفهمه</td></tr>
      <tr><td><span class="en">Token</span></td><td>قطعة نص يقرأها النموذج</td></tr>
      <tr><td><span class="en">Context window</span></td><td>كمية النص التي يراها دفعة واحدة</td></tr>
      <tr><td><span class="en">Hallucination</span> / هلوسة</td><td>إجابة خاطئة بثقة</td></tr>
      <tr><td><span class="en">RAG</span></td><td>استرجاع مصادر ثم الإجابة منها</td></tr>
      <tr><td><span class="en">Agent</span> / وكيل</td><td>نظام يخطّط ويستخدم أدوات نحو هدف</td></tr>
      <tr><td><span class="en">Automation</span> / أتمتة</td><td>تشغيل خطوات بين تطبيقات تلقائياً</td></tr>
      <tr><td><span class="en">Fine-tuning</span></td><td>تدريب إضافي لتخصص ضيق</td></tr>
      <tr><td><span class="en">Multimodal</span></td><td>يفهم أو يولّد أكثر من نوع وسائط</td></tr>
    </tbody>
  </table>
  <div class="callout note"><span class="callout-label">ملاحظة SCHOOLERX</span>
  <p>لا تحفظ المصطلحات للحفظ الأكاديمي. احفظها لأنها تساعدك على اختيار الأداة الصحيحة وشرح احتياجك بوضوح.</p></div>
</section>
""")

    parts.append("""
</article>
</body>
</html>
""")
    return "".join(parts)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    html = build()
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
