from multiprocessing import Process
import os
import time


def square_numbers(num):
    for i in range(num):
        print(i)
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    processes = []

    num_processes = os.cpu_count()  # Get the number of CPU cores

    print(f"Number of cores: {num_processes}")

    for i in range(num_processes):
        process = Process(target=square_numbers, args=(100,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Finished processing")
