# Cubix Data Engineering Capstone Project

This repository contains the final capstone project for the Postgraduate Course in Data Engineering at the **Cubix Institute of Technology**. The project demonstrates a production-ready, structured Python application tailored for data engineering workflows, emphasizing clean code, automation, and modern software development practices.

## 🚀 Project Overview

The goal of this project is to build a robust, maintainable data engineering module. It showcases how to structure a data pipeline application from scratch, manage complex dependencies, and automate quality control using Continuous Integration (CI).

### Key Features
*   **Production-Grade Architecture:** Structured with a dedicated source package (`src/`) and decoupled unit tests (`tests/`).
*   **Modern Dependency Management:** Built using **Poetry** to ensure reproducible environments and deterministic builds.
*   **Quality Assurance & Automation:** Integrated pre-commit hooks and automated **CI/CD pipelines** via GitHub Actions.
*   **Robust Coding Standards:** Configured with automated code linting and formatting tools (`black`, `flake8`, `isort`).

---

## 🛠️ Tech Stack & Tools

*   **Language:** Python 3.10+
*   **Dependency Management:** [Poetry](https://python-poetry.org)
*   **CI/CD & Automation:** GitHub Actions, Pre-commit
*   **Testing Framework:** PyTest

---

## 📁 Repository Structure

```text
├── .github/workflows/     # CI/CD pipeline definitions (GitHub Actions)
├── src/                   # Main application source code and ETL logic
├── tests/                 # Unit tests and test fixtures
├── .gitignore             # Git ignore patterns
├── .pre-commit-config.yaml# Pre-commit hooks configuration
├── poetry.lock            # Lockfile for exact dependency versions
├── pyproject.toml         # Poetry configuration, metadata, and tool settings
└── README.md              # Project documentation
```

---

## ⚙️ Getting Started & Installation

### Prerequisites
Ensure you have Python 3.10+ and **Poetry** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com
cd cubix_data_engineer_capstone
```

### 2. Install Dependencies
Use Poetry to create a virtual environment and install all required packages (including development tools):
```bash
poetry install
```

### 3. Set Up Pre-commit Hooks
Activate the pre-commit hooks to ensure every commit complies with the code quality guidelines:
```bash
poetry run pre-commit install
```

---

## 🧪 Running Tests & Quality Checks

### Run Unit Tests
The project utilizes `pytest` for automated test suites. Execute the tests within the Poetry environment:
```bash
poetry run pytest
```

### Manual Code Quality Checks
You can trigger the lints and formatters manually across all files at any time:
```bash
poetry run pre-commit run --all-files
```

---

## 🔄 Continuous Integration (CI)

This project features a fully automated **GitHub Actions** workflow. Upon every `push` or `pull_request` to the main branch, the pipeline automatically:
1. Sets up the specified Python environment.
2. Installs dependencies via Poetry.
3. Runs the entire `pytest` suite to prevent regressions.

---
*Developed by **Zsombor Hadady** as part of the Cubix Data Engineering Curriculum (2026).*