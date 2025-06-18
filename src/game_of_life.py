import random

class GameOfLife:
    def __init__(self, filas, columnas, estado_inicial=None):
        # si no dan estado inicial, genero uno aleatorio
        self.filas = filas
        self.columnas = columnas
        if estado_inicial:
            self.estado = estado_inicial
        else:
            self.estado = [
                [random.choice([0, 1]) for _ in range(self.columnas)]
                for _ in range(self.filas)
            ]

    def step(self):
        # aplico reglas de conway
        nuevo_estado = [
            [0 for _ in range(self.columnas)]
            for _ in range(self.filas)
        ]
        for i in range(self.filas):
            for j in range(self.columnas):
                vivos = 0
                # cuento vecinos vivos
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.filas and 0 <= nj < self.columnas:
                            vivos += self.estado[ni][nj]
                # regla 1 y 2: muere si pocos o muchos
                if self.estado[i][j] == 1 and (vivos < 2 or vivos > 3):
                    nuevo_estado[i][j] = 0
                # regla 3: sobrevive
                elif self.estado[i][j] == 1 and (vivos == 2 or vivos == 3):
                    nuevo_estado[i][j] = 1
                # regla 4: reproduccion
                elif self.estado[i][j] == 0 and vivos == 3:
                    nuevo_estado[i][j] = 1
                # en cualquier otro caso queda muerta (0)
        self.estado = nuevo_estado

    def run(self, pasos):
        # corro varias iteraciones
        for _ in range(pasos):
            self.step()

    def get_state(self):
        # devuelvo el tablero actual
        return self.estado
