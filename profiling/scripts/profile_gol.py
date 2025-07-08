#!/usr/bin/env python3
import os
import sys
import cProfile

# ── Configuración de import para encontrar src ────────────────────────────────
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)
# ─────────────────────────────────────────────────────────────────────────────

from src.game_of_life_parallel import main  # tu función main(size, steps, workers)

def build_profile(size: int, steps: int, workers: int):
    """
    Ejecuta main(size, steps, workers) bajo cProfile
    y escribe el resultado en profiling/cprofile/gol_{size}_{steps}.pstats
    """
    perfil_dir = os.path.join(project_root, 'profiling', 'cprofile')
    os.makedirs(perfil_dir, exist_ok=True)

    profile_path = os.path.join(perfil_dir, f'gol_{size}_{steps}.pstats')
    cProfile.run(
        f'main(size={size}, steps={steps}, workers={workers})',
        filename=profile_path
    )
    print(f"Perfil guardado en {profile_path}")

if __name__ == '__main__':
    # Parámetros por defecto: tamaño 512, 100 pasos, 4 procesos
    # Puedes cambiarlos con: python profile_gol.py 256 50 2
    if len(sys.argv) == 4:
        size    = int(sys.argv[1])
        steps   = int(sys.argv[2])
        workers = int(sys.argv[3])
    else:
        size, steps, workers = 512, 100, 4

    build_profile(size, steps, workers)
