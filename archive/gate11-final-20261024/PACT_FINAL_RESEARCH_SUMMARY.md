# PACT final research summary
Classification: **PACT_GATE11_NO_GO**. Development frozen. These are Gate11 recovered-output findings within that gate's limitations.

| Frozen comparison | E change | H8 change | Modeled dynamic power change |
|---|---:|---:|---:|
| b14_opt C1/B3T | -0.3574% | -5.6876% | -0.2321% |
| b15_opt C1/B2 | -1.2667% | -1.6828% | -0.8226% |

Use the preserved Gate11 report for exact E/H8 definitions and workload/population bindings. E/H8 are intermediate activity metrics; the power column is a fixed-duty model estimate, not measured silicon power.

Completed findings: a meaningful predictor/implementation discrepancy exists in at least one b14 comparison (C2 predicted H8 -9.6995%, implemented +4.8490%). Local hotspot reductions did not produce material overall power savings. Common dominant capacitance cancellation was not established. Gate11 factor accounting says capacitance helps both b14 PACT cases; b15 C1's positive capacitance term offsets7.57% of activity-only savings. A distinct experimentally validated DAC contribution did not emerge. Gate10A's frozen criteria failed; no new cutoff is introduced.

Completed evidence work includes archive/retained hashes, the12-record end-to-end verifier,18 activity/route accounting rows, nine net/power reaggregations, seven available comparisons and the preregistered factor accounting. These are recovered-output accounting/verification, not new routed experiments.

Unresolved: exact missing raw workloads/traces/maps/netlists/SPEF and qualified runtime; timing-aware occupancy/glitches and physical causality; time-resolved peak power and dynamic IR-drop. No transient, thermal, EM, silicon or industrial signoff result is established. Numerical optimizer replay remained blocked by absent Numba; a passing end-to-end verifier does not remove that blocker.

Authority: Gate11/08_reports/PACT_GATE11_DECISION.md, PACT_GATE11_PHYSICAL_POWER_CAUSALITY.md, PACT_GATE11_CAUSAL_FINDINGS.md, PACT_GATE11_DAC_NOVELTY.md, PACT_GATE11_RESULTS.csv and its metadata. They are copied byte-for-byte and remain the detailed scientific record.
