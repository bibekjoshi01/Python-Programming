from threading import Thread
import time

db_value = 0


def update_db_value():
    global db_value
    local_copy = db_value

    # Process some data
    local_copy += 1
    time.sleep(0.1)  # Simulate a delay in processing

    db_value = local_copy

if __name__ == "__main__":
    print("Start Value", db_value)

    thread1 = Thread(target=update_db_value)
    thread2 = Thread(target=update_db_value)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End Value", db_value)