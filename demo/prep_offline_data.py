"""
Run this ONCE, ahead of time, on a machine with a good internet connection —
ideally the same laptop you'll present from.

It downloads the small example dataset used in the live demo and saves it
as a local Parquet file so the actual demo notebook
doesn't depend on venue wifi.

Usage:
    python prep_offline_data.py
"""

import pathlib

import ibis


def main() -> None:
    out_dir = pathlib.Path("data")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "penguins.parquet"

    con = ibis.duckdb.connect()

    print("Fetching example dataset (requires internet)...")
    penguins = ibis.examples.penguins.fetch(backend=con)

    penguins.to_parquet(out_path)
    print(f"Saved {penguins.count().execute()} rows to {out_path}")
    print("You're set -- the demo notebook will run fully offline from here.")


if __name__ == "__main__":
    main()
