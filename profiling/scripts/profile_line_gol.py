#!/usr/bin/env python3
import os
import sys

# ── Protección para @profile y configuración de import ────────────────────────
try:
    profile
except NameError:
    def profile(func):
        return func

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)
# ─────────────────────────────────────────────────────────────────────────────

from src.game_of_life_parallel import main  # tu función main(size, steps, workers)

if __name__ == "__main__":
    # Parámetros para line_profiler
    size    = 512
    steps   = 100
    workers = 4

    # Ejecuta la función bajo @profile
    main(size, steps, workers)
