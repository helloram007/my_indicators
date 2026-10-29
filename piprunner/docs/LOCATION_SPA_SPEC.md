# Location and Strong Price Action setup specification

Status: confirmed strategy intent plus proposed mechanical details. 29 October 2026. Supersedes the earlier missing SPA definition and the user's corrected P3 wording. Indicator code remains UI 0.9 until this feature is implemented.

## Confirmed by the user

- SPA means **Strong Price Action**.
- The strategy identifies the end of **P2, the pullback**. The mention of P3 was corrected explicitly.
- Price retraces to **either support/resistance OR supply/demand**; both are not required.
- **Any one** of pin-bar rejection, strong engulfing or piercing qualifies the SPA-pattern branch, in the 4H direction.
- A supply/demand zone becomes invalid on **any wick strictly beyond its far edge**. Do not wait for a 4H close. This does not change the distinct close-confirmed structural bias rule.
- User supplied PriceActionNinja's guide as the supply/demand methodology reference.

The existing 15m entry sequence, stop, expiry and management invariants remain unchanged. A qualified 1H SPA observation is not an immediate market entry and cannot bypass the 15m sequence.

## Course reference and limits

Source: [Supply And Demand Trading The Definitive Guide](https://priceactionninja.com/the-ultimate-guide-to-trading-supply-and-demand-zones/), reviewed 29 October 2026, especially the manual zone-drawing and price-action entry sections.

The guide places demand around the base preceding an upward departure and an associated low; supply uses a base preceding a downward departure and an associated high. It allows different base-candle boundary choices, discusses freshness and favors observing rejection on a return. These are discretionary guidelines rather than a fully specified detector. Automated base selection, boundary convention, departure thresholds, freshness limits and S/R definitions still need an explicit research specification. Its entry, stop and management examples do not replace End-of-P2 rules. Explanations about institutional intent are not directly observable inputs.

## Setup composition

Confirmed intent: directional 4H context AND a retracement to an eligible location AND at least one approved directional SPA pattern on completed 1H evidence. Proposed execution details below are not promoted to confirmed rules merely because the user supplied the guide.

For longs use support/demand and bullish SPA with bullish 4H bias; for shorts use resistance/supply and bearish SPA with bearish 4H bias. Neutral/unknown bias blocks qualification. The directional side mapping and the exact requirement that 4H bias still agrees at the 1H close are proposed mechanical details consistent with the intent, requiring chart review.

1H directional structure need not itself be bullish/bearish unless separately approved. Do not silently require three-timeframe alignment: the SPA can precede a full 1H structural reversal. Existing research structure classification is context, not an additional approved gate.

## Zone contract and causal lifecycle

Zone record: ID, type (S/R or S/D), timeframe, lower/upper prices, base origin, creation/departure confirmation time, first available time, active/invalidated status, first return time, touch count, invalidation timestamp and evidence bar. Freeze boundaries on creation; never enlarge a zone after seeing later price.

Demand far edge is its lower boundary; supply far edge is its upper boundary. CONFIRMED invalidation tests are low < demand lower edge or high > supply upper edge. Equality alone is not beyond. A proximal-edge touch enters the zone; it does not invalidate it. The first subsequent far-edge breach permanently retires that zone ID; a rebound cannot resurrect it.

Never use the eventual 4H high/low to invalidate a zone before the breach actually occurred. Proposed reproducible implementation: creation uses closed 4H evidence, while invalidation is monitored using closed 15m bars on the 15m chart and closed 1H bars on 1H. A wick is sufficient even if that monitoring candle closes back inside. This is a wick rule with up-to-one-monitor-bar reporting delay, not a close-beyond rule. A 4H-only chart cannot reconstruct the complete order of 1H/15m events without an intrabar-array implementation. Document that restriction before coding. Whether immediate tick-time visual invalidation is also wanted remains OPEN; historical tests must not pretend to know its exact tick time.

At a qualification timestamp, invalidation has priority over a pattern or zone touch on the same monitoring interval. A candle that pierces the far edge and reverses strongly is not a valid signal from that S/D zone. Another independent valid S/R zone could still qualify under the OR rule; do not invalidate every location because one S/D zone fails.

OPEN: whether the same wick rule also governs separately defined S/R zones; formation algorithm; base length/selection; open-versus-close proximal boundary; association with a swing outside the base; reversal/continuation zone eligibility; first-touch only; maximum age/touches; overlapping-zone selection; minimum departure and zone width.

Before claiming automatic course-matched zones, compare annotated examples. A manually specified price-zone research mode can help calibrate boundaries, but must be labelled manual and must use an availability timestamp so backtests do not trade a zone before it was known. Pine cannot simply read arbitrary hand-drawn TradingView rectangles.

## Proposed SPA pattern definitions for implementation review

All ratios below are configurable PROPOSALS, not supplied thresholds or course claims. Use completed standard 1H candles. Define range r=high-low, body b=abs(close-open), upper wick u=high-max(open,close), lower wick w=min(open,close)-low. Reject zero-range candles. Retain all matching pattern IDs instead of choosing only one when patterns overlap.

Pin-bar candidate: bullish w >= 2*b, w >= 0.60*r, u <= 0.20*r, and close in the top 35% of range; bearish mirrors these tests. Require the dominant wick to intersect the eligible location. Body color is not mandatory in this proposal; rejection direction and close position decide direction. Explicitly test dojis rather than letting a zero body make every ratio pass.

Engulfing candidate: current bullish and previous bearish for longs, mirrored for shorts. Current real body covers the previous real body including equality, and is at least 1.2 times the previous body with b/r >=0.60. A zero previous body does not qualify. Body engulfing is proposed; full-wick engulfing is a separate optional experiment. Define whether the current or previous candle must touch the location before enabling this predicate.

Piercing candidate: previous bearish and current bullish; current close strictly exceeds the previous body's midpoint but remains below its open. For forex, proposed relaxed opening condition is current open <= previous close, with no required gap below the previous low. Strict gapped piercing is a separate candidate. For shorts, propose the mirrored dark-cloud-cover pattern and name it accurately; this bearish counterpart has NOT yet been explicitly approved. Do not silently enable a bullish piercing pattern for bearish HTF setups.

Location contact proposal: either candle in a two-candle pattern may overlap an active eligible zone, and the confirming candle must close in the permitted direction within one 1H candle after contact. Pin bars require their own contact. Exact timing window and close-outside-versus-inside requirements remain PROPOSED. Numeric strength and contact rules must be reviewed on accepted/rejected examples before calling the implementation approved SPA.

## Proposed qualification state machine

WAIT_CONTEXT -> WAIT_LOCATION after directional 4H bias and eligible known zone exist. WAIT_LOCATION -> WAIT_SPA on an active zone return. WAIT_SPA -> SPA_CONFIRMED at a completed 1H candle that passes any enabled approved pattern, location contact and context checks. Record all evidence and create a setup ID, then hand off to WAIT_15M_CHOCH. No orders yet.

Any pre-entry state -> CANCELLED on S/D far-edge wick breach, or approved context/setup timeout rule. Bias-loss policy and setup timeout need selection. Invalidated zones cannot create a fresh setup without a new zone ID. S/R and S/D are independent alternative branches, not a requirement to intersect both zones. Multiple matching patterns produce one setup ID, not duplicate orders.

## Functional tests to add with implementation

- Z01 Demand low equal to far edge remains active; one tick below invalidates despite a close back inside. Supply test mirrors this.
- Z02 Invalidation at the observation timestamp never uses a later 4H extreme; test 15m/hourly prefix and replay parity.
- Z03 Same-interval far-edge breach and SPA candle fails that S/D branch. A separate valid S/R branch can still qualify.
- Z04 Zone boundaries/availability never change retroactively; creation, touch and retirement are separate events. No pre-creation setup.
- Z05 First touch versus retouch and age behavior follow an explicit selected policy, never an unstated default.
- S01 S/R only and S/D only each pass location with a valid pattern; absence of both fails. Each individual pattern can satisfy the OR branch.
- S02 Correct location with wrong-direction SPA fails; neutral/unknown 4H blocks; unavailable location predicates read UNDEFINED.
- S03 Pin-bar numeric equality, one-tick failures, tiny/zero bodies, dojis and zero-range bars behave explicitly.
- S04 Engulfing tests body equality, wick-only engulfing, strength threshold, opposite body direction and prior doji rejection.
- S05 Piercing tests strict midpoint penetration, full engulf versus partial piercing, forex gap mode and explicitly enabled bearish counterpart.
- S06 An unclosed 1H candle cannot qualify; multiple matching patterns generate one setup with all evidence IDs.
- S07 SPA confirmation alone cannot bypass the distinct 15m CHoCH, swing break, retest and signal-candle requirements.
- A08 Draw labelled S/D boxes with timeframe, proximal/distal edges, touch and invalidation reasons. Display SPA pattern type/time and location evidence; toggling annotations preserves ledgers. Distinct zone opacity prevents obscuring current structure lines.

## Delivery gates

First finalize the zone detector research definition and pattern contact/threshold choices, then implement causal 4H zone lifecycle and independent candle detectors with fixtures. Integrate 1H qualification only after OR composition and invalidation precedence pass. Update the checklist with truthful WAITING/PASS/INVALIDATED/UNDEFINED states. Preserve all earlier replay/compilation gates; this specification does not imply tests have run or features exist.
