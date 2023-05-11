# Feynman GNN

Reference: [Learning Feynman Diagrams using Graph Neural Networks](https://arxiv.org/pdf/2211.15348.pdf)

Train a Graph Neural Network to predict the matrix element (probability) of Feynman diagrams.

## Installation

Requirements:

- Linux environment
- Mamba: [Installation guide](https://mamba.readthedocs.io/en/latest/installation.html) (suggested Mambaforge).
- VS Code, for code editing

Install the virtual environment. As of now, we use CPU only, but it is easily extendable to CUDA support.

```bash
# Create and setup python env: install dependencies and feygnn package
make

# Activate env
conda activate ./.venv
```

To use the installed virtual environment as a kernel for jupyter notebooks, select it from VS Code from the
notebook visualization.

## Usage

### 1. Generate dataset

Apparently, the latest version of the notebook to generate the dataset is: `./Notebooks/dataset_builder_v3_0.ipynb`.
That notebook has been "prettified" and saved as `Dataset_generator.ipynb`. You can execute it quickly from CLI with:

```bash
make datagen
```

Alternatively, you can open the notebook and execute it cell-by-cell.

The results are stored inside `./data/raw` folder.

### 2. Train

Apparently, the latest version of the notebook to train the GNN is: `./Notebooks/Feynman_GNN_v5.0.ipynb`.
That notebook has been "prettified" and saved as `Train_Feynman_GNN.ipynb.ipynb`.

To visualize ML logs, run Tensorboard from command line (updated instructions in the notebook):

```bash
conda run -p ./.venv tensorboard --logdir mlruns --host localhost --port 8888
```

And visualize them from the browser at [http://localhost:8888](http://localhost:8888).

## Reproducibility

The exact copy of the Python (conda) environment used in the experiments is in `environment.yml` was
generated from `./.venv` (initially generated from `env-env.yml`) with the command:

```bash
conda env export -p ./.venv -f environment.yml --no-builds
```
