#!/usr/bin/env python3
import time
import os
import json
import sys
from src.game_of_life_parallel import main

def measure(size, steps, workers):
    t0 = time.time()
    main(size, steps, workers)
    return time.time() - t0

if __name__ == "__main__":
    os.makedirs(os.path.join("results", "strong"), exist_ok=True)
    size, steps = 512, 100
    workers_list = [1, 2, 4, 8]
    results = []
    for w in workers_list:
        dt = measure(size, steps, w)
        print(f"workers={w} → {dt:.3f}s")
        results.append({"workers": w, "time": dt})
    with open(os.path.join("results", "strong", "strong_512_100.json"), "w") as f:
        json.dump(results, f, indent=2)
