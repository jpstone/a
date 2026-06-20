# US-03: Choice, gate, and prompt semantics

Derived from: [3. Choice, Gate, and Prompt Semantics](../agentic-redesign-references.md#us-03-source)

## Problem

Human-facing governance prompts need consistent numbered semantics so only explicit numbered choices mutate decision state.

## User story

As a human reviewer, I want choice, gate, and prompt semantics implemented, so that human-facing governance prompts need consistent numbered semantics so only explicit numbered choices mutate decision state.

## In scope

- Require numbered choices for governed decisions.
- Define non-binary semantic choices with Something else and Discuss.
- Define binary gates as Yes/No/Discuss only.
- Define fixed binary decisions with two domain outcomes plus Discuss.
- Ensure prompt proposals and Discuss are non-mutating.

## Out of scope

- Free-form final governed decisions without numbered confirmation.
- Turning binary gates into custom semantic prompts.
- Recording Discuss as a HumanDecision.

## Acceptance criteria

- [ ] All governed choices shown to humans are numbered.
- [ ] Governed state mutates only from a numbered human selection.
- [ ] Non-binary semantic choices include relevant options, Something else, Discuss, and custom-prose confirmation.
- [ ] Binary gates always present Yes, No, Discuss and only Yes satisfies the gate.
- [ ] Fixed binary decisions present exactly two domain outcomes plus Discuss.
- [ ] Discuss creates no governed mutation and no HumanDecision.
