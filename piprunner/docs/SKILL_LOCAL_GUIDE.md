# Using your Piprunner + End-of-P2 skill locally

## Current setup: two independent skills (5 November 2026)

The original single skill below is retained as a compatibility router. Use these names for new chats:

- `$mta-end-of-p2` — standalone MTA-End-of-P2, without the Piprunner fractal signal gate.
- `$piprunner-mta-end-of-p2` — Piprunner + MTA-End-of-P2, adding confirmed 15m Williams Fractal continuation evidence while preserving the full baseline sequence and risk rules.

Installed folders are `C:\Users\rrapo\.agents\skills\mta-end-of-p2` and `C:\Users\rrapo\.agents\skills\piprunner-mta-end-of-p2`. Maintained copies are under this repository's `piprunner\skills\` directory. Each contains SKILL.md, its own portable references/contract.md and agents/openai.yaml. No dependency on the other skill is required.

Open this project in Codex, start a chat, and use for example:

> Use $mta-end-of-p2. Read the current product requirements and explain the baseline 4H → 1H → 15m workflow and next incomplete feature.

> Use $piprunner-mta-end-of-p2. Design the additional 15m Williams Fractal confirmation gate. Keep the End-of-P2 sequence intact and identify the unresolved timing and expiry choices before implementation.

Open `piprunner\workflows\mta-workflow-dashboard.html` in a browser. Choose either indicator and Horizontal, Vertical or Both. Select a step to inspect the required gate and chart evidence. This offline design preview has no market feed; actual TradingView panels and separate indicator entrypoints remain pending. Use Print / save PDF for a printable view.

For reinstall/update, the PowerShell instructions below apply with `piprunner-end-of-p2` replaced by the desired new skill folder. Copy the whole folder, refresh matching files, and restart Codex if discovery has not updated. Direct-path fallback: ask the AI to read `C:\Users\rrapo\.agents\skills\mta-end-of-p2\SKILL.md` or the combined equivalent. Maintain product rules in GitHub first and then refresh the installed copy.

## Historical single-skill instructions

Created 5 November 2026. Skill name: `piprunner-end-of-p2`.

## What it does

The skill tells an AI how to develop, review and explain your strategy consistently. It preserves 4H → 1H → 15m priority, your End-of-P2 entry/risk rules, configurable teaching annotations and the distinction between confirmed rules, proposed mechanics and unresolved decisions. It reads current repository documents rather than relying on an old chat.

It also records your correction: original Piprunner uses a 15m Williams Fractal continuation signal, and that signal is not implemented yet. Generic 15m swing/BOS/CHoCH annotations do not complete it. Creating this skill does not change the TradingView indicator or add the missing signal.

## Where the files live

Maintained repository copy:

`C:\Users\rrapo\Documents\ChatGPT\LearnToTrade\Indicators\Piprunner\piprunner\skills\piprunner-end-of-p2`

The folder contains SKILL.md (workflow), references/strategy-contract.md (portable rules and fractal requirements), and agents/openai.yaml (display information).

Local discovery copy for this machine:

`C:\Users\rrapo\.agents\skills\piprunner-end-of-p2`

Keep the complete folder together. The repository copy is the maintained original; the local copy needs refreshing when it changes. Installing a skill does not grant GitHub or TradingView access. The AI still needs the project files and any tools required by the task.

## Start a session

1. Open the Piprunner project folder in Codex: `C:\Users\rrapo\Documents\ChatGPT\LearnToTrade\Indicators\Piprunner`.
2. Start a new chat. Type `$piprunner-end-of-p2` and your task. If the app provides a skill picker, select Piprunner + End of P2.
3. Ask it to read current project context before changing code. Check that it identifies what is implemented and what is missing.
4. Give the particular feature, correction or chart question. You do not need to repeat the full strategy.

Codex supports explicit skill mentions and automatic matching by description. Official documentation says local skills are discovered from `.agents/skills` locations and changes are detected automatically; restart Codex if a new skill does not appear. Product interfaces differ: CLI/IDE support `$` mentions or `/skills`; ChatGPT uses an `@` picker. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills). If this desktop version does not surface the installed name, use the direct-path fallback below.

## Copyable prompts

Resume development:

> Use $piprunner-end-of-p2. Read the current repository context, decisions, roadmap and source. Explain the next incomplete feature and continue the agreed work without changing confirmed End-of-P2 rules.

Specify the missing fractal feature:

> Use $piprunner-end-of-p2. Design the missing 15m Williams Fractal continuation signal. Show confirmation timing and candidate annotations. Identify the decisions needed to use it as an optional hybrid gate. Preserve the End-of-P2 signal-candle entry and risk rules. Do not implement an entry replacement without resolving its role.

Teach from a chart (attach the screenshot):

> Use $piprunner-end-of-p2. Walk through this chart from 4H to 1H to 15m. Explain what is met, waiting, blocked or unimplemented. Distinguish open-candle moves from confirmed breaks and fractal candidates from qualified entries.

Review code:

> Use $piprunner-end-of-p2. Review the current Pine script for future-data use, timeframe confirmation, fractal availability timing and accidental changes to the End-of-P2 rules. Report evidence and unresolved definitions before editing.

Record a correction:

> Use $piprunner-end-of-p2. My rule correction is: [state the rule]. Update the decision log, context and affected skill reference. Identify which earlier decision it supersedes and whether code changes are needed.

## Refresh or install on another Windows machine

Obtain the repository and locate its `piprunner\skills\piprunner-end-of-p2` folder. In PowerShell, adjust the source path for that machine, then copy the complete folder:

```powershell
$strategySkillSource = 'C:\Users\rrapo\Documents\ChatGPT\LearnToTrade\Indicators\Piprunner\piprunner\skills\piprunner-end-of-p2'
$strategySkillsRoot = Join-Path $env:USERPROFILE '.agents\skills'
New-Item -ItemType Directory -Force -Path $strategySkillsRoot | Out-Null
Copy-Item -LiteralPath $strategySkillSource -Destination $strategySkillsRoot -Recurse -Force
```

This refreshes matching files; it does not remove obsolete files from earlier versions. Review any locally edited installed copy before overwriting it. This first version has no executable helpers or required credentials. On another OS, use that user's `.agents/skills` directory and copy the same folder. Other AI clients may require their own skill location; alternatively instruct them to read SKILL.md explicitly.

## If it is missing or behaves incorrectly

- Check that `.agents\skills\piprunner-end-of-p2\SKILL.md` exists, with no extra nested folder. Restart Codex if discovery has not refreshed.
- If there are duplicate entries, check for another copy with the same name in repository/user skill directories. Avoid maintaining conflicting copies.
- Direct-path fallback: “Read and apply `C:\Users\rrapo\.agents\skills\piprunner-end-of-p2\SKILL.md`, then review this project's next feature.” This works without claiming the skill picker has discovered it.
- If the AI cannot read the repository, open the correct project folder. A skill reference is not a copy of the live source or a substitute for repository access.
- If the AI says fractals are complete because 2/2 pivots exist, point it to the skill's critical status correction and ask for the actual continuation-signal code and tests.
- If TradingView shows only EMAs, verify the complete Pine source and its final marker. The previous loaded editor copy stopped at line128; full UI1.1.0 has 714 physical lines. Do not solve that by changing trading rules.

## Maintain it over time

Make rule changes in the repository first, recording confirmed versus proposed decisions. Update the skill only when its reusable instructions or portable contract change; use PROJECT_CONTEXT for routine progress. Refresh the installed copy afterward. A fresh session should read current context, so old chats are not required.

Successful skill validation checks its format and references. It does not validate profitability, Pine compilation, replay behavior or every future AI response. Ask for those checks separately when developing the relevant feature.
