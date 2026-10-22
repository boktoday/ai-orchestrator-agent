# Talk to your agent: a glossary of the words that get good work

A working vocabulary for ordinary people directing an AI agent. Every term: what it means in plain words, and how to say it so the agent does the right thing. Built from real work: websites, agents, voice, video, research, cron briefs.

## How to use this

Three habits beat any word list:
1. **Name the thing.** "The header" beats "the top bit".
2. **Say the outcome, not the vibe.** "Make the heading 36px on phones" beats "make it pop".
3. **Give the test.** "Check it at 390px wide and show me a screenshot" tells the agent when it is done.

Every entry below ends with **Say:**: a sentence you can copy.

---

# 1. The web page

**HTML page**: the actual file a browser reads. Structure, not looks.
Say: "Give me one HTML file I can open by double-clicking."

**CSS**: the styling rules: colours, spacing, fonts. Separate from HTML on purpose.
Say: "Put the styling in a CSS block inside the same file."

**Hero section**: the big top area with the headline, sub-line and main button. The first screen.
Say: "Rebuild the hero: headline, one-line sub, button, and a photo on the right."

**Feature card**: a small box with an icon, a title and two lines of text, repeated in a row.
Say: "Three feature cards under the hero."

**CTA (call to action)**: the button or line that tells the reader what to do next.
Say: "One clear CTA: Book a consultation."

**Header / navbar**: the strip at the top with the logo, links and menu button.
Say: "Make the header sticky and give it 24px side padding."

**Footer**: the bottom strip: contact, legal, copyright.
Say: "Footer with email, phone and ABN."

**Hamburger menu**: the three-line button that opens the mobile menu.
Say: "At phone width, hide the links and use a hamburger that actually opens."

**Hero illustration / hero art**: the picture on the right of the hero.
Say: "Illustration on the right, same palette, nothing cluttered."

**SVG**: a picture drawn with maths, so it stays sharp at any size. Logos and icons.
Say: "Give me the logo as an SVG, not a PNG."

**Raster vs vector**: a photo is raster (pixels, blurs when enlarged); a logo should be vector (SVG).
Say: "That logo is blurry when big. Rebuild it as a vector."

**Hex colour**: the six-character colour code, e.g. `#2e7c5b`. Exact, unlike "green".
Say: "Use #e3a468 for buttons and #1a120f for text."

**Palette**: the fixed set of colours the brand uses.
Say: "Stick to the palette: cream, ink, terracotta, sage."

**Typeface / font stack**: the fonts. A stack lists fallbacks.
Say: "Headings in Fraunces, body in Inter, system fonts as fallback."

**Padding vs margin**: padding is space inside the box; margin is space outside it. Mixing them up squashes layouts.
Say: "Add 16px padding inside the card, not margin."

**Spacing shorthand trap**: `padding: 14px 0` also sets left and right to zero and can wipe earlier padding. Ask for specific sides.
Say: "Set padding-top and padding-bottom only; leave the sides alone."

**Border radius**: how rounded the corners are. Zero means sharp corners.
Say: "border-radius: 0 everywhere. Sharp corners."

**Grid / flexbox**: two layout systems. Grid for rows and columns of cards; flex for a single row of things.
Say: "Lay the cards out with grid, three across on desktop, one on phones."

**Responsive**: adapts to screen size.
Say: "Make it responsive: three columns at 1440px, one column at 390px."

**Breakpoint**: the width where the layout changes.
Say: "Switch to the mobile layout below 820px."

**Viewport**: the visible area of the screen. Also the meta tag that tells phones not to zoom out.
Say: "Include the viewport meta tag."

**Overflow**: content wider than the screen, causing sideways scrolling. The most common phone bug.
Say: "Check for horizontal overflow at 390px and fix it."

**Clipping / clipped**: something cut off by its container. Text touching an edge or a letter half-gone.
Say: "The O looks clipped. Add padding to the icon's viewBox."

**CSS clip / clip-path**: intentionally cutting a shape, like masking a photo into an arch.
Say: "Clip the photo into an arch shape."

**Media query**: the CSS rule that applies only at certain sizes.
Say: "Put the mobile adjustments inside a max-width: 820px media query."

**Accessibility (a11y)**: usable with screen readers, keyboards, and thumbs. Labels, tap targets, contrast.
Say: "Add aria-labels to icon buttons and make tap targets at least 44px."

**Alt text**: the words a screen reader speaks for an image.
Say: "Write alt text for every image."

**Favicon**: the little icon in the browser tab.
Say: "Add a favicon in the brand colours."

**OG card / social image**: the preview image shown when a link is shared.
Say: "Make a 1200×630 OG card and wire the meta tags."

**Metadata / meta tags**: hidden page information: title, description, preview image, canonical address.
Say: "Set the title, description, og:title, og:image and canonical URL."

**Canonical URL**: the one official address of a page, so search engines do not treat copies as duplicates.
Say: "Set the canonical to https://example.com/."

**Slug**: the address fragment, e.g. `/hire` in `example.com/hire`.
Say: "Use /hire as the slug, no .html."

**SEO**: search engine optimisation: being found. Titles, headings, speed, links, structure.
Say: "Audit the SEO: title, description, one H1, alt text, sitemap."

**AEO / llms.txt**: optimisation for AI assistants: a plain-text file at `/llms.txt` that tells AI tools what the site is and what it offers.
Say: "Write an llms.txt and add it to the root."

**robots.txt**: instructions for crawlers.
Say: "Add robots.txt pointing at the sitemap."

**sitemap.xml**: a list of every page, for search engines.
Say: "Generate sitemap.xml with all pages."

**JSON-LD / schema markup**: structured data in the page that tells machines what the content is: an article, a person, an FAQ.
Say: "Add JSON-LD for Person and Organization."

**Landing page**: a single page built to get one action, not to browse.
Say: "Build a landing page with one CTA and no navigation."

**Conversion**: the percentage of visitors who do the thing.
Say: "Where does the visitor drop off before booking?"

---

# 2. Files, code and versions

**Repo (repository)**: the project's folder, versioned, usually on GitHub.
Say: "Put this in the repo, not just my Desktop."

**Commit**: a saved snapshot with a message. The undo point.
Say: "Commit it with a clear message."

**Push**: send commits to the remote (GitHub). Local only means nobody else can see it.
Say: "Push it and tell me the commit hash."

**Branch**: a parallel copy for work in progress.
Say: "Do this on a branch, not on main."

**Pull request (PR)**: a proposal to merge a branch, with review.
Say: "Open a PR so I can see the diff."

**Diff**: exactly what changed, line by line.
Say: "Show me the diff before you push."

**Deploy**: publish the site so the world sees it.
Say: "Deploy and give me the live URL."

**Live vs local**: local is a file on your machine; live is what visitors see. They are not the same and the difference explains most "it looks fine here" surprises.
Say: "Check the live site, not the local file."

**Cache / hard refresh**: the browser or CDN keeps an old copy. Ctrl+F5 forces a fresh one.
Say: "The page looks old. Is it a cache problem?"

**CDN**: servers worldwide that serve the same files, fast.
Say: "Serve the assets from the CDN."

**Static site**: plain files, no server code. Cheap, fast, hard to break.
Say: "Make it a static site, no backend."

**Server**: a computer that answers requests and holds data.
Say: "This needs a server, not a static page."

**Local-first**: the app works on the device; the internet is optional. Data stays home.
Say: "Make it local-first: everything works offline, data stays on the device."

**IndexedDB / localStorage**: two ways a browser stores data on the device. localStorage is simple key-value; IndexedDB handles real records.
Say: "Save the answers in IndexedDB so they survive a refresh."

**Environment variable / .env**: settings and secrets kept outside the code, in a file that never ships.
Say: "Put the key in .env and read it from there, never paste secrets into the page."

**API**: a way for one program to ask another to do something.
Say: "Call the weather API and show the result."

**API key**: the password that lets your program use someone's service. A secret, always.
Say: "Which key does it need, and where is it stored?"

**Endpoint**: the specific address of one API action.
Say: "POST to this endpoint with the token in the header."

**HTTP status**: the answer code: 200 fine, 404 not found, 429 rate limited, 500 server broke.
Say: "What status did it return?"

**Rate limit**: you are asking too fast and the service says wait.
Say: "It is rate limited. Back off and retry."

**Webhook**: a message one service sends to yours when something happens.
Say: "Set a webhook so the form submission lands in my inbox."

**JSON**: the standard text format for data: `{"key": "value"}`.
Say: "Return it as JSON and pretty-print it."

**Markdown**: simple text formatting with `#` headings and `-` bullets.
Say: "Give it to me as markdown."

**Token**: the unit of text a model reads and is billed for: roughly three-quarters of a word.
Say: "That file is long. Will it fit in the context window?"

**Context window**: the model's working memory in one go.
Say: "Summarise the document first, then work from the summary."

---

# 3. The agent itself

**Agent**: an AI that can do things: read files, run commands, browse, build, then check its own work.
Say: "Do it end to end and verify the result."

**Harness**: the program that gives the model tools, memory and rules. Hermes is one.
Say: "Set this up as a Hermes job."

**Skill**: a saved procedure the agent loads when a task matches. Reusable know-how.
Say: "Turn this into a skill so you remember how next time."

**Tool call**: one action the agent takes: run a command, read a file, fetch a page.
Say: "Use a tool call to check the live page, don't guess."

**Prompt**: what you tell the agent. Specific beats polite.
Say: "Here is the goal, the constraints and how to check success."

**System prompt / profile**: standing instructions that shape how the agent behaves every time.
Say: "Make that part of your standing instructions."

**Memory**: facts the agent keeps across sessions.
Say: "Remember that permanently."

**Context**: everything the agent is holding in its head for this task. It is finite.
Say: "The context is getting long. Write a handoff before it compacts."

**Guardrails**: limits on what the agent may do without asking.
Say: "Ask before anything destructive or public."

**Approval / human-in-the-loop**: a pause for your yes on irreversible steps.
Say: "Do not delete or publish anything without my yes."

**Sandbox**: an isolated place to run risky things.
Say: "Try it in a scratch folder first."

**Autonomy level**: how far the agent goes alone: report, draft, do, or do-and-publish.
Say: "Draft only tonight. I'll say before it goes live."

**Cron job / scheduled task**: work that happens on a clock without you.
Say: "Every Monday at 6:45, send me the fuel brief."

**Webhook subscription**: the agent wakes on an event instead of a clock.
Say: "Watch the feed and tell me when it changes."

**Hallucination**: confident invention. The agent says it knows when it guessed.
Say: "Do not fill gaps. Say 'I don't know' and go and check."

**Grounding**: checking answers against real sources instead of memory.
Say: "Ground every claim in the source files and quote them."

**Verification**: proving the work, not describing it.
Say: "Verify it live and show me the evidence."

---

# 4. Working with models

**LLM (large language model)**: the text engine: Claude, GPT, DeepSeek, Gemini, MiniMax, and open models.
Say: "Use the cheap fast model for this."

**Model size**: small and fast versus large and careful, usually a price trade.
Say: "This is mechanical. Use the small model."

**Open weights**: the model can be downloaded and run on your own machines.
Say: "Is there an open version we can run locally?"

**Local model**: runs on your laptop or desktop with no cloud. Private, slower, needs hardware.
Say: "Run it on the local model so nothing leaves the machine."

**Quantisation (GGUF)**: shrinking a model to fit smaller machines with a small quality cost.
Say: "Use the 4-bit quantised version."

**Temperature**: the style dial: low is careful and repeatable, high is creative and erratic.
Say: "Low temperature. This needs to be accurate, not interesting."

**Reasoning effort**: how long the model thinks before answering.
Say: "Think hard about this one."

**Fine-tuning**: training a model further on your own examples.
Say: "Do we need fine-tuning, or is a good prompt enough?"

**RAG (retrieval)**: looking things up and putting the right pages in front of the model before it answers.
Say: "Look it up first. Don't answer from memory."

**Embeddings / vector database**: turning text into numbers so a search can find meaning, not just matching words.
Say: "Index the documents so it can search by meaning."

**MCP (Model Context Protocol)**: a standard way to plug tools and data into an agent. The "USB port" for AI.
Say: "Is there an MCP server for it, rather than a custom script?"

**MCP server**: the program on the other end of that connection.
Say: "Connect the MCP server and list its tools."

**Tool schema**: the description the agent reads to know how to call a tool.
Say: "Check the tool's schema before calling it."

**Multimodal**: a model that can read images and audio, not just text.
Say: "Look at the screenshot and tell me what is wrong."

**Vision check / QC**: the agent looks at what it built and judges it like a person would.
Say: "Render it and look at it. Do not trust the code."

**Render gate**: an automated check at real screen sizes before shipping.
Say: "Run the render gate at 1440 and 390 and report overflow and JS errors."

**Playwright / headless browser**: a browser the agent can drive invisibly to test pages.
Say: "Screenshot it with Playwright at phone size."

**Console errors**: the browser's complaint line. The first thing to check when a page misbehaves.
Say: "Any console errors?"

---

# 5. Images, audio, video

**Prompt (image)**: the description you give the image model. Subject, setting, light, style, framing.
Say: "Generate it with a prompt that names the lens and the light."

**Aspect ratio**: the shape: 16:9 landscape, 9:16 vertical, 1:1 square.
Say: "16:9, landscape, for YouTube."

**Resolution**: pixel dimensions: 1920×1080 means full HD landscape.
Say: "1080p, 1920×1080."

**Upscale**: enlarging an image with a model that invents plausible detail.
Say: "Upscale to 4K."

**Background removal**: cutting the subject out cleanly.
Say: "Remove the background and give me a transparent PNG."

**Character sheet / consistency**: a fixed reference image of a person so every shot matches.
Say: "Keep the same face and wardrobe across every shot."

**B-roll / inserts**: the cutaway shots: hands, ingredients, steam, tools.
Say: "Give me six inserts to cut between."

**Shot list / storyboard**: the planned sequence of shots, one line each.
Say: "Write the shot list with durations before generating anything."

**Ken Burns**: slow push or drift on a still image to imply motion.
Say: "Slow push-in on each still."

**Codec**: the compression format: H.264 for video, AAC for audio, MP3 or WAV for sound.
Say: "H.264 MP4 with AAC audio."

**Bitrate**: how much data per second. Higher is cleaner and heavier.
Say: "Keep it under 5MB at decent quality."

**Frame rate (fps)**: frames per second. 25 or 30 for normal video.
Say: "25 frames per second."

**Faststart**: a video flag that lets playback begin before the full download.
Say: "Re-encode with faststart so it plays instantly."

**Transcode**: converting one format to another.
Say: "Transcode it to 720p for messaging."

**LUFS**: the loudness standard. −16 LUFS is a sensible target for speech on the web.
Say: "Normalise the audio to −16 LUFS."

**Clipping (audio)**: the waveform hitting the ceiling and distorting. Peaks at 0 dB mean trouble.
Say: "It sounds crunchy. Check for clipping and limit the peaks."

**TTS (text to speech)**: a model reading text aloud.
Say: "Read it aloud in her voice."

**STT / transcription**: turning speech into text.
Say: "Transcribe the recording and timestamp it."

**Voice cloning**: building a synthetic copy of a person's voice from a sample. Consent first, always.
Say: "Clone it only with recorded consent, and say on every file that it is synthetic."

**Lipsync**: making a face match recorded speech.
Say: "Lipsync the portrait to the audio."

**Captions / subtitles / SRT**: the text track of what is being said.
Say: "Give me an SRT for the captions."

**Thumbnail**: the still that sells the video in a list.
Say: "A 1280×720 thumbnail with three words maximum."

---

# 6. Getting a good result

**Goal**: what done looks like, in one sentence.
Say: "Done means: the page loads at 390px with no sideways scroll."

**Constraint**: the fence: brand colours, no new dependencies, British English.
Say: "Constraint: stay inside this palette and don't add libraries."

**Acceptance test**: the check that decides success.
Say: "Check the live URL, count the links, and paste the evidence."

**Scope**: what is in and out. Scope creep is how small jobs become weeks.
Say: "Just this page. Nothing else."

**Draft vs publish**: reviewable work versus live work.
Say: "Draft it in a file first. I'll say when it goes live."

**Rollback**: the way back if it goes wrong.
Say: "How do I undo this in one step?"

**Handoff**: a written summary so the next session can continue.
Say: "Write a handoff before you stop."

**Receipts**: the evidence: commit hash, live URL, screenshot, file path.
Say: "Give me the receipts: hash, URL, screenshot."

---

# 7. Words that cause trouble (and the fix)

- "Make it pop" → say what: bigger headline, more contrast, more space.
- "Modern" → say which: sharp corners, generous spacing, one accent colour.
- "Clean it up" → say which mess: alignment, wording, spacing, dead links.
- "Faster" → say where: image size, scripts, fonts.
- "Mobile friendly" → say the width and the test: 390px, no sideways scroll, tap targets 44px.
- "Fix the bug" → say the symptom: what you did, what you saw, what you expected.
- "Use AI" → say which job: draft, check, summarise, generate, decide.

---

# 8. If you learn only twenty words

hero, header, footer, CTA, card, palette, hex colour, font, padding, responsive, breakpoint, overflow, repo, commit, push, deploy, cache, API key, token, prompt.

Those twenty will get you through nine jobs out of ten. The rest you can look up here while the agent waits.
