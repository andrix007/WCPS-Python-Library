# Web Coverage Processing Service (WCPS) Python Interface

## Overview

This repository contains the implementation of a Python-based interface for interacting with Web Coverage Processing Service (WCPS) servers. The interface is designed to streamline the process of querying geospatial data by abstracting the complexities of WCPS query language into a more user-friendly Pythonic API.

## Features

- **Datacube Abstraction**: A `Datacube` class that acts as a Pythonic representation of a WCPS datacube, allowing for easy manipulation and querying of geospatial data.
  
- **Connection Management**: The `connect` function efficiently manages connections to WCPS servers, ensuring seamless communication and data retrieval.

- **Query Generation**: The `QueryBuilder` class translates Python methods into WCPS queries, enabling users to write Python code that automatically generates the correct WCPS queries.

## Accomplishments

- **Implemented Core Functionalities**: Successfully developed essential components (`Datacube`, `connect`, `query`) to interact with WCPS servers.

- **Unit Testing**: Conducted thorough unit testing for three critical functions to ensure reliability and correctness. These tests simulate server interaction and validate the behavior of the data retrieval process.

- **Documentation and Examples**: Created a comprehensive Jupyter notebook that demonstrates how to use the interface. The notebook serves as interactive documentation, guiding users through various use cases and showcasing the interface's capabilities.

## Getting Started

To start using this WCPS Python interface, clone the repository and navigate to the project directory. Set up a virtual environment and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/wcps-python-interface.git

# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Unix or MacOS
venv\Scripts\activate  # For Windows

# Install dependencies (if any)
pip install -r requirements.txt

```
Run the unit tests to ensure that everything is set up correctly:
```bash
python -m tests/unit_tests.py
```
To explore how the interface works, open the provided Jupyter notebook:
```
jupyter notebook example/example.ipynb
``` 
