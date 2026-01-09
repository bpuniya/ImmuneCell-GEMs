# Model Metadata

Each model should have an entry in `metadata/models.csv`.

## Required fields
- `model_id` (unique)
- `cell_type` (e.g., CD4_Teff, CD4_Treg, Eosinophil)
- `format` (json|mat|xml|sbml)
- `path` (relative to repo root)
- `source` (publication or reconstruction pipeline)
- `organism` (e.g., Homo sapiens)
- `notes` (optional)

## Optional (recommended)
- `donor_id`
- `condition` (healthy, disease, stimulation)
- `tissue`
- `omics_source` (bulk RNA, scRNA, proteomics)
- `reconstruction_tool` (e.g., tINIT, FASTCORE, CORDA)
- `objective` (biomass_rxn_id)
