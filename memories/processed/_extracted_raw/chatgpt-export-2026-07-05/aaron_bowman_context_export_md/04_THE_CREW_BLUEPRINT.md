# The Crew Blueprint

## Purpose

The Crew Blueprint is a training platform for stagehands and live-event workers.

Core direction:

- entry-level stagehand education
- practical jobsite readiness
- production labor onboarding
- department-specific training over time
- supervisor/lead development
- legal/compliance education
- mental health/lifestyle awareness for live-event workers

## Course 1

Known title:

**Stagehand Fundamentals: How to Work Your First Load-In, Show Call, and Load-Out**

Core structure:

- initially 10 modules
- later references to an 83-lesson outline
- end-of-module quizzes
- quiz pass threshold: 80%
- retakes allowed

## Lesson Structure

Canonical lesson blocks:

- In This Lesson You Will Learn
- Short Answer
- What This Looks Like on a Call
- Beginner Mistakes
- Professional Habit
- Key Takeaway

Later additions:

- Safety Notes
- Reflection Questions
- Key Takeaways styled box

## Safety / Compliance Positioning

Important language rules:

- The course is orientation/job-readiness, not certification.
- Specialized work requires proper training and employer authorization.
- Safety disclaimer should appear on relevant pages.
- Avoid OSHA certification claims unless authorized.
- Do not issue unauthorized certificates.

## LMS / Technical History

Earlier WordPress/LMS context:

- thecrewblueprint.com via IONOS / WordPress Grow
- theme: Extendable
- plugins included Crew Blueprint Core, Site Shell, LMS, Resource Hub, Safety Notices
- LMS used shortcode and JSON-based workflows
- direct-fetch split JSON consumer was tested
- Module files included manifest, lessons, and quiz JSON

Split JSON model:

- `module-XX-manifest.json`
- `module-XX-lessons.json`
- `module-XX-quiz.json`

Important later decision:

- Aaron disabled the LMS completely on 2026-06-11.
- Reason: display/transfer pattern did not preserve written course packet flow.
- Direction shifted toward content creation workflow first.
- Robust LMS rebuild paused.
- Create/store course packets now; build simpler MVP display later.

## Content Creation Workflow

Original workflow:

1. Gemini asks for/reframes a topic.
2. ChatGPT / Course Studio creates core structure or lesson outline.
3. Claude creates Research Guide with core subjects and key topics.
4. ChatGPT Scholar researches key topics and compiles packets.
5. Claude drafts full lesson.
6. Manus proofreads and reviews scoring system.
7. Claude finalizes revisions and generates `.docx`.

Updated decision:

- Aaron approved the revised workflow previously provided by ChatGPT.
- Manus can be used temporarily until access ends.
- Alternatives such as DeepSearch/Qwen/Meta Llama were mentioned for later.

## Brand / Visual System

Approved direction:

- Dark industrial training-platform look.
- Near-black / charcoal backgrounds.
- Industrial yellow/gold and amber accents.
- White/off-white body text.
- Muted gray secondary text.
- Subtle borders and shadows.
- Condensed/industrial headings.
- Clean readable body.
- Mobile-first layout.

Known color references:

- Background: `#050708`
- Panel: `#0e1216`
- Card: `#151a20`
- Gold: `#f5b400`
- Amber: `#ffcf3a`
- Text: `#f4f6f8`
- Muted: `#b7bec6`

Avoid:

- generic school look
- white pages
- cluttered dashboard
- tiny mobile text
- neon
- gaming-site look
- rewriting lesson content without permission

## Pages / Legal Content

Additional pages requested:

- Accessibility
- Affiliate Disclosure
- Cookies Disclaimer
- Limitation of Liability
- Privacy policy / cookie compliance content
