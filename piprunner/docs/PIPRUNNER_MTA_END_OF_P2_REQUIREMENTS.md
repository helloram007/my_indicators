# Piprunner + MTA-End-of-P2

Product2 requirements v1, 5 November 2026. Independent combined indicator CONFIRMED. User selected **additional fractal confirmation while preserving the full End-of-P2 entry sequence**. Inherits every baseline rule in [MTA_END_OF_P2_REQUIREMENTS.md](MTA_END_OF_P2_REQUIREMENTS.md) and [SHARED_MTA_CONTRACT.md](SHARED_MTA_CONTRACT.md).

## Additional requirements

- P01: implement a 15m Williams Fractal continuation signal as an additional qualification gate. Generic swing pivots or a single fractal marker are insufficient.
- P02: supplied default2 left / 2 right; confirmation only after right-side candles close. Expose pivot origin and confirmation/publication separately. Exact equality/dual-pivot handling is OPEN.
- P03: original long pattern: preceding highs showHH and lowsHL, then a confirmedLH high fractal appears. Original short: preceding highsLH and lowsLL, then a confirmedHL low fractal appears. Selection/order/strictness of preceding references and replacement/consumption policy remain OPEN. HTF direction and valid 1H setup remain mandatory in the combined product.
- P04: preserve CHoCH → separate swing break → retest → signal candle; preserve signal candle±one tick, retest stop, three-bar expiry, minimum 2R, 50% TP1 and runner. Never switch to original Piprunner's fractal ± one pip, opposite-fractal stop or 1R target.
- P05: expose candidate state, confirmation delay, source references, direction, setup linkage and rejection reasons in labels/dashboard. New `showFractals` affects drawings only; `useFractalConfirmation` affects experiment identity and plan eligibility. Proposed default for this named combined mode is ON; default/preset is still a proposal. Disabled-gate mode must be labelled baseline comparison, never fractal-confirmed.
- P06: optional EMA36/100 filter is independent of the fractal gate and visual EMAs. Original supplied relation is36 > 100 for long / 36 < 100 for short; proposed evaluation context 15m confirmed close, timing/default off await review. The user's additional-fractal choice does not make EMA mandatory.
- P07: compare baseline and combined on identical input data. Gateoff reproduces MTA baseline; gate on adds a restriction rather than bypassing baseline requirements.

## Proposed gate placement — not confirmed

Preferred design candidate: evaluate and link fractal evidence in parallel with15m baseline stages, then require eligible fractal confirmation at VALIDATE_PLAN, before ARMED. A confirmed candidate may predate the signal only within an approved same-setup window. If unavailable when the signal closes, remain WAIT_FRACTAL and do not backdate an order. Reject stale/invalid baseline signal rather than extending its life indefinitely. No entry is eligible before the later publication of all mandatory gates.

OPEN: can confirmation arrive after the signal; allowable same-setup window; when signal validity begins/ends while waiting; whether the three-bar clock starts from the baseline signal or arming; treatment if intended entry already traded before arming; candidate consumption/replacement; whether a further price break of theLH/HLfractal is required. Until these are resolved, a missing gate may display WAIT/UNDEFINED but cannot create executable plans. No new breakout requirement is invented here.

## Implementation and acceptance

Fractal continuation detector/gate NOT implemented. Current prototype structural pivots do not satisfyP01. Separate combined entrypoint not created by this requirements split.

F01: no publication before right-bar close; future bars cannot rewrite confirmed events. F02: mirroredHH/HL→LH andLH/LL→HLfixtures, missing precursor/equal/dual-pivot cases. F03: permitted baseline with no fractal remains blocked/waiting when gate on; valid fractal cannot bypass any missing baseline stage. F04: 4Hconflict rejects fractal; expired setup cannot reuse it. F05: gate off ledger equals baseline; EMA flag independent; show/hide/orientation parity. F06: signal/confirmation clock, crossed-entry and expiry-boundary fixtures after policy approval. F07: tick entry, retest stop,2R,partial/runner identical tobaseline on matched eligible setups. F08: actual Pine compile/replay/reload/source clock tests. No success-rate claim without locked costs and out-of-sample evaluation.
