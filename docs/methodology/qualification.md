# Qualification and scientific scope

Legal transformations preserve each FF exactly once, clock domains, chain capacities and fixed SI/SO endpoints. Reconstructed SI-to-SO traversal must contain no cycles, forks or orphans. Canonical order, OpenDB metadata and exported Verilog must agree; functional D/CK/Q/QN connectivity is preserved as applicable.

Selected physical implementations require independent workload/FF-transition checks, zero recorded detailed-route DRC and available nonnegative global-route setup/hold values. Global-route WNS is not detailed-route timing signoff. Search HPWL feasibility and routed wire-budget acceptance are separate checks.

The [end-to-end gate](../../results/pact_end_to_end_20261004/REPORT.md) compares complete FAN collapsed stuck-at fault-class identities, multiplicities and detected identities on the same original functional circuit/library. Individual uncollapsed class members were not enumerated. Post-route inserted buffers are not new source fault targets.

Static power-integrity qualification is separate from these correctness gates. [Gate 10A](../../reports/gate10a/report.md) qualifies nine frozen architectures but finds no material static-PI benefit under its registered thresholds. Neither an activity win nor a correctness pass establishes transient/thermal or signoff benefit. [Final limitations](../experiments/negative_results.md).
