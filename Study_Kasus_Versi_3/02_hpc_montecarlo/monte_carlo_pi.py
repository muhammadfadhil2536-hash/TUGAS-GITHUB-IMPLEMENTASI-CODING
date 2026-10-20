"""Estimasi pi dengan simulasi Monte Carlo serial dan multiprocessing."""
from multiprocessing import Pool, cpu_count
from random import Random
from time import perf_counter

TRIALS = 400_000

def count_inside(args):
    trials, seed = args
    rng = Random(seed)
    inside = 0
    for _ in range(trials):
        x, y = rng.random(), rng.random()
        if x*x + y*y <= 1:
            inside += 1
    return inside

if __name__ == "__main__":
    start = perf_counter()
    serial_inside = count_inside((TRIALS, 42))
    serial_pi = 4 * serial_inside / TRIALS
    serial_time = perf_counter() - start

    workers = min(4, max(1, cpu_count()))
    chunk = TRIALS // workers
    jobs = [(chunk if i < workers - 1 else TRIALS - chunk * (workers - 1), 100 + i)
            for i in range(workers)]
    start = perf_counter()
    with Pool(workers) as pool:
        parallel_inside = sum(pool.map(count_inside, jobs))
    parallel_pi = 4 * parallel_inside / TRIALS
    parallel_time = perf_counter() - start

    print(f"Nilai pi referensi: 3.141593")
    print(f"Estimasi serial   : {serial_pi:.6f} ({serial_time:.3f} detik)")
    print(f"Estimasi paralel  : {parallel_pi:.6f} ({parallel_time:.3f} detik)")
    print(f"Worker            : {workers}")
    print("Estimasi adalah pendekatan; hasil serial dan paralel memakai sampel acak berbeda.")
