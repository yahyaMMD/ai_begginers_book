#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SCHOOLERX — كتاب الذكاء الاصطناعي للأطفال (بسيط جداً)."""

from pathlib import Path

OUT = Path("/workspace/book/ai-beginners-handbook.html")

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=IBM+Plex+Sans:wght@500;700&display=swap');

:root {
  --ink: #2A2450;
  --navy: #3D2A6E;
  --purple: #6B3FA0;
  --purple-soft: #F3ECFA;
  --orange: #FF8A1F;
  --orange-soft: #FFF3E6;
  --gold: #FFC94D;
  --pink: #FF5FA2;
  --teal: #12B5C9;
  --teal-soft: #E6F9FC;
  --green: #22A06B;
  --green-soft: #E8F8F0;
  --paper: #FFFFFF;
  --sky: #FFF9F2;
  --rule: #E8E0F0;
  --muted: #6A6288;
  --font: 'Cairo', Tahoma, sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 12.5pt; direction: rtl; }
body {
  font-family: var(--font);
  color: var(--ink);
  background: #efeaf7;
  line-height: 1.7;
}

.en { font-family: 'IBM Plex Sans', sans-serif; direction: ltr; unicode-bidi: isolate; }

@media screen {
  body { padding: 18px 0 40px; }
  .book {
    width: 160mm; margin: 0 auto; background: var(--paper);
    box-shadow: 0 14px 40px rgba(61,42,110,.18); border-radius: 4px;
  }
}

@page {
  size: 160mm 220mm;
  margin: 12mm 14mm 14mm 14mm;
  @bottom-center {
    content: counter(page);
    font-family: 'Cairo', sans-serif;
    font-size: 9pt; color: #9a90b5;
  }
}
@page :first { margin: 0; @bottom-center { content: none; } }

@media print {
  html, body { background: #fff; padding: 0; }
  .book { box-shadow: none; width: auto; }
  .no-print { display: none !important; }
  .cover, .toc-page, .front-matter { break-before: page; }
  .part-opener { break-before: page; break-after: avoid; }
  .chapter { break-before: auto; margin-top: 0.75em; padding-top: 0.4em; border-top: 2px dashed var(--rule); }
  #ch-1, #ch-10, #ch-14, #ch-18, #ch-19 { break-before: page; border-top: none; margin-top: 0; padding-top: 0; }
  .cover { break-before: avoid; }
  h1.chapter-title, .lead { break-after: avoid; page-break-after: avoid; }
  .fig { break-before: avoid; page-break-before: avoid; break-inside: avoid; }
  .step, .try, .safe, .idea, .prompt, .project, .takeaway, .cards { break-inside: avoid; }
}

.screen-toolbar {
  position: sticky; top: 0; z-index: 40;
  background: linear-gradient(90deg, #3D2A6E, #6B3FA0);
  color: #fff; font-size: 13px; padding: 10px 14px;
  display: flex; justify-content: space-between; align-items: center;
}
.screen-toolbar button {
  background: linear-gradient(90deg, #FF8A1F, #FFC94D);
  border: 0; border-radius: 999px; padding: 7px 14px;
  font-family: var(--font); font-weight: 800; cursor: pointer; color: #2A1848;
}

.cover { height: 220mm; overflow: hidden; background: #f5f5f7; break-after: page; }
.cover img { width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block; }

p { margin: 0 0 .55em; }
.lead { font-size: 1.05rem; color: var(--muted); font-weight: 600; margin-bottom: .8em; }

h1.chapter-title {
  font-size: 1.45rem; font-weight: 800; color: var(--navy); line-height: 1.25;
  margin: 0 0 .4em; padding-bottom: .28em;
  border-bottom: 4px solid transparent;
  border-image: linear-gradient(270deg, var(--orange), #FFC94D, var(--purple)) 1;
}
h2 { font-size: 1.12rem; font-weight: 800; color: var(--purple); margin: .95em 0 .35em; }
h3 { font-size: 1rem; font-weight: 800; color: var(--navy); margin: .75em 0 .3em; }

ul, ol { margin: 0 0 .75em; padding-inline-start: 1.25em; }
li { margin-bottom: .28em; }
li::marker { color: var(--orange); font-weight: 800; }

.chapter-num { font-size: .78rem; font-weight: 800; color: var(--orange); margin-bottom: .15em; }

.part-opener {
  padding: .7em .8em; border-radius: 16px; margin-bottom: .5em;
  background:
    radial-gradient(circle at 100% 0%, rgba(255,138,31,.18), transparent 45%),
    radial-gradient(circle at 0% 100%, rgba(107,63,160,.14), transparent 50%),
    var(--purple-soft);
}
.part-label { font-weight: 800; color: var(--orange); margin-bottom: .25em; }
.part-opener h1 { font-size: 1.5rem; color: var(--navy); font-weight: 800; margin-bottom: .25em; }
.part-opener p { color: var(--muted); font-weight: 600; }

.toc-page h1, .front-matter .chapter-title {
  font-size: 1.4rem; font-weight: 800; color: var(--navy);
  border-bottom: 4px solid var(--orange); padding-bottom: .3em; margin-bottom: .8em;
}
.toc { list-style: none; padding: 0; }
.toc li { display: flex; gap: .35em; align-items: baseline; margin-bottom: .32em; font-size: .92rem; font-weight: 600; }
.toc .toc-part { margin-top: .75em; font-weight: 800; color: var(--purple); font-size: .85rem; }
.toc .dots { flex: 1; border-bottom: 2px dotted var(--rule); min-width: .6em; margin-bottom: .2em; }

.bubble {
  background: var(--purple-soft); border-radius: 18px 18px 4px 18px;
  padding: .7em .85em; margin: .6em 0 .8em; font-weight: 600;
  border: 2px solid #e0d0f2;
}
.bubble.me {
  background: var(--orange-soft); border-color: #ffd7a8;
  border-radius: 18px 18px 18px 4px;
}

.step {
  display: grid; grid-template-columns: 36px 1fr; gap: .5em;
  background: #fff; border: 2px solid var(--rule); border-radius: 14px;
  padding: .48em .62em; margin: .38em 0 .48em;
  box-shadow: 0 3px 0 rgba(107,63,160,.07);
}
.step .num {
  width: 36px; height: 36px; border-radius: 50%;
  display: grid; place-items: center;
  background: linear-gradient(135deg, var(--orange), #FFC94D);
  color: #2A1848; font-weight: 800; font-size: 1rem;
}
.step .body strong { color: var(--navy); display: block; margin-bottom: .1em; }

.try {
  background: var(--green-soft); border: 2px solid #9fe0c0; border-radius: 16px;
  padding: .7em .85em; margin: .7em 0;
}
.try .label { color: var(--green); font-weight: 800; font-size: .78rem; display: block; margin-bottom: .2em; }

.safe {
  background: #FFE8F2; border: 2px solid #ffb6d5; border-radius: 16px;
  padding: .7em .85em; margin: .7em 0;
}
.safe .label { color: #c2185b; font-weight: 800; font-size: .78rem; display: block; margin-bottom: .2em; }

.idea {
  background: var(--teal-soft); border: 2px solid #9fe4ef; border-radius: 16px;
  padding: .7em .85em; margin: .7em 0;
}
.idea .label { color: #0b7f8f; font-weight: 800; font-size: .78rem; display: block; margin-bottom: .2em; }

.prompt {
  background: #2A2450; color: #fff8ee; border-radius: 14px;
  padding: .7em .85em; margin: .5em 0 .75em;
  border-inline-start: 6px solid var(--orange);
  font-weight: 600; white-space: pre-wrap; line-height: 1.55;
}

.fig {
  margin: .4em 0 .55em; text-align: center;
  background: var(--sky); border-radius: 14px; padding: .35em;
  border: 2px solid #ffe0b8;
}
.fig img {
  width: 100%; max-height: 36mm; object-fit: cover; object-position: center;
  border-radius: 10px; display: block;
}
.fig .cap { font-size: .74rem; color: var(--muted); font-weight: 700; margin-top: .22em; }

.cards { display: grid; grid-template-columns: 1fr 1fr; gap: .55em; margin: .6em 0 .9em; }
.card {
  background: var(--purple-soft); border-radius: 14px; padding: .65em .7em;
  border: 2px solid #e2d4f3;
}
.card h4 { margin: 0 0 .2em; color: var(--purple); font-size: .92rem; }
.card p { margin: 0; font-size: .88rem; font-weight: 600; color: var(--muted); }

.project {
  background: #fff; border-radius: 16px; padding: .7em .8em; margin: .55em 0 .75em;
  border: 2px solid var(--rule); border-inline-start: 6px solid var(--orange);
}
.project h3 { margin: 0 0 .25em; color: var(--navy); }
.project .meta { font-size: .82rem; color: var(--muted); font-weight: 700; margin-bottom: .3em; }

.takeaway {
  background: linear-gradient(270deg, var(--purple-soft), #fff);
  border: 2px solid #e0d0f2; border-radius: 16px; padding: .75em .85em; margin: .9em 0;
}
.takeaway h3 { margin: 0 0 .3em; color: var(--purple); font-size: 1rem; }

.hero-pills { display: flex; flex-wrap: wrap; gap: .35em; margin: .5em 0 .9em; }
.hero-pills span {
  background: var(--orange-soft); color: #9a4b00; border-radius: 999px;
  padding: .18em .65em; font-size: .75rem; font-weight: 800; border: 1px solid #ffd7a8;
}

.big-emoji { font-size: 1.4rem; }
.colophon { margin-top: 1.2em; color: var(--muted); font-weight: 600; font-size: .9rem; }
"""


def fig(src, cap):
    return f'<figure class="fig"><img src="{src}" alt="{cap}"/><figcaption class="cap">{cap}</figcaption></figure>'


def step(n, title, body):
    return f'<div class="step"><div class="num">{n}</div><div class="body"><strong>{title}</strong><div>{body}</div></div></div>'


def try_it(html):
    return f'<div class="try"><span class="label">جرّب الآن ★</span>{html}</div>'


def safe(html):
    return f'<div class="safe"><span class="label">قاعدة أمان ❤️</span>{html}</div>'


def idea(html):
    return f'<div class="idea"><span class="label">فكرة لطيفة</span>{html}</div>'


def prompt(text):
    return f'<div class="prompt">{text.strip()}</div>'


def takeaways(items):
    return '<div class="takeaway"><h3>ماذا تعلّمنا؟</h3><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"


def part(num, title, blurb):
    return f"""
<section class="part-opener" id="part-{num}">
  <div class="part-label">القسم {num}</div>
  <h1>{title}</h1>
  <p>{blurb}</p>
</section>
"""


def chapter(num, title, body):
    return f"""
<section class="chapter" id="ch-{num}">
  <div class="chapter-num">الدرس {num}</div>
  <h1 class="chapter-title">{title}</h1>
  {body}
</section>
"""


def build():
    a = "/workspace/book/assets/kids"
    # relative paths for HTML
    img = {
        "meet": "assets/kids/kids-meet-ai.jpg",
        "open": "assets/kids/kids-open-chatgpt.jpg",
        "account": "assets/kids/kids-create-account.jpg",
        "ask": "assets/kids/kids-ask-ai.jpg",
        "friends": "assets/kids/kids-three-friends.jpg",
        "howto": "assets/kids/kids-how-to-ask.jpg",
        "picture": "assets/kids/kids-make-picture.jpg",
        "safe": "assets/kids/kids-stay-safe.jpg",
    }

    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="author" content="SCHOOLERX"/>
<title>الذكاء الاصطناعي للأطفال | SCHOOLERX</title>
<style>{CSS}</style>
</head>
<body>
<div class="screen-toolbar no-print">
  <span><strong>كتاب الأطفال</strong> · SCHOOLERX</span>
  <button onclick="window.print()">طباعة / PDF</button>
</div>
<article class="book">
<section class="cover" id="cover">
  <img src="assets/cover.png" alt="غلاف كتاب الذكاء الاصطناعي للأطفال — SCHOOLERX"/>
</section>
""")

    parts.append(f"""
<section class="front-matter" id="hello">
  <div class="chapter-num">مرحباً</div>
  <h1 class="chapter-title">هذا الكتاب لك أنت!</h1>
  <p class="lead">أهلاً يا بطل! هذا الكتاب يعلّمك الذكاء الاصطناعي كأنك تلعب لعبة جديدة. كلمات سهلة. خطوات واضحة. صور تساعدك.</p>
  {fig(img["meet"], "أنت + صديق ذكي على الحاسوب")}
  <div class="hero-pills">
    <span>للأطفال</span><span>سهل جداً</span><span>خطوة بخطوة</span><span>مع صور</span>
  </div>
  <h2>ماذا ستتعلّم؟</h2>
  <ul>
    <li>ما هو الذكاء الاصطناعي؟</li>
    <li>كيف تفتح ChatGPT وتسأل سؤالاً</li>
    <li>أصدقاء آخرين مثل Claude و Gemini</li>
    <li>كيف تتكلم مع الذكاء الاصطناعي بوضوح</li>
    <li>كيف تطلب منه أن يرسم لك صورة</li>
    <li>كيف تبقى آمناً على الإنترنت</li>
  </ul>
  {safe("<p>إذا احتجت حساباً أو بريداً إلكترونياً… اطلب مساعدة شخص كبير تثق به (أب، أم، معلّم).</p>")}
</section>
""")

    parts.append("""
<section class="toc-page" id="toc">
  <h1>ماذا داخل الكتاب؟</h1>
  <ul class="toc">
    <li class="toc-part">القسم 1 — ما هو الذكاء الاصطناعي؟</li>
    <li><span>1. صديق ذكي على الحاسوب</span><span class="dots"></span></li>
    <li><span>2. أين تراه كل يوم؟</span><span class="dots"></span></li>
    <li class="toc-part">القسم 2 — ابدأ مع ChatGPT</li>
    <li><span>3. افتح الموقع</span><span class="dots"></span></li>
    <li><span>4. اصنع حساباً</span><span class="dots"></span></li>
    <li><span>5. اسأل أول سؤال</span><span class="dots"></span></li>
    <li><span>6. أسئلة ممتعة للتجربة</span><span class="dots"></span></li>
    <li class="toc-part">القسم 3 — أصدقاء آخرون</li>
    <li><span>7. تعرّف على Claude</span><span class="dots"></span></li>
    <li><span>8. تعرّف على Gemini</span><span class="dots"></span></li>
    <li><span>9. أي صديق نختار؟</span><span class="dots"></span></li>
    <li class="toc-part">القسم 4 — كيف نتكلم معه؟</li>
    <li><span>10. اطلب بوضوح</span><span class="dots"></span></li>
    <li><span>11. أعطِه دوراً</span><span class="dots"></span></li>
    <li><span>12. أضف تفاصيل</span><span class="dots"></span></li>
    <li><span>13. ألعاب تدريب</span><span class="dots"></span></li>
    <li class="toc-part">القسم 5 — الصور</li>
    <li><span>14. اطلب صورة</span><span class="dots"></span></li>
    <li><span>15. صف الصورة ببساطة</span><span class="dots"></span></li>
    <li class="toc-part">القسم 6 — مرح إضافي</li>
    <li><span>16. صوت وموسيقى</span><span class="dots"></span></li>
    <li><span>17. فيديو قصير</span><span class="dots"></span></li>
    <li class="toc-part">القسم 7 — مشاريع ممتعة</li>
    <li><span>18. عشرة مشاريع للأطفال</span><span class="dots"></span></li>
    <li class="toc-part">القسم 8 — كن بطلاً آمناً</li>
    <li><span>19. قواعد الأمان</span><span class="dots"></span></li>
    <li><span>20. ماذا بعد؟</span><span class="dots"></span></li>
  </ul>
</section>
""")

    # PART 1
    parts.append(part("1", "ما هو الذكاء الاصطناعي؟", "هيا نفهم الفكرة الكبيرة بكلمات صغيرة."))

    parts.append(chapter("1", "صديق ذكي على الحاسوب", f"""
<p class="lead">الذكاء الاصطناعي هو برنامج ذكي يساعد الناس. ليس إنساناً حقيقياً. وليس وحشاً. هو مثل صديق على الشاشة يحب الإجابة والرسم والشرح.</p>
{fig(img["meet"], "صديقك الذكي جاهز للمساعدة")}
<div class="bubble">أنت: مرحبا! اشرح لي الساعة بطريقة مضحكة.</div>
<div class="bubble me">الذكاء الاصطناعي: حسناً! الساعة مثل دائرة بيتزا…</div>
<h2>ببساطة شديدة</h2>
<ul>
  <li>تكتب له سؤالاً</li>
  <li>هو يقرأ سؤالك</li>
  <li>ثم يكتب لك جواباً</li>
</ul>
{idea("<p>اسمه بالإنجليزية <span class='en'>AI</span>. وبالعربية: الذكاء الاصطناعي. معناها: ذكاء مصنوع على الحاسوب.</p>")}
{takeaways([
  "الذكاء الاصطناعي برنامج مساعد.",
  "نتكلم معه بالكتابة (وأحياناً بالصوت).",
  "هو ليس بشرياً… لكنه مفيد جداً."
])}
"""))

    parts.append(chapter("2", "أين تراه كل يوم؟", f"""
<p class="lead">ربما تستخدمه الآن دون أن تعرف اسمه!</p>
<div class="cards">
  <div class="card"><h4>يوتيوب</h4><p>يقترح فيديوهات قد تحبها</p></div>
  <div class="card"><h4>الألعاب</h4><p>شخصيات تتحرك بذكاء</p></div>
  <div class="card"><h4>الخرائط</h4><p>تُظهر الطريق الأسرع</p></div>
  <div class="card"><h4>الصور</h4><p>الهاتف يرتّب صور وجهك</p></div>
</div>
{idea("<p>بعض الأدوات ماهرة في شيء واحد (مثل تمييز الوجوه). وبعضها يقدر يكتب ويرسم ويشرح. لا تحتاج حفظ أسماء معقدة. فقط تذكّر: هناك أدوات كثيرة… ونحن سنتعلم أشهرها.</p>")}
{try_it("<p>اسأل شخصاً كبيراً: «أين نرى الذكاء الاصطناعي في بيتنا؟» اكتبوا معاً 3 أشياء.</p>")}
"""))

    # PART 2 ChatGPT
    parts.append(part("2", "ابدأ مع ChatGPT", "هيا نفتح أشهر صديق ذكي… خطوة خطوة."))

    parts.append(chapter("3", "افتح الموقع", f"""
<p class="lead">سنذهب إلى موقع <span class="en">ChatGPT</span>. اتبع الخطوات بهدوء.</p>
{step(1, "افتح المتصفح", "مثل Chrome أو أي متصفح عندك. هذا البرنامج الذي تفتح به الإنترنت.")}
{step(2, "اضغط خانة الكتابة فوق", "في أعلى الصفحة يوجد مكان للكتابة (شريط العنوان).")}
{fig(img["open"], "اكتب chatgpt.com في الأعلى")}
{step(3, "اكتب هذا", 'اكتب بالإنجليزية بالضبط: <strong class="en">chatgpt.com</strong> ثم اضغط Enter.')}
{step(4, "انتظر الصفحة", "ستفتح صفحة ChatGPT. إذا لم تفتح، اطلب مساعدة شخص كبير.")}
{safe("<p>لا تدخل إلى مواقع غريبة تشبه الاسم. الموقع الصحيح: <span class='en'>chatgpt.com</span></p>")}
{try_it("<p>افتح المتصفح الآن واكتب <span class='en'>chatgpt.com</span>. هل ظهرت الصفحة؟ ضع علامة ✓</p>")}
"""))

    parts.append(chapter("4", "اصنع حساباً", f"""
<p class="lead">للحفظ والمتابعة تحتاج حساباً. افعل هذا مع شخص كبير.</p>
{fig(img["account"], "إنشاء حساب مع مساعدة كبيرة")}
{step(1, "ابحث عن زر التسجيل", "قد ترى كلمات مثل Sign up أو إنشاء حساب.")}
{step(2, "استخدم بريداً بإذن", "الشخص الكبير يضع بريداً إلكترونياً خاصاً به أو مناسباً لك.")}
{step(3, "كلمة السر سرّية", "لا تشارك كلمة السر مع أصدقاء الصف. فقط مع ولي أمرك إن احتجت.")}
{step(4, "أكّد الحساب", "أحياناً تصل رسالة إلى البريد. الشخص الكبير يفتحها ويكمل.")}
{safe("<p>لا تكتب اسم مدرستك الحقيقي، عنوان بيتك، أو رقم هاتف داخل المحادثة.</p>")}
"""))

    parts.append(chapter("5", "اسأل أول سؤال", f"""
<p class="lead">الآن الجزء الممتع: اكتب سؤالاً واضغط إرسال.</p>
{fig(img["ask"], "اكتب سؤالك في الصندوق الأسفل")}
{step(1, "ابحث عن صندوق الكتابة", "عادة في أسفل الصفحة.")}
{step(2, "اكتب سؤالاً سهلاً", "مثلاً: «اشرح لي القمر كأنني طفل 8 سنوات.»")}
{step(3, "اضغط إرسال", "زر السهم أو Enter.")}
{step(4, "اقرأ الجواب", "إذا لم تفهم… اكتب: «اشرح أسهل.»")}
<div class="bubble">مثال سؤال جيد:<br/>علّمني جدول 7 بطريقة لعبة ممتعة.</div>
{try_it("<p>اسأل الآن: «أعطني نكتة قصيرة عن القطط.» ثم اسأل: «أعطني نكتة أخرى.»</p>")}
{takeaways([
  "نكتب في الصندوق السفلي.",
  "إذا صعب الجواب نطلب شرحاً أسهل.",
  "يمكن سؤال أكثر من مرة."
])}
"""))

    parts.append(chapter("6", "أسئلة ممتعة للتجربة", f"""
<p class="lead">انسخ فكرة… وغيّرها كما تحب.</p>
{prompt("اشرح لي البرق كأنني في الصف الثاني.")}
{prompt("اخترع قصة قصيرة عن روبوت يحب الآيس كريم.")}
{prompt("أعطني 5 أفكار لرسم سهل بالألوان.")}
{prompt("ساعدني أرتّب حقيبتي للمدرسة غداً في 4 خطوات.")}
{prompt("حوّل هذه الجملة إلى لغز مضحك: الشمس تشرق صباحاً.")}
{idea("<p>إذا أجاب بشيء غريب أو خطأ… قل لشخص كبير. الذكاء الاصطناعي يخطئ أحياناً.</p>")}
"""))

    # PART 3 friends
    parts.append(part("3", "أصدقاء آخرون", "ChatGPT ليس الوحيد. هناك أصدقاء أذكياء آخرون."))

    parts.append(chapter("7", "تعرّف على Claude", f"""
<p class="lead"><span class="en">Claude</span> صديق ذكي آخر. كثير من الناس يحبونه للكتابة الطويلة والشرح الهادئ.</p>
{fig(img["friends"], "ChatGPT و Claude و Gemini أصدقاء مساعدون")}
<h2>متى تجربه؟</h2>
<ul>
  <li>عندما تريد قصة أطول</li>
  <li>عندما تريد تلخيص درس بهدوء</li>
  <li>عندما تريد مساعدة في ترتيب أفكارك</li>
</ul>
{step(1, "افتح موقعه مع شخص كبير", "ابحثوا معاً عن Claude AI من الشركة Anthropic.")}
{step(2, "سجّل الدخول", "مثل أي موقع… بمساعدة كبيرة.")}
{step(3, "اسأله بنفس أسلوب ChatGPT", "اكتب بوضوح واطلب شرحاً سهلاً.")}
{idea("<p>فكّر هكذا: ChatGPT صديق سريع وكثير المهارات. Claude صديق هادئ يحب الشرح الجميل.</p>")}
"""))

    parts.append(chapter("8", "تعرّف على Gemini", f"""
<p class="lead"><span class="en">Gemini</span> من Google. مفيد إذا كنت تستخدم أدوات Google.</p>
<ul>
  <li>يساعد في الشرح والبحث</li>
  <li>يرتبط أحياناً بخدمات Google</li>
  <li>طريقة السؤال نفسها: اكتب بوضوح!</li>
</ul>
{try_it("<p>مع شخص كبير: افتحوا Gemini واسألوا: «علّمني دورة الماء في الطبيعة بكلمات أطفال.»</p>")}
"""))

    parts.append(chapter("9", "أي صديق نختار؟", f"""
<p class="lead">لا تحتاج حفظ جداول معقدة. استخدم هذه القاعدة الذهبية:</p>
<div class="cards">
  <div class="card"><h4>للسؤال العام</h4><p>ابدأ بـ ChatGPT</p></div>
  <div class="card"><h4>للشرح الطويل</h4><p>جرّب Claude</p></div>
  <div class="card"><h4>مع عالم Google</h4><p>جرّب Gemini</p></div>
  <div class="card"><h4>مهم جداً</h4><p>اسأل شخصاً كبيراً دائماً</p></div>
</div>
{idea("<p>الأهم ليس اسم الأداة… الأهم أن تسأل سؤالاً واضحاً.</p>")}
"""))

    # PART 4 prompting
    parts.append(part("4", "كيف نتكلم معه؟", "السر ليس كلمات سحرية. السر أن تكون واضحاً ولطيفاً."))

    parts.append(chapter("10", "اطلب بوضوح", f"""
<p class="lead">إذا قلت «ساعدني» فقط… لن يعرف بماذا. إذا قلت طلبك بوضوح… يساعدك أفضل.</p>
{fig(img["howto"], "4 خطوات للكلام الواضح")}
<h2>ضعيف</h2>
{prompt("ساعدني.")}
<h2>أفضل</h2>
{prompt("اشرح لي الحيوانات العاشبة في 5 جمل سهلة.")}
{takeaways([
  "وضّح ماذا تريد.",
  "قل لمن الجواب (لطفل مثلي).",
  "قل الشكل: نقاط أو قصة قصيرة."
])}
"""))

    parts.append(chapter("11", "أعطِه دوراً", f"""
<p class="lead">يمكنك أن تقول له: تظاهر أنك معلّم… أو قاصّ قصص… أو مدرب ألعاب.</p>
{prompt("أنت معلّم علوم لطيف للأطفال. اشرح لي لماذا السماء زرقاء بكلمات بسيطة جداً.")}
{prompt("أنت قاصّ قصص مضحكة. اكتب قصة من 6 جمل عن تنين يخاف من الفقاعات.")}
{prompt("أنت مدرّب كرة قدم للأطفال. أعطني تمارين منزلية آمنة لمدة 10 دقائق.")}
{try_it("<p>اختر دوراً واحداً وجرّبه الآن. هل صار الجواب أجمل؟</p>")}
"""))

    parts.append(chapter("12", "أضف تفاصيل", f"""
<p class="lead">التفاصيل مثل المكونات في الكعكة. كلّما أوضحت أكثر… النتيجة ألذ.</p>
<h2>أضف دائماً</h2>
<ul>
  <li>الموضوع</li>
  <li>لمن؟ (عمري 8 سنوات)</li>
  <li>الطول (قصير / 5 نقاط)</li>
  <li>الأسلوب (مضحك / هادئ / كقصة)</li>
</ul>
{prompt("""الموضوع: الفضاء
لمن: طفل عمره 8 سنوات
الطول: فقرة قصيرة
الأسلوب: ممتع مع مثال
المطلوب: ما هو النجم؟""")}
{idea("<p>بعد الجواب اكتب: «اجعله أقصر» أو «أضف مثالاً» أو «اجعله أسهل».</p>")}
"""))

    parts.append(chapter("13", "ألعاب تدريب", f"""
<p class="lead">تدريب = لعب!</p>
{try_it("<p><strong>لعبة 1:</strong> اطلب نفس السؤال بطريقتين: قصيرة وطويلة. أي جواب أحببت؟</p>")}
{try_it("<p><strong>لعبة 2:</strong> أعطِه دور معلّم ثم دور مهرّج لنفس الموضوع. قارن.</p>")}
{try_it("<p><strong>لعبة 3:</strong> اطلب قائمة 5 أفكار لهدية عيد ميلاد لصديق يحب الرسم.</p>")}
{prompt("أعطني 3 عناوين مضحكة لقصة عن قطة رائدة فضاء.")}
"""))

    # PART 5 images
    parts.append(part("5", "اصنع صوراً", "يمكنك أن تطلب صورة… كما تطلب رسمة من صديق."))

    parts.append(chapter("14", "اطلب صورة", f"""
<p class="lead">بعض الأدوات ترسم بالذكاء الاصطناعي. داخل ChatGPT يمكنك غالباً طلب صورة.</p>
{fig(img["picture"], "اطلب صورة واضحة وممتعة")}
{step(1, "افتح المحادثة", "في ChatGPT أو أداة الصور التي يسمح بها ولي أمرك.")}
{step(2, "اكتب ماذا تريد أن ترى", "مثال: ديناصور لطيف يقرأ كتاباً.")}
{step(3, "انتظر الصورة", "ثم قل: غيّر اللون إلى أزرق… أو اجعله يضحك.")}
{safe("<p>لا تطلب صور أصدقائك الحقيقيين أو أشخاص غرباء. اطلب شخصيات خيالية لطيفة.</p>")}
"""))

    parts.append(chapter("15", "صف الصورة ببساطة", f"""
<p class="lead">لا تحتاج كلمات صعبة. قل 4 أشياء فقط:</p>
<ol>
  <li>من؟ (قطة / روبوت / طفل مستكشف)</li>
  <li>ماذا يفعل؟</li>
  <li>أين؟</li>
  <li>ما الإحساس؟ (مرح / هادئ / مغامرة)</li>
</ol>
{prompt("ارسم روبوتاً صغيراً يزرع وردة في حديقة، ألوان دافئة، شكل لطيف للأطفال.")}
{prompt("ارسم قلعة سحابية فوق البحر، ألوان باستيل، بدون رعب.")}
{prompt("ارسم حقيبة مدرسية تطير بين النجوم، أسلوب كرتوني سعيد.")}
{try_it("<p>اختر حيوانك المفضل واطلب له صورة وهو يلعب رياضتك المفضلة.</p>")}
"""))

    # PART 6 extras
    parts.append(part("6", "مرح إضافي", "الصوت والموسيقى والفيديو… فكرة سريعة فقط."))

    parts.append(chapter("16", "صوت وموسيقى", f"""
<p class="lead">بعض الأدوات تحول الكتابة إلى صوت… أو تصنع مقطوعة موسيقية قصيرة.</p>
<ul>
  <li>اكتب نصاً قصيراً ثم اطلب قراءته بصوت لطيف (مع شخص كبير).</li>
  <li>للموسيقى: صف الإحساس مثل «موسيقى سعيدة لوقت الرسم».</li>
</ul>
{prompt("موسيقى هادئة ومرحة لمدة قصيرة لوقت المطالعة، بدون كلام مخيف.")}
{safe("<p>استمع دائماً بحضور شخص كبير للأدوات الجديدة.</p>")}
"""))

    parts.append(chapter("17", "فيديو قصير", f"""
<p class="lead">هناك أدوات تصنع فيديو قصير من جملة. النتائج تتغير بسرعة… والأهم الفكرة.</p>
{step(1, "اكتب مشهداً قصيراً", "قطة تلعب بالخيط في غرفة مضيئة.")}
{step(2, "اطلب مدة قصيرة", "ثوانٍ قليلة كافية.")}
{step(3, "شاهد مع شخص كبير", "واختر المقطع الأجمل.")}
{idea("<p>لا تحتاج إخراج فيلم طويل. فكرة صغيرة = نجاح كبير.</p>")}
"""))

    # PART 7 projects
    parts.append(part("7", "مشاريع ممتعة", "اختر مشروعاً… وأنهه اليوم!"))

    projects = [
        ("كاتب القصص", "اكتب قصة 10 جمل عن بطلك المفضل", "ChatGPT أو Claude", "دور قاصّ + تفاصيل البطل + طلب رسمة غلاف"),
        ("معلّم الرياضيات اللطيف", "افهم فكرة واحدة صعبة في حسابك", "ChatGPT", "اشرح كأنني 8 سنوات + مثال + تمرين صغير"),
        ("بطاقة عيد ميلاد", "نص جميل لبطاقة", "ChatGPT + رسم", "اكتب تهنئة قصيرة ثم اطلب صورة احتفال"),
        ("مدرب المفردات", "تعلّم 7 كلمات جديدة", "ChatGPT", "كلمة + معنى سهل + جملة + رسم ذهني"),
        ("عالم الفضاء الصغير", "ملصق معلومات عن كوكب", "ChatGPT", "5 حقائق سهلة + صورة متخيلة للكوكب"),
        ("نادي النكات النظيف", "5 نكات مناسبة للأطفال", "ChatGPT", "اطلب نكات لطيفة بدون إحراج"),
        ("مخطط الحقيبة", "قائمة صباح المدرسة", "ChatGPT", "خطوات صباحية قصيرة مع وقت"),
        ("مسرحية دقائق", "حوار بين شخصين لـ 1 دقيقة", "Claude", "مشهد مضحك قصير لتمثيله مع صديق"),
        ("مجلة الصف", "عنوان + فقرة خبر مدرسي خيالي", "Gemini أو ChatGPT", "اكتب خبر «روبوت زار مدرستنا»"),
        ("يوميات الامتنان", "3 أشياء جميلة حصلت اليوم", "ChatGPT", "حوّلها إلى فقرة يوميات لطيفة"),
    ]
    proj_html = ['<p class="lead">كل مشروع صغير… لكنه يعلمك مهارة كبيرة.</p>']
    for i, (name, goal, tools, how) in enumerate(projects, 1):
        proj_html.append(f"""
<div class="project">
  <h3>مشروع {i}: {name}</h3>
  <p class="meta">الهدف: {goal}<br/>الأداة: <span class="en">{tools}</span></p>
  <p><strong>كيف؟</strong> {how}</p>
</div>
""")
    proj_html.append(try_it("<p>اختر مشروعاً واحداً الآن وأهه خلال 15 دقيقة.</p>"))
    parts.append(chapter("18", "عشرة مشاريع للأطفال", "\n".join(proj_html)))

    # PART 8 safety
    parts.append(part("8", "كن بطلاً آمناً", "القوة الحقيقية = الذكاء + الأمان + اللطف."))

    parts.append(chapter("19", "قواعد الأمان", f"""
{fig(img["safe"], "ابقَ آمناً ولطيفاً على الإنترنت")}
<ol>
  <li>لا تشارك كلمة السر.</li>
  <li>لا تكتب عنوان بيتك أو رقم هاتفك في المحادثة.</li>
  <li>إذا ظهر شيء يخيفك… أغلق الصفحة وأخبر شخصاً كبيراً.</li>
  <li>كن لطيفاً في كلامك. الكلمات الطيبة تصنع أجوبة أجمل.</li>
  <li>لا تنسخ واجب المدرسة كاملاً بدون فهم. اطلب شرحاً لتتعلّم.</li>
</ol>
{safe("<p>الذكاء الاصطناعي يخطئ أحياناً. لا تصدّق كل شيء بسرعة. اسأل معلّمك أو ولي أمرك.</p>")}
{takeaways([
  "الأمان أولاً.",
  "اطلب مساعدة كبيرة عند الحاجة.",
  "تعلّم… لا تغش."
])}
"""))

    parts.append(chapter("20", "ماذا بعد؟", f"""
<p class="lead">أحسنت! أنت الآن تعرف البداية.</p>
<h2>خطتك للأسبوع القادم</h2>
<ol>
  <li>كل يوم: سؤال واحد واضح لـ ChatGPT</li>
  <li>يومين: تجربة دور مختلف (معلّم / قاصّ)</li>
  <li>مرة: اصنع صورة واحدة لطيفة</li>
  <li>مرة: أنهِ مشروعاً من درس 18</li>
</ol>
<div class="bubble me">أنت صار عندك مفتاح سحري: السؤال الواضح.</div>
{idea("<p>علّم صديقاً واحداً ما تعلمته. التعليم يثبت الفهم!</p>")}
<p class="colophon">نهاية كتاب الأطفال<br/>من إعداد <strong class="en">SCHOOLERX</strong><br/>كبرت الآن خطوة… إلى لقاء في المغامرة التالية!</p>
"""))

    parts.append("</article></body></html>")
    return "".join(parts)


def main():
    # Fix accidental typo in CSS if any
    html = build().replace("--gold: #FFC manifest;", "--gold: #FFC94D;")
    # also fix if downstream leftover
    html = html.replace(" downstream ", " ")
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
