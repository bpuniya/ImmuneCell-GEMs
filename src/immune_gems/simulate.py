from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Dict, Any
import cobra

@dataclass
class SimulationResult:
    status: str
    objective_value: float | None
    fluxes: Dict[str, float]

def fba(model: cobra.Model, objective: Optional[str] = None, fluxes_of_interest: Optional[list[str]] = None) -> SimulationResult:
    if objective:
        model.objective = objective
    sol = model.optimize()
    fluxes = {}
    if fluxes_of_interest:
        for rid in fluxes_of_interest:
            if rid in model.reactions:
                fluxes[rid] = float(sol.fluxes.get(rid, 0.0))
            else:
                fluxes[rid] = float("nan")
    return SimulationResult(status=str(sol.status), objective_value=(float(sol.objective_value) if sol.objective_value is not None else None), fluxes=fluxes)
