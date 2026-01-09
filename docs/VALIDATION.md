# Validation Panels

This repo uses **portable, qualitative validation tests** designed to work across immune-cell GEMs.

## Core panels

### 1) Hypoxia glycolytic shift
- **Perturbation:** reduce oxygen uptake (e.g., set lower bound to -1 instead of -50)
- **Readout:** lactate secretion, glycolysis fluxes (e.g., LDH), biomass/ATP proxy
- **Expectation:** lactate secretion and/or glycolytic flux increases (context-dependent), with reduced OXPHOS capacity

### 2) Glucose limitation
- **Perturbation:** reduce glucose uptake bound
- **Readout:** lactate secretion, PPP, FAO compensation
- **Expectation:** reduced lactate and increased reliance on alternative fuels if available

### 3) Butyrate / SCFA uptake
- **Perturbation:** allow butyrate uptake and check growth/ATP and effector-related proxies
- **Readout:** uptake rates, acetate secretion, TCA flux changes
- **Expectation:** model-specific; document expected direction in `metadata/phenotypes/`

---

## Adding a new validation test
1) Add a new JSON under `metadata/media/` if a new condition is needed.
2) Add a new function under `src/immune_gems/validation.py`.
3) Add it to `scripts/run_validation_panel.py`.
4) Add a short notebook in `notebooks/` that generates at least one figure or table.
