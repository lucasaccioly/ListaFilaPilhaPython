#5. Em um sistema de comércio eletrônico, os pedidos online são processados em uma fila. Implemente uma classe de fila que gerencie os pedidos online e processe-os na ordem de chegada.
class OnlineOrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        self.queue.append(order)

    def process_first_order(self):
        if not self.is_empty():
            print(f"Processando o pedido online: {self.queue[0]}")
            self.queue.pop(0)
        else:
            print("A fila de pedidos online está vazia!")

    def get_first_order(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def get_last_order(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return None

    def count_orders(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
    online_order_queue = OnlineOrderQueue()

# Adicionando pedidos à fila
online_order_queue.add_order("Pedido online 1: Notebook")
online_order_queue.add_order("Pedido online 2: Smartphone")
online_order_queue.add_order("Pedido online 3: Tablet")

# Verificando o primeiro pedido da fila
print(f"Primeiro pedido da fila: {online_order_queue.get_first_order()}")

# Verificando o último pedido da fila
print(f"Último pedido da fila: {online_order_queue.get_last_order()}")

# Contando quantos pedidos estão na fila
print(f"Quantos pedidos estão na fila: {online_order_queue.count_orders()}")

# Processando o primeiro pedido da fila
online_order_queue.process_first_order()

# Verificando se a fila de pedidos online está vazia
print(f"A fila de pedidos online está vazia? {online_order_queue.is_empty()}")