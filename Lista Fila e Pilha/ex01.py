#1. Você está desenvolvendo um sistema de fila de impressão para uma empresa. Os documentos são adicionados à fila e impressos na ordem em que foram recebidos. Implemente um programa Python que use a classe de fila para simular esse processo. Apresente algumas situações para inserir documentos na fila e verificar situações como: o primeiro da fila, o último da fila, quantos estão na fila.
class PrintQueue:
    def __init__(self):
        self.queue = []

    def add_document(self, document):
        self.queue.append(document)

    def print_first_document(self):
        if not self.is_empty():
            print(f"Imprimindo o documento: {self.queue[0]}")
            self.queue.pop(0)
        else:
            print("A fila está vazia!")

    def get_first_document(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def get_last_document(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return None

    def count_documents(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
    print_queue = PrintQueue()

# Adicionando documentos à fila
print_queue.add_document("Documento 1")
print_queue.add_document("Documento 2")
print_queue.add_document("Documento 3")

# Verificando o primeiro documento da fila
print(f"Primeiro documento da fila: {print_queue.get_first_document()}")

# Verificando o último documento da fila
print(f"Último documento da fila: {print_queue.get_last_document()}")

# Contando quantos documentos estão na fila
print(f"Quantos documentos estão na fila: {print_queue.count_documents()}")

# Imprimindo o primeiro documento da fila
print_queue.print_first_document()

# Verificando se a fila está vazia
print(f"A fila está vazia? {print_queue.is_empty()}")