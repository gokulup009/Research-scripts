# research-scripts

A collection of scripts and notebooks for my research — including preprocessing, simulation helpers, postprocessing (dump analysis, correlation functions, structure factors), and plotting utilities.

---

## Repository layout

```
research-scripts/
├── README.md
├── LICENSE
├── requirements.txt
├── data/                 # (optional) sample input/output files
├── notebooks/            # Jupyter notebooks for analysis
├── plotting/             # plotting utilities (matplotlib, xmgrace)
├── preprocessing/        # generate input configs, initial states
├── postprocessing/       # analyze outputs (dump, correlation, etc.)
│   ├── process_dump.py
│   ├── change_atom_type.py
│   ├── merge.py          # merge multiple dump frames into one
│   └── ...
├── simulations/          # job launchers, SLURM/PBS/local run scripts
└── utils/                # reusable Python helpers
```

---

## Installation

Create a virtualenv and install dependencies (if any):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Each folder contains scripts with docstrings and examples. For example:

* **Preprocessing** → build LAMMPS inputs, map molecules.
* **Simulations** → job submission scripts (SLURM/PBS) or nohup helpers.
* **Postprocessing** → modify dump files, calculate correlation functions, structure factors.
* **Plotting** → reusable matplotlib/xmgrace scripts.
* **Notebooks** → Jupyter-based analysis and visualization.

---

## postprocessing/merge.py

A simple script to merge two LAMMPS-style dump files frame by frame. It shifts atom IDs to avoid duplicates and can change atom types to distinguish atoms from each file.

---
## postprocessing/dump_type.py

dump_type.py processes a LAMMPS dump file and reassigns atom types based on their original type values. In the example, types ≤3200 are set to 1, type 3201 becomes 2, and all higher types become 3. This allows grouping many atom types into a smaller set for easier analysis or visualization.

## Contributing

* Keep commits small and meaningful.
* Add usage examples under `examples/` or in docstrings.
* Use branches/PRs for bigger changes.

## License

