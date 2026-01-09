# ImmuneCell-GEMs

A curated, standardized collection of **immune cell genome-scale metabolic models (GEMs)** with **reproducible media constraints**, **validation notebooks**, and **benchmark scripts**.

> Goal: make it easy to run *the same* simulation/validation workflow across multiple immune cell types and donors—without spending days normalizing models.

---

## Repository layout

- `models/`  
  Place model files here (recommended: `.json` or `.mat`; `.xml` supported). Organize by cell type:
  - `models/CD4_Teff/`
  - `models/CD4_Treg/`
  - `models/CD8_Naive/`
  - `models/Eosinophil/`
  - etc.

- `metadata/`  
  Model metadata and provenance:
  - `metadata/models.csv` (one row per model)
  - `metadata/media/` (media definitions)
  - `metadata/phenotypes/` (expected qualitative behaviors)

- `scripts/`  
  Command-line utilities (Python):
  - standardize exchange bounds (media)
  - run FBA/FVA
  - run validation panels and write results

- `notebooks/`  
  Reproducible figure notebooks (Jupyter).

- `src/immune_gems/`  
  Minimal Python package used by scripts & notebooks.

---

## Quickstart (Python)

### 1) Create environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Add models
Put model files under `models/<CELL_TYPE>/...` (see `metadata/models.csv` for expected fields).

### 3) Run a basic validation panel
```bash
python scripts/run_validation_panel.py --cell_type Eosinophil --media hypoxia
```

### 4) Generate a summary table
```bash
python scripts/summarize_results.py --results_dir results
```

---

## Media definitions
Media are stored as JSON under `metadata/media/` and applied consistently across models:
- `base.json`
- `hypoxia.json`
- `glucose_low.json`
- `fatty_acid_oxidation.json`
- `butyrate_uptake.json`

---

## What “validation” means here
Validation is deliberately designed to be **portable** across models and to generate outputs that are useful for:
- papers (supplemental tables)
- teaching modules
- interview figures (heatmaps, pathway flux changes)

Each validation test includes:
1) **the perturbation** (e.g., O2 uptake reduced)  
2) **the readout** (e.g., lactate secretion, glycolysis flux)  
3) **the expectation** (qualitative direction + rationale)

See `docs/VALIDATION.md`.

---

## Citing
If you use this repository, please cite the corresponding paper/software release.

See `CITATION.cff`.

---

## License
MIT (see `LICENSE`).
