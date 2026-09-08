---
name: slack
description: >
  Write a Slack message from the current context, in the formatting dialect
  that will actually render for how it is delivered: returned as bare text to
  copy into the composer (default), saved as a Slack draft, or sent. Use when
  the user invokes /slack, or asks for something they can paste into Slack, a
  Slack draft, or a Slack message to a person or channel.
argument-hint: "[draft|send] [to <person or #channel>] [what to say]"
---

# Slack

Turn the current context into a Slack message. Slack has two formatting dialects and the message must be written in the one
that matches the delivery path. Read the rules before writing a word:

`references/slack-formatting.md` (relative to this file)

### Step 1: pick the delivery mode

| Mode | When | Dialect |
|------|------|---------|
| **copy** (default) | No mode word, or the user says "copy", "paste", "give me" | Paste dialect |
| **draft** | The user says "draft", and names a person or channel, and the Slack tool is available | Tool dialect |
| **send** | The user says "send" (or an unambiguous equivalent), and names a person or channel | Tool dialect |

Defaults are conservative. If in doubt between copy and draft, copy. If in
doubt between draft and send, draft. Never send a message the user has not
asked to send in this invocation; earlier permission does not carry over.

If draft or send is requested but the Slack tool is not available, or the
recipient cannot be resolved (`slack_search_users`, `slack_search_channels`),
fall back to copy and say why.

### Step 2: decide what the message says

Work out from the conversation:

- **What happened** that the recipient needs to know. Usually the outcome of
  the last piece of work: a PR, a finding, a decision, a blocker.
- **Who is reading it** and what they already know. A teammate in the thread
  needs less than a manager catching up.
- **The ask**, if any. One ask, stated plainly.

Then apply the content rules in the reference: lead with the point, short
lines, the user's voice, no AI tells, searchable names over descriptions.

If the request includes a brief ("tell Pete the migration is done"), that is
the content. If it does not, the content is a summary of the session's most
recent completed work, and the recipient is whoever the context points at.

Length: a Slack message is read on a phone. Aim for under 120 words. Use
bullets only for genuinely parallel items; three or more, never one.

### Step 3: write it in the right dialect

**Paste dialect (copy mode)** — the message must look right in two states:
after the user clicks Slack's "Apply formatting?" toast, and raw if they do
not. So:

- Only these markers: `*bold*`, `_italic_`, `~strike~`, `` `code` ``,
  `> quote`, and fenced code blocks with the fences on their own lines.
- `•` (the character, not a dash) for bullets. `1.` for numbered items.
- Bare URLs, at the end of a line or alone on one. No `[text](https://…)`, no
  `<url|text>`.
- No `**double**`, no `#` headings, no tables, no `---`, no nesting.
- Names as plain text; no `<@U…>` mentions.

**Tool dialect (draft and send modes)** — standard Markdown:

- `**bold**` for emphasis. Never single asterisks; they become italic.
- `[text](https://…)` links, `- ` bullets, `1.` numbers, `> ` quotes, fenced
  blocks with a language tag if useful.
- A `**bold**` line where you would want a heading. Headings lose emphasis.
- A blank line after every list, or the next paragraph glues onto it.
- Mentions as `<@U…>` with a real ID from `slack_search_users`.

### Step 4: deliver

**copy:** Your entire reply is the message and nothing else. No code
block, no preamble, no "here's your message", no note after it, no offer to
adjust. The user runs `/copy` on the reply and pastes the result straight into
Slack, so any extra character you add is a character they have to delete. The
terminal will render `*bold*` as italic and `> quote` as a blockquote; ignore
that, the raw text is what gets copied. Do not add notes about the message
(which name to @-mention, that Apply formatting exists); the user knows. If a
fact could not be verified, leave it out of the message rather than caveat it.

**draft:** Resolve the recipient to an ID (a user ID doubles as the DM
channel ID). Call `slack_send_message_draft`. Tell the user it is in their
Slack drafts for that conversation and give the link the tool returns. If the
tool returns `draft_already_exists`, say so and fall back to copy.

**send:** Show the message first, then call `slack_send_message`. Return the
message link. Do not read it back through the API to check formatting; the
read-back is lossy. If the user wants to check rendering, the link is the
check.

### Cold read

Before delivering, read the message once as the recipient, on a phone, with
no context from this session. Anything that makes them stop and decode gets
rewritten. Check the dialect one last time: no single asterisks in tool mode,
no double asterisks in copy mode.
