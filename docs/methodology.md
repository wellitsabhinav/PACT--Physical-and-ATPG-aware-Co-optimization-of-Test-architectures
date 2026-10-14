# Methodology

PACT tests three separate hypotheses: proxy improvement, implemented transfer and downstream physical impact. The first two produced measured tradeoffs; the final registered static-PI study did not establish material benefit. The project is [frozen](research_status.md).

| Read | Defines |
|---|---|
| [Objectives and schedules](methodology/objectives.md) | HPWL/routed wire, E/H4/H8, epsilon, M3/M5 versus implementation-aware schedules |
| [Candidate physical model](methodology/physical_model.md) | Shared-net capacitance/geometry, bounded logic, source-localized peaks and known errors |
| [ATPG and replay](methodology/atpg.md) | Pattern/FF identities, serial semantics and fault-equivalence scope |
| [Search and selection](methodology/search.md) | Legal mutations, independent lanes, budgets and saved endpoints |
| [Qualification](methodology/qualification.md) | Topology, functional connectivity, DRC, timing and downstream gates |
| [Static power/IR methodology](../reports/gate10a/methodology.md) | Frozen activity-derived power, fixed-duty and supply assumptions |

[Canonical evidence](reproduction/canonical_results.md) maps each claim to exact files. [Negative findings](experiments/negative_results.md) explain failed transfer and downstream materiality without treating proxy improvements as physical signoff.
