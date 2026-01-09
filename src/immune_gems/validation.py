from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, List
import cobra
from .media import apply_exchange_bounds
from .simulate import fba

@dataclass
class ValidationOutput:
    test_name: str
    status: str
    objective: float | None
    readouts: Dict[str, float]
    notes: str = ""

def hypoxia_glycolytic_shift(model: cobra.Model) -> ValidationOutput:
    # reduce oxygen uptake to simulate hypoxia
    apply_exchange_bounds(model, {"EX_o2[e]": -1}, strict=False)
    readouts = ["EX_lac_L[e]", "LDH_L", "EX_o2[e]"]
    res = fba(model, fluxes_of_interest=readouts)
    return ValidationOutput(
        test_name="hypoxia_glycolytic_shift",
        status=res.status,
        objective=res.objective_value,
        readouts=res.fluxes,
        notes="Check lactate secretion and LDH flux under reduced O2 uptake."
    )

def glucose_limitation(model: cobra.Model) -> ValidationOutput:
    apply_exchange_bounds(model, {"EX_glc_D[e]": -1}, strict=False)
    readouts = ["EX_lac_L[e]", "EX_glc_D[e]"]
    res = fba(model, fluxes_of_interest=readouts)
    return ValidationOutput(
        test_name="glucose_limitation",
        status=res.status,
        objective=res.objective_value,
        readouts=res.fluxes,
        notes="Check lactate secretion under glucose limitation."
    )

def butyrate_uptake(model: cobra.Model) -> ValidationOutput:
    apply_exchange_bounds(model, {"EX_2hb[e]": -5}, strict=False)
    readouts = ["EX_2hb[e]"]
    res = fba(model, fluxes_of_interest=readouts)
    return ValidationOutput(
        test_name="butyrate_uptake",
        status=res.status,
        objective=res.objective_value,
        readouts=res.fluxes,
        notes="Placeholder for SCFA uptake (adjust exchange IDs as needed)."
    )

TESTS = {
    "hypoxia_glycolytic_shift": hypoxia_glycolytic_shift,
    "glucose_limitation": glucose_limitation,
    "butyrate_uptake": butyrate_uptake,
}
