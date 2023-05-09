# Feynman GNN

Ref: [Learning Feynman Diagrams using Graph Neural Networks](https://arxiv.org/pdf/2211.15348.pdf)

## Installation

Requirements:

- Mamba: [Installation guide](https://mamba.readthedocs.io/en/latest/installation.html) (suggested Mambaforge).

Install the virtual environment. As of now, we use CPU only, but it is easily extendable to CUDA support.

```bash
# Install dependencies
mamba env create -p ./.venv --file environment.yml
conda activate ./.venv

# Install feygnn package
conda run -p ./.venv python -m pip install --no-deps -e .

# Activate env
conda activate ./.venv
```

## Usage

Apparently, the latest version of the notebook to generate the dataset is: `./Notebooks/dataset_builder_v3_0.ipynb`.
