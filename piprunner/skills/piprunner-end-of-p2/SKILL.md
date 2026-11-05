---
name: piprunner-end-of-p2
description: Route legacy requests for the former combined Piprunner skill to the separately named MTA-End-of-P2 or Piprunner + MTA-End-of-P2 product.
---

# Legacy strategy skill router

Superseded on 5 November 2026 by two independent skills. Locate the current my_indicators checkout, read piprunner/docs/INDICATOR_SPLIT.md and the current context/decisions.

- MTA-End-of-P2 / baseline / standalone: use the mta-end-of-p2 skill.
- Piprunner + MTA-End-of-P2 / additional Williams Fractal confirmation: use piprunner-mta-end-of-p2.
- If the user has not identified a product and the task differs by product, ask which; shared documentation work can continue meanwhile.

If the named skills are not installed, read their repository copies under piprunner/skills/ or the corresponding product requirements documents. Do not treat the old references/strategy-contract.md as the current product decision: it is historical. The user has now CONFIRMED additional fractal confirmation while preserving the entire End-of-P2 sequence for the combined product. Timing and lifecycle details remain OPEN.

The existing UI1.1.0 prototype remains unchanged. This router does not claim either separate indicator or fractal signal has been implemented. Preserve tick entry, retest stop, three-bar expiry, minimum2R, 50%TP1 and runner; do not introduce the original Piprunner one-pip/1R rules.
