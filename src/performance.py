import os, time, csv, math
from multiprocessing import freeze_support
from game_of_life import GameOfLife
from game_of_life_parallel import GameOfLifeParallel
import matplotlib.pyplot as plt

# lista de tamanos de tablero para testear
tamanos_tablero = [32, 64, 128, 256, 512, 1024]
reps = 50

if __name__ == "__main__":
    freeze_support()
    print("==> Empezando benchmark secuencial vs paralelo")

    # aseguro carpeta de salida
    if not os.path.exists("output"):
        os.makedirs("output")

    # corro y guardo CSV
    with open("output/benchmark.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["celdas", "seq_prom", "par_prom"])
        for n in tamanos_tablero:
            print(f"  Procesando {n}×{n} celdas...", end=" ")
            # secuencial
            gol_seq = GameOfLife(n, n)
            t0 = time.perf_counter()
            for _ in range(reps):
                gol_seq.step()
            seq = (time.perf_counter() - t0) / reps
            print(f"seq={seq:.4f}s", end=" ")

            # paralelo
            gol_par = GameOfLifeParallel(n, n)
            t1 = time.perf_counter()
            for _ in range(reps):
                gol_par.step_parallel()
            par = (time.perf_counter() - t1) / reps
            print(f"par={par:.4f}s")

            w.writerow([n * n, seq, par])
    print("==> CSV generado en output/benchmark.csv")

    # leo datos del CSV
    celdas, seqs, pars = [], [], []
    with open("output/benchmark.csv") as f:
        rd = csv.DictReader(f)
        for fila in rd:
            celdas.append(int(fila["celdas"]))
            seqs.append(float(fila["seq_prom"]))
            pars.append(float(fila["par_prom"]))

    #grafico secuencial vs paralelo
    print("==> Generando gráfico secuencial vs paralelo")
    plt.figure()
    plt.plot(celdas, seqs,
             label="secuencial",
             color="#FF6F61",  
             linewidth=3,
             marker="o",
             markersize=6)
    plt.plot(celdas, pars,
             label="paralelo",
             color="#6B5B95",  
             linewidth=3,
             marker="D",
             markersize=6)
    plt.xlabel("Número de celdas")
    plt.ylabel("Tiempo promedio (s)")
    plt.legend()
    plt.savefig("output/seq_vs_par.png")
    plt.close()
    print("==> Gráfico guardado en output/seq_vs_par.png")

    #grafico log-log con curvas teoricas
    print("==> Generando gráfico log-log con curvas teóricas")
    plt.figure()
    plt.loglog(celdas, seqs,
               label="secuencial",
               color="#FF6F61",   
               linewidth=3,
               marker="o",
               markersize=6)
    plt.loglog(celdas, pars,
               label="paralelo",
               color="#6B5B95",   
               linewidth=3,
               marker="D",
               markersize=6)
    plt.loglog(celdas, [c for c in celdas],
               "--", label="O(n)",
               color="#2A9D8F")   
    plt.loglog(celdas, [c * math.log(c) for c in celdas],
               "--", label="O(n log n)",
               color="#E76F51")  
    plt.loglog(celdas, [c ** 2 for c in celdas],
               "--", label="O(n²)",
               color="#264653")   
    plt.xlabel("Celdas (log)")
    plt.ylabel("Tiempo (log)")
    plt.legend()
    plt.savefig("output/loglog_all.png")
    plt.close()
    print("==> Gráfico guardado en output/loglog_all.png")
