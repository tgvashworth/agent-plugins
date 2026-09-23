# Follow-up work from review

Keep useful suggestions that sit just outside the PR's purpose from getting
lost or expanding the change indefinitely.

- **Fix here** when the issue is caused by this PR or blocks its correctness,
  security, or safe release. A ticket is not a substitute for a necessary fix.
- **File a ticket** for a worthwhile improvement that can safely ship
  separately. Check the project's tracker and existing tickets first. Capture
  the problem, why it matters, the proposed scope, acceptance criteria, and
  links to the PR and originating feedback. Reuse a matching ticket rather
  than duplicating it. Use existing authorisation to file it; if permission or
  the destination is missing, prepare the ticket and ask for what is needed.
- **Agree a fast follow** when the change should happen promptly but the
  current PR can safely merge first. A fast follow means: merge this PR, then
  implement the requested changes in a separate follow-up PR. Track it in a
  ticket with the agreed scope, acceptance criteria, and owner if known.
  Present it as a proposal until the user agrees; if a reviewer made it a
  merge condition, obtain their agreement to defer before treating it as
  non-blocking. Do not invent an owner, deadline, or commitment.

In a review reply, explain what stays in this PR, what moves to the ticket,
and why it can wait. Link the ticket and name any agreed fast follow. Leave
the deferred thread unresolved for the reviewer unless the user explicitly
directs otherwise. Include deferred work in the final handoff, and do not
start implementing it just because the ticket now exists.
