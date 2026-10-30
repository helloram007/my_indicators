# Supply & Demand Trading — Validated Rules and Multi-Timeframe Design

Reference review | PriceActionNinja | Version 1.0

> Archived from the ChatGPT conversation “Validate Supply Demand Rules”. The title and assessments reflect that conversation; this document does not establish a validated trading edge. Numerical settings are proposed research parameters.
> Source conversation: https://chatgpt.com/c/6ae468fc-d91c-83ed-bb38-f8696c4373ed
> Archived: 2026-10-30.
> Citation markers unavailable outside the original chat have been removed; named source links are preserved.

The original conversation reviewed the [PriceActionNinja Supply and Demand Guide](https://priceactionninja.com/the-ultimate-guide-to-trading-supply-and-demand-zones/) and compared its principles with other supply-and-demand trading explanations and published backtest examples.

**My assessment: the guide is a useful foundation for identifying trading zones, but several concepts need to be made more precise before they can become reliable TradingView indicator or strategy rules.**

For your End-of-P2 trading approach, I recommend separating the system into three responsibilities:

# 4H

HTF

**Direction and location**

Determine market structure, identify strong supply/demand zones, and define where a P2 pullback could finish.

# 1H

ATF

**Setup and confirmation**

Identify price reactions, CHoCH, BOS, rejection/engulfing candles, and refined zones.

# 15m

LTF

**Entry and risk management**

Confirm the local structural shift, wait for break and retest, then validate entry, stop-loss, and reward/risk.

The central principle is:

**The HTF tells us WHERE to trade, the ATF tells us WHEN a setup is developing, and the LTF tells us HOW to execute it.**

---

## 1. Validation of the PriceActionNinja knowledge

The guide correctly emphasises strong departures, fresh zones, compact bases, price-action confirmation, and the importance of structure. It also describes two trading approaches: entering through limit orders at a zone or waiting for rejection/engulfing confirmation.

However, a useful trading concept is not automatically a proven statistical edge.

| Concept from the guide | Assessment | Rule for our strategy |
|--------|--------|--------|
| Strong impulse creates a potential zone | Sound as a price-action observation | Require a measurable departure |
| Fresh zones deserve priority | Reasonable hypothesis | Prioritise first retest |
| Compact bases are preferred | Useful filtering concept | Measure base candle count and width |
| BOS increases zone importance | Strong structural rationale | Record whether departure broke structure |
| HTF alignment matters | Appropriate multi-timeframe filter | Require directional alignment |
| Pin bars and engulfing candles confirm reactions | Useful but imperfect signals | Combine candles with structure |
| Every zone has unfilled institutional orders | Not directly verifiable from candles | Never treat as established fact |
| Zones work only once | Too absolute | Prioritise first touch, study subsequent touches |
| Fixed zone expiry periods | Unproven universal rule | Make expiry configurable |
| Fixed pip buffers | Not robust across instruments | Use instrument-aware volatility buffers |

### Three important corrections

**1. A candle chart cannot prove institutional orders remain at a zone.** It can show where price previously accelerated, consolidated, or reversed. That is an observable fact; the explanation involving unfilled bank orders remains a hypothesis.

**2. The article makes conflicting claims about zone strength.** It describes RBR/DBD continuation zones as important, while elsewhere favouring RBD/DBR reversal zones. Rather than assuming one formation always outperforms another, our software should classify both and measure their performance separately.

**3. The guide's age, first-touch, and stop-buffer rules need testing.** It recommends different age limits by timeframe and fixed pip ranges, but these should not be universal rules for EURUSD, GBPUSD, gold, and indices.

Independent published tests also show mixed results: some narrowly defined zone strategies have shown positive results on limited samples, while other tests have been statistically inconclusive. This supports testing objective rules rather than assuming a particular win rate.

## 2. The four supply and demand formations

These formations should be the foundation of our zone-detection engine.

```svg
<svg viewBox="0 0 170 105" width="100%" xmlns="http://www.w3.org/2000/svg"><rect x="55" y="43" width="57" height="22" rx="3" fill="#16a34a" fill-opacity=".16" stroke="#16a34a" stroke-dasharray="3 3" /><polyline points="8,87 23,71 36,77 53,53 66,56 77,51 90,55 102,52 124,30 135,36 160,9" stroke="#16a34a" stroke-width="3" fill="none" stroke-linejoin="round" /></svg>
```

**Rally–Base–Rally (RBR)**

Demand continuation. Bullish price movement pauses, then continues higher.

```svg
<svg viewBox="0 0 170 105" width="100%" xmlns="http://www.w3.org/2000/svg"><rect x="55" y="43" width="57" height="22" rx="3" fill="#dc2626" fill-opacity=".16" stroke="#dc2626" stroke-dasharray="3 3" /><polyline points="8,9 23,31 36,24 53,54 66,50 77,56 90,51 102,55 124,78 135,73 160,98" stroke="#dc2626" stroke-width="3" fill="none" stroke-linejoin="round" /></svg>
```

**Drop–Base–Drop (DBD)**

Supply continuation. Bearish movement pauses, then continues lower.

```svg
<svg viewBox="0 0 170 105" width="100%" xmlns="http://www.w3.org/2000/svg"><rect x="65" y="68" width="49" height="23" rx="3" fill="#16a34a" fill-opacity=".16" stroke="#16a34a" stroke-dasharray="3 3" /><polyline points="8,10 29,32 43,27 61,76 75,83 88,77 100,82 112,78 132,42 143,48 161,9" stroke="#16a34a" stroke-width="3" fill="none" stroke-linejoin="round" /></svg>
```

**Drop–Base–Rally (DBR)**

Demand reversal. A bearish move ends in a base followed by an upward departure.

```svg
<svg viewBox="0 0 170 105" width="100%" xmlns="http://www.w3.org/2000/svg"><rect x="65" y="13" width="49" height="23" rx="3" fill="#dc2626" fill-opacity=".16" stroke="#dc2626" stroke-dasharray="3 3" /><polyline points="8,96 29,73 43,79 61,29 75,23 88,29 100,23 112,28 132,63 143,56 161,96" stroke="#dc2626" stroke-width="3" fill="none" stroke-linejoin="round" /></svg>
```

**Rally–Base–Drop (RBD)**

Supply reversal. A bullish move ends in a base followed by a downward departure.

Illustrative formation shapes, not actual market candles or evidence of profitability. Green represents demand; red represents supply.

For your strategy, both continuation and reversal formations matter. A DBR zone can mark the end of a bearish pullback within a larger 4H uptrend. Likewise, an RBR demand zone can be created as that uptrend resumes.

**Important:** A DBR formation does not automatically mean the 4H trend has reversed. The classification describes the local price pattern, not necessarily the higher-timeframe trend.

---

## 3. Objective zone identification rules

These are my proposed software-ready rules, not fixed thresholds established by PriceActionNinja. We should test and refine the numerical parameters.

| Rule | Proposed initial requirement |
|--------|--------|
| Z01 — Base | 1–3 completed candles; configurable maximum of 5 |
| Z02 — Compactness | Base high-to-low range ≤ 1.5 × ATR(14) |
| Z03 — Departure | Move ≥ 1.5 × ATR(14) from the base boundary within 3 candles |
| Z04 — Departure direction | Bullish for demand, bearish for supply |
| Z05 — Structure | Flag whether departure produces a confirmed BOS or CHoCH |
| Z06 — Zone boundaries | Use the entire base candle range initially |
| Z07 — Freshness | No qualifying revisit after departure confirmation |
| Z08 — Zone width | Record width in pips, points and ATR |
| Z09 — Invalidation | Default to a completed candle closing beyond the distal boundary |
| Z10 — Confirmation | Only use completed candles; no forward-looking swing recognition |

### Precisely drawing zone boundaries

Illustrative candles. The upper boundary of a demand zone is proximal; the lower boundary is distal. For supply, the proximal boundary is the lower edge and the distal boundary is the upper edge.

For automated detection, the initial full-base method is:

- Demand: proximal = highest high of base; distal = lowest low of base.
- Supply: proximal = lowest low of base; distal = highest high of base.

The article also describes a swing-extreme-to-base-candle method. We should preserve this as a second configurable drawing method and compare it with the full-base method.

We must not allow the software to redraw historical zone boundaries using information unavailable when the zone was first confirmed.

---

## 4. Higher Timeframe — 4H rules

HTF-01 through HTF-07 | Direction and location

The 4H chart should answer: *What is the larger market direction, and which price zones are relevant to a potential continuation trade?*

| ID | Required analysis | Proposed rule |
|--------|--------|--------|
| HTF-01 | Trend structure | Classify confirmed HH/HL, LH/LL, or range |
| HTF-02 | Trend state | Bullish, bearish, transitional, or neutral |
| HTF-03 | Demand zones | Detect bullish DBR and RBR formations |
| HTF-04 | Supply zones | Detect bearish RBD and DBD formations |
| HTF-05 | Zone quality | Evaluate freshness, departure, base, BOS and location |
| HTF-06 | FVG confluence | Mark FVGs from completed 4H candles; record overlap |
| HTF-07 | Trade bias | Permit trend continuation only when structure and zone direction align |

### Proposed 4H zone-quality score

The original conversation included an interactive score display, but no recoverable weights or grading formula. Define and test those before implementing the priority threshold of 80/100.

These weights and grade thresholds are preliminary design choices, not validated probabilities of success. Hard invalidation rules take precedence over the score.

In an uptrend, the software should highlight fresh 4H demand zones where a P2 pullback might terminate. In a downtrend, it should highlight fresh 4H supply zones.

Opposing zones must also be retained because they can affect available reward/risk and profit targets.

### 4H bias example

Bullish continuation candidate:

1. Previous confirmed higher high and higher low establish the bullish structure.
2. A fresh 4H demand zone exists below price.
3. Price pulls back into or towards that zone.
4. Price shows rejection, and the relevant 4H structural confirmation is observed.
5. The system authorises 1H bullish setup monitoring.

A rejection alone is not enough to declare a new bullish trend. If the 4H prints a confirmed bearish CHoCH against the previous uptrend, the state should become *transitional* until continuation or reversal is resolved.

---

## 5. Analysis Timeframe — 1H rules

ATF-01 through ATF-07 | Setup development

Once the 4H identifies a valid area of interest, the 1H chart should determine whether buyers or sellers are actually responding.

| ID | Condition | Required behaviour |
|--------|--------|--------|
| ATF-01 | HTF permission | Only monitor direction permitted by 4H |
| ATF-02 | Zone interaction | Record the 1H candle touching the 4H zone |
| ATF-03 | Price reaction | Detect qualifying rejection or engulfing candle |
| ATF-04 | Structure | Track internal CHoCH and subsequent BOS |
| ATF-05 | Refined zone | Identify local 1H supply/demand created by the reaction |
| ATF-06 | FVG | Record directional FVG confluence, if present |
| ATF-07 | LTF permission | Allow 15m execution monitoring once the 1H setup is valid |

**Crucial distinction:** We should not require the 1H CHoCH to occur on the same candle as the 4H zone touch. A zone touch is an event; structural confirmation may occur several candles later.

For the initial design, qualifying 1H signal candles can use your existing Balanced Pin Bar and Engulfing definitions. We should not introduce different candle thresholds into the zone module without testing them.

---

## 6. Lower Timeframe — 15m execution rules

LTF-01 through LTF-09 | Entry and execution

The 15m chart is where the End-of-P2 trade should become executable, using your established sequence.

**4H zone + bias confirmed**

**1H reaction + setup zone identified**

**15m CHoCH within 1H setup zone**

**Break of the defined swing**

**Valid retest + signal candle**

**Place conditional entry**

Minimum 2R and all risk/invalidation checks passed

### Preserve these existing End-of-P2 rules

| Feature | Specification |
|--------|--------|
| Entry trigger | Break of 15m signal candle + 1 tick buffer |
| Stop-loss | Beyond retest-sequence extreme |
| CHoCH-to-retest maximum | 8 completed 15m candles |
| Retest-to-signal maximum | 4 completed 15m candles, including first retest candle |
| Pending entry expiry | 3 completed 15m candles |
| Minimum available reward/risk | 2R |
| Initial testing risk | 0.5% of account |
| First profit-taking | 50% at TP1 |
| Runner | Remaining 50% |
| Break-even | Structure-based |
| Trailing stop | 15m structure |

The new supply-and-demand module should provide **location and setup quality**, not replace these trade-management decisions.

If the 15m stop lies inside the wider 4H zone, the trade can still be executed under the existing strategy, but the backtest should measure whether wider HTF invalidation gives different results.

---

## 7. Zone lifecycle and invalidation

One of the most important requirements for software is to distinguish a zone that is merely detected from one that is genuinely available to trade.

| State | Meaning | Software action |
|--------|--------|--------|
| Candidate | Base identified, departure not yet qualified | Monitor |
| Confirmed | Departure conditions satisfied on closed candles | Draw zone |
| Fresh | No qualifying return since confirmation | Eligible |
| Touched | Price returns to zone | Start reaction monitoring |
| Reacted | Price leaves after touching | Record reaction outcome |
| Mitigated | One or more qualifying prior visits | Lower priority |
| Invalidated | Price violates configured structural boundary | Exclude from new entries |
| Expired | Maximum age reached | Archive or hide |

For a bullish demand zone, I propose two separate invalidation concepts:

**Zone invalidation:** A completed 4H candle closes below the demand zone's distal boundary, using a configurable volatility buffer if required.

**Trade invalidation:** The actual 15m trade reaches its defined stop-loss.

These must be tracked independently. A stopped-out 15m trade does not automatically invalidate the whole 4H demand zone, and a 4H invalidation event does not necessarily mean an earlier 15m stop was triggered.

Also, a wick through the distal line followed by recovery should be recorded as a sweep or penetration event, not automatically equated with a confirmed close-based structural break.

---

## 8. Worked bullish End-of-P2 example

Hypothetical EURUSD scenario — prices are illustrative, not a historical signal.

| Timeframe | Observation | Decision |
|--------|--------|--------|
| 4H | Higher highs and higher lows | Bullish bias |
| 4H | Fresh demand between 1.0800–1.0850 | Potential P2 termination area |
| 1H | Price enters demand; bullish rejection appears | Monitor bullish setup |
| 1H | Local bullish structural shift develops | Refine 1H SPA zone |
| 15m | Bullish CHoCH inside the 1H setup area | Begin confirmation sequence |
| 15m | Defined swing is broken, followed by retest | Look for qualified signal |
| 15m | Bullish engulfing signal closes | Determine buy-stop above signal high |
| Risk | Stop beyond retest extreme | Calculate position size |
| Target | Unobstructed space allows at least 2R | Permit conditional entry |

Consider an example entry at 1.0861 and stop at 1.0831. That is 30 pips of initial risk, so a 2R target would be 1.0921.

But if a credible opposing supply zone begins at 1.0900, the strategy should flag insufficient reward space rather than assume the full 2R remains unobstructed.

---

## 9. TradingView software implementation requirements

I recommend developing the supply-and-demand capability as a separate, reusable module before integrating it with Piprunner or End-of-P2.

| Phase | Feature | Deliverable |
|--------|--------|--------|
| 1 | 4H structure and bias | HH, HL, LH, LL, CHoCH, BOS |
| 2 | 4H zone detection | RBR, DBD, DBR, RBD rectangles |
| 3 | Zone-quality engine | Freshness, impulse, BOS, score |
| 4 | FVG detection | 4H and 1H imbalance overlays |
| 5 | Zone lifecycle | Touch, mitigation, invalidation, expiry |
| 6 | 1H setup engine | SPA, reaction, local structure |
| 7 | 15m execution engine | CHoCH, breakout, retest and signal |
| 8 | Risk and management | Entry, SL, TP, partial exits |
| 9 | Testing and analytics | Zone outcome, R-multiple, expectancy |

For the backtest, every zone should store at minimum: symbol, timeframe, formation type, creation time, confirmation time, proximal/distal prices, ATR, departure strength, structure-break status, freshness, touch count, maximum penetration, reaction outcome, and eventual invalidation time.

We should also maintain two distinct performance datasets: **zone reactions** and **actual executed trades**. A zone can produce a bounce without ever generating a valid End-of-P2 entry.

Finally, all higher-timeframe values must use confirmed data, and fractal swing confirmation must respect the required right-side candles. Otherwise, historical results can be distorted by repainting or lookahead bias.

---

## 10. Recommended starting configuration

These are initial research settings, not optimised values.

| Parameter | Initial setting |
|--------|--------|
| HTF / ATF / LTF | 4H / 1H / 15m |
| Zone formations | All four |
| Base candle count | 1–3 |
| Maximum base width | 1.5 ATR |
| Departure threshold | 1.5 ATR |
| Departure window | 3 candles |
| Zone boundary method | Full candle range |
| Fresh zone preference | First touch |
| Zone close-based invalidation | Enabled |
| FVG requirement | Optional, scored |
| HTF structural alignment | Mandatory |
| Zone score threshold | 80 for priority display |
| Entry method | Existing End-of-P2 confirmation |

### Final recommendation

The most important next step is **Phase 1: formalising 4H bias, and Phase 2: detecting and drawing supply/demand zones with precise rules**. Once those are trustworthy, we can add 1H reactions and 15m confirmation without making the system unnecessarily restrictive.

I would initially keep a 4H structure and zone map entirely visible, including opposing zones, with labels such as `4H DEMAND | DBR | FRESH | BOS`, while using separate status indicators for whether a trade is actually permitted.

This gives you a cleaner discretionary chart today and an objective foundation for automated trading later.

Primary reference: [PriceActionNinja Definitive Guide](https://priceactionninja.com/the-ultimate-guide-to-trading-supply-and-demand-zones/). Additional comparison: [CMC Funded — Supply and Demand Trading](https://cmcmarketsfunded.com/learn/supply-and-demand-trading/).