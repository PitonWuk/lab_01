"""
Завдання 1
Розробіть додаток, що імітує чергу запитів до сервера.
Мають бути клієнти, які надсилають запити на сервер, кожен
з яких має свій пріоритет. Кожен новий клієнт потрапляє у
чергу залежно від свого пріоритету. Зберігайте статистику
запитів (користувач, час) в окремій черзі.
Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.

"""
from collections import deque
import time

class ServerQueue:
    def __init__(self):
        self.request_queue = deque()
        self.statistics_queue = deque()

    def add_request(self, client, priority):
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        request = {"client": client, "priority": priority, "time": request_time}
        self.request_queue.append((priority, request))
        print(f"Request from {client} with priority {priority} added to the queue.")

    def process_requests(self):
        while self.request_queue:
            priority, request = self.request_queue.popleft()
            self.statistics_queue.append(request)
            print(f"Processing request from {request['client']} with priority {priority} at {request['time']}.")

    def display_statistics(self):
        print("\nStatistics:")
        for request in self.statistics_queue:
            print(f"{request['client']} - Priority: {request['priority']}, Time: {request['time']}")

server = ServerQueue()

server.add_request("Client1", 2)
server.add_request("Client2", 1)
server.add_request("Client3", 3)

server.process_requests()
server.display_statistics()

