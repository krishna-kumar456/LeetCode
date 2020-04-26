import random
import multiprocessing

def compute(results):
    results.append(sum([random.randint(1, 100) for i in range(100000)]))


with multiprocessing.Manager() as manager:
    results = manager.list()
    workers = [multiprocessing.Process(target=compute(ex), for ex in range(8))]

    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

    print("Results : " + results)