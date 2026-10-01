import time
import threading
import multiprocessing
import asyncio


# Task that simulates I/O work
def work(task_number):
    time.sleep(1)
    return f"Task {task_number} completed"


# ---------------- THREADING ----------------
def run_threading():
    threads = []

    start = time.time()

    for i in range(5):
        t = threading.Thread(target=work, args=(i + 1,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()

    print("Threading Time:", round(end - start, 2), "seconds")


# ---------------- MULTIPROCESSING ----------------
def run_multiprocessing():
    start = time.time()

    processes = []

    for i in range(5):
        p = multiprocessing.Process(
            target=work,
            args=(i + 1,)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()

    print("Multiprocessing Time:", round(end - start, 2), "seconds")


# ---------------- ASYNCIO ----------------
async def async_work(task_number):
    await asyncio.sleep(1)
    return f"Task {task_number} completed"


async def run_asyncio():
    start = time.time()

    tasks = []

    for i in range(5):
        tasks.append(async_work(i + 1))

    await asyncio.gather(*tasks)

    end = time.time()

    print("AsyncIO Time:", round(end - start, 2), "seconds")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":

    print("Comparing Threading, Multiprocessing and AsyncIO")
    print("-----------------------------------------------")

    run_threading()

    run_multiprocessing()

    asyncio.run(run_asyncio())