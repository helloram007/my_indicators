# Project context and handover

Last updated: 29 October 2026.

## User goal

Build a TradingView hybrid trading indicator/strategy feature by feature. End-of-P2 governs the multi-timeframe process; selected Piprunner components are optional A/B experiments. The user wants chart annotations that explain every required checklist item and train visual recognition, with controls to reduce or disable annotations later.

## Confirmed scope

- Platform: TradingView, explicitly confirmed by the user on 29 October 2026.
- Repository: `https://github.com/helloram007/my_indicators`; project directory: `piprunner/`.
- Architecture: 4H bias, 1H setup, 15m structure and entry.
- HTF always has priority: 4H authorizes direction, 1H qualifies setup, 15m confirms execution. Lower-timeframe signals cannot override confirmed 4H direction. Neutral/unknown 4H blocks new directional qualification. Zone-own-timeframe invalidation remains independent (D-018/D-019); post-fill bias-change management is not defined by this priority rule.
- Preserve 15m CHoCH → separate swing break → retest → signal candle → entry one tick beyond the signal candle.
- Preserve three-bar expiry, stop beyond retest extreme, minimum 2R opportunity, 50% TP1 and runner. Exact unresolved interpretations remain OPEN.
- EMA36/100 and Williams Fractals are optional; hiding annotations never changes decisions.
- Start with 4H Bias in depth, with non-repainting structural rules and tests.
- Store durable context in GitHub so future assistants can continue without asking for the entire conversation again.

## Current implementation status

Latest delivery **UI 1.0.3** (30 October 2026): user sees blank charts and Style only contains Source diagnostic close. Full local .pine/.txt/Git copies contain 21 plots and object outputs, so incomplete pasted source or stale chart instance is strongly suspected, NOT verified. Moved diagnostic output from header to end so a header-only excerpt cannot masquerade as the full indicator. No structure/zone/SPA calculation changes. Read COMPILE_CHECKS. Next critical step is full-source replacement in a new Pine Editor indicator and checking final marker/current title; if unresolved obtain complete editor source/errors, not more visibility toggling. Exact-revision platform checks remain pending.

Latest source is **UI 1.0.2** (30 October 2026). User requested `Inputs in status line` off by default. Every input explicitly uses display.none; settings remain editable. Only display arguments/revision changed, verified by reverse-transform source comparison. Cannot programmatically set the existing instance's global Style checkbox; do not claim literal unchecked state. Audit outputs and logic unchanged. Fresh .pine/.txt delivered; TradingView checks still pending.

Latest delivery is **UI 1.0.1** (30 October 2026). User reported CE10213 missing output; delivered UI 1.0 was complete with 20 top-level plot calls and matching download/Git hashes, so exact cause is unverified. Added an explicit Data Window close plot near the header and final completeness marker; now 21 plots. Same logic. Fresh .pine and .txt copies provided. Read COMPILE_CHECKS before further debugging; do not claim TradingView compilation or that partial paste is proven. Await the user's compiler outcome/full editor source if needed.

Latest script is **UI 1.0**, still `src/piprunner_4h_bias.pine`. User authorized zone/SPA implementation. Added PROPOSED automatic S/D detection (fixed base length, 2-candle departure, body/range + ATR thresholds), latest demand/supply per source timeframe, confirmed own-timeframe close invalidation beyond frozen 30% full-base buffer, configurable boxes/invalidation lines and 1H HTF-aligned S/D SPA candidate labels. Thresholds and simplified boundary choices remain proposed. Details/limitations: `ZONES_SPA_IMPLEMENTATION.md`. S/R branch, full setup lifecycle, qualified 15m sequence and all orders/management remain unimplemented. Do not call this a complete End-of-P2 entry strategy.

Confirmed invariants: SPA means Strong Price Action; end of P2; S/R OR S/D plus any one directional pattern; own-zone-timeframe CLOSE (not wick) beyond buffered invalidation; 4H always authorizes direction. Candidates use only implemented S/D branch. Bull piercing on by default, bearish dark-cloud experiment off. Latest-only zone replacement is a research simplification, not invalidation. Existing structure/timeframe visibility rules persist.

Run `python -m unittest discover -s piprunner/tests -v`: 32 reference tests pass. Snapshot/source comparison confirms existing structure and original 16 audit plots unchanged. Reference tests do not compile/execute Pine. Earlier revisions visibly run on user charts; UI 1.0 compiler/runtime/replay/visual acceptance remains pending. First review 4H boxes against user examples, then 1H SPA contacts. Known gaps: S/R, zone pooling/freshness/aging policy, malformed-feed recovery, comprehensive event export and actual entry rules. No empirical performance claims.

Presentation preferences are in ANNOTATION_STYLE: horizontal lines, distinct timeframe colors, Large BOS/CHoCH text by default. UI_02/UI_03 preserve earlier presentation history; DECISIONS records rule ownership.

The Word copy could not be visually rendered because the renderer was unavailable. `requirements.md` is the reviewable design text. Later platform confirmation and progress are recorded here and in DECISIONS; the older requirements section D02 asking to choose a platform is superseded by decision D-001. Its other feed/session questions remain open. Do not treat the Word copy as a current progress ledger.

## First implementation to build

The Pine v6 source and reference fixtures have now been written. Next: compile/load UI 1.0, review proposed zones and patterns against user examples, run own-timeframe close and visibility/replay checks, then define S/R and setup/15m entry rules before enabling qualification or orders. Keep candidate B4H v0 explicitly labelled PROPOSED. Do not enable orders or claim the user has approved its structural behavior.

Candidate summary: strict confirmed L/R pivots (proposed default 2/2), independent high/low lists, two highs and two lows for classification, HH+HL bullish and LH+LL bearish, mixed structure neutral, insufficient data unknown. Close-based protected-level invalidation wins over same-update pivot classification; rearming needs fresh evidence. Verify full details in the requirements before coding.

Include AN01–AN04 and a checklist shell for later stages, plus Training/Guided/Minimal/Off visibility. Distinguish origin/confirmation/publication time. Pending features cannot show PASS. Reference tests B01–B14 and annotation tests A02–A06; B15 needs chart review. Pine compilation and replay are separate verification gates.

Known implementation limits: chart support restricted to standard 15m/1H/4H; native feed sessions; malformed OHLC latches UNKNOWN until corrected-data reload; missing-session detection and automatic recovery not implemented. Initial annotation controls are a subset of the full future design. See `4H_BIAS.md` for precise supported controls and outstanding acceptance tests. Complete event export remains pending; numeric audit plots are present.

## Still open

User chart review 001 is recorded in `CHART_REVIEW_001.md` (snapshot https://www.tradingview.com/x/JPaT4zMi/). Indicator output is visible on 4H/1H/15m, with matching current bearish state, evidence pairs, 13:00 UTC confirmation and 1.33386 protection. Treat this as user-provided execution/partial visual evidence, not independent exact-revision compilation or replay validation. Current 4H is open above protection; waiting for its close is consistent with the rule. Readability issues: checklist covers candles, confirmation labels overlap, pivot-side colors can confuse trend interpretation. UI 0.3 resolved the main clutter concern according to later user feedback; UI 0.4 enlarges event text. Closed-bar/replay checks remain open; do not change model rules based on one image.

Approval of the 4H candidate and feed/session boundaries; automated zone formation and S/R invalidation, FVG status, numeric SPA/contact definitions and bearish piercing counterpart; precise 15m structure, retest and candle predicates; expiry inclusivity; stop buffer; meaning of minimum 2R; target and runner policy; sizing, costs and test datasets. Read the complete decision register D01–D11 in requirements.

## Continuation routine

1. Read repository/project instructions and these context documents.
2. Inspect current branch, status, recent commits and actual source/tests. Repository state can be newer than this handover.
3. Continue the first incomplete roadmap item. Platform is already confirmed; do not ask again.
4. Record verification honestly and update this handover plus the roadmap and decisions as appropriate.

## Source provenance

User requests in this development chat establish the confirmed scope above. The earlier discussion was titled `Analyse Strategy Integration`, conversation ID `6ae359fc-2d4c-83eb-a580-3d277ef48ff1`. Its assistant recommendations were proposals, not user approvals. The repository documents are intended to be self-contained; access to that chat is not required to continue.
