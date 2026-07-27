"""Additional chapter expansions for the AI beginner handbook generator."""

EXPANSIONS = {
    "4": """
<h2>Choosing and switching LLMs like a pro</h2>
<p>Beginners often ask, "Which model is best?" A better question is, "Which model is best for this job, with this data, at this budget?" Treat LLMs like specialists on a bench. One may be stronger at careful writing, another at fast brainstorming, another at coding, another at live web research, and another at multimodal understanding.</p>
<table>
  <thead><tr><th>Need</th><th>Model habit to prefer</th><th>Switch when...</th></tr></thead>
  <tbody>
    <tr><td>Polished writing</td><td>Give voice samples and ask for revisions</td><td>The output sounds generic after two critique passes</td></tr>
    <tr><td>Analysis</td><td>Ask for assumptions, tradeoffs, and uncertainty</td><td>It ignores constraints or overstates confidence</td></tr>
    <tr><td>Long documents</td><td>Use large context or Projects-style knowledge</td><td>It forgets earlier sections or invents details</td></tr>
    <tr><td>Fresh facts</td><td>Use search or research tools with citations</td><td>Answers need current prices, dates, laws, or news</td></tr>
    <tr><td>Images, files, audio</td><td>Use multimodal input directly</td><td>You are describing a file that you could simply upload</td></tr>
  </tbody>
</table>
<div class="callout tip"><span class="callout-label">Tip</span><p>Run important prompts in two models, then ask a third pass: "Compare these two answers. Where do they disagree? Which parts are best supported?" This is cheaper than being confidently wrong.</p></div>
<h2>When to switch models</h2>
<ul>
  <li><strong>After a clear failure:</strong> If a model misunderstands the task twice, switch instead of endlessly rewording.</li>
  <li><strong>When the modality changes:</strong> A text model may not be the best choice for screenshots, charts, invoices, or photos.</li>
  <li><strong>When stakes increase:</strong> For legal, medical, financial, or public-facing work, use the model/tool with stronger grounding, citations, and review controls.</li>
  <li><strong>When speed matters:</strong> Use smaller/faster models for extraction, tagging, rewriting, and drafts. Save premium models for judgment-heavy work.</li>
</ul>
<h2>Multimodal tips</h2>
<p>When uploading an image or PDF, do not just ask, "What is this?" Give the model a job. For example, ask it to inspect a landing page screenshot for trust gaps, summarize a chart for executives, or extract action items from a photographed whiteboard.</p>
<div class="prompt">Analyze this screenshot as a conversion specialist. Return: 1) what the page is trying to sell, 2) the strongest trust signals, 3) the top five friction points, 4) specific copy or layout fixes. If something is unreadable, say so.</div>
<div class="callout warn"><span class="callout-label">Warning</span><p>Multimodal models can misread small text, confusing charts, and cropped screenshots. Zoom in, upload originals when possible, and verify numbers manually before using them.</p></div>
""",
    "6": """
<h2>Claude Projects: practical setup</h2>
<p>A Claude Project is most useful when it has a stable job. Instead of one giant "work" project, create focused spaces such as <em>Newsletter Editor</em>, <em>Client Proposal Assistant</em>, or <em>Support Policy Helper</em>. Add only the knowledge that should shape answers: voice guide, offer details, example work, policies, FAQs, and current constraints.</p>
<ol>
  <li><strong>Name the outcome:</strong> "Draft client-ready proposals" beats "Marketing help."</li>
  <li><strong>Add project instructions:</strong> Role, audience, tone, forbidden claims, preferred format, and when to ask clarifying questions.</li>
  <li><strong>Upload source material:</strong> Keep it curated. Remove outdated docs so the assistant does not blend old and new facts.</li>
  <li><strong>Save winning prompts:</strong> Put your best repeat prompts in the Project notes or your AI Playbook.</li>
</ol>
<div class="callout example"><span class="callout-label">Artifacts examples</span><ul><li>A one-page sales proposal that you can edit in the side panel.</li><li>A simple landing page mockup in HTML.</li><li>A comparison table for vendor selection.</li><li>A checklist, rubric, or SOP your team can reuse.</li></ul></div>
<h2>Eight practical Claude prompts</h2>
<div class="prompt">Using the Project knowledge, draft a client proposal for [client]. Include problem, recommended plan, timeline, assumptions, and open questions. Do not invent pricing.</div>
<div class="prompt">Turn this messy transcript into a clean SOP with owner, trigger, tools, steps, quality check, and escalation path.</div>
<div class="prompt">Critique this draft against our voice guide. Return a table: issue, why it matters, suggested rewrite.</div>
<div class="prompt">Create an Artifact: a one-page executive brief from these notes. Use headings, bullets, and a final recommendation.</div>
<div class="prompt">Act as a skeptical customer. List the objections this landing page does not answer yet.</div>
<div class="prompt">Summarize these sources into claims we can safely make, claims needing evidence, and claims to avoid.</div>
<div class="prompt">Build a reusable checklist for reviewing [deliverable] before it goes to a client.</div>
<div class="prompt">Create three versions of this email: warm, concise, and firm. Preserve the facts exactly.</div>
<div class="callout mistake"><span class="callout-label">Common mistakes</span><ul><li>Uploading every file "just in case" instead of curating sources.</li><li>Using Projects for private data without checking company policy.</li><li>Asking for a final answer before asking Claude to inspect gaps.</li><li>Forgetting that Artifacts are drafts, not automatically approved assets.</li></ul></div>
""",
    "7": """
<h2>Gemini inside Workspace: everyday workflows</h2>
<p>Gemini becomes valuable when it works where your files already live. The trick is to use it for bounded tasks: summarize a thread, draft a Doc section, find patterns across notes, or turn a Drive folder into a briefing. Keep sensitive data rules in mind, especially in shared workspaces.</p>
<h3>Gmail workflow: thread to decision</h3>
<ol>
  <li>Open the thread and ask for the current decision, blockers, and people mentioned.</li>
  <li>Ask Gemini to draft a reply with a specific tone and length.</li>
  <li>Check names, dates, attachments, commitments, and quoted facts.</li>
  <li>Send only after you personally approve the wording.</li>
</ol>
<h3>Docs workflow: rough notes to polished page</h3>
<ol>
  <li>Paste messy notes into a Doc.</li>
  <li>Ask for an outline first, not a full draft.</li>
  <li>Approve the structure, then ask for one section at a time.</li>
  <li>Use comments or suggestions for edits instead of overwriting important text.</li>
</ol>
<h3>Drive workflow: folder to brief</h3>
<ol>
  <li>Collect the relevant Docs, Sheets, PDFs, and slides in one folder.</li>
  <li>Ask for a source-aware summary: what is known, missing, and contradictory.</li>
  <li>Ask for a deliverable such as an FAQ, project brief, or decision memo.</li>
</ol>
<div class="workflow"><strong>Workspace operating loop</strong><div class="flow"><span class="step">Find source</span><span class="arrow">&rarr;</span><span class="step">Ask narrow question</span><span class="arrow">&rarr;</span><span class="step">Draft</span><span class="arrow">&rarr;</span><span class="step">Verify</span><span class="arrow">&rarr;</span><span class="step">Share</span></div></div>
<h2>Six Gemini prompts</h2>
<div class="prompt">Summarize this Gmail thread into decisions, open questions, promised follow-ups, and risks. Quote the message date for each commitment.</div>
<div class="prompt">Draft a 150-word reply that is friendly, clear, and action-oriented. Include two options for next steps.</div>
<div class="prompt">Turn this Doc into an executive summary with: context, recommendation, tradeoffs, and next action.</div>
<div class="prompt">Review this proposal for unclear claims, missing evidence, and places where a table would help.</div>
<div class="prompt">From these Drive files, create a project brief. Separate confirmed facts from assumptions.</div>
<div class="prompt">Create a meeting agenda from this Doc and recent email context. Limit to 30 minutes.</div>
<div class="callout warn"><span class="callout-label">Grounding check</span><p>Workspace AI can sound certain while pulling from the wrong file or old thread. Ask it to identify the source document or message before you trust an answer.</p></div>
""",
    "8": """
<h2>Deep research workflow</h2>
<p>Perplexity is strongest when you treat research as a pipeline, not a single answer. Start broad, narrow the question, inspect sources, then synthesize. Your goal is not to collect links; it is to reach a defensible conclusion with citations you would be comfortable showing a manager or client.</p>
<ol>
  <li><strong>Frame the research question:</strong> Include geography, date range, audience, and decision you need to make.</li>
  <li><strong>Run a broad scan:</strong> Ask for the landscape, major viewpoints, and key terms you should know.</li>
  <li><strong>Open the sources:</strong> Check publication date, author, original data, and whether the page actually supports the claim.</li>
  <li><strong>Ask follow-ups:</strong> Request counterarguments, recent changes, and primary sources.</li>
  <li><strong>Export a brief:</strong> Summary, evidence table, open questions, and recommendation.</li>
</ol>
<div class="callout tip"><span class="callout-label">Citation hygiene</span><p>Prefer primary sources, official docs, peer-reviewed papers, government datasets, company filings, and reputable reporting. Do not cite a page just because it was returned. Click it, scan it, and confirm the cited line supports your statement.</p></div>
<h2>Six research prompts</h2>
<div class="prompt">Research [topic] for a beginner business owner in [country]. Give the current landscape, important terms, top risks, and five sources worth reading.</div>
<div class="prompt">Find recent data on [market]. Prefer primary sources. Return a table with claim, source, date, and confidence.</div>
<div class="prompt">What are the strongest arguments for and against [decision]? Include citations for each side and note what evidence is missing.</div>
<div class="prompt">Create a buyer's guide for [software category]. Compare pricing model, best-fit customer, limitations, and recent changes.</div>
<div class="prompt">Build a timeline of major developments in [topic] over the last 24 months. Cite each milestone.</div>
<div class="prompt">I need to brief my team on [issue]. Produce a one-page memo with recommendation, evidence, risks, and next questions.</div>
<h2>Perplexity vs ChatGPT search</h2>
<table>
  <thead><tr><th>Use Perplexity when...</th><th>Use ChatGPT search when...</th></tr></thead>
  <tbody>
    <tr><td>You want fast citation-first research and source discovery.</td><td>You want research blended into drafting, planning, or analysis.</td></tr>
    <tr><td>The source list matters as much as the answer.</td><td>You will iterate toward a deliverable such as a memo or email.</td></tr>
    <tr><td>You are comparing current public information.</td><td>You need conversation memory, files, or custom instructions involved.</td></tr>
  </tbody>
</table>
""",
    "9": """
<h2>NotebookLM business playbooks</h2>
<p>NotebookLM is best when you want answers grounded in your own material. Think of each notebook as a mini knowledge base for one job: onboarding, policies, product research, sales enablement, grant writing, or course creation. The quality of the notebook depends less on the AI and more on the sources you choose.</p>
<h3>Source curation rules</h3>
<ul>
  <li><strong>Use authoritative files:</strong> final policies, current product docs, approved messaging, transcripts, contracts you are allowed to analyze, and research PDFs.</li>
  <li><strong>Remove stale material:</strong> If old pricing or policies remain, NotebookLM may blend them with current facts.</li>
  <li><strong>Name sources clearly:</strong> "2026 Pricing FAQ" is better than "final_v3_reallyfinal.pdf."</li>
  <li><strong>Ask source-specific questions:</strong> "According to the onboarding guide..." keeps answers grounded.</li>
</ul>
<div class="callout example"><span class="callout-label">Five detailed use cases</span><ol><li><strong>Support policy desk:</strong> Upload refund rules, warranty terms, escalation SOPs, and macros. Ask for draft replies with cited policy sections.</li><li><strong>Sales battlecard:</strong> Add competitor notes, product docs, objections, and case studies. Generate talk tracks and objection responses.</li><li><strong>Employee onboarding:</strong> Upload handbook, benefits guide, org chart, and role SOPs. Create a first-week FAQ and quiz.</li><li><strong>Course builder:</strong> Add lesson transcripts, readings, and worksheets. Generate study guides, flashcards, and module summaries.</li><li><strong>Research room:</strong> Add reports and interviews. Ask for themes, contradictions, evidence tables, and open questions.</li></ol></div>
<h2>Study guide and podcast tips</h2>
<p>The study guide is great for turning dense sources into a learning path. Use it, then ask follow-up questions about weak areas. Audio overviews are useful for first exposure, commute review, or stakeholder previews, but they should not replace reading the cited sections for high-stakes work.</p>
<div class="prompt">Using only the uploaded sources, create a study guide for a new team member. Include key terms, must-read sources, a 10-question quiz, and common misunderstandings.</div>
<div class="prompt">Create a business briefing from these sources. Separate facts, interpretations, risks, and recommended next actions. Cite the source for each major claim.</div>
<div class="callout mistake"><span class="callout-label">Common mistake</span><p>Do not make one giant notebook for your whole company. Smaller notebooks produce clearer answers and are easier to audit.</p></div>
""",
    "10": """
<h2>The five components of a strong prompt</h2>
<p>A prompt is a brief. Good briefs reduce guessing. Most beginner prompts fail because they include a task but omit context, audience, constraints, source material, and output format.</p>
<table>
  <thead><tr><th>Component</th><th>What it answers</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td>Role</td><td>Who should the AI act like?</td><td>Act as a practical small-business CFO.</td></tr>
    <tr><td>Task</td><td>What should it produce?</td><td>Create a cash-flow checklist.</td></tr>
    <tr><td>Context</td><td>What background matters?</td><td>Audience: first-time agency owner.</td></tr>
    <tr><td>Constraints</td><td>What boundaries apply?</td><td>No jargon; max 12 items; flag risks.</td></tr>
    <tr><td>Format</td><td>How should output look?</td><td>Table with priority, action, and why.</td></tr>
  </tbody>
</table>
<h2>Before and after</h2>
<div class="callout mistake"><span class="callout-label">Before</span><p>"Write a marketing plan for my bakery."</p></div>
<div class="callout example"><span class="callout-label">After</span><div class="prompt">Act as a local business marketing strategist. Create a 30-day marketing plan for a neighborhood sourdough bakery in Austin. Goal: increase weekday morning foot traffic. Budget: $500. Audience: office workers within 2 miles. Include daily actions, low-cost partnership ideas, email/social copy themes, and how to measure success. Table format.</div></div>
<p>The second prompt gives the model something to optimize. It can now make tradeoffs instead of writing generic advice.</p>
<h2>Temperature and style intuition</h2>
<p>If a tool exposes temperature or creativity settings, think of it as a "variation dial." Low settings are better for extraction, summaries, policy replies, and structured outputs. Higher settings are useful for names, hooks, concepts, and brainstorming. If the tool does not expose temperature, you can still steer style with words such as "literal," "conservative," "playful," "unexpected," or "executive."</p>
<div class="workflow"><strong>Prompt iteration loop</strong><div class="flow"><span class="step">Draft brief</span><span class="arrow">&rarr;</span><span class="step">Generate</span><span class="arrow">&rarr;</span><span class="step">Critique</span><span class="arrow">&rarr;</span><span class="step">Add constraints</span><span class="arrow">&rarr;</span><span class="step">Finalize</span></div></div>
<div class="takeaway"><h3>Verification checklist</h3><ul><li>Are facts traceable to a source?</li><li>Did it follow the requested format?</li><li>Are assumptions labeled?</li><li>Could a beginner act on the answer?</li><li>Does the tone match the audience?</li></ul></div>
""",
    "13": """
<h2>Diffusion with a little more detail</h2>
<p>Diffusion models learn by seeing images with noise added to them, then learning how to remove that noise step by step. During generation, the model starts with noise and repeatedly nudges it toward patterns that match your prompt. This is why small wording changes can shift composition, lighting, or style: the prompt guides many tiny decisions, not one single drawing command.</p>
<p>Most tools also support some form of reference image, image editing, or control input. A reference image can lock the subject, pose, style, or composition more reliably than text alone. Use text for intent and references for consistency.</p>
<h2>Styles glossary</h2>
<table>
  <thead><tr><th>Style term</th><th>Use it when you want...</th></tr></thead>
  <tbody>
    <tr><td>Editorial photo</td><td>Magazine-like realism with polished composition.</td></tr>
    <tr><td>Product packshot</td><td>Clean e-commerce images with controlled lighting.</td></tr>
    <tr><td>Isometric 3D</td><td>Friendly app, SaaS, or explainer visuals.</td></tr>
    <tr><td>Watercolor</td><td>Soft education, children's content, or gentle storytelling.</td></tr>
    <tr><td>Vector illustration</td><td>Flat icons, infographics, and brand systems.</td></tr>
    <tr><td>Cinematic still</td><td>Dramatic light, film framing, and story mood.</td></tr>
  </tbody>
</table>
<h2>Tool picker flowchart</h2>
<div class="workflow"><strong>Pick your image tool</strong><div class="flow"><span class="step">Need best aesthetics?</span><span class="arrow">&rarr;</span><span class="step">Midjourney</span><span class="arrow">&rarr;</span><span class="step">Need text in image?</span><span class="arrow">&rarr;</span><span class="step">Ideogram</span><span class="arrow">&rarr;</span><span class="step">Need chat edits?</span><span class="arrow">&rarr;</span><span class="step">DALL-E</span><span class="arrow">&rarr;</span><span class="step">Need design workflow?</span><span class="arrow">&rarr;</span><span class="step">Leonardo or Flux tools</span></div></div>
<div class="prompt">Create a product hero image for [product]. Subject: [details]. Setting: [surface/background]. Lighting: soft studio side light. Style: premium editorial product photography. Composition: room for headline text on the left. Avoid distorted labels, extra logos, and unrealistic hands.</div>
<h2>Ethics and practical rights</h2>
<p>Use AI images to accelerate concepts, mood boards, ads, thumbnails, and internal drafts. Be careful with living artists' names, celebrity likenesses, medical or political imagery, and anything that could deceive people. For commercial work, save the prompt, tool, date, license terms, and final edits. That record helps you answer client questions later.</p>
<div class="callout warn"><span class="callout-label">Beginner rule</span><p>If the image could affect someone's reputation, finances, safety, or legal rights, add human review and disclose synthetic content where appropriate.</p></div>
""",
    "15": """
<h2>Think in shots, not scenes</h2>
<p>Video AI works best when you ask for one clear shot at a time. A "scene" may include multiple camera angles, actions, and timing changes. A "shot" is simpler: one subject, one action, one camera move, one mood. If you need a 30-second ad, plan it as five or six short clips and edit them together.</p>
<table>
  <thead><tr><th>Shot type</th><th>What it does</th><th>Prompt cue</th></tr></thead>
  <tbody>
    <tr><td>Establishing</td><td>Shows place and context</td><td>wide shot of...</td></tr>
    <tr><td>Medium</td><td>Shows person and action</td><td>medium shot, waist up...</td></tr>
    <tr><td>Close-up</td><td>Shows detail or emotion</td><td>macro close-up of hands...</td></tr>
    <tr><td>Over-the-shoulder</td><td>Shows a screen or conversation</td><td>over the shoulder, laptop visible...</td></tr>
    <tr><td>Product hero</td><td>Makes an object feel premium</td><td>slow push-in, studio lighting...</td></tr>
  </tbody>
</table>
<h2>Aspect ratios</h2>
<ul>
  <li><strong>16:9:</strong> YouTube, websites, presentations, horizontal ads.</li>
  <li><strong>9:16:</strong> TikTok, Reels, Shorts, mobile-first stories.</li>
  <li><strong>1:1:</strong> Feed posts, simple product loops, flexible social assets.</li>
  <li><strong>4:5:</strong> Social feed ads where vertical space matters.</li>
</ul>
<div class="callout note"><span class="callout-label">Limitations</span><p>Video models still struggle with exact text, consistent faces across many shots, complex physics, precise product labels, and long cause-and-effect sequences. Generate short clips, then use normal editing tools for timing, captions, logos, and audio.</p></div>
<h2>Beginner production pipeline</h2>
<div class="workflow"><strong>15-second social ad</strong><div class="flow"><span class="step">Write message</span><span class="arrow">&rarr;</span><span class="step">Storyboard 3 shots</span><span class="arrow">&rarr;</span><span class="step">Generate stills</span><span class="arrow">&rarr;</span><span class="step">Animate clips</span><span class="arrow">&rarr;</span><span class="step">Edit</span><span class="arrow">&rarr;</span><span class="step">Add captions</span></div></div>
<div class="prompt">Shot 2 of 4: close-up of a founder placing a handmade candle into a shipping box, warm morning window light, shallow depth of field, slow push-in, realistic small business documentary style, 5 seconds, vertical 9:16, no readable brand text.</div>
<div class="exercise"><h4>Exercise - Build a shot list</h4><p>Choose one product or idea. Write five shots: opening, problem, solution, proof, and call to action. Keep each prompt under 60 words.</p></div>
""",
    "17": """
<h2>Expanded video tool comparison</h2>
<table>
  <thead><tr><th>Tool</th><th>Best workflow</th><th>Strengths</th><th>Beginner watch-out</th></tr></thead>
  <tbody>
    <tr><td>Runway</td><td>Creative suite for generating, extending, editing, and experimenting.</td><td>Useful controls, creator-friendly interface, strong for teams.</td><td>Credits disappear quickly if you generate without a shot plan.</td></tr>
    <tr><td>Kling</td><td>Cinematic motion tests, expressive action, social clips.</td><td>Often strong motion and dramatic visual results.</td><td>Access, limits, and policies can change by region.</td></tr>
    <tr><td>Pika</td><td>Fast ideation, stylized clips, simple image-to-video tests.</td><td>Quick to learn and good for playful social concepts.</td><td>Less ideal when you need fine production control.</td></tr>
    <tr><td>Sora</td><td>High-end text or image-to-video when available.</td><td>Strong scene understanding and premium output potential.</td><td>Availability, limits, and review policies matter.</td></tr>
    <tr><td>Veo</td><td>Cinematic prompting within the Google ecosystem.</td><td>Good fit for users already working in Google tools.</td><td>Prompt clarity still matters more than brand name.</td></tr>
  </tbody>
</table>
<h2>Workflow for each tool type</h2>
<h3>Runway-style creator suite</h3>
<ol><li>Start with a reference image or clear text prompt.</li><li>Generate 3-5 variations.</li><li>Use edit/extend tools only on the strongest take.</li><li>Export the best seconds into your editor.</li></ol>
<h3>Kling/Sora/Veo-style cinematic generation</h3>
<ol><li>Write a film-style shot description.</li><li>Keep motion physically plausible.</li><li>Generate separate shots for different angles.</li><li>Add captions, logos, and sound in post.</li></ol>
<h3>Pika-style fast social iteration</h3>
<ol><li>Use a bold simple concept.</li><li>Try multiple styles quickly.</li><li>Pick the most shareable result.</li><li>Do not over-polish a joke or trend clip.</li></ol>
<div class="callout tip"><span class="callout-label">Picking guide</span><p>If you are learning, choose the tool with the easiest access and enough credits to practice. If you are serving clients, choose the tool with predictable licensing, review features, and export quality. If you are making social content, speed and iteration may matter more than perfect realism.</p></div>
<div class="prompt">Compare these five video concepts for [brand]. Score each for feasibility with AI video, visual clarity, likely cost in iterations, and business value. Recommend the safest first test.</div>
""",
    "18": """
<h2>Practical voice settings</h2>
<p>ElevenLabs and PlayHT both reward careful script preparation. Before changing voices endlessly, fix the script: short sentences, clear pronunciation, natural pauses, and one idea per line. Then adjust settings. Names vary by tool, but the concepts are similar.</p>
<table>
  <thead><tr><th>Setting</th><th>Beginner intuition</th><th>Use carefully when...</th></tr></thead>
  <tbody>
    <tr><td>Stability</td><td>Higher is more consistent; lower can feel more expressive.</td><td>The read sounds flat or too unpredictable.</td></tr>
    <tr><td>Similarity</td><td>How closely the generated voice follows the selected voice.</td><td>Cloned voices require consent and policy review.</td></tr>
    <tr><td>Style / exaggeration</td><td>Adds performance energy.</td><td>Too much can sound salesy or unnatural.</td></tr>
    <tr><td>Speed</td><td>Controls pacing.</td><td>Educational content usually needs slower pacing than ads.</td></tr>
  </tbody>
</table>
<h2>Script formatting that helps</h2>
<div class="prompt">Welcome to the quick tour. [PAUSE]<br/>In the next sixty seconds, you will learn the three features that save the most time.<br/><br/>First: automatic meeting notes. [SHORT PAUSE]<br/>Second: follow-up drafts. [SHORT PAUSE]<br/>Third: weekly summaries your team can actually read.</div>
<p>Use line breaks where a human would breathe. Spell unusual names phonetically in parentheses. Avoid long clauses, dense numbers, and tongue-twisters. For technical videos, generate a rough read first, listen for awkward phrases, then rewrite the script before final generation.</p>
<h2>Use cases</h2>
<ul>
  <li>Training videos and internal SOP walkthroughs.</li>
  <li>Podcast intros, ad reads, and trailer drafts.</li>
  <li>Product explainers, app demos, and onboarding tours.</li>
  <li>Accessibility versions of written guides.</li>
  <li>Placeholder narration before hiring a human narrator.</li>
</ul>
<div class="callout mistake"><span class="callout-label">Common mistakes</span><ul><li>Generating from a script written for reading, not listening.</li><li>Using a cloned voice without written permission.</li><li>Publishing without checking pronunciation of names, prices, and URLs.</li><li>Leaving breaths, silence, or music mix to the AI tool instead of editing audio properly.</li></ul></div>
""",
    "19": """
<h2>Suno and Udio prompt formulas</h2>
<p>Music prompts work best when they describe the musical container, not just the topic. Include genre, mood, tempo, instrumentation, vocal style, structure, and what to avoid. If you write lyrics, keep lines singable: short, concrete, and rhythmic.</p>
<div class="prompt">Formula: [genre] + [mood] + [tempo] + [instruments] + [vocal style] + [song structure] + [theme] + [avoid].</div>
<table>
  <thead><tr><th>Prompt part</th><th>Examples</th></tr></thead>
  <tbody>
    <tr><td>Genre</td><td>indie pop, lo-fi hip hop, acoustic folk, synthwave, orchestral trailer</td></tr>
    <tr><td>Mood</td><td>optimistic, reflective, playful, cinematic, calm</td></tr>
    <tr><td>Tempo</td><td>80 BPM ballad, 100 BPM walking pace, 128 BPM dance</td></tr>
    <tr><td>Structure</td><td>verse, pre-chorus, chorus, bridge, final chorus</td></tr>
  </tbody>
</table>
<h2>Eight music prompts</h2>
<ol class="small">
  <li>Upbeat indie pop, 105 BPM, handclaps, clean guitar, warm male vocal, chorus about starting before you feel ready.</li>
  <li>Lo-fi hip hop study loop, mellow keys, vinyl texture, no vocals, 75 BPM, calm and focused.</li>
  <li>Corporate explainer bed, light marimba and soft synth pulse, optimistic, seamless loop, no vocals.</li>
  <li>Acoustic folk song, intimate female vocal, fingerpicked guitar, lyrics about building a small business one day at a time.</li>
  <li>Synthwave intro, 90s tech optimism, driving bass, bright arpeggios, no vocals, 30-second theme.</li>
  <li>Children's educational song, playful ukulele, simple chorus teaching the word "algorithm," friendly group vocals.</li>
  <li>Cinematic trailer cue, low strings, rising percussion, hopeful final lift, no choir, 60 seconds.</li>
  <li>Podcast outro, relaxed neo-soul groove, Rhodes piano, tasteful drums, no lead vocal, fade ending.</li>
</ol>
<div class="callout warn"><span class="callout-label">Commercial use notes</span><p>Check the plan terms before publishing, monetizing, or giving tracks to clients. Keep records of the tool, prompt, date, subscription level, and any human edits. If you need exclusivity, brand ownership, or broadcast certainty, talk to a music licensing professional or hire a composer.</p></div>
<div class="callout tip"><span class="callout-label">Practical habit</span><p>Generate three variations from the same prompt: one safe, one more energetic, and one more minimal. The best music direction often appears by comparison.</p></div>
""",
    "20": """
<h2>A full daily productivity system</h2>
<p>The best personal AI system is simple enough to use on a busy day. Give AI three jobs: capture, clarify, and convert. Capture messy input from email, meetings, notes, and reading. Clarify what matters. Convert it into replies, tasks, study notes, or decisions.</p>
<div class="workflow"><strong>Daily AI operating rhythm</strong><div class="flow"><span class="step">Morning plan</span><span class="arrow">&rarr;</span><span class="step">Inbox triage</span><span class="arrow">&rarr;</span><span class="step">Meeting capture</span><span class="arrow">&rarr;</span><span class="step">Learning block</span><span class="arrow">&rarr;</span><span class="step">End-of-day review</span></div></div>
<h3>Morning planning prompt</h3>
<div class="prompt">Here are my tasks, calendar, and constraints for today: [paste]. Help me choose the top three outcomes, identify quick wins, and create a realistic schedule with buffers. Ask if anything is unclear.</div>
<h3>Email template</h3>
<div class="prompt">Draft a reply to this email thread. Goal: [goal]. Tone: [warm/firm/brief]. Include: acknowledgement, answer, next step, and deadline if needed. Do not promise anything not stated in the thread.</div>
<h3>Meeting template</h3>
<div class="prompt">From this transcript, produce: summary, decisions, action items with owner and due date, risks, open questions, and a follow-up email draft. Flag unclear owners.</div>
<h3>Learning template</h3>
<div class="prompt">Teach me [topic] as a beginner. First explain the mental model, then give a worked example, common mistakes, a 10-question quiz, and a 7-day practice plan.</div>
<h2>End-of-day review</h2>
<p>At the end of the day, paste completed tasks, unfinished work, and any meeting notes. Ask AI to identify loose ends and draft tomorrow's first work block. This prevents the "where was I?" problem that wastes the first hour of many mornings.</p>
<div class="callout tip"><span class="callout-label">Make it stick</span><p>Use one notes app as your command center. If your prompts, summaries, and action lists are scattered across five tools, the system will feel impressive but fail in practice.</p></div>
<div class="action-steps"><h3>Action Steps</h3><ol><li>Create a reusable "Daily AI Desk" note.</li><li>Add the four templates above.</li><li>Use them for five workdays before changing the system.</li></ol></div>
""",
    "21": """
<h2>Department playbooks</h2>
<p>Business AI works when each team has a repeatable playbook: approved sources, safe prompts, review rules, and success metrics. Avoid the vague instruction "use AI more." Give each department one workflow that saves time without lowering quality.</p>
<table>
  <thead><tr><th>Department</th><th>High-value AI job</th><th>Sample prompt</th></tr></thead>
  <tbody>
    <tr><td>Marketing</td><td>Campaign drafts and content repurposing</td><td>Turn this webinar transcript into five LinkedIn posts, three email angles, and a landing page FAQ. Preserve claims exactly.</td></tr>
    <tr><td>Support</td><td>Policy-aware draft replies</td><td>Using only the refund policy below, draft a calm customer reply and cite the policy line that supports it.</td></tr>
    <tr><td>Sales</td><td>Call summaries and follow-ups</td><td>Summarize this sales call into pain points, buying signals, objections, next steps, and a personalized follow-up email.</td></tr>
    <tr><td>HR</td><td>Structured hiring and onboarding docs</td><td>Create an interview scorecard for [role] based on this job description. Include consistent criteria and bias cautions.</td></tr>
    <tr><td>Operations</td><td>SOPs, incident reviews, vendor comparisons</td><td>Turn these process notes into an SOP with owner, trigger, steps, QA check, and escalation path.</td></tr>
  </tbody>
</table>
<h2>Review rules by risk</h2>
<ul>
  <li><strong>Low risk:</strong> Internal summaries, brainstorming, first drafts. Light review.</li>
  <li><strong>Medium risk:</strong> Customer emails, hiring materials, sales claims. Human approval required.</li>
  <li><strong>High risk:</strong> Legal, medical, financial, disciplinary, security, or public crisis communication. Expert review required.</li>
</ul>
<div class="callout example"><span class="callout-label">Support playbook</span><p>Sources: help center, refund policy, escalation matrix, tone guide. Workflow: classify issue, retrieve policy, draft reply, flag uncertainty, human sends. Metric: first response time improves while customer satisfaction stays stable.</p></div>
<div class="callout tip"><span class="callout-label">Manager tip</span><p>Ask teams to save before-and-after examples. A small library of real wins is more persuasive than a slide deck about AI transformation.</p></div>
<div class="exercise"><h4>Exercise - One workflow per team</h4><p>Pick one department. Write its approved sources, forbidden uses, review rule, and one prompt that can be tested this week.</p></div>
""",
    "22": """
<h2>Triggers, actions, and AI in the middle</h2>
<p>An automation begins when a trigger happens: a form is submitted, an email is labeled, a row is added, a date arrives, or a webhook receives data. Actions do the work: create a task, send a message, update a CRM, draft an email, or write a file. AI is most useful in the middle, where messy human language must become structured decisions.</p>
<table>
  <thead><tr><th>AI-in-the-middle pattern</th><th>Example</th><th>Guardrail</th></tr></thead>
  <tbody>
    <tr><td>Classify</td><td>Tag support email as billing, bug, refund, or urgent.</td><td>Escalate if confidence is low.</td></tr>
    <tr><td>Extract</td><td>Pull name, company, budget, and deadline from a form.</td><td>Validate required fields before writing.</td></tr>
    <tr><td>Draft</td><td>Create a reply, proposal, or social post.</td><td>Save as draft for approval.</td></tr>
    <tr><td>Summarize</td><td>Turn a call transcript into CRM notes.</td><td>Link back to transcript.</td></tr>
    <tr><td>Route</td><td>Send leads to the right salesperson.</td><td>Log the reason for routing.</td></tr>
  </tbody>
</table>
<h2>Failure modes to expect</h2>
<ul>
  <li>Bad trigger data: missing fields, duplicate records, or unexpected file types.</li>
  <li>Overconfident AI: the model guesses instead of saying it does not know.</li>
  <li>Silent breakage: an app permission expires and the workflow stops.</li>
  <li>Runaway volume: a loop creates hundreds of tasks or messages.</li>
  <li>No owner: everyone assumes the automation is being monitored.</li>
</ul>
<h2>Decision tree</h2>
<div class="workflow"><strong>Should you automate?</strong><div class="flow"><span class="step">Repeated weekly?</span><span class="arrow">&rarr;</span><span class="step">Rules clear?</span><span class="arrow">&rarr;</span><span class="step">Mistakes reversible?</span><span class="arrow">&rarr;</span><span class="step">Human approval needed?</span><span class="arrow">&rarr;</span><span class="step">Build small test</span></div></div>
<div class="callout warn"><span class="callout-label">Safety rule</span><p>For any workflow that sends external messages, changes money, deletes data, or updates official records, start with a draft or review queue. Earn autonomy with logs and evidence.</p></div>
<div class="prompt">Design an automation for [task]. List trigger, inputs, AI step, output format, actions, failure modes, human approval points, and success metric.</div>
""",
    "23": """
<h2>n8n install notes</h2>
<p>n8n can run in n8n Cloud or self-hosted. Cloud is easiest for beginners because hosting, updates, and availability are handled for you. Self-hosting gives more control over data location and advanced configuration, but you become responsible for updates, backups, security, and uptime. If you self-host, use the official docs, start with a simple Docker setup, protect credentials, and do not expose test workflows publicly.</p>
<div class="callout note"><span class="callout-label">AI agent nodes concept</span><p>In n8n, AI features can act like a reasoning step inside a workflow. The model receives structured input, may use connected tools, and returns a result for later nodes. Keep the agent's job narrow: extract fields, classify a ticket, draft a response, or choose the next route.</p></div>
<h2>Workflow 1: lead enrichment</h2>
<ol>
  <li>Trigger: new Typeform or website form submission.</li>
  <li>Set node: normalize fields such as name, email, company, budget, and need.</li>
  <li>AI node: summarize the lead and score fit from 1-5 using your criteria.</li>
  <li>IF node: route high-fit leads to CRM and low-fit leads to a nurture list.</li>
  <li>Action: create CRM record, Slack alert, and follow-up task.</li>
  <li>Log: write score, reason, and raw submission to a Sheet for audit.</li>
</ol>
<h2>Workflow 2: support triage</h2>
<ol>
  <li>Trigger: new support email or help desk ticket.</li>
  <li>AI node: classify category, urgency, sentiment, and requested outcome.</li>
  <li>Knowledge step: include policy snippets or links if available.</li>
  <li>Action: assign queue and draft a reply.</li>
  <li>Approval: human reviews urgent, refund, legal, or angry tickets.</li>
  <li>Metric: track response time and re-open rate.</li>
</ol>
<h2>Workflow 3: weekly metrics narrative</h2>
<ol>
  <li>Trigger: schedule every Monday morning.</li>
  <li>Read nodes: pull rows from Sheets, analytics, or CRM.</li>
  <li>Function/Set node: calculate changes from last week.</li>
  <li>AI node: write a plain-English narrative with wins, risks, and questions.</li>
  <li>Action: send to Slack or email as a draft.</li>
  <li>Review: manager confirms before it becomes the official report.</li>
</ol>
""",
    "24": """
<h2>Make modules explained</h2>
<p>In Make, a scenario is a visual chain of modules. A module can watch for new data, search records, transform text, call an AI service, create a record, or send a message. Routers split a scenario into paths, filters decide whether data continues, and iterators handle lists such as line items or multiple attachments.</p>
<table>
  <thead><tr><th>Make concept</th><th>Plain-English meaning</th></tr></thead>
  <tbody>
    <tr><td>Trigger module</td><td>The event that starts the scenario.</td></tr>
    <tr><td>Action module</td><td>A step that does something in an app.</td></tr>
    <tr><td>Router</td><td>A fork in the road for different paths.</td></tr>
    <tr><td>Filter</td><td>A rule that decides whether a path runs.</td></tr>
    <tr><td>Formatter / tools</td><td>Clean dates, text, numbers, and lists.</td></tr>
  </tbody>
</table>
<h2>Scenario 1: lead ad to CRM</h2>
<ol><li>Trigger: new Facebook Lead Ad.</li><li>AI module: summarize need and score fit.</li><li>Filter: continue only if email is present.</li><li>Router: high score to sales Slack, lower score to nurture list.</li><li>Action: create or update HubSpot contact.</li><li>Email module: send a personalized first-touch draft to a review inbox.</li></ol>
<h2>Scenario 2: YouTube upload package</h2>
<ol><li>Trigger: new video in YouTube channel or row marked ready.</li><li>Get transcript or paste script from Drive.</li><li>AI module: create title options, description, chapters, and shorts ideas.</li><li>Google Docs module: write packaging draft.</li><li>Slack module: notify editor with the Doc link.</li><li>Filter: do not publish automatically.</li></ol>
<h2>Scenario 3: low CSAT recovery</h2>
<ol><li>Trigger: survey response with rating below threshold.</li><li>Search module: find customer account and recent tickets.</li><li>AI module: summarize likely issue and draft apology response.</li><li>Router: billing, bug, or service complaint paths.</li><li>Create ticket for manager review.</li><li>Log outcome in a Sheet for monthly analysis.</li></ol>
<div class="callout tip"><span class="callout-label">Make habit</span><p>Run scenarios with sample data first. Inspect every bundle so you know exactly what each module receives and sends.</p></div>
""",
    "25": """
<h2>Zapier paths, filters, and formatters</h2>
<p>Zapier is friendly because it hides much of the technical plumbing. The advanced power comes from three ideas. <strong>Filters</strong> stop a Zap unless conditions are met. <strong>Paths</strong> send different cases down different branches. <strong>Formatters</strong> clean text, dates, numbers, line items, and names so later steps receive predictable data.</p>
<div class="callout note"><span class="callout-label">AI by Zapier</span><p>AI by Zapier can summarize, classify, extract, and draft inside a Zap. Give it a narrow job and a strict output format. For external messages, create drafts or approval tasks instead of sending automatically at first.</p></div>
<h2>Zap 1: Gmail label to draft reply</h2>
<ol>
  <li>Trigger: new Gmail message with label "AI draft."</li>
  <li>AI step: summarize sender intent and draft a reply in your tone.</li>
  <li>Formatter: trim long quoted threads if needed.</li>
  <li>Filter: continue only if the message is not from a blocked domain.</li>
  <li>Action: create Gmail draft.</li>
  <li>Action: add a task reminding you to review it.</li>
</ol>
<h2>Zap 2: Typeform feedback to Slack insight</h2>
<ol>
  <li>Trigger: new Typeform response.</li>
  <li>AI step: classify sentiment, theme, and urgency.</li>
  <li>Paths: bug reports to product channel, praise to wins channel, urgent complaints to support lead.</li>
  <li>Action: write all responses to a Sheet.</li>
  <li>Weekly digest Zap: summarize themes for the team.</li>
</ol>
<h2>Zap 3: new CRM deal to kickoff checklist</h2>
<ol>
  <li>Trigger: deal moves to "closed won."</li>
  <li>Search: find company and primary contact.</li>
  <li>AI step: create kickoff checklist from deal notes.</li>
  <li>Formatter: split checklist into task lines.</li>
  <li>Action: create project tasks in Asana, Trello, or ClickUp.</li>
  <li>Action: draft welcome email for account owner approval.</li>
</ol>
<div class="callout mistake"><span class="callout-label">Beginner mistake</span><p>Do not build a 20-step Zap on day one. Build three steps, test with real data, then add filters and paths after you see where messy cases appear.</p></div>
""",
    "26": """
<h2>Agent architecture by analogy</h2>
<p>Imagine hiring an intern for a specific job. The LLM is the intern's reasoning and communication ability. Tools are what the intern is allowed to use: browser, email, calendar, database, spreadsheet, code runner, or CRM. Memory is the notebook they keep. Planning is the habit of breaking a goal into steps. Guardrails are the manager's rules: budget, permissions, review points, and when to stop.</p>
<table>
  <thead><tr><th>Agent part</th><th>Beginner analogy</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td>Goal</td><td>The assignment</td><td>Prepare a weekly competitor brief.</td></tr>
    <tr><td>Tools</td><td>Allowed apps</td><td>Search web, read Drive folder, create Doc.</td></tr>
    <tr><td>Memory</td><td>Working notes</td><td>Previous competitor list and style preferences.</td></tr>
    <tr><td>Planner</td><td>To-do list</td><td>Find sources, extract claims, compare, draft.</td></tr>
    <tr><td>Evaluator</td><td>Quality check</td><td>Are all claims cited? Is the brief under one page?</td></tr>
  </tbody>
</table>
<h2>Tools, memory, and planning examples</h2>
<ul>
  <li><strong>Tool example:</strong> A support agent can read a policy notebook and draft replies, but cannot issue refunds without approval.</li>
  <li><strong>Memory example:</strong> A personal planning agent remembers your preferred working hours and recurring goals, but not private data it does not need.</li>
  <li><strong>Planning example:</strong> A research agent first lists questions, then searches, then writes a source table, then drafts a memo.</li>
</ul>
<div class="callout warn"><span class="callout-label">Risks</span><ul><li><strong>Compounding errors:</strong> One bad assumption can affect many later actions.</li><li><strong>Tool misuse:</strong> The agent may update the wrong record or message the wrong person.</li><li><strong>Runaway loops:</strong> Poor stop conditions can waste time, credits, or API calls.</li><li><strong>Data exposure:</strong> Broad permissions create bigger privacy risk.</li></ul></div>
<div class="prompt">Write an agent spec for [workflow]. Include goal, allowed tools, forbidden actions, memory needed, step plan, approval gates, logs, success metric, and kill switch.</div>
<div class="callout tip"><span class="callout-label">Safe starting point</span><p>If you cannot describe the workflow as a checklist, it is too early to make it an agent. Build a supervised automation first.</p></div>
""",
    "27": """
<h2>Five agent workflow specs</h2>
<h3>1. Marketing campaign assistant</h3>
<p><strong>Goal:</strong> create a campaign draft pack from approved product facts. <strong>Tools:</strong> brand docs, product page, calendar, Doc creation. <strong>Output:</strong> audience, hooks, email draft, social variants, review checklist. <strong>Approval:</strong> marketer approves before publishing.</p>
<h3>2. Support response assistant</h3>
<p><strong>Goal:</strong> reduce first-response time. <strong>Tools:</strong> policy notebook, ticket system, macro library. <strong>Output:</strong> category, urgency, draft reply, cited policy. <strong>Escalate:</strong> angry customers, refunds, legal threats, safety issues, low confidence.</p>
<h3>3. Research briefing agent</h3>
<p><strong>Goal:</strong> prepare a weekly brief on a defined topic. <strong>Tools:</strong> web search, saved source list, Docs. <strong>Output:</strong> source table, key changes, risks, recommendation. <strong>Rule:</strong> no uncited factual claims.</p>
<h3>4. Operations SOP agent</h3>
<p><strong>Goal:</strong> turn transcripts and notes into standard operating procedures. <strong>Tools:</strong> transcript folder, SOP template, task manager. <strong>Output:</strong> SOP draft, checklist, missing questions. <strong>Approval:</strong> process owner signs off.</p>
<h3>5. Personal weekly planning agent</h3>
<p><strong>Goal:</strong> convert calendar, tasks, and goals into a realistic week plan. <strong>Tools:</strong> calendar read access, task list, notes. <strong>Output:</strong> top outcomes, schedule blocks, risks, prep list. <strong>Limit:</strong> read-only until trusted.</p>
<h2>Evaluation tips</h2>
<table>
  <thead><tr><th>Metric</th><th>Question to ask</th></tr></thead>
  <tbody>
    <tr><td>Accuracy</td><td>Are facts correct and sourced?</td></tr>
    <tr><td>Usefulness</td><td>Would a human act on the output without rewriting everything?</td></tr>
    <tr><td>Safety</td><td>Did it avoid forbidden actions and escalate correctly?</td></tr>
    <tr><td>Cost</td><td>How many runs, credits, or API calls did it use?</td></tr>
    <tr><td>Reliability</td><td>Does it work on boring real cases, not just demos?</td></tr>
  </tbody>
</table>
<div class="callout example"><span class="callout-label">Test set</span><p>Before launch, collect 20 real examples: easy, normal, edge case, and failure case. Run the agent, score the outputs, and fix the instructions before adding more autonomy.</p></div>
<div class="action-steps"><h3>Action Steps</h3><ol><li>Pick one spec above.</li><li>Define forbidden actions and escalation rules.</li><li>Run it manually for 10 cases before automating.</li></ol></div>
""",
    "29": """
<h2>Trends that matter to beginners</h2>
<p>The future of AI can sound abstract, but the practical implication is simple: more work will move from "open a blank page" to "brief, supervise, verify, and improve." Beginners should not try to predict every model release. Build durable habits that improve with any tool: clear instructions, good source material, thoughtful review, and workflow design.</p>
<table>
  <thead><tr><th>Trend</th><th>What it means in practice</th><th>Beginner move</th></tr></thead>
  <tbody>
    <tr><td>Multimodal tools</td><td>Text, images, audio, video, files, and screens work together.</td><td>Practice uploading real materials and asking specific questions.</td></tr>
    <tr><td>Longer context</td><td>Models can work with bigger documents and project histories.</td><td>Learn source curation and document hygiene.</td></tr>
    <tr><td>Agents</td><td>AI will take more multi-step actions with tools.</td><td>Study automation, permissions, logging, and approval gates.</td></tr>
    <tr><td>On-device AI</td><td>Some AI runs locally on phones and computers.</td><td>Watch for privacy-friendly workflows and offline assistants.</td></tr>
    <tr><td>Regulation and provenance</td><td>Disclosure, rights, and audit trails matter more.</td><td>Keep records of prompts, sources, licenses, and human review.</td></tr>
  </tbody>
</table>
<h2>Careers shaped by AI</h2>
<table>
  <thead><tr><th>Career direction</th><th>Core skill</th><th>Portfolio proof</th></tr></thead>
  <tbody>
    <tr><td>AI productivity specialist</td><td>Prompting and workflow redesign</td><td>Before/after case studies with hours saved.</td></tr>
    <tr><td>Automation builder</td><td>Zapier, Make, n8n, APIs, guardrails</td><td>Five working workflows with logs and documentation.</td></tr>
    <tr><td>AI content producer</td><td>Writing, image/video/audio direction</td><td>Campaign pack, thumbnails, scripts, and edited samples.</td></tr>
    <tr><td>AI operations analyst</td><td>Process mapping, data cleanup, reporting</td><td>SOP library and weekly metrics narrative system.</td></tr>
    <tr><td>Domain expert with AI</td><td>Deep field knowledge plus AI leverage</td><td>Specialized assistant, research brief, or decision tool.</td></tr>
  </tbody>
</table>
<div class="callout tip"><span class="callout-label">Practical implication</span><p>The safest career bet is to combine AI fluency with a real domain: healthcare admin, education, law operations, marketing, finance, construction, nonprofits, or local business. AI skill without context is shallow; domain skill with AI becomes leverage.</p></div>
<div class="exercise"><h4>Exercise - Pick your trend bet</h4><p>Choose one trend above. Write a 30-day practice project that produces visible proof: a workflow, a brief, a content pack, or a small internal tool.</p></div>
""",
}

CSS_FIXES = """
.cover { min-height: auto; height: 220mm; page-break-after: always; }
.cover-inner { min-height: auto; height: 100%; }
.part-opener { min-height: auto !important; padding: 0.35em 0 0.7em !important; justify-content: flex-start; }
@media print {
  .part-opener { break-after: avoid; page-break-after: avoid; }
  .callout, .prompt, .workflow, .takeaway, .action-steps, .exercise { break-inside: avoid; page-break-inside: avoid; }
  table { break-inside: auto; page-break-inside: auto; }
  ol.small li, ul.small li { margin-bottom: 0.12em; }
  ol.small, ul.small { font-size: 0.84rem; line-height: 1.32; }
}
"""
