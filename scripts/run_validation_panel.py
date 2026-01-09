#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

from immune_gems.io import load_model
from immune_gems.media import load_media, apply_exchange_bounds
from immune_gems.validation import TESTS

def main():
    ap = argparse.ArgumentParser(description="Run validation tests for immune-cell GEMs.")
    ap.add_argument("--model_path", type=str, help="Path to a model file (.json/.xml/.mat). If omitted, uses metadata/models.csv with --model_id.")
    ap.add_argument("--model_id", type=str, help="Model ID from metadata/models.csv (alternative to --model_path).")
    ap.add_argument("--media", type=str, default="base", help="Media name (base, hypoxia, glucose_low, butyrate_uptake)")
    ap.add_argument("--tests", type=str, default="hypoxia_glycolytic_shift,glucose_limitation,butyrate_uptake", help="Comma-separated tests.")
    ap.add_argument("--outdir", type=str, default="results", help="Output directory.")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    outdir = root / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    if args.model_path:
        model_path = Path(args.model_path)
        model_id = model_path.stem
    else:
        if not args.model_id:
            raise SystemExit("Provide --model_path or --model_id")
        meta = pd.read_csv(root / "metadata" / "models.csv")
        row = meta.loc[meta["model_id"] == args.model_id]
        if row.empty:
            raise SystemExit(f"model_id not found: {args.model_id}")
        model_path = root / row.iloc[0]["path"]
        model_id = args.model_id

    model = load_model(model_path)

    # Apply base media first, then overlay selected media
    base_media = load_media(root / "metadata" / "media" / "base.json")
    apply_exchange_bounds(model, base_media.get("exchange_bounds", {}), strict=False)

    if args.media and args.media != "base":
        media_obj = load_media(root / "metadata" / "media" / f"{args.media}.json")
        apply_exchange_bounds(model, media_obj.get("exchange_bounds", {}), strict=False)

    selected_tests = [t.strip() for t in args.tests.split(",") if t.strip()]
    records = []
    for t in selected_tests:
        if t not in TESTS:
            raise SystemExit(f"Unknown test: {t}. Available: {list(TESTS)}")
        # copy model for each test to avoid side effects
        m = model.copy()
        out = TESTS[t](m)
        rec = {"model_id": model_id, "media": args.media, "test": out.test_name, "status": out.status, "objective": out.objective, **{f"readout__{k}": v for k, v in out.readouts.items()}, "notes": out.notes}
        records.append(rec)

    df = pd.DataFrame.from_records(records)
    outfile = outdir / f"{model_id}__{args.media}__validation.csv"
    df.to_csv(outfile, index=False)
    print(f"Wrote: {outfile}")

if __name__ == "__main__":
    main()
