# er model

This project generates simple random graphs using the classical Erdos Renyi model. It provides a minimal and reproducible structure for producing multiple independent samples of G(n, p) networks and saving them as image files for inspection or analysis.

## overview

The Erdos Renyi model G(n, p) constructs a graph with n vertices where each possible edge is included with probability p. This project uses that model to create a sequence of small random graphs and store them as static images. These images illustrate the variability and sparsity patterns that arise when p is small.

## project structure

The repository includes a lightweight Python package under src along with example output images. The environment is defined through pyproject.toml for reproducibility and clarity.

## usage

The project is designed to be run inside the configured environment. It produces a set of graph images named sequentially and saved in the project directory. The parameters n and p can be adjusted to explore different regimes of the Erdos Renyi model.

## dependencies

The project relies on standard scientific Python libraries for graph generation and visualization. All dependencies are declared in pyproject.toml for consistent installation.

