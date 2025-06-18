import os
import matplotlib.pyplot as plt
from game_of_life import GameOfLife

def vera_patron(pat, nombre, filas, cols, pasoss):
    # creo carpeta de salida si no existe
    out = f"output/{nombre}"
    if not os.path.exists(out):
        os.makedirs(out)
    gol = GameOfLife(filas, cols, estado_inicial=pat)
    for paso in range(pasoss):
        edo = gol.get_state()
        plt.imshow(edo, cmap='binary')
        plt.title(f"{nombre} paso {paso}")
        plt.axis('off')
        plt.savefig(f"{out}/{nombre}_{paso}.png")
        plt.close()
        gol.step()

if __name__ == "__main__":
    # patrones clasicos
    blinkr = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
    ]
    glidr = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
    ]
    toad = [
        [0,0,0,0],
        [0,0,0,0],
        [0,1,1,1],
        [1,1,1,0]
    ]

    # visualizo 10 pasos de cada uno
    vera_patron(blinkr, "blinkr", 5, 5, 10)
    vera_patron(glidr,  "glidr",  5, 5, 10)
    vera_patron(toad,   "toad",   4, 4, 10)
