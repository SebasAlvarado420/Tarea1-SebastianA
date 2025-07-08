# Al principio de src/game_of_life_parallel.py
try:
    from line_profiler import profile
except ImportError:
    # Si no existe line_profiler (p.ej. en cProfile), definimos un dummy
    def profile(func):
        return func

import random
from multiprocessing import Pool
from typing import List, Tuple

def _proc_fila(args: Tuple[int, int, List[List[int]]]) -> Tuple[int, List[int]]:
    i, cols, estado = args
    filas = len(estado)
    nueva = []
    for j in range(cols):
        vivos = 0
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < filas and 0 <= nj < cols:
                    vivos += estado[ni][nj]
        if estado[i][j] == 1 and vivos in (2, 3):
            nueva.append(1)
        elif estado[i][j] == 0 and vivos == 3:
            nueva.append(1)
        else:
            nueva.append(0)
    return (i, nueva)

class GameOfLifeParallel:
    def __init__(self, filas: int, cols: int, estado_inicial: List[List[int]] = None):
        self.filas = filas
        self.cols = cols
        if estado_inicial:
            self.estado = estado_inicial
        else:
            self.estado = [
                [random.choice([0, 1]) for _ in range(cols)]
                for _ in range(filas)
            ]

    @profile
    def step_parallel(self, workers: int):
        args = [(i, self.cols, self.estado) for i in range(self.filas)]
        with Pool(processes=workers) as p:
            filas_nuevas = p.map(_proc_fila, args)
        nuevo = [None] * self.filas
        for i, fila in filas_nuevas:
            nuevo[i] = fila
        self.estado = nuevo

def main(size: int, steps: int, workers: int):
    gol = GameOfLifeParallel(size, size)
    for _ in range(steps):
        gol.step_parallel(workers)
    return gol.estado

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python game_of_life_parallel.py <size> <steps> <workers>")
        sys.exit(1)
    sz, st, wk = map(int, sys.argv[1:])
    final = main(sz, st, wk)
    for fila in final:
        print("".join(str(c) for c in fila))
