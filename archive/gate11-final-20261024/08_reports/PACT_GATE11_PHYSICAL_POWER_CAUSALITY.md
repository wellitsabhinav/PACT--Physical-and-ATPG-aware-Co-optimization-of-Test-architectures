# PACT Gate 11 — Physical Power Causality

23 October 2026 (Asia/Calcutta). Decision: **NO-GO** for another optimizer stage or a DAC claim under the current evidence; keep PACT frozen. This bounded decision does not imply that scan-power optimization is generally ineffective.

## 1. Executive summary

Recorded gains partially transfer: primary candidates reduce modeled FF/combinational transitions and estimated average power. Effects are small because implemented aggregate E reductions are small, clock/internal power persists, and H8 targets a local cycle maximum rather than workload energy. Search predictions also fail in some coordinates. A dominant capacitance-cancellation mechanism is contradicted in three of five power-covered PACT cases. These results do not establish a distinct new DAC contribution.

| Comparison | E % | H8 % | FF Q transitions % | Combinational transitions % | Dynamic estimate % | Dynamic delta µW |
| --- | --- | --- | --- | --- | --- | --- |
| b14_opt C1 / B3T | -0.3574 | -5.6876 | -1.0388 | -0.2000 | -0.2321 | -1.5418 |
| b15_opt C1 / B2 | -1.2667 | -1.6828 | -2.2058 | -1.3505 | -0.8226 | -7.4135 |

Recovered: 18 Gate09 architecture results, nine net/power export pairs, all 17 Gate10A attempts including three failures, Stage-A tables, evaluator source, selected orders/provenance and 12 end-to-end records. New: hash audits, component aggregation, predictor-transfer comparison, spatial budgets and exactly one registered fixed-factor experiment. Blocked: new matched netlist/VCD/SAIF replay, raw SPEF/routed reproduction, fresh OpenROAD power and timing-aware peak/dynamic-IR analysis.

## 2. Research question

Why do scan activity objectives fail to consistently produce meaningful physical shift-power gains, and is there a nontrivial, potentially novel, solvable DAC mechanism? No objective, order, weight, selection or historical threshold was changed to answer this question.

## 3. Recovered historical evidence

Stage A completion: 19/19 selected and 27/30 indexed architectures qualified; original/portable table checksums and projections pass. Gate09 mixed generalization is recovered at seed 11. b14 C1/C3 scan-path wire changes: +0.043699%/+0.066987%; E −0.357366%/−0.273978%; H8 −5.687626%/−5.732276%. b15 C1/C2/C3 scan-path wire: +1.336176%/+0.896204%/+1.249134%; E −1.266742%/−1.365970%/−1.011480%; H8 −1.682756%/+4.151258%/−1.340455%.

These wire percentages concern the connected scan-path net-length upper bound, including functional branches. Detailed-route total wire is separate: b14 C1 65,969 → 65,933 µm (−0.054571%); b15 C1 110,472 → 110,678 µm (+0.186473%).

For s5378, Stage-A B0 total route is 26,639 µm; qualified P0 totals are 26,655–26,717 µm, corroborating non-improvement for those P0 results. The exact earlier phase1 HPWL raw comparison was not recovered; its reported HPWL gain is not a newly verified measurement.

Gate10A's registered static-PI outcome is unchanged: worst-drop improvements 3/8 µV; no architecture meets ≥1% relative AND ≥100 µV absolute improvement in BOTH worst and p99 drop, plus guardrails. This is a static-PI criterion. No new dynamic-power materiality cutoff is invented.

| Design | Architecture | Scan-path µm | Total route µm | E (fF·transitions) | H8 | Data transitions | Dynamic mW |
| --- | --- | --- | --- | --- | --- | --- | --- |
| b14_opt | B0 | 7737.925 | 66604 | 321614006.551 | 663.024 | 62890111 | MISSING |
| b14_opt | B1 | 7772.815 | 66670 | 318399272.682 | 660.755 | 62355515 | MISSING |
| b14_opt | B2 | 7134.270 | 66004 | 321673617.471 | 709.665 | 63019562 | MISSING |
| b14_opt | B3T | 7128.285 | 65969 | 381238038.670 | 635.554 | 73422428 | 0.664406 |
| b14_opt | B4 | 17740.960 | 76663 | 317798825.640 | 682.424 | 59428676 | MISSING |
| b14_opt | B5 | 8321.800 | 67162 | 304124378.781 | 680.607 | 58941540 | 0.573919 |
| b14_opt | CS_C1 | 7131.400 | 65933 | 379875624.242 | 599.406 | 73221563 | 0.662864 |
| b14_opt | CS_C2 | 7192.955 | 65994 | 374669100.998 | 666.372 | 72229562 | MISSING |
| b14_opt | CS_C3 | 7133.060 | 66011 | 380193530.162 | 599.122 | 73310251 | 0.663400 |
| b15_opt | B0 | 22724.085 | 112514 | 722000716.372 | 756.854 | 134218936 | MISSING |
| b15_opt | B1 | 21667.565 | 111376 | 769712632.615 | 738.816 | 141072375 | MISSING |
| b15_opt | B2 | 20788.795 | 110472 | 762723552.495 | 724.461 | 141064234 | 0.901273 |
| b15_opt | B3T | 20996.255 | 110684 | 850179717.043 | 693.367 | 154665972 | MISSING |
| b15_opt | B4 | 37422.085 | 127078 | 675469434.621 | 699.184 | 113095828 | MISSING |
| b15_opt | B5 | 23782.035 | 113356 | 610729605.623 | 720.438 | 110973429 | 0.787930 |
| b15_opt | CS_C1 | 21066.570 | 110678 | 753061810.773 | 712.270 | 138967476 | 0.893860 |
| b15_opt | CS_C2 | 20975.105 | 110596 | 752304978.541 | 754.535 | 139047618 | 0.894651 |
| b15_opt | CS_C3 | 21048.475 | 110651 | 755008752.684 | 714.750 | 139418764 | 0.895762 |

## 4. Experimental methodology

Recover selected regular files only from existing F: archives, checking container and member SHA-256. Use a fresh output namespace. Freeze the historical Gate10A power selection before new comparisons. Recompute per-net totals and classify sources from the recovered Liberty sequential definitions and exported instance/pin identities. Independently sum per-instance power and compare to frozen totals; native cell-category aggregates are separate because they use binary32 reduction.

Existing Windows Python 3.12.5 and installed analysis packages were reused. No install, build, search, ATPG, placement, route, extraction or simulation was run. The sole optional experiment was registered before factor swaps in `07_hypothesis/followup_01_preregistration.md`. Actual resources: 1.500 s wall, 1.406 s CPU, 69.60 MiB peak working set, 18,429 bytes workspace growth including logs/manifest.

## 5. Baseline fairness and provenance

Include all nine historical power records unchanged: b14 B3T/C1/C3/B5; b15 B2/C1/C2/C3/B5. b14 C2's adverse H8 result and every B0/B1/B2/B3T/B4/B5 result remain in the 18-row table. Missing power is blank. The subset is inherited from the prior user-frozen Gate10A population, not Gate11 outcome selection.

Fairness receipts match source netlist/FF identities/placement/coordinates, patterns, K=2, seed 11, endpoint policy, constraints, simulation models and common backend/extraction settings within design. b14: 245 FFs, chains 123/122, 453 patterns, 111,438 shift cycles. b15: 449 FFs, chains 225/224, 464 patterns, 208,800 shift cycles. The earlier invalid b14 446-pattern attempt is not reused. Coverage concerns the frozen mapped-source collapsed-fault universe, not new post-route buffer faults.

Use Nangate45 typical, 1.1 V, period 10 ns (100 MHz), clock duty50%, nonclock assumed duty0.5, scan enable asserted. Windows cover identical load/unload shifting, excluding setup/capture. No gain is attributed to fewer equivalent shift cycles.


- Recovered source snapshot: archived main worktree HEAD `e84f4afbf04a918060b4ad845f5166d8e6c7b92c`, from preserved Git audit G005. Selective regular-file restoration, not a full Git clone; original member hashes identify the actual bytes.
- Gate09 PACT SHA `71b059d9d1a00735d79b6a428693eaba549a5f33`; b14 comparison implementation SHA `e43da79d76d363fe67ae120d5e53a3c2d04a9a2f44549601d8df2daabc05cf3e`. Row-specific provenance is retained separately.
- Gate10A parent `53ebab37fd76970d7c5e676b0caec13c7c16296e`; preregistration `b9869834a3479a57f256c83fa74a4617faab4af2`.
- Common OpenROAD `08f67ee5ecd14db5a42be8c610bbfd1ccf079299`, version `26Q2-1164-g08f67ee5ec`, binary SHA-256 `fcd7dcfc37d329bd43a7ede75805319a2e70e6879da11d42b4fd1c2e50e645c3`.
- ORFS `5e8b1450d19263f797a27c4f371b9dd19f32a3aa`; declared embedded OpenSTA `76c4d6df3537ccce331b5caa812196c3330ba7c4`. Supporting OpenROAD source `dc5eee77c45dba8e5ace2fc89c38c6d9a4ed6e0f` differs from the binary. Standalone STA 3.1.0 was not the power engine.
- FAN_ATPG base `26b2b36c0e9db11a4b6d9e759df6e44357121f39`; qualified repair `4c253bfa613e5827f17c42a5fce8be7bea779e1e`.
- I99T sources `8a2c3b500ee7ff20e7031de92592b737bedc6d8c`.
- Nangate45 typical Liberty SHA-256 `8d540a4d4cf6d09d27c87ad067857a9c0c2eeb023ab7a56e058cd3113db4e9b1`; exact library/RC bytes recovered and verified.

B0 uses source order; B1 native placed greedy; B2 endpoint-inclusive Manhattan 2-opt (`6fff875551fe13a2aae3a22f871a6ca7f8d5c1cf`); B3T patched partitioned directed scan-pin ordering (`5c3751171685d507939ee7064a67feec786e5219`); B4 activity-disagreement greedy; B5 fixed 0.5/0.5 geometry/activity greedy. Generation commits differ from the common qualification backend.

## 6. Netlist-level activity

Exact CPU backend `icarus_vpi_settled_counts_v1` records compact uint8 net/cycle settled timestamp counts with completeness/overflow/unknown checks. Source fails unknown active nets/transitions; setup uses an unmeasured marker. Historical FF-Q crosschecks cover every physical FF/cycle against independent simultaneous chain replay. Timestamp settling is zero-delay, not glitch-accurate physical activity.

All nine exported FF-Q populations equal selected counts (245/449). Every net source maps to an instance/pin or explicit PORT source. The scan-data scope includes buffers/ports and differs from strict FF-Q counts. Raw logical/physical maps/patterns are missing, so logical-workload equivalence is receipt-supported rather than freshly replayed. Complete-count validation is a recovered historical record, not a new read of absent payloads. No new initialization, X-state or high-occupancy qualification is claimed.

| Design | Variant | Search ΔE % | Implemented ΔE % | Search ΔH8 % | Implemented ΔH8 % |
| --- | --- | --- | --- | --- | --- |
| b14_opt | CS_C1 | -1.5495 | -0.3574 | -11.4659 | -5.6876 |
| b14_opt | CS_C2 | -3.5473 | -1.7231 | -9.6995 | 4.8490 |
| b14_opt | CS_C3 | -1.3835 | -0.2740 | -11.4659 | -5.7323 |
| b15_opt | CS_C1 | -1.5436 | -1.2667 | -0.1036 | -1.6828 |
| b15_opt | CS_C2 | -1.7467 | -1.3660 | 0.3536 | 4.1513 |
| b15_opt | CS_C3 | -1.1906 | -1.0115 | -0.1036 | -1.3405 |

Implemented E sums mapped ground-plus-pin activity. Search E is a depth 3 candidate-capacitance surrogate; their absolute magnitudes are different models, not two energies. Deltas use each model's own reference. b14 C2 H8 and b15 C1/C3 H4 reversals prove transfer weakness without uniquely attributing it to depth or routing.

For the five power-covered PACT variants, implemented ΔE correlates descriptively with ΔFF-Q transitions (r0.9967), Δcombinational transitions (r0.9898) and Δdynamic estimate (r0.9844). ΔH8 does not order average-power effects consistently (r−0.7985). These five rows share two designs/references, one seed and common activity inputs; no independent-sample inference or confidence interval is justified.

## 7. Routed parasitic/power analysis

Historical receipts bind detailed-route OpenRCX SPEF/ODB, and saved logs/scripts read them. Recovered CSVs carry extracted ground, incident coupling and Liberty pin capacitance. Ground-plus-pin values reproduce all frozen E totals. Raw SPEF/ODB is absent, so this verifies export provenance/arithmetic, not a fresh extraction.

Power is embedded OpenSTA internal plus switching; leakage is separate. Instance total power feeds static PDNSim. Native Sequential/Combinational/Clock categories are observable below. The Clock category is not all clock-driven energy: sequential internal power also contains clock-driven components.

| Design | Native category | Ref internal µW | Ref switching µW | Ref dynamic share % | C1 dynamic delta µW |
| --- | --- | --- | --- | --- | --- |
| b14_opt | Sequential | 143.784 | 30.909 | 26.29 | -0.8577 |
| b14_opt | Combinational | 140.429 | 221.716 | 54.51 | -0.8223 |
| b14_opt | Clock | 58.930 | 68.639 | 19.20 | 0.1382 |
| b15_opt | Sequential | 265.148 | 89.548 | 39.35 | -3.5906 |
| b15_opt | Combinational | 132.400 | 183.610 | 35.06 | -3.4631 |
| b15_opt | Clock | 106.092 | 124.476 | 25.58 | -0.3605 |

b14 C1's Clock category grows0.1382 µW and offsets part of sequential/combinational savings; b15 Clock falls0.3605 µW. Internal power is not αCV²f. Incident coupling sums may count each physical coupling from both incident nets; no qualified coupling-switching energy is inferred from their sum.

Analytical ground-plus-pin data switching: P=0.5×V²×E×10⁻¹⁵/T because N counts both transition directions, equivalent to α₀₁CV²f for charge events/cycle. This excludes clock/internal/coupling/hazard energy and is not a new power-tool result. Workload dynamic energy estimates P×T: b14 reference/C1 0.740401/0.738683 µJ; b15 1.881859/1.866379 µJ. Workload durations match exactly.

No matched ideal-versus-routed power comparison was recovered. No transient peak-window power/current, dynamic IR, ground bounce, thermal or signoff result is invented. Averaged counts at fixed duty cannot supply those quantities.

## 8. H1/H2/H3 results

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

### Registered factor accounting

| Design | Variant | Activity / reference E % | Capacitance / reference E % | Offset of activity saving % | Matched reference E % |
| --- | --- | --- | --- | --- | --- |
| b14_opt | B5 | -20.6580 | 0.4277 | 2.0704 | 99.96195 |
| b14_opt | CS_C1 | -0.3529 | -0.0045 | -1.2766 | 100.00000 |
| b14_opt | CS_C3 | -0.2452 | -0.0287 | -11.7152 | 100.00000 |
| b15_opt | B5 | -20.7271 | 0.8123 | 3.9190 | 99.89963 |
| b15_opt | CS_C1 | -1.3705 | 0.1037 | 7.5690 | 100.00000 |
| b15_opt | CS_C2 | -1.3322 | -0.0337 | -2.5322 | 100.00000 |
| b15_opt | CS_C3 | -1.0855 | 0.0741 | 6.8230 | 100.00000 |

PACT support matches 100%; B5 retains >99.89% reference E with explicit unmatched residuals. The symmetric product decomposition reproduces ΔE up to roundoff without choosing an attribution order. It does not solve nonlinear H8 maximum attribution.

### Spatial budget

| Design | H8 bin | Ref mean dynamic share % | Same-bin mean dynamic Δ% | H8 maximum Δ% |
| --- | --- | --- | --- | --- |
| b14_opt | 34 | 3.5883 | 1.0453 | -5.6876 |
| b15_opt | 35 | 2.8499 | -0.9324 | -1.6828 |

Per-net/cell distributions, top 1%/10% contributions and all 4×4/8×8 bins are retained. Rank fractions are descriptive, not success thresholds. Historical maxima/p95/p99 cycle summaries are recovered; without raw cycle rows, overlap/duration of exact high-power events cannot be reconstructed.

## 9. Contradictions and failure cases

- b14 C2 search H8 improves while implemented H8 worsens; its missing power export remains blank.
- b15 C2 has the largest implemented E gain but worsens H8; C1 has the larger average-power estimate gain.
- b14 C1's same winning H8 bin has higher mean power despite lower H8.
- B5 reduces estimated dynamic power13.6192%/12.5759%, showing that the flow can register larger modeled effects, but increases scan-path wire16.7434%/14.3983%. It is not an equal-wire-budget replacement.
- All17 Gate10A attempts include three implementation/qualification failures. Invalid earlier nominal implementations are not independent scientific samples.
- New blockers/failures: WSL cannot mount its missing configured disk; optimizer verifier fails on absent Numba. Two new accounting attempts stopped on PORT naming and method/candidate schema assertions. Failed sources/logs remain; corrected analysis passes without model/selection changes. Report packaging also hit a Windows command-length limit before process creation and was split into bounded writes.

## 10. Statistical/modeling limitations

Only seed 11 has matched b14/b15 power data. No independent seed variation, significance or confidence interval is reported. Related families and one technology cannot establish industrial generalization. Identical historical nominal repeats show numerical repeatability, not calibrated physical accuracy. Native float reduction errors are checked separately from scientific materiality. Fixed duty, unavailable occupancy, state/slew approximations, missing glitches and coupling validation remain uncalibrated; observed deltas exceed arithmetic roundoff but are not shown to exceed physical-model uncertainty.

The historical static-IR threshold is preserved. No new sub1% power cutoff is imposed. NO-GO reflects absent distinct mechanism/correction/benefit under this evidence, not a theorem that every fractional-percent saving is valueless.

## 11. Scientific interpretation

Two transfer boundaries matter: the search surrogate sometimes mispredicts implemented weighted switching; then modest data-activity gains are diluted by persistent clock/internal budgets. A local maximum can improve while the same bin's mean energy rises. Capacitance creates a small inconsistent offset. This explains the recovered model without uniquely establishing real-silicon causality.

## 12. Potential novel claims

A validated permutation-to-time-resolved physical-power predictor controlling clock/internal/load/hazard effects could be a research question. No new predictor, optimizer, independent circuit intervention or held-out physical validation was demonstrated. Adding capacitance weighting (already in E) or recognizing logic switching (already in final counts) is not an achieved new contribution.

## 13. DAC relevance

`PACT_GATE11_DAC_NOVELTY.md` provides primary-source checks/access limits. Routing-aware ordering, explicit routability constraints, pattern/response correlation and induced switching have substantial prior art. This is useful negative-result/reproducibility evidence; a distinct DAC-level advance is not established. The literature review is targeted, not exhaustive.

## 14. Final decision

**NO-GO. Preserve artifacts and keep PACT optimizer development frozen.** Recovered failures are known approximation/budget/localization limitations without a demonstrated novel correction. Missing raw/runtime evidence is not positive evidence and blocks stronger causal/signoff conclusions. No new sweep, optimizer or architecture is justified.

If independent verification is later authorized, first recover exact b14 B3T/C1 routed netlists, ODB/SPEF/SDC, identity maps, qualified 453-pattern workload, stimulus, full traces and the qualified binary; verify hashes, then replay that one pair with measured duty and cycle-synchronous activity/power. Timing-aware extension is required before physical peak/glitch/dynamic-IR claims. This is a prerequisite, not an authorized optimization campaign or evidence that one pair establishes novelty.

See `PACT_GATE11_REPRODUCIBILITY.md` for artifact locations and the final storage audit for disk totals/system-level caveats.
