# Deslop style rules

The reader is mid-task and will read the words exactly once. Every string must
hand over its meaning in one pass: the real noun, the plain verb, the concrete
fact. Anything that makes the reader decode — cleverness, metaphor,
personification, compression, drama, filler — taxes them to make the writing
look good. Spend nothing of the reader's attention on the writing itself.

A wordy-but-plain sentence beats a short-but-clever one.

These rules draw on the ASD-STE100 Simplified Technical English standard
(controlled vocabulary, simple grammar, hard length limits) and on
plain-English microcopy practice. They are generic: apply them everywhere
unless the target's own conventions (a repo's commit style, a house glossary,
a product's established voice) say otherwise.

## Sentences and grammar

- **One idea per sentence.** Instructions: one instruction per sentence,
  unless two actions are simultaneous.
- **Length caps.** Instructions ≤ 20 words. Descriptions ≤ 25 words. Split
  anything longer. Paragraphs ≤ 6 sentences, one topic each, topic sentence
  first.
- **Active voice.** "The job retries three times", not "Three retries are
  attempted by the job".
- **Simple tenses only.** Present, past, future, imperative. Avoid stacked
  auxiliaries ("must have been", "would have been able to") and `-ing` verb
  forms where a simple form works ("Save the file", not "Saving the file is
  required").
- **Command verb first** for instructions: "Upload a file first." Put any
  warning or precondition *before* the action it governs.
- **Full sentences, full stops.** No fragments joined with dashes. "Optional.
  You can rename it later." — not "Optional — you can rename it later."
- **Avoid em-dashes.** Use a full stop, a colon, or a comma. A colon
  introduces a cause or a list: "Could not save: the connection timed out."
- **Do not drop words to save space.** Keep articles and connectives. "How
  many items expected." makes the reader decode; "How many items to ask
  for." does not. Never use a slash to compress ("and/or", "click/tap").
- **Noun clusters ≤ 3 words.** "The eviction policy for the session cache",
  not "session cache eviction policy configuration".
- **Vertical lists** for sequences and sets of more than about three items.
  Prose lists hide steps.

## Words

- **Short, common words.** use, not utilise; about, not approximately; help,
  not assist; start, not commence; enough, not sufficient; to, not in order to.
- **One word, one meaning.** Use the same term for the same thing everywhere
  in the target, and never the same term for two things. Never invent a noun;
  if the domain has a name for it, use that name.
- **Name the specific noun** when it is known. "That file type is not
  supported", not "That item is not available". Generic words ("thing",
  "item") only when the type genuinely varies.
- **Un-nominalise.** "decide", not "make a decision"; "implementing", not "the
  implementation of".
- **Address the reader as "you".** Contractions are fine for positives
  ("you'll", "it's"). **Always spell out negatives** — "do not", "cannot",
  "will not" — a missed negative changes the meaning.
- **British spelling** (colour, organise, behaviour) unless the target's
  conventions or an API name say otherwise.
- **No "please", no emoji, no exclamation marks.** Anywhere. Instructions are
  imperative: "Wait while we import your data."
- **Full stop on every message**, help text, and confirmation.

## Anti-patterns

The failure modes of "clever" writing. Each earns a rewrite.

**Mannered prose.** Metaphor and flourish in place of direct statement. The
mannered writer produces "a dial worth turning" instead of "a parameter worth
varying", and "this point earns its keep" instead of "this point still
matters". The phrases exist to display the writer, not to convey the idea, and
readers can tell. That is why mannered prose irritates: it makes the reader
work harder so the writer can perform. It is also imprecise. A metaphor drags
in connotations the writer did not choose and cannot control. The fix is to
say what you mean. When a literal phrase is available, use it.

| Wrong | Right |
| --- | --- |
| A dial worth turning. | A parameter worth varying. |
| This point earns its keep. | This point still matters. |
| The cache is the beating heart of the service. | Every request reads from the cache. |
| We are flying blind on retries. | We do not log retries. |

**Personification.** The app, a setting, a number, a list, or code never asks,
knows, refuses, wants, or decides. Say what happens or what the reader can do.

| Wrong | Right |
| --- | --- |
| The importer refuses files over 10 MB. | The importer cannot open files over 10 MB. |
| The schedule knows no other frequency. | Frequency is daily or weekly. |
| This folder holds your drafts. | This folder contains your drafts. |

**Saying what isn't.** Negation riddles and drama in place of the plain fact.

| Wrong | Right |
| --- | --- |
| There is no way back from here. | You cannot undo this. |
| Not everything here is what it seems. | (state the actual fact) |

**Quaint vocabulary.** Archaic, literary, or twee word choices.

| Wrong | Right |
| --- | --- |
| Nobody by that name. | No users match that name. |
| {name} had already gone. | {name} was already removed. |
| Nought | 0 |

**Over-compression.** Dropped words that force decoding. The test is one-pass
comprehension, not length. When in doubt, put the words back.

**Marketing-speak and AI tells.** The thing is described, never sold. Ban:
"successfully", trailing "!", "Get started", "Ready to…", "powerful",
"seamless", "robust", "leverage", "unlock", "delve", "elevate", "streamline",
"landscape", "Oops", "We are sorry", "Something went wrong". Ban the shapes
too: false antithesis ("It's not X, it's Y"), staccato triads ("Clear.
Simple. Done."), rule-of-three adjective padding, hedging openers ("It's
worth noting that", "Importantly", "At its core"), empty transitions
("Furthermore", "Moreover", "That said").

**Hedged obligation.** Be precise: `must` for hard requirements with
consequences; `need to` for steps that merely block progress. Never "should
probably", "might want to", "it may be worth".

## Rules by target

### User-facing copy and microcopy

Buttons, labels, headings, tooltips, empty states, help text, validation
errors, success and error messages, emails, notifications, admin screens.

- **Buttons: verb + object, always.** "Save project", "Add member", "Delete
  workspace". Predictable and scannable; never a bare "Save" or "OK".
- **Sentence case; lowercase domain nouns.** Capitalise only true proper nouns.
- **Success messages: noun + past participle.** "Project saved." "Member
  removed." Never "successfully", never "has been Xed", never "Your changes
  have been saved!".
- **Refusals: state the permission plainly.** "You do not have permission to
  delete this project." Add who can only when the reader can act on it
  ("Ask a workspace admin."). Never bare jargon ("Invalid flow parameters.")
  and never apology.
- **Errors: fact, cause, action.** What failed, why if known, what to do.
  "Could not save: the connection timed out. Try again." Drop the cause if
  you do not know it; never replace it with "Something went wrong".
- **Validation: tell the reader what to do.** "Enter an email address."
  Not "Email address is required" and never "This field is required".
- **Empty states: what is absent, then the action.** "This workspace has no
  members. Add one." Plain declarative, then imperative.
- **Help text: full sentences, fact first.** "Optional. You can rename it
  later." Two short sentences beat one fragment.
- Do not rewrite deliberate marketing or brand voice to these rules, and do
  not imitate it in product copy.

Calibration — strings that pass:

- "Project saved."
- "You cannot undo this."
- "You do not have permission to delete this project."
- "Could not save: the connection timed out. Try again."
- "This workspace has no members. Add one."
- "Optional. You can rename it later."
- "Enter an email address."

### Code comments

A comment is read by someone who has the code in front of them and nothing
else. It earns its place only by saying what the code cannot.

- **Say why, not what.** Delete a comment that restates the line below it.
- **No PR numbers, ticket IDs, names, or project names.** A future reader has
  none of that context and the pointer rots. State the constraint itself, not
  where it was decided.
- **No project-state markers.** Nothing that reads as "currently", "for now",
  "not yet", "will be added later", "TODO: remove after migration". Describe
  the code as if it has always been this way. If work is genuinely
  outstanding, that belongs in a ticket, not a comment.
- **No agent working memory.** Narration of the change being made ("Added
  null check here"), notes to a reviewer, reasoning about why an edit is
  correct, or a summary of what was tried. Remove it.
- **Doc comments describe the contract**: what it does, what it takes, what it
  returns, what it throws. Not how it is implemented.
- Match the file's existing comment style (sentence case, full stops, comment
  marker) rather than imposing a new one.

### Commit messages

Follow the repo's own conventions first. Where the repo has none, use the
format in [the packaged commit guidance](../../../templates/common.md): a short imperative subject saying what
changed, then optional bullets with the detail, then optional next steps.

- Subject ≤ ~65 characters, imperative, no trailing full stop, no type prefix
  unless the repo uses one.
- Body explains why, not how — the diff shows how.
- No attribution footers, no conversation history ("as discussed", "per
  review"), no ticket-only subjects ("Fix ABC-123").
- Repo-relative paths only.

### PR titles and bodies

Follow [the packaged PR guidance](../../../templates/pr-body.md): two-pass drafting (capture the change,
then rewrite for a stranger), summary bullets, test plan, issue links. The
body must stand alone for a reader with no context: state the problem, then
the change. Strip iteration history and review back-and-forth.

### Ticket titles and bodies

- **Title** names the problem or outcome in plain words, and is unique in a
  list. "Export ignores archived accounts", not "Export bug" or "Investigate
  export issue".
- **Body** answers three things, in order: what is wrong or wanted, what
  "done" looks like, and any context a stranger needs (where it happens, who
  it affects, links to evidence). Short paragraphs or a list.
- No pasted chat transcripts, no "we should probably", no speculation about
  the fix unless it is the point of the ticket. If the fix is known, say it
  plainly as the acceptance criterion.

## Cold read

Before finishing, read every changed string as a stranger who will read it
exactly once. If any phrase draws attention to itself — a smile, a nice turn,
a pause to decode — rewrite it until there is nothing to notice.
