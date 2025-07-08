#!/usr/bin/env python3
import os
import glob
import json
import argparse
import matplotlib.pyplot as plt

def plot_strong(input_path: str, output_path: str):
    # Lee el JSON de escalamiento fuerte (puede ser lista de dicts o dict con arrays)
    with open(input_path, "r") as f:
        data = json.load(f)

    if isinstance(data, list):
        # formato: [{"workers": 1, "time": 34.19}, ...]
        workers = [entry["workers"] for entry in data]
        times   = [entry["time"]    for entry in data]
        size = steps = ""
    else:
        # formato: {"workers": [1,2,4,8], "times": [...], "size":512, "steps":100}
        workers = data["workers"]
        times   = data["times"]
        size    = data.get("size", "")
        steps   = data.get("steps", "")

    plt.figure()
    plt.plot(workers, times, marker="o")
    plt.title(f"Escalamiento fuerte (size={size}, steps={steps})")
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo (s)")
    plt.grid(True)
    plt.savefig(output_path)
    print(f"→ Gráfica fuerte guardada en {output_path}")

def plot_weak(input_dir: str, output_path: str):
    # Busca todos los archivos weak_*.txt
    pattern = os.path.join(input_dir, "weak_*.txt")
    files   = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No encontré ningún archivo con patrón '{pattern}'")

    workers, times = [], []
    for fn in files:
        line = open(fn).read().strip()
        # Línea esperada: "workers=4 size=64×64 steps=100 time=21.739s"
        parts = dict(p.split("=",1) for p in line.split())
        workers.append(int(parts["workers"]))
        times.append(float(parts["time"].rstrip("s")))

    plt.figure()
    plt.plot(workers, times, marker="o")
    plt.title("Escalamiento débil (≈10000 celdas/proceso)")
    plt.xlabel("Número de procesos")
    plt.ylabel("Tiempo (s)")
    plt.grid(True)
    plt.savefig(output_path)
    print(f"→ Gráfica débil guardada en {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Visualizar escalamiento fuerte o débil del Game of Life paralelo"
    )
    parser.add_argument("mode", choices=["strong","weak"],
                        help="Modo: strong (fuerte) o weak (débil)")
    parser.add_argument("-i","--input", required=True,
                        help="Para strong: ruta al JSON; para weak: carpeta con los weak_*.txt")
    parser.add_argument("-o","--output", required=True,
                        help="Ruta donde guardar el PNG de salida")
    args = parser.parse_args()

    if args.mode == "strong":
        plot_strong(args.input, args.output)
    else:
        plot_weak(args.input, args.output)

if __name__ == "__main__":
    main()
