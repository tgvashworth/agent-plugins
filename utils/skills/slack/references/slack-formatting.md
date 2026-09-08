# Slack formatting: what actually survives

Every rule here was checked by sending real messages to a Slack DM and looking
at the rendered result (screenshots, not the API read-back — the read-back
drops tables, code-block languages and rich-text styling, so it lies). Rules
marked *(not verified)* are inferences; treat them as cautious defaults.

There is no single "Slack markdown". There are two dialects, and the message
must be written in the one that matches how it will reach Slack.

| Path | Dialect | Who parses the markers |
|------|---------|------------------------|
| User pastes text into the Slack composer | **Paste dialect** (Slack mrkdwn subset) | Slack's composer, and only if the user clicks *Apply* on the "Apply formatting?" toast |
| Sent or drafted through the Slack MCP tool | **Tool dialect** (standard Markdown) | The tool converts Markdown to Slack blocks before Slack sees it |

Mixing them is the classic failure: `*bold*` sent through the tool comes out
*italic*; `**bold**` pasted into the composer comes out as literal asterisks
around bold text.

## Paste dialect (copy and paste into the composer)

This is the main case. The user copies text from the terminal and pastes it
into Slack's WYSIWYG composer.

### What the composer does with a paste

- Every marker is inserted **literally**. Nothing is formatted on paste.
- A toast appears: *"Apply formatting? Apply · Don't ask again"*. If the user
  clicks **Apply**, a small set of markers is converted (below). If they just
  press Enter, the message is sent exactly as pasted, asterisks and all.
- So the message must read well **both** ways: formatted after Apply, and as
  raw text without it. Use few markers, and only ones that look acceptable
  when left literal.
- Bare URLs are auto-linked on paste. The **first** URL gets an unfurl card
  under the message (a big preview for web pages; a compact card for
  installed apps like Linear or GitHub).
- `:shortcode:` emoji convert to emoji on paste. Unicode emoji pass through.
- Blank lines and single newlines are preserved exactly.

### Markers that work after Apply (and look fine when literal)

| Write | After Apply | Left literal |
|-------|-------------|--------------|
| `*bold*` | **bold** | `*bold*` — readable |
| `_italic_` | *italic* | `_italic_` — readable |
| `~strike~` | ~~strike~~ | `~strike~` — readable |
| `` `code` `` | `code` | `` `code` `` — readable |
| `> quote` at line start | blockquote bar | `> quote` — readable |
| ```` ``` ```` on its own line, above and below | code block | fence lines visible — acceptable |

That is the whole list. Everything else is either ignored or made worse.

### Markers that break

| Write | What happens |
|-------|--------------|
| `**bold**` | Bold **with literal asterisks** either side. Never use. |
| `__text__` | Italic with literal underscores. Never use. |
| `~~text~~` | Literal tildes, no strike. |
| `# Heading` | Literal `#`. No headings exist in Slack messages. |
| `[text](https://…)` | Literal brackets and parens, URL linked inside them. |
| `<url\|text>` | Literal angle brackets; the `\|text` is swallowed into the URL. This is API syntax only. |
| `<@U123>` / `<#C123>` | Literal. Mentions cannot be pasted *(mention resolution not verified; assume it fails)*. |
| `- item` | Literal dash. Not turned into a list. |
| Tables, `---` | Literal pipes and dashes. |
| Nested bullets | No nesting. Flatten. |

### Structure that works

- **Bullets:** the bullet character `•` (U+2022) followed by a space, at the
  start of the line. It is plain text, so it survives every path identically.
- **Numbered lists:** `1.`, `2.` as plain text. Stays literal, reads fine.
- **Section labels:** a short `*Bold label*` line, then the content directly
  under it. This replaces headings.
- **Title line:** optional leading emoji, then `*Title*`. Reads fine literally.
- **Links:** bare URL, at the end of the line or on its own line. One or two
  per message; the first one grows a preview card. Put the most important
  link first. Never wrap a URL in brackets or angle brackets.
- **Mentions:** write the name as plain text (`Pete`). Tell the user to swap in
  the real @-mention in the composer if they want a ping.
- **Spacing:** one blank line between sections. No blank line between a label
  and its list.
- **Code:** backticks for identifiers; a fenced block for anything multi-line.
  Fences on their own lines. No language tag (it becomes literal text).

### Worked example

Renders cleanly after Apply, and reads fine raw:

```
:rocket: *Alert routing rollout: week 2*

Shipped the new routing UI to 20% of customers on Tuesday. Zero escalations, two minor bugs, both fixed.

*Next*
• Bump to 50% on Thursday if error rates stay flat
• Rewrite the empty-state copy, it reads stiff

*Need from you*
1. Sign-off on the 50% bump: https://linear.app/incident-io/issue/ENG-1234
2. Ten minutes on the `routing_v2` flag, it can't be toggled per-org yet

> Blocker: percentage rollouts only until ENG-1240 lands.

Shout if anything is unclear :pray:
```

### If the user has turned the toast off

If they clicked "Don't ask again", or prefer the raw look, they can enable
*Preferences → Advanced → Format messages with markup* to get a composer that
parses the same markers on send *(not verified in this workspace)*. The paste
dialect above is still the right one to write in.

## Tool dialect (Slack MCP `slack_send_message` / `slack_send_message_draft`)

The tool takes **standard Markdown** and converts it to Slack rich-text blocks.

| Write | Renders as |
|-------|------------|
| `**bold**` | bold |
| `_italic_` or `*italic*` | italic — **so single asterisks are italic here, never bold** |
| `~~strike~~` | strikethrough |
| `` `code` `` | inline code |
| `[text](https://…)` | link with text |
| bare URL | link |
| `<https://url\|text>` | link with text (passes through) |
| `<@U123>` | working mention (with a real user ID) |
| `- item` or `• item` | bullet list (real list block) |
| `  - nested` | nested bullet |
| `1. item` | numbered list |
| `> quote` | blockquote |
| ```` ```lang ```` | code block with syntax highlighting |
| Markdown table | real table |
| `:tada:` or unicode emoji | emoji |
| `\*` | literal asterisk |

### What the tool loses

- `# Headings` become plain lines with no emphasis. Use a `**bold**` line.
- `---` is dropped.
- Blank lines around lists collapse. A non-blank line **directly after** a list
  item is glued onto the list as a continuation. Always leave a blank line
  after a list.
- The tool appends a footer: *Sent using @Claude*. It cannot be removed.
- Read-back through `slack_read_channel` shows the stored text, not the
  rendered blocks: tables vanish, code-block languages vanish, `**` shows as
  `*`. Do not use it to judge formatting.

### Drafts

`slack_send_message_draft` puts the message in the user's Drafts for that
channel or DM, unsent. Only one attached draft is allowed per channel; a second
call fails with `draft_already_exists` until the user sends or deletes the
first. To DM someone, use their user ID as the channel ID.

## Content rules that apply to both dialects

- Lead with the point. First line says what happened or what you need.
- One ask per message where possible, stated as a sentence, near the top or
  in a clearly labelled section.
- Short lines. Slack wraps at a narrow width; a 40-word sentence is a wall.
- No AI tells: no "I hope this finds you well", no "Great question", no
  summary of what the message is about to say, no sign-off boilerplate.
- Write as the user, in their voice, to a colleague. Not as an assistant
  reporting to a manager.
- Names of things the reader can search for (ticket keys, flag names, PR
  numbers) beat descriptions of them.

## How to re-verify these rules

1. Send a test through the tool to the user's own DM (their user ID as
   `channel_id`) and screenshot the result in the Slack web client. The
   screenshot is the truth; the API read-back is lossy.
2. For the paste path, `pbcopy` from a sandboxed shell does not reach the
   system clipboard. Instead, open the DM in Chrome and dispatch a synthetic
   paste into the composer with the JavaScript tool:

   ```js
   const editor = document.querySelector('[data-qa="message_input"] .ql-editor');
   editor.focus();
   const dt = new DataTransfer();
   dt.setData('text/plain', text);
   editor.dispatchEvent(new ClipboardEvent('paste', {clipboardData: dt, bubbles: true, cancelable: true}));
   ```

   Slack's real paste handler runs, including the "Apply formatting?" toast.
   Screenshot before Apply, after Apply, and after sending.
