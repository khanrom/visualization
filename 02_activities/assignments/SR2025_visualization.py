from __future__ import annotations

import re
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# ---------------------------
# 1) CSV loader
# ---------------------------
COLS = [
    "Creation Date",
    "Status",
    "First 3 Chars of Postal Code",
    "Intersection Street 1",
    "Intersection Street 2",
    "Ward",
    "Service Request Type",
    "Division",
    "Section",
]

def read_sr2025(path: str | Path) -> pd.DataFrame:
    """
    SR2025.csv has some unquoted commas inside the Division field (e.g., 'Environment, Climate & Forestry'),
    which causes ordinary CSV parsing to fail. This loader merges any extra comma-split fields back into
    the Division column and keeps the last field as Section.
    """
    path = Path(path)
    rows = []

    with path.open("r", encoding="utf-8", errors="replace") as f:
        header = f.readline()  # discard; we trust COLS
        for line in f:
            line = line.rstrip("\n")
            parts = line.split(",")

            if len(parts) == 9:
                rows.append(parts)
            elif len(parts) > 9:
                # First 7 fields are stable; join the middle into Division; last is Section
                fixed = parts[:7] + [",".join(parts[7:-1]).strip()] + [parts[-1]]
                rows.append(fixed)
            else:
                # Rare; pad missing trailing fields
                rows.append(parts + [""] * (9 - len(parts)))

    df = pd.DataFrame(rows, columns=COLS)

    # types
    df["Creation Date"] = pd.to_datetime(df["Creation Date"], errors="coerce")
    df["Ward Num"] = df["Ward"].str.extract(r"\((\d+)\)").astype("float")
    df["Ward Name"] = df["Ward"].str.replace(r"\s*\(\d+\)\s*$", "", regex=True).str.strip()
    df["Month"] = df["Creation Date"].dt.to_period("M").dt.to_timestamp()

    return df


# ---------------------------
# 2) Filters / helpers
# ---------------------------
INFRA_DIVISIONS = {
    "Transportation Services",
    "Toronto Water",
    "Solid Waste Management Services",
    "Environment, Climate & Forestry",
    "Parks and Recreation",
}

def filter_infrastructure(df: pd.DataFrame) -> pd.DataFrame:
    infra = df[df["Division"].isin(INFRA_DIVISIONS)].copy()

    # Keep only rows with essentials present
    infra = infra.dropna(subset=["Creation Date", "Ward", "Service Request Type", "Month"])
    return infra


# ---------------------------
# 3) Viz 1: Monthly time series for top infra request types
# ---------------------------
def plot_viz1_time_series(infra: pd.DataFrame, outpath: str | Path, top_k: int = 8) -> None:
    # Top K service request types within infrastructure
    top_types = infra["Service Request Type"].value_counts().head(top_k).index

    monthly = (
        infra[infra["Service Request Type"].isin(top_types)]
        .groupby(["Month", "Service Request Type"])
        .size()
        .reset_index(name="n")
    )

    total = infra.groupby("Month").size().reset_index(name="total_infra")

    plt.figure(figsize=(12, 6))
    ax = plt.gca()

    # Total line (thin, unobtrusive)
    ax.plot(total["Month"], total["total_infra"], linewidth=1.5, label="Total infrastructure requests")

    # Category lines
    for sr_type in top_types:
        sub = monthly[monthly["Service Request Type"] == sr_type]
        ax.plot(sub["Month"], sub["n"], linewidth=1.5, label=sr_type)

    ax.set_title("Toronto 311 (2025): Monthly Infrastructure Requests (Top Categories)")
    ax.set_xlabel("Month (2025)")
    ax.set_ylabel("Number of requests")
    # Log scale (use log1p if zeros are possible)
    ax.set_yscale("log")

    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), borderaxespad=0)

    # Improve legibility
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), borderaxespad=0)
    plt.tight_layout()

    outpath = Path(outpath)
    outpath.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outpath, dpi=300)
    plt.close()



# ---------------------------
# 4) Run
# ---------------------------
if __name__ == "__main__":
    df = read_sr2025("02_activities/assignments/SR2025.csv")
    infra = filter_infrastructure(df)

    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    viz2_long = (
    infra.groupby(["Ward", "Service Request Type"])
         .size()
         .reset_index(name="n")
)
    top_types = infra["Service Request Type"].value_counts().head(10).index
    viz2_long = viz2_long[viz2_long["Service Request Type"].isin(top_types)]
    viz2_long["n"] = viz2_long["n"].astype(int)
    viz2_long.to_csv(out_dir / "viz2_ward_category_long.csv", index=False)
    print("Wrote data/processed/viz2_ward_category_long.csv")


    plot_viz1_time_series(infra, "outputs/figures/viz1_infra_time_series.png", top_k=8)

    print("Saved:")
    print(" - outputs/figures/viz1_infra_time_series.png")
    
