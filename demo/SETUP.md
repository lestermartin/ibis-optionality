# Setup: Ibis — Bringing Optionality to Python Dataframes

Everything here gets you to a working copy of `ibis_optionality_demo.ipynb`.
The DuckDB half needs nothing but Python. The Trino half needs one of the
two options in Step 3 — pick whichever is easier for you.

## 1. Install Python dependencies

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Cache the demo dataset locally (do this before you're on stage)

```bash
python prep_offline_data.py
```

This downloads the small example dataset once and saves it to
`data/penguins.parquet`. The notebook loads from that local file, so the
live session doesn't depend on venue wifi holding up.

## 3. Get a Trino endpoint (pick one)

### Option A — Local, offline, via Docker (recommended for presenting)

Requires [Docker](https://docs.docker.com/get-docker/).

```bash
docker compose up -d
```

This starts a single-node Trino cluster on `localhost:8080` with the
built-in `memory` connector enabled (`trino-catalog/memory.properties`) —
no external database or cloud account needed. Use these connection values:

```
TRINO_HOST=localhost
TRINO_PORT=8080
TRINO_USER=demo
TRINO_CATALOG=memory
TRINO_SCHEMA=default
```

(No password required.) Give it 20–30 seconds to finish starting before
running the notebook's Trino cell. Stop it afterward with `docker compose down`.

### Option B — Hosted, no install: Starburst Galaxy

A free-tier hosted Trino cluster — this is the same service the
[official Ibis Trino tutorial](https://ibis-project.org/tutorials/backends/starburst-galaxy/1_basics)
uses, so it's a well-trodden path.

1. Sign up at [starburst.io/platform/galaxy](https://www.starburst.io/platform/galaxy/)
   and create a cluster.
2. From the Galaxy console, grab your host, port (usually `443`), username,
   and password.
3. Use those as your `TRINO_*` values, and set `TRINO_CATALOG` /
   `TRINO_SCHEMA` to a catalog you have access to (Galaxy ships a `sample`
   catalog with a `demo` schema you can write into for testing).

## 4. Set your Trino connection values

Either export them as environment variables before launching Jupyter:

```bash
export TRINO_HOST=localhost
export TRINO_PORT=8080
export TRINO_USER=demo
export TRINO_CATALOG=memory
export TRINO_SCHEMA=default
```

...or just edit the values directly in the notebook's Trino cell — either
works. Environment variables keep secrets (Option B's password) out of the
notebook file, which matters more if you'll share it afterward.

## 5. Launch the notebook

```bash
jupyter lab ibis_optionality_demo.ipynb
```

Run the cells top to bottom. Sections 1–4 only need DuckDB (and work fully
offline if you did Step 2). Section 5 needs whichever Trino endpoint you
set up in Step 3.

## Files in this folder

| File | Purpose |
|---|---|
| `ibis_optionality_demo.ipynb` | The live demo notebook |
| `prep_offline_data.py` | Run once beforehand to cache the dataset locally |
| `requirements.txt` | Python dependencies |
| `docker-compose.yml` + `trino-catalog/memory.properties` | Local Trino cluster (Option A) |

## Learn more

- Docs & tutorials: <https://ibis-project.org>
- Source: <https://github.com/ibis-project/ibis>
- Official tutorial repo: <https://github.com/ibis-project/ibis-tutorial>
