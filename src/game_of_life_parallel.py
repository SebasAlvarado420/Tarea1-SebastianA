from multiprocessing import Pool
import random

def _proc_fila(args):
    i, cols, estado = args
    filas = len(estado)
    nueva = []
    for j in range(cols):
        vivos = 0
        for di in (-1,0,1):
            for dj in (-1,0,1):
                if di==0 and dj==0: continue
                ni, nj = i+di, j+dj
                if 0<=ni<filas and 0<=nj<cols:
                    vivos += estado[ni][nj]
        val = 1 if (estado[i][j]==1 and vivos in (2,3)) or (estado[i][j]==0 and vivos==3) else 0
        nueva.append(val)
    return (i, nueva)

class GameOfLifeParallel:
    def __init__(self, filas, cols, estado_inicial=None):
        self.filas = filas
        self.cols   = cols
        if estado_inicial:
            self.estado = estado_inicial
        else:
            self.estado = [[random.choice([0,1]) for _ in range(cols)] for _ in range(filas)]

    def step_parallel(self):
        args = [(i, self.cols, self.estado) for i in range(self.filas)]
        with Pool() as p:
            filas_nuevas = p.map(_proc_fila, args)
        nuevo = [None]*self.filas
        for i, fila in filas_nuevas:
            nuevo[i] = fila
        self.estado = nuevo
