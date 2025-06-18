# Tarea 1 - Juego de la Vida - Sebastian Alvarado

## Descripción
Implementación en Python del autómata celular de Conway (Game of Life) con dos versiones:
- **Secuencial** (`src/game_of_life.py`)
- **Paralela** utilizando `multiprocessing` (`src/game_of_life_parallel.py`)

## Estructura del proyecto
```
Tarea1-SebastianA/
├─ src/
│  ├ game_of_life.py
│  ├ game_of_life_parallel.py
│  ├ visualize.py
│  └ performance.py
├─ tests/
│  └ test_game_of_life.py
├─ notebooks/
│  └ visualization.ipynb
├─ output/
│  ├ blinkr/
│  ├ glidr/
│  ├ toad/
│  ├ benchmark.csv
│  ├ seq_vs_par.png
│  └ loglog_all.png
├─ requirements.txt
└─ README.md
```

## Instalación (Windows)
```powershell
cd C:\Users\Usuario\Desktop\Tarea1-SebastianA
python -m venv venv           # crear entorno virtual
.\venv\Scripts\Activate.ps1 # activar entorno
pip install -r requirements.txt # instalar dependencias
```

## Uso

1. **Tests unitarios**
   ```powershell
   pytest -q  # ejecuta pruebas de soledad, blinker y glider
   ```
2. **Visualización de patrones**
   ```powershell
   python src\visualize.py
   ```
   - Genera 10 imágenes para cada patrón en `output/blinkr/`, `output/glidr/` y `output/toad/`.
3. **Medición de rendimiento**
   ```powershell
   python src\performance.py
   ```
   - Produce:
     - `output/benchmark.csv` (tiempo promedio por paso)
     - `output/seq_vs_par.png` (gráfico estático secuencial vs paralelo)
     - `output/loglog_all.png` (gráfico estático log–log con curvas O(n), O(n log n), O(n²))

## Resultados
- **Patrones**: Carpetas `output/blinkr/`, `output/glidr/`, `output/toad/` con PNGs  
- **Benchmark**: Archivo `benchmark.csv` con datos de tiempos empíricos  
- **Gráficos**: `seq_vs_par.png` y `loglog_all.png`

## Análisis
- La implementación secuencial escala aproximadamente **O(n)** con el número de celdas.  
- La versión paralela mejora el rendimiento en tableros grandes (>=512×512), pero el overhead penaliza en casos pequeños.  
- El conteo de vecinos en doble bucle es el principal cuello de botella.

## Conclusión
Se confirma que reglas locales simples generan patrones complejos y que el uso de paralelismo puede acelerar la simulación en escenarios con gran cantidad de celdas.
