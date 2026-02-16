# Erdős–Rényi Model

<img src="https://github.com/easai/er-model/blob/main/graph1.png" width="300" />

This repository provides a compact, self‑contained environment for generating and examining finite realizations of the Erdős–Rényi random graph ensemble. The project focuses on the canonical `G(n, p)` formulation, in which each potential edge among n labeled vertices is included independently with probability p. Although elementary to define, this model exhibits a rich collection of structural phase transitions and serves as a foundational object in probabilistic combinatorics, network science, and the study of branching‑process approximations.

## Overview

The Erdős–Rényi model `G(n, p)` constructs a graph with n vertices where each possible edge is included with probability p. This project uses that model to create a sequence of small random graphs and store them as static images. These images illustrate the variability and sparsity patterns that arise when p is small.

## Project structure

The repository includes a lightweight Python package under src, along with example output images. The environment is defined through `pyproject.toml` for reproducibility and clarity.

## Usage

The project is designed to be run inside the configured environment. It produces a set of graph images named sequentially and saved in the project directory. The parameters n and p can be adjusted to explore different regimes of the Erdős–Rényi model.

## Dependencies

The project relies on standard scientific Python libraries for graph generation and visualization. All dependencies are declared in `pyproject.toml` for consistent installation.

## References
[Erdős–Rényi graphs and Branching processes](https://economics.mit.edu/sites/default/files/inline-files/Lecture%203%20-%20Erdos-Renyi%20Graphs%20and%20Branching%20Processes.pdf)

