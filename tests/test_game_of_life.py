import sys, os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest  ## importo pytest pa' los tests
from src.game_of_life import GameOfLife  ## traigo clase del juego

def test_soledad():
    ## estado con una sola celula viva aislada
    ini = [[0,0,0],[0,1,0],[0,0,0]]
    gol = GameOfLife(3,3,estado_inicial=ini)  ## inicializo game
    gol.step()  ## un paso
    assert gol.get_state()[1][1] == 0  ## verifica que muere x soledad

def test_blinker():
    ## testeo el oscilador blinker en 2 pasos
    ini = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0]
    ]  ## forma vertical
    gol = GameOfLife(5,5,estado_inicial=ini)  ## inicializo blinker
    gol.step(); gol.step()  ## 2 pasos
    assert gol.get_state() == ini  ## vuelve al estado inicial

def test_glider():
    ## testeo el glider q se mueve en 4 pasos
    ini = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
    ]  ## patron glider
    gol = GameOfLife(5,5,estado_inicial=ini)  ## inicializo
    gol.run(4)  ## corro 4 generaciones
    fin = gol.get_state()
    # el glider avanza 1 pos diagonal en 4 pasos, reviso solo una celula
    assert fin[2][3] == 1  ## deberia haber una celula viva en (2,3)
