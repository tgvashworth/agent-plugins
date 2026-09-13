# Verification and code pointers

Every quiz topic needs two things: a pointer the user can inspect before
answering and evidence that resolves the topic afterward. They may be the same
source.

## Point to the code

Prefer the most stable link available:

1. For a PR or pushed commit, use a permanent repository link pinned to the
   exact commit and line range.
2. For local or unpushed work, use a Markdown link whose label is the filename
   and whose target is the absolute path with a line suffix, for example
   `handler.ts` pointing to `/absolute/path/to/handler.ts:42`.
3. If a question spans several lines, point at the first line that contains the
   decision and describe the expression or block in words. Do not paste enough
   surrounding code to disclose the answer.

Usually put the pointer after the question. If the question explicitly tests
recall, say "without looking" and withhold the link until resolving the topic.
Use recall questions sparingly; this skill normally tests understanding with
the source open.

## Prove the conclusion

Use the strongest direct evidence available:

1. The implementation and the caller or consumer that gives it meaning.
2. A focused test that distinguishes the relevant behaviours.
3. A checked-in specification, ADR, schema, configuration file, or codebase
   instruction that defines the rule.
4. A PR discussion or issue that records the decision.
5. A local command or one-line repro whose output demonstrates the behaviour.
6. A local dashboard or external documentation when the behaviour depends on
   a live system or third-party contract.

For a repository convention, find the closest applicable instruction or design
source rather than citing a general project document. Confirm its scope from
the directory hierarchy, referenced component, or current configuration.

When a misunderstanding has a numerical consequence, calculate or reproduce
it only from current inputs. Label estimates as estimates; do not invent scale,
traffic, retry, latency, or cost figures merely to make the question feel more
important.

Do not cite a test merely because it touches the changed code; check that its
assertion proves the conclusion. Do not treat comments, PR prose, or old
learning-ledger entries as stronger than executable code or current specs.

When evidence conflicts, call out the conflict and stop treating the question
as having a definitive answer. Turn it into a finding for the closing summary
instead of grading the user's answer.

For inline behaviour choices, trace each choice through the exact path being
asked about. An incorrect choice must be false there, not merely less likely or
true only under an unstated assumption.

## Resolve without lecturing

A resolution should normally be one or two sentences plus evidence:

```text
Yes. The retry is limited to idempotent requests because the caller supplies
the retry policy in the linked client.ts line, and the focused case is asserted
in the linked client.test.ts line.
```

For a prompted or unresolved answer, add only the missing causal link before
moving on. Keep broader context for the final summary.
