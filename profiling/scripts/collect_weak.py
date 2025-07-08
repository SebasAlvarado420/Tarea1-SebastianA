#!/usr/bin/env python3
import os
import sys
import time

# — AÑADIMOS ROOT DEL PROYECTO AL PATH —
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.game_of_life_parallel import main

def collect_weak(workers_list, steps=100, cells_per_worker=10000):
    """
    Para cada número de workers en workers_list:
      - calcula tamaño de la cuadrícula de modo que filas*cols = workers*cells_per_worker
      - ejecuta main(size, steps, workers) y mide tiempo
      - guarda resultado en results/weak/weak_{workers}.txt
    """
    out_dir = os.path.join(project_root, 'results', 'weak')
    os.makedirs(out_dir, exist_ok=True)

    for p in workers_list:
        # tamaño cuadrícula para mantener ~10000 celdas por worker
        total_cells = p * cells_per_worker
        size = int(total_cells**0.5)
        print(f"→ p={p}, size={size}×{size}", flush=True)

        t0 = time.time()
        main(size, steps, p)
        tp = time.time() - t0

        fname = os.path.join(out_dir, f"weak_{p}.txt")
        with open(fname, 'w') as f:
            f.write(f"workers={p} size={size} steps={steps} time={tp:.3f}s\n")
        print(f"   guardado en {fname}", flush=True)

if __name__ == "__main__":
    # núcleos a probar en weak scaling
    workers = [1, 2, 4, 8]
    collect_weak(workers)
