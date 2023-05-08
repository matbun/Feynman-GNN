from setuptools import setup, find_packages

setup(
    name="feygnn",
    description="Feynman GNN: https://arxiv.org/pdf/2211.15348.pdf",
    author="Matteo Bunino and authors of paper @ https://arxiv.org/pdf/2211.15348.pdf",
    author_email="matteo.bunino@cern.ch",
    version="0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
