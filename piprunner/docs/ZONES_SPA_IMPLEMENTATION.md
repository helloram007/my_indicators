# UI 1.0 supply demand and Strong Price Action research release

The user authorized implementation of the zone and SPA specification. This revision adds automated S/D candidate boxes and HTF-aligned 1H SPA research annotations to the existing three-timeframe structure script. It does not complete the entry strategy, place orders or claim to reproduce every discretionary zone in the course.

## Confirmed rules implemented

Invalidation buffer defaults to 30% of the full selected base high-low range. Demand threshold is base low minus the buffer, rounded down to tick size; supply is base high plus the buffer, rounded up. Threshold and geometry remain frozen until a new same-side candidate replaces the old one. Equality and wick-only breaches do not invalidate. The zone's own timeframe close must be strictly beyond its threshold.

4H directional bias controls the 1H SPA candidate: no counter-4H signals and no direction supplied by lower timeframes when 4H is neutral/unknown. A pattern is only a research candidate at a valid location, not permission to enter. The separate 15m sequence, tick offset, expiry, stop, reward/partial/runner requirements remain unimplemented.

## Explicit proposed detector defaults

The automated detector uses exactly **2 base candles followed by 2 departure candles**. Base length is configurable 1–6. Each base candle body must be at most 50% of its own range; full base range must be at most 1.2 times ATR14 measured at the last base candle. Each departure body must be at least 50% of its own range. Both departure bodies point the same way, the final close must leave the full base, and net displacement from first departure open to last close must be at least 1.0 ATR14. Base/departure ratios are configurable proposals.

Demand contact zone: full base minimum low to maximum real-body top among base candles. Supply: minimum real-body bottom to full base maximum high. The 30% buffer always uses the full base range, not the narrower contact-zone height. This is an explicit simplified base detector, not a claim that the user approved these boundary/strength choices. It does not associate a separate swing outside the selected base or rank reversal versus continuation origins.

Each timeframe retains only its **latest demand and latest supply**. A newer same-side candidate replaces the older reference even if the old zone is still valid. That replacement is not invalidation. No first-touch-only, age expiry or historical pool of all zones is claimed. Retouches remain eligible in this research release. Compare the boxes with user-drawn examples before accepting the detector.

## Timeframes and display

4H zones are available on all supported charts. 1H zones are available on 1H/15m; 15m zones only on 15m. The detector and lifecycle run inside their source contexts and return offset confirmed fields, independent of visibility. Zone drawing starts at the base origin but is not available until the second departure candle closes. Lower chart intervals cannot retire an HTF zone.

Default display: 4H and 1H S/D boxes on, 15m S/D off to reduce clutter. Original structure drawings remain. Zone fills default to 92% transparency. Each box has a timeframe/type label; its separate dotted invalidation line states the close threshold. Show latest invalidated zones optionally in gray, frozen to invalidation time. Visibility is independent of calculation and contact qualification. The boxes are latest-endpoint views, not a complete historical zone ledger/export.

## One-hour SPA candidates

Completed 1H candles are requested independently on 1H/15m charts. Configurable patterns:

- Pin: nonzero body/range; rejection wick at least 2 bodies and 60% of range; opposite wick at most 20%; close in the opposite-end 35%. Dominant rejection wick must contact an active zone. Body color is not required. Dojis are excluded.
- Engulf: opposite prior body, full real-body coverage including equality, current body at least 1.2 prior bodies and 60% of its own range. Prior doji excluded. Full-wick engulf is not required.
- Bullish piercing: prior bearish body, current bullish body, strict midpoint penetration with close below prior open. Forex default opening condition allows open <= prior close; strict gap below prior low is optional.
- Bearish dark-cloud counterpart: implemented as an **off-by-default experiment**, because that counterpart has not been explicitly approved. It mirrors the midpoint/open rules and is named accurately.

Pin requires current wick contact. Two-candle patterns may use either candle for location contact by default; prior-candle contact can be disabled. The zone must already exist at the contacted candle's opening time and must still be active when the pattern confirms. Same-timestamp zone invalidation wins. A pattern can contact either the active 4H or 1H corresponding S/D side. Multiple matching patterns yield one label listing their names. No additional three-structure alignment gate is introduced.

**Partial branch limitation:** automatic S/R detection is not implemented because its rules are undefined. This release implements the S/D alternative and explicitly identifies S/R as pending. It must not be presented as a complete implementation of the user's S/R OR S/D setup. No fallback from failed S/D to invented S/R exists.

The bottom-left research panel reports the latest 1H S/D SPA candidate and remaining gates. SPA visibility and retained label count are configurable; Off hides both panels/educational drawings. Historical candidate labels are records of the context at publication; they are not active orders or perpetual setups. No setup lifetime/cancellation/rearm engine exists yet.

## Verification

32 independent Python reference tests pass: original 21 plus 11 zone/SPA tests. New fixtures cover buffer/tick arithmetic, invalid metadata, wick/equality versus close, zone-timeframe isolation, immutable levels, no pre-creation contact, compact-base/departure detection, pin/engulf/piercing, off-by-default bearish counterpart, HTF gating and invalidation priority. These do not compile or execute Pine. The shared structural snapshot and original 16 numeric audit plots remain unchanged by source comparison.

TradingView compilation/replay and visual validation are pending. Test each supported chart, exact own-timeframe invalidation, base/departure input extremes, both sides, equality/one-tick cases, no early boxes or SPA, independent requests and toggle parity. Check labels/boxes against user annotations before calling the detector course-matched. Data-feed gaps/revisions and malformed-history recovery are not solved by this feature.

## Use

Replace the whole existing Pine Editor source with `src/piprunner_4h_bias.pine` (filename retained for continuity), save and update. Title must show **UI 1.0**. Use 15m to see all structure layers; enable 15m S/D separately if desired. Initially compare only 4H boxes against user-drawn zones, then review 1H patterns. Do not add a duplicate indicator over the existing copy.

Next: TradingView acceptance, calibration of proposed zone/pattern thresholds, explicit S/R detector definition, then actual setup lifecycle and qualified 15m entry sequence. Preserve all confirmed HTF, buffer, own-close and management invariants.
