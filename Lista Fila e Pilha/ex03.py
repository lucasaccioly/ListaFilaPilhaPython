#3. Imagine um sistema de gerenciamento de pedidos para um restaurante. Os pedidos dos clientes são colocados em uma fila e processados na ordem em que foram feitos. Use a classe de fila para gerenciar os pedidos e processá-los na ordem correta. Apresente algumas situações para inserir documentos na fila e verificar situações como: o primeiro da fila, o último da fila, quantos estão na fila.
class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        self.queue.append(order)

    def process_first_order(self):
        if not self.is_empty():
            print(f"Processando o pedido: {self.queue[0]}")
            self.queue.pop(0)
        else:
            print("A fila de pedidos está vazia!")

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
    order_queue = OrderQueue()

# Adicionando pedidos à fila
order_queue.add_order("Pedido 1: Hamburguer")
order_queue.add_order("Pedido 2: Pizza")
order_queue.add_order("Pedido 3: Salada")

# Verificando o primeiro pedido da fila
print(f"Primeiro pedido da fila: {order_queue.get_first_order()}")

# Verificando o último pedido da fila
print(f"Último pedido da fila: {order_queue.get_last_order()}")

# Contando quantos pedidos estão na fila
print(f"Quantos pedidos estão na fila: {order_queue.count_orders()}")

# Processando o primeiro pedido da fila
order_queue.process_first_order()

# Verificando se a fila de pedidos está vazia
print(f"A fila de pedidos está vazia? {order_queue.is_empty()}")