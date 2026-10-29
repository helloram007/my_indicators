# Decision log

Use CONFIRMED for explicit user requirements, PROPOSED for implementation candidates and OPEN for unresolved choices. Tests establish code behavior, not user approval of trading rules.

## D-001 Target platform

Status: CONFIRMED. Date: 29 October 2026. Source: user said “yes this is for tradingview”.

Implement for TradingView. New scripts will use Pine Script v6 as the development language choice. This resolves the platform part of requirements D02; feed, symbols and sessions remain OPEN. Official language reference: https://www.tradingview.com/pine-script-docs/welcome/.

## D-002 Project location and persistent handover

Status: CONFIRMED. Date: 29 October 2026. Source: user supplied the repository, requested the `piprunner` folder and asked to keep context in GitHub for future AI readers.

Store strategy code and documentation under `piprunner/`. Root discovery instructions may link to that directory. Maintain PROJECT_CONTEXT, this log and the roadmap as work progresses. Current development branch: `piprunner/setup`; no merge into main is recorded at this handover.

## D-003 Rule preservation and optional modules

Status: CONFIRMED. Source: initial development request and annotation follow-up.

End-of-P2 invariants listed in PROJECT_CONTEXT and requirements C01–C07 remain governing requirements. EMA/fractal experiments and visual controls are separate. Do not infer approval of precise missing rules from approval to start building.

## D-004 First structural implementation

Status: PROPOSED. Candidate: B4H v0, requirements Sections 3–5.

Build as a labelled research indicator with annotations and causal tests. User chart review must approve or revise the candidate before it becomes the approved bias model. No order execution in this first feature.

## D-005 First source delivery

Status: implementation milestone, not structural rule approval. Date: 29 October 2026. Source: user authorized proceeding with the first feature.

Added Pine v6 proposed B4H v0 with learning annotations, a Python reference oracle and ten passing local tests. Pine compilation/replay and full B01–B14/A01–A07 acceptance remain pending. Deliberate first-version restrictions and gaps are recorded in `4H_BIAS.md`: 15m/1H/4H standard charts only, no session-gap inference, no automatic repaired-history recovery, partial annotation-control coverage and numeric diagnostics rather than a complete event exporter. No orders enabled. Do not treat this milestone as completion of the feature acceptance gate.

## D-006 Learning display revision 0.2

Status: implemented presentation proposal; chart acceptance pending. Date: 29 October 2026. Source: user said “next” after review 001 identified overlap and explanatory issues.

Added configurable compact/full panel, optional future rows, opacity, deterministic vertical label spacing, structure-aware colors and a live-price/close-only explanation. Detailed future items are summarized by default, not removed from requirements. Structural calculation and audit plots remain unchanged; high/low snapshot fields were added for drawings only. Full details and remaining tests: `UI_02.md`. No change to B4H approval status.

## D-007 Horizontal levels and break annotations

Status: requested presentation implemented; BOS/CHoCH classification PROPOSED pending chart review. Date: 29 October 2026. Source: user supplied UI 0.2 screenshot, said chart looks clumsy and requested horizontal annotations, current annotation, BOS/CHoCH and timeframe.

Default Horizontal lines replaces bubble history with two current 4H references, right-edge labels, three retained break segments and Summary panel. Detailed semantics and controls are in `UI_03.md`. 4H close crossing a confirmed reference is BOS with prior directional bias, CHoCH against it, otherwise unclassified Break; consume each pivot once. No 1H/15m engine or order conditions added. Existing bias calculations unchanged. Fifteen independent local tests pass; Pine compilation of this revision remains pending.

## D-008 Event text and timeframe colors

Status: CONFIRMED user presentation requirements; exact future colors PROPOSED. Date: 29 October 2026. Source: user says UI 0.3 gives a clear view, requests distinct colors for future 1H/15m structure and larger BOS/CHoCH text everywhere.

UI 0.4 adds event-text size Normal/Large/Huge, default Large; panel/swing size remains independent. Future timeframe layers must use distinct configurable colors and explicit timeframe prefixes. Proposed palette and validation details are in `ANNOTATION_STYLE.md`. No trading rule approval or 1H/15m implementation is inferred.

## Update format

For future decisions include date, source of authorization, status, exact choice, superseded requirement/decision, affected files/tests and remaining questions. Preserve prior entries; supersede explicitly instead of erasing the history.
