from __future__ import annotations
from pathlib import Path
from typing import Optional
import cobra

def load_model(path: str | Path) -> cobra.Model:
    """Load a COBRA model from .json, .xml/.sbml, or .mat (if supported by cobra)."""
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".json":
        return cobra.io.load_json_model(str(path))
    if suffix in {".xml", ".sbml"}:
        return cobra.io.read_sbml_model(str(path))
    if suffix == ".mat":
        # cobra supports MATLAB .mat for some formats; otherwise users can convert to JSON.
        return cobra.io.load_matlab_model(str(path))
    raise ValueError(f"Unsupported model format: {suffix} ({path})")
