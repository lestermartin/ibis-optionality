# Ibis: Bringing Optionality to Python Dataframes

Slides and live-demo code for my session at **Data in the D**, 2026 (Detroit).

> Love the power of writing lazy executed dataframe code in Python that runs
> on your favorite distributed data cluster? Would like some flexibility to
> swap out your processing engine for another? If so, you need optionality
> in your Python dataframe API.
>
> [Ibis](https://ibis-project.org/) offers a Python dataframe API that lets
> your code run on nearly 20 backend data processing systems. It is *the*
> portable dataframe library. Imagine being able to run your Ibis code in
> Polars on your laptop and then moving it to PySpark in your favorite cloud
> provider with just changing a property. No need to imagine; you can do it
> today.
>
> This presentation walks through the features available in Ibis as well as
> compares it with other popular dataframe APIs. You'll see how to
> mix-and-match SQL and dataframe API transformations as desired, and how to
> change the backend system where your code is executed. You'll see a demo
> of a job running in DuckDB for local testing, then with a single line of
> code changed, running in a Trino cluster.

## What's in here

```
.
├── slides/
│   ├── ibis-optionality-slides.pptx   # the deck (editable)
│   └── ibis-optionality-slides.pdf    # the deck (quick view, no PowerPoint needed)
└── demo/
    ├── ibis_optionality_demo.ipynb    # the live-coding notebook
    ├── prep_offline_data.py           # run once beforehand to cache demo data locally
    ├── requirements.txt
    ├── docker-compose.yml             # optional: local single-node Trino
    ├── trino-catalog/memory.properties
    └── SETUP.md                       # full step-by-step setup + Trino options
```

## The demo, in short

The notebook builds one small analysis function against the classic
`penguins` dataset, runs it locally on **DuckDB**, then — changing only the
connection, not the function — runs the *exact same code* against a
**Trino** cluster. That swap is the whole pitch: prototype locally, deploy
wherever your team actually runs, without rewriting anything.

```python
def top_species_by_mass(t):
    return (
        t.filter(t.body_mass_g.notnull())
         .group_by("species")
         .aggregate(avg_mass_g=t.body_mass_g.mean())
         .order_by(ibis.desc("avg_mass_g"))
    )

top_species_by_mass(penguins)          # DuckDB, on your laptop
top_species_by_mass(penguins_on_trino) # Trino, unchanged function
```

## Quick start

```bash
cd demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python prep_offline_data.py     # caches the dataset locally, do this before presenting
jupyter lab ibis_optionality_demo.ipynb
```

The DuckDB half of the notebook works fully offline after the step above.
The Trino half needs an endpoint — see **[`demo/SETUP.md`](demo/SETUP.md)**
for two ways to get one in a few minutes (a local Docker-based cluster, or
a free hosted Starburst Galaxy cluster).

## Before you present

- [ ] Fill in your name/contact on the title and closing slides
- [ ] Update the "this talk's repo" link on the closing slide once this is pushed
- [ ] Run `prep_offline_data.py` on real wifi, ahead of time
- [ ] Pick and test a Trino option from `demo/SETUP.md` beforehand

## Learn more about Ibis

- Docs & tutorials: <https://ibis-project.org>
- Source: <https://github.com/ibis-project/ibis>
- Official tutorial repo: <https://github.com/ibis-project/ibis-tutorial>

## License

Code in `demo/` is licensed under the [MIT License](LICENSE). Slides are
freely reusable and adaptable for non-commercial talks with attribution.
