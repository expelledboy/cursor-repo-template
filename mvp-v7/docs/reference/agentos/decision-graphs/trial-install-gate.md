# Decision Graph: trial-install-gate (agentos.decision-graph/v1)

Status: Draft
Date: 2026-01-15
Purpose: Enforce reactive governance: Trial-by-default, Install-by-approval.

```yaml
spec_version: agentos.decision-graph/v1
name: trial-install-gate
description: choose trial vs ask_user vs installed
expression_language: string

nodes:
  - id: start
    type: decision
    question: "Is this a persistent install request?"
    when: "context.intent.install == true"
    then: install_gate
    else: trial_gate

  - id: trial_gate
    type: decision
    question: "Is this low-risk and reversible?"
    when: "context.risk.level <= 2"
    then: done_trial
    else: ask_user

  - id: install_gate
    type: decision
    question: "Install requires explicit user approval"
    when: "context.user.approval.install == true"
    then: done_installed
    else: ask_user

  - id: ask_user
    type: ask
    ask:
      prompt: "I can proceed as a session-local trial, or install persistently with your approval."
      questions:
        - id: q_install
          text: "Install this change persistently, or trial-only for this session?"
          options: ["install", "trial-only"]
          default: "trial-only"
          branch_default: new_branch

  - id: done_trial
    type: terminal
    output: { mode: trial }

  - id: done_installed
    type: terminal
    output: { mode: installed }
```

