import os
import random
import time
from multiprocessing import Pool


def estimate(number):
    trials_in_quarter_unit_circle = 0
    print(f"PID : {os.getpid()} / number: {number}")

    for step in range(number):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_circle = (x * x) + (y * y) <= 1.0
        trials_in_quarter_unit_circle += is_in_circle

    return trials_in_quarter_unit_circle


if __name__ == '__main__':
    start = time.time()

    total_number = int(1e8)
    process_count = 8
    pool = Pool(process_count)

    number_per_process = total_number // process_count
    trial_per_process = [number_per_process] * process_count
    print(f"number per process : {number_per_process} / trial per process : {trial_per_process}")

    result = pool.map(estimate, trial_per_process)
    print(result)
    print(time.time() - start)
