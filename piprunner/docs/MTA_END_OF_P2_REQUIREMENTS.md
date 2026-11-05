# MTA-End-of-P2

Product1 requirements v1, 5 November 2026. Name and independent product boundary CONFIRMED. Applies [SHARED_MTA_CONTRACT.md](SHARED_MTA_CONTRACT.md); workflow/panels: [DASHBOARD_WORKFLOW.md](DASHBOARD_WORKFLOW.md).

## Purpose and exclusions

Standalone End-of-P2 multi-timeframe indicator. 4H controls direction, 1H qualifies the pullback ending at S/R OR S/D with SPA, 15m supplies the full End-of-P2 sequence. No Williams Fractal signal requirement in this product. Existing structural pivots may remain as the proposed swing extractor without being presented as Piprunner signals. Visual EMAs may be shared; EMA trading filters are outside the core baseline and must be explicitly labelled experiments if later added.

## Functional requirements

- M01: publish finalized 4H structural permission, protection, evidence and reason; UNKNOWN/NEUTRAL blocks new directional setup qualification.
- M02: identify source-owned S/R and S/D locations with separate IDs/lifecycles; apply own-zone-timeframe buffered-close invalidation to S/D. S/R mechanics remain OPEN.
- M03: qualify 1H end-of-P2 only with eligible location AND any one approved directional SPA pattern AND current 4H permission. Current S/D research candidates cannot be labelled full setup qualification.
- M04: create a proposed unique setup record carrying direction, HTF version, location ID, qualification time and invalidation/expiry policy. Policy details require approval.
- M05: link distinct 15m CHoCH, swing-break, retest and signal-candle events to that setup. No entry until all mandatory stages pass in approved order.
- M06: compute one-tick signal-candle entry and retest-extreme stop; freeze the plan after approved validation; reject nonpositive risk and failed minimum 2R. Exact policies remain OPEN.
- M07: track three-bar pending expiry and explicit cancellation/rejection reasons. Indicator tracking does not submit orders.
- M08: depict50% TP1 and runner under an approved policy. Do not invent targets or a runner stop from generic fractals.
- M09: expose every workflow stage in both dashboard orientations with per-step annotation switches; calculations independent of display.
- M10: retain baseline traceability and test results separate from product2; identify itself as MTA-End-of-P2 in title, panels and exported events.

## Delivery status

Reusable research code exists for M01/M02 and partial M03/M09 in the legacy prototype. Separate indicator entrypoint not yet created. S/R, full setup/lifecycle, qualified execution, risk and management remain pending. Existing generic BOS/CHoCH are explanatory structure events, not completed M05.

## Acceptance

A01: no fractal or EMA requirement blocks an otherwise qualified core-baseline fixture. A02: bearish 4H cannot produce bullish qualification despite bullish 1H/15m; unknown/neutral 4H blocks. A03: zone wick/equality holds; own-timeframe strict close beyond buffer invalidates on the correct source clock. A04: location without SPA orSPA without location cannot qualify. A05: missing/reordered execution stage cannot arm; separate swing break has its own event reference. A06: correct long/short tick entry and retest stop; expiry boundary and RR tests only after definitions resolved. A07: 50% quantity and runner consistency in future harness. A08: horizontal/vertical/per-step toggle parity, causal publication and replay/reload stability. All must be exercised against actual Pine in addition to local reference fixtures.
