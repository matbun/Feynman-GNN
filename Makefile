# Create and setup python env: install dependencies and feygnn package
build:
	mamba env create -p ./.venv --file environment.yml
	conda run -p ./.venv python -m pip install --no-deps -e .

# Generate dataset by executing a notebook end-to-end
datagen:
	conda run -p ./.venv jupyter nbconvert --to notebook --stdout --execute Dataset_generator.ipynb