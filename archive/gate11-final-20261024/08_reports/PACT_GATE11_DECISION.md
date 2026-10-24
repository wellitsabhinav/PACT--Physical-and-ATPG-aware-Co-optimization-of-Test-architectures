# PACT Gate 11 decision

Classification: **NO-GO**

Preserve research artifacts and keep PACT optimizer development frozen. A credible distinct DAC contribution is not established.

| Comparison | E % | H8 % | FF Q transitions % | Combinational transitions % | Dynamic estimate % | Dynamic delta µW |
| --- | --- | --- | --- | --- | --- | --- |
| b14_opt C1 / B3T | -0.3574 | -5.6876 | -1.0388 | -0.2000 | -0.2321 | -1.5418 |
| b15_opt C1 / B2 | -1.2667 | -1.6828 | -2.2058 | -1.3505 | -0.8226 | -7.4135 |

## Exact supporting evidence

1. `03_activity/predictor_implemented_transfer.csv`: b14 C2 predicted H8−9.6995% becomes implemented+4.8490%. Approximation/coverage/physical-transfer weakness is demonstrated, but no new solution.
2. `03_activity/source_class_activity.csv` and `04_power/native_power_components.csv`: real modeled scan/logic reductions remain small; clock/internal budgets persist. Retained b14 density-zero control leaves31.37% of nominal dynamic power.
3. `06_causality/followup_01_factor_accounting.csv`: capacitance helps both b14 PACT cases; b15 C1's positive capacitance term offsets7.57% of activity-only savings. Dominant common capacitance cancellation is not supported.
4. `06_causality/spatial_budget.csv`: b14 H8 improves5.6876% while the same bin's mean dynamic power rises1.0453%; local maxima are not mean total power.
5. Frozen Gate10A static-PI criteria fail. Primary dynamic differences remain fixed-duty estimates, without new timing-aware/transient/signoff measurements or a newly imposed materiality cutoff.
6. `PACT_GATE11_DAC_NOVELTY.md`: overlapping physical/routing/correlation methods exist; a distinct validated correction is absent.

## Confidence and work status

Confidence is strong for recovered-output accounting and the bounded freeze recommendation; limited for unique silicon causes/generalization. H1: Inconclusive for the specific omitted-combinational cause; prediction mismatch is observed. H2: Not Supported as dominant common cause. H3: Supported for local/peak versus mean/total mismatch. Timing-aware physical causality remains unresolved.

Completed: archive/member/retained hash checks; 12-record end-to-end verifier; all 18 activity/route rows; nine net/power reaggregations and seven available comparisons; one preregistered factor experiment; literature overlap check; reports and versioned reproduction helper.

Blocked: exact raw b14/b15 patterns/netlists/counts/SPEF, new simulation/duty occupancy, qualified OpenROAD runtime, ideal/routed rerun, physical peak and dynamic IR. WSL disk paths are missing; Numba is absent for the separate optimizer verifier. Missing evidence is never scored as positive.

Smallest prerequisite for reopening: recover/hash the exact b14 B3T/C1 workload/maps/routed inputs/traces and qualified runtime, then validate occupancy/time-resolved power for that pair under a new registration. No optimizer change is warranted beforehand. Missing bindings: `00_audit/required_binding_recovery.json`.
