# PACT Gate 11 — causal findings

The recovered estimates show small, real average-power reductions. The strongest discrepancy is a local peak metric compared with whole-workload mean power. It does not mean that no switching changed.

| Comparison | E % | H8 % | FF Q transitions % | Combinational transitions % | Dynamic estimate % | Dynamic delta µW |
| --- | --- | --- | --- | --- | --- | --- |
| b14_opt C1 / B3T | -0.3574 | -5.6876 | -1.0388 | -0.2000 | -0.2321 | -1.5418 |
| b15_opt C1 / B2 | -1.2667 | -1.6828 | -2.2058 | -1.3505 | -0.8226 | -7.4135 |

**Why did E/H8 improve?** Frozen permutations changed correlated scan loads/responses and induced data activity under wire constraints. H8 changes a source-localized cycle maximum. Search and final routed metrics differ substantially; neither is a direct watt/voltage measure. No new optimizer ran.

**Did modeled activity decrease?** b14 C1 FF-Q transitions: 6,389,951 → 6,323,571; combinational: 66,979,151 → 66,845,222. b15 C1 FF-Q: 22,286,672 → 21,795,076; combinational: 118,675,166 → 117,072,400. These are new reaggregations of frozen zero-delay netlist exports, not new simulations. All 18 architectures' aggregate outcomes remain reported.

**Why is total power change small?** Implemented E falls only 0.27–1.37% in the five power-covered PACT cases. Substantial internal and clock energy lies outside E. Retained b14 density controls leave 208.404 µW at zero nonclock data activity, 31.37% of nominal 664.406 µW. This fixed-model floor includes clock-network and sequential clock-driven internal power; the historical intervention is not a new Gate11 experiment or a universal silicon floor.

**Which contributions dominate?** b14 reference dynamic shares: combinational 54.51%, sequential 26.29%, Clock 19.20%. b15: 35.06%, 39.36%, 25.58%. Internal power is about 51.65%/55.88% of dynamic power. Cell-class percentages and internal/switching percentages are orthogonal and must not be added.

| Design | Native category | Ref internal µW | Ref switching µW | Ref dynamic share % | C1 dynamic delta µW |
| --- | --- | --- | --- | --- | --- |
| b14_opt | Sequential | 143.784 | 30.909 | 26.29 | -0.8577 |
| b14_opt | Combinational | 140.429 | 221.716 | 54.51 | -0.8223 |
| b14_opt | Clock | 58.930 | 68.639 | 19.20 | 0.1382 |
| b15_opt | Sequential | 265.148 | 89.548 | 39.35 | -3.5906 |
| b15_opt | Combinational | 132.400 | 183.610 | 35.06 | -3.4631 |
| b15_opt | Clock | 106.092 | 124.476 | 25.58 | -0.3605 |

**Does extra capacitance explain it?** Only a small design-dependent part. The sole registered factor experiment contradicts a common dominant-offset mechanism. With N counting both transition directions, the analytical ground-plus-pin switching estimate is 0.5×V²×E/T (after fF→F conversion), excluding clock/internal power.

| Design | Variant | Activity / reference E % | Capacitance / reference E % | Offset of activity saving % | Matched reference E % |
| --- | --- | --- | --- | --- | --- |
| b14_opt | B5 | -20.6580 | 0.4277 | 2.0704 | 99.96195 |
| b14_opt | CS_C1 | -0.3529 | -0.0045 | -1.2766 | 100.00000 |
| b14_opt | CS_C3 | -0.2452 | -0.0287 | -11.7152 | 100.00000 |
| b15_opt | B5 | -20.7271 | 0.8123 | 3.9190 | 99.89963 |
| b15_opt | CS_C1 | -1.3705 | 0.1037 | 7.5690 | 100.00000 |
| b15_opt | CS_C2 | -1.3322 | -0.0337 | -2.5322 | 100.00000 |
| b15_opt | CS_C3 | -1.0855 | 0.0741 | 6.8230 | 100.00000 |

**Is a correctable algorithmic weakness demonstrated?** Depth-limited geometry/activity/source-localization prediction has a demonstrated weakness. A broader calibrated model could address engineering mismatch, but Gate11 does not show that a correction changes the qualified feasible frontier or yields a useful new physical benefit.

**Is that weakness distinct from prior work?** Not established. Physical-aware ordering, routing constraints, pattern/response correlations and induced logic switching are established topics. Literature access limits and direct links are in the novelty report.

## H1 — Surrogate objective mismatch: Inconclusive for omitted-combinational causality

Prediction: search E/H4/H8 gains may not predict implemented logic activity or power. Measurement: b14 C2 predicts H8 −9.6995% but implemented H8 rises 4.8490%; b15 C1 predicts H4 −4.2107% but implemented H4 rises 2.6185%. The depth-3 settled search model approximates candidate capacitance and fixes the buffer skeleton; final E includes all mapped settled data-net transitions.

Observed surrogate mismatch is supported, but its specific attribution to omitted combinational switching is not isolated. Supporting evidence: predictor/implemented reversals and attenuation; E omits internal and clock power. Contradiction to a simplistic omission claim: final E already includes combinational nets, and all five power-covered PACT cases reduce both FF-Q and combinational transitions. Implemented E and dynamic estimates move in the same direction. Descriptive r=0.9844 for their five dependent deltas is partly model-coupled, not independent prediction validation.

Confounders: depth coverage, geometry/capacitance approximation, baseline-fixed buffers and routing differ together. Saved H8 diagnostics predate Gate11 and report omitted-region/capacitance errors, but ordered nonlinear substitutions do not uniquely allocate causes. Confidence: high in observed mismatch; limited in assigning it specifically to omitted logic. No new algorithmic correction is validated.

## H2 — Physical capacitance cancels activity: Not Supported as the dominant common explanation

Prediction: positive capacitance contributions counteract activity savings. The registered fixed-factor analysis matches 100% of PACT reference E support. Capacitance helps b14 C1/C3 and b15 C2; it offsets only 7.57%/6.82% of activity-only savings in b15 C1/C3. Unweighted total capacitance is not a reliable attribution.

Supporting evidence: small positive offsets in two b15 cases. Contradiction: negative offsets in three of five PACT comparisons, including both b14 cases. B5 saves about 20% E and 12.6–13.6% dynamic power despite greater scan-path wire cost; its different wire budget prevents treating it as a feasible replacement.

Confounders: exact arithmetic within the saved ground-plus-pin C×N model is not a timing-aware circuit intervention. Coupling, slew, glitches and internal power lie outside the identity; raw SPEF/mapping was not recovered. Confidence: high for saved-model accounting; physical/signoff extension untested.

## H3 — Gains are localized: Supported for peak-versus-average mismatch

Prediction: an improved local maximum need not appreciably change total mean energy. b14 C1 H8 improves 5.6876%, but full-chip maximum per-cycle C×N improves only 0.1967%, E 0.3574%, and average dynamic power 0.2321%. The winning H8 bin contributes 3.59% of reference average dynamic power; its mean dynamic power rises 1.0453%, with the same winning bin 34. b15's winning bin contributes 2.85% and its mean falls 0.9324%.

Supporting evidence: spatial accounting, retained maximum/percentile summaries, persistent clock budgets and the same-bin b14 counterexample. Limit: average bin share does not establish share at the exact peak cycle; a rare local reduction can still matter to a local transient constraint. Cycle-synchronous Liberty power, occupancy and timing-aware activity were not recovered. Confidence: high for local/peak versus whole/mean distinction; physical peak-power and dynamic-IR benefits inconclusive. Activity maps do not prove dynamic IR improvement.

The causal explanation is bounded to the recovered activity-derived model. It does not uniquely establish silicon causality, physical glitches, transient peak power or dynamic IR. Missing raw inputs and the broken qualified runtime prevent a fresh physical reproduction.
