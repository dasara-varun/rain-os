# Rain OS Workflow Governance

## Canonical project loop

Rain OS uses a bounded phase loop:

1. **Discuss:** define the user problem and non-goals.
2. **Plan:** research upstream, write acceptance tests, and identify reuse.
3. **Execute:** make the smallest change in an isolated branch or worktree.
4. **Verify:** run VM, package, accessibility, security, and recovery tests.
5. **Ship:** publish artifacts, known issues, and rollback instructions.
6. **Learn:** record the decision and update the guide.

This combines the useful phase discipline of GSD Core, the evidence and security emphasis of ECC, the cross-functional reviews of gstack, and the minimality principle of ponytail.

## Ralph-style bounded loop

A Ralph loop may repeat only a narrowly defined task. Each cycle reads the current issue, makes one change, runs tests, records evidence, and stops when the acceptance criterion passes or the limit is reached.

```text
MAX_ITERATIONS=5
while iteration < MAX_ITERATIONS:
    inspect current state
    implement smallest safe change
    run targeted tests
    record result
    if acceptance passes: stop successfully
    if same failure repeats twice: stop for human diagnosis
    iteration += 1
stop with a report; never loop indefinitely
```

Ralph is not permitted for releases, signing-key changes, destructive storage operations, broad repository rewrites, or external publishing without a human gate.

## Skill discovery

Use skill discovery only after defining the task. Search for a skill, inspect its source and license, run it in a scratch branch, and record whether it is retained. Do not install a skill because its name sounds relevant. A skill may contain hooks, shell commands, MCP definitions, or broad permissions.

## Memory and context

Use a project memory bank with versioned decisions, current state, accepted constraints, and open risks. Context compression is optional and local. Important facts must remain in repository documents and tests, not only in agent memory.

## Definition of done

No task is complete because an agent says it is complete. It is complete when the acceptance tests pass, the changed files are reviewed, the rollback is documented, the guide is updated, and the iteration record contains evidence.
