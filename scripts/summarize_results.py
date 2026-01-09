#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

def main():
    ap = argparse.ArgumentParser(description="Summarize validation result CSVs into one table.")
    ap.add_argument("--results_dir", type=str, default="results")
    ap.add_argument("--out", type=str, default="results/summary.csv")
    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    rdir = root / args.results_dir
    files = sorted(rdir.glob("*.csv"))
    if not files:
        raise SystemExit(f"No result CSVs found in {rdir}")

    dfs = [pd.read_csv(f) for f in files]
    out = pd.concat(dfs, ignore_index=True)
    out_path = root / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    print(f"Wrote: {out_path}")

if __name__ == "__main__":
    main()
