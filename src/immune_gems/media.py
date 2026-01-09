from __future__ import annotations
from pathlib import Path
from typing import Dict, Any
import json
import cobra

def load_media(media_path: str | Path) -> Dict[str, Any]:
    media_path = Path(media_path)
    with media_path.open("r", encoding="utf-8") as f:
        return json.load(f)

def apply_exchange_bounds(model: cobra.Model, exchange_bounds: Dict[str, float], strict: bool = False) -> cobra.Model:
    """Apply exchange lower bounds. Negative means uptake allowed.

    If strict=True, raises when an exchange rxn is missing.
    """
    for rxn_id, lb in exchange_bounds.items():
        if rxn_id not in model.reactions:
            if strict:
                raise KeyError(f"Reaction not found in model: {rxn_id}")
            continue
        rxn = model.reactions.get_by_id(rxn_id)
        rxn.lower_bound = float(lb)
    return model
