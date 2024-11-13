#2. Você está desenvolvendo um sistema de fila de atendimento para um banco. Os clientes entram na fila e são atendidos pelos funcionários na ordem de chegada. Use a classe de fila para simular o atendimento dos clientes. Apresente algumas situações para inserir documentos na fila e verificar situações como: o primeiro da fila, o último da fila, quantos estão na fila.
class BankQueue:
    def __init__(self):
        self.queue = []

    def add_client(self, client):
        self.queue.append(client)

    def attend_first_client(self):
        if not self.is_empty():
            print(f"Atendendo o cliente: {self.queue[0]}")
            self.queue.pop(0)
        else:
            print("A fila está vazia!")

    def get_first_client(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def get_last_client(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return None

    def count_clients(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
    bank_queue = BankQueue()

# Adicionando clientes à fila
bank_queue.add_client("João")
bank_queue.add_client("Maria")
bank_queue.add_client("Pedro")

# Verificando o primeiro cliente da fila
print(f"Primeiro cliente da fila: {bank_queue.get_first_client()}")

# Verificando o último cliente da fila
print(f"Último cliente da fila: {bank_queue.get_last_client()}")

# Contando quantos clientes estão na fila
print(f"Quantos clientes estão na fila: {bank_queue.count_clients()}")

# Atendendo o primeiro cliente da fila
bank_queue.attend_first_client()

# Verificando se a fila está vazia
print(f"A fila está vazia? {bank_queue.is_empty()}")