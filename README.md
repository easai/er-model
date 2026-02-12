# Erdős–Rényi Model

This repository provides a compact, self‑contained environment for generating and examining finite realizations of the Erdős–Rényi random graph ensemble. The project focuses on the canonical `G(n, p)` formulation, in which each potential edge among n labeled vertices is included independently with probability p. Although elementary to define, this model exhibits a rich collection of structural phase transitions and serves as a foundational object in probabilistic combinatorics, network science, and the study of branching‑process approximations.

## overview

The Erdős–Rényi model `G(n, p)` constructs a graph with n vertices where each possible edge is included with probability p. This project uses that model to create a sequence of small random graphs and store them as static images. These images illustrate the variability and sparsity patterns that arise when p is small.

## project structure

The repository includes a lightweight Python package under src, along with example output images. The environment is defined through `pyproject.toml` for reproducibility and clarity.

## usage

The project is designed to be run inside the configured environment. It produces a set of graph images named sequentially and saved in the project directory. The parameters n and p can be adjusted to explore different regimes of the Erdős–Rényi model.

## dependencies

The project relies on standard scientific Python libraries for graph generation and visualization. All dependencies are declared in `pyproject.toml` for consistent installation.


