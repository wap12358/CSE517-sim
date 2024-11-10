from config import *
from sorted_doubly_linked_list import SortedDoublyLinkedList
from rand import RandomNumberGenerator
from device import Job, Device, End
from numpy import mean
from tqdm import tqdm

rng = RandomNumberGenerator()

def test(arrival_rate, service_rate, nr_jobs: int, rand_dist: str):
    events = SortedDoublyLinkedList()

    source = Device('Arrive', arrival_rate, rand_dist)
    device1 = Device('Device 1', service_rate, rand_dist)
    device2 = Device('Device 2', service_rate, rand_dist)
    end = End('Complete', 0, rand_dist)

    source.connect(device1)
    device1.connect(device2)
    device2.connect(end)

    for i in range(nr_jobs):
        source.enqueue(Job(i))

    events.insert(source, 0)
    ts = 0

    while not events.is_empty():
        # events.display()
        device, ts = events.dequeue()
        device.operation(ts, events)

    ret = end.stat()
    # for item in end.queue:
    #     print(item)
    return ret

nr_jobs: int = int(1e4)
arrival_rate = int(1e4)
for test_case in ['exponential', 'uniform', 'deterministic']:
    with open(f'{test_case}.csv', 'w') as f:
        pass
    for service_rate in tqdm(range(2000, 30000, 2000)):
        avg_sojourn = []
        avg_nr_item = []
        for i in range(100):
            duration, sojourn_times = test(arrival_rate, service_rate, nr_jobs, test_case)
            # print(sum(result)/nr_jobs)
            avg_sojourn.append(mean(sojourn_times))
            avg_nr_item.append(sum(sojourn_times)/duration)
        with open(f'{test_case}.csv', 'a') as f:
            f.write(f"{arrival_rate},{service_rate},")
            f.write(','.join(str(x) for x in avg_sojourn))
            f.write(',')
            f.write(','.join(str(x) for x in avg_nr_item))
            f.write('\n')