from threading import Thread
import time


def square_numbers(num):
    for i in range(num):
        print(i)
        i * i
        time.sleep(0.1)


if __name__ == "__main__":
    threads = []

    for i in range(1000):
        thread = Thread(target=square_numbers, args=(100,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Finished processing")
