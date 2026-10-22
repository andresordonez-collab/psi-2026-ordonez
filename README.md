# PSI 2-2026 Andres Ordonez Botero

[![CI](https://github.com/andresordonez-collab/psi-2026-ordonez/actions/workflows/ci.yml/badge.svg)](https://github.com/andresordonez-collab/psi-2026-ordonez/actions/workflows/ci.yml)

Repositorio base reproducible para los laboratorios de **Procesamiento de Señales e Imágenes (13318)**, USACH.

## Instalación y pruebas (sin Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e ".[dev,notebook]"
pytest -v
ruff check .
