#4. Você está criando um aplicativo de lista de tarefas pendentes. As tarefas são adicionadas à fila concluídas uma por uma. Use a classe de fila para implementar a lista de tarefas e concluir as tarefas na ordem em que foram adicionadas.
class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        self.queue.append(task)

    def complete_first_task(self):
        if not self.is_empty():
            print(f"Concluindo a tarefa: {self.queue[0]}")
            self.queue.pop(0)
        else:
            print("A lista de tarefas está vazia!")

    def get_first_task(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def get_last_task(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return None

    def count_tasks(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0
    task_queue = TaskQueue()

# Adicionando tarefas à fila
task_queue.add_task("Tarefa 1: Comprar leite")
task_queue.add_task("Tarefa 2: Fazer exercícios")
task_queue.add_task("Tarefa 3: Estudar para a prova")

# Verificando a primeira tarefa da fila
print(f"Primeira tarefa da fila: {task_queue.get_first_task()}")

# Verificando a última tarefa da fila
print(f"Última tarefa da fila: {task_queue.get_last_task()}")

# Contando quantas tarefas estão na fila
print(f"Quantas tarefas estão na fila: {task_queue.count_tasks()}")

# Concluindo a primeira tarefa da fila
task_queue.complete_first_task()

# Verificando se a lista de tarefas está vazia
print(f"A lista de tarefas está vazia? {task_queue.is_empty()}")