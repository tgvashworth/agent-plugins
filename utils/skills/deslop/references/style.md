# Plain English writing rules

Write so the reader can understand the text on the first reading and continue their task. State the facts and make any required action clear. Include the words needed to explain the meaning, even if the sentence becomes longer.

Apply these rules to product copy, code comments, commit messages, pull requests, and tickets. Follow established terminology and conventions for the product or repository where they differ from this guide. Use British spelling unless an existing convention or technical identifier requires otherwise.

## Sentences and structure

- Give each sentence one main idea. Give each instruction one action, unless two actions must happen together.
- Keep instructions to 20 words or fewer and descriptions to 25 words or fewer. Split longer sentences without removing words needed for clarity.
- Keep each paragraph about one topic, with no more than six sentences. Start with the main point.
- Use active voice and simple verb forms where possible. Write "The job retries three times."
- Start instructions with the action verb. Put any condition or warning before the action it affects: "To continue, upload a file."
- Use complete sentences in prose. Short labels, headings, and status messages can use phrases where the meaning is clear.
- Use full stops, commas, and colons. Avoid em dashes and slashes used to combine words or alternatives.
- Keep articles and connecting words. Do not shorten a sentence into a phrase the reader must work out.
- Avoid groups of more than three nouns. Write "the eviction policy for the session cache" instead of "session cache eviction policy configuration".
- Use numbered lists for steps that follow an order. Use bullets for sets of four or more items, or when a list makes comparison easier.

## Words and tone

Use common words and direct verbs. Prefer "use", "about", "help", and "start" to "utilise", "approximately", "assist", and "commence". Write "decide" instead of "make a decision".

Name the specific object when it is known. Use "file", "project", or "member" instead of "item" when that is what you mean. Use the same term for the same thing throughout. Use established names for technical concepts.

Address the reader as "you". Contractions such as "you'll" and "it's" are fine. Spell out negatives: "do not", "cannot", and "will not".

State facts directly. Avoid metaphors, decorative language, dramatic phrasing, and unusual words chosen for effect. Describe software behaviour without giving software human thoughts or intentions. Write "The importer cannot open files over 10 MB."

Remove promotional claims and stock phrases. Avoid words such as "seamless", "powerful", and "unlock" when they add no concrete information. Remove openings such as "It is worth noting" and transitions such as "Furthermore" when the connection is already clear.

Do not use rhetorical contrasts such as "It is not X, it is Y" to introduce a straightforward fact. Avoid slogans made from short fragments or lists of adjectives. State the actual behaviour or result.

Use "must" for requirements with consequences and "need to" for steps required to continue. Do not weaken a required action with "should probably" or "might want to". State uncertainty when the facts are uncertain.

Do not use "please", emojis, or exclamation marks. Preserve deliberate brand language in marketing content. Apply this guide to product copy without copying the tone of nearby marketing.

## Product copy

Use sentence case. Capitalise proper nouns and technical identifiers as required. End messages, help text, and confirmations with full stops. Buttons, labels, and headings do not need full stops.

| Type               | Rule                                                                  | Example                                                                   |
| ------------------ | --------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Button             | Name the action and its object.                                       | Save project                                                              |
| Success message    | Name the object and the completed action. Omit "successfully".        | Project saved.                                                            |
| Permission error   | State the missing permission. Add a useful next step when one exists. | You do not have permission to delete this project. Ask a workspace admin. |
| Other error        | State what failed, the cause if known, and what to do next.           | Could not save: the connection timed out. Try again.                      |
| Validation message | Tell the reader what to enter or change.                              | Enter an email address.                                                   |
| Empty state        | State what is absent and give the next action.                        | This workspace has no members. Add a member.                              |
| Help text          | Put the relevant fact first.                                          | This name is optional. You can change it later.                           |
| Warning            | State the consequence before the action.                              | You cannot undo this.                                                     |

Use terms the reader understands. Omit an unknown cause rather than inventing one. Avoid apologies and vague errors such as "Something went wrong". Offer only actions that can help resolve the problem.

## Code comments

Explain constraints and reasons that are not clear from the code. Remove comments that merely restate the next line.

State the constraint itself. Leave out ticket numbers, attribution, conversation history, and notes to reviewers. Do not describe the edit you just made or record what you tried.

Describe the code's behaviour without phrases such as "for now" or "will be added later". Track outstanding work in tickets.

Use documentation comments to describe behaviour, inputs, outputs, and possible errors. Follow the file's existing comment format and punctuation.

## Commit messages

Follow the repository's conventions. Where none exist:

- Start the subject with an imperative verb that describes the change.
- Keep the subject to about 65 characters or fewer, with no trailing full stop or type prefix.
- Add a body when context is needed. Explain why the change is necessary.
- Leave out attribution footers and references to conversations or review discussions.
- Give the subject a useful description even when it includes a ticket number.
- Use paths relative to the repository.

## Pull requests

Write the title and description for a reviewer who has not seen the conversation. State the problem, explain the change, and describe the resulting behaviour.

Use short summary bullets when they help. Include a test plan or verification results, and link relevant issues. State any material limits to the checks performed.

Remove drafting history, review exchanges, and descriptions of abandoned attempts. After drafting, check that the description stands alone.

## Tickets

Give the title enough detail to identify the problem or desired outcome in a list. Write "Export ignores archived accounts" instead of "Export bug".

Describe the problem or request first. Then define the result needed to close the ticket. Add the context needed to understand or reproduce it, including affected users and links to evidence.

Leave out chat transcripts and vague suggestions. Include a proposed fix when it is known or when assessing it is the purpose of the ticket. If the fix is known, state the required result clearly.

## Final check

Read the text as someone who knows nothing about the drafting process. Check that each sentence is clear on the first reading. Confirm that the facts are accurate, the terms are consistent, and any required action is obvious.

Remove repetition and wording that adds no useful meaning. Restore any words needed for clarity.