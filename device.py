from rand import RandomNumberGenerator
from sorted_doubly_linked_list import SortedDoublyLinkedList

class Job:
    def __init__(self, id: int):
        self.id = id
        self.history = []
        self.sojourn_time = 0
        self.busy_until = 0
    
    def __str__(self):
        return f"id={self.id}, Arr: {self.history[0]}, last op: {self.history[-1]}"

class Device:
    def __init__(self, name: str, service_rate: int | float):
        self.name = name
        self.service_rate = service_rate
        self.queue = []
        self.connected_devices = []
        self.rng = RandomNumberGenerator()
        self.busy_until = 0
    
    def connect(self, device):
        self.connected_devices.append(device)
    
    def enqueue(self, job: Job):
        self.queue.append(job)
    
    def dequeue(self) -> Job:
        return self.queue.pop(0)
    
    def operation(self, current_ts: int, events: SortedDoublyLinkedList):
        # print(f"{self.name}\t{current_ts}\t{len(self.queue)}")

        job: Job = self.dequeue()
        service_time = self.rng.exponential(self.service_rate)
        next_operation_ts = current_ts + service_time
        self.busy_until = job.busy_until = next_operation_ts
        next_device: Device = self.select_next_device(job)

        job.history.append(tuple((current_ts, service_time, self.name)))
        if self.queue:
            events.insert(self, max(next_operation_ts, self.queue[0].busy_until))
        if not next_device.queue:
            events.insert(next_device, max(next_operation_ts, next_device.busy_until))
        next_device.enqueue(job)
    
    def select_next_device(self, job: Job):
        return self.connected_devices[0]
    
    def __str__(self):
        return self.name

class End(Device):
    def operation(self, current_ts: int, events: SortedDoublyLinkedList):
        return # do nothing if this is a terminal device in the network. in fact, this is a dummy device used to collect completed jobs.
    
    def stat(self):
        sojourn_times = []
        for item in self.queue:
            arrive_ts = item.history[0][0] + item.history[0][1]
            complete_ts = item.history[-1][0] + item.history[-1][1]
            item.history.append(tuple((complete_ts, 0, self.name)))
            item.sojourn_time = complete_ts - arrive_ts
            sojourn_times.append(item.sojourn_time)
        return sojourn_times