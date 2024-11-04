from config import *
from sorted_doubly_linked_list import SortedDoublyLinkedList
from rand import RandomNumberGenerator
from device import Job, Device, End

rng = RandomNumberGenerator()

def test(arrival_rate, service_rate, nr_jobs: int):
    events = SortedDoublyLinkedList()

    source = Device('Arrive', arrival_rate)
    device1 = Device('Device 1', service_rate)
    device2 = Device('Device 2', service_rate)
    end = End('Complete', 0)

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

nr_jobs: int = int(1e5)
arrival_rate = int(1e4)
with open('result.csv', 'w') as f:
    pass
for service_rate in range(1000, 100000, 1000):
    result = test(arrival_rate, service_rate, nr_jobs)
    print(sum(result)/nr_jobs)
    with open('result.csv', 'a') as f:
        f.write(f"{arrival_rate},{service_rate},")
        f.write(','.join(str(x) for x in result))
        f.write('\n')