#8. Em um programa de edição de texto, implemente a funcionalidade de "Desfazer" e "Refazer" usando uma pilha para armazenar o histórico de comandos executados pelo usuário.
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        self.undo_stack.append(self.text)
        self.text = command(self.text)
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
        else:
            print("Não há comandos para desfazer!")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
        else:
            print("Não há comandos para refazer!")

    def get_text(self):
        return self.text

# Definição de comandos
def insert_text(text, new_text):
    return text + new_text

def delete_text(text, num_chars):
    return text[:-num_chars]

def replace_text(text, old_text, new_text):
    return text.replace(old_text, new_text)

# Criação de uma instância da classe TextEditor
editor = TextEditor()

# Execução de comandos
editor.execute_command(lambda text: insert_text(text, "Olá, mundo!"))
editor.execute_command(lambda text: insert_text(text, " Este é um exemplo de texto."))
editor.execute_command(lambda text: delete_text(text, 10))

# Desfazer comandos
editor.undo()
print(editor.get_text())  # Saída: "Olá, mundo! Este é um exemplo de texto."

# Refazer comandos
editor.redo()
print(editor.get_text())  # Saída: "Olá, mundo! Este é um exemplo de texto."

# Execução de outro comando
editor.execute_command(lambda text: replace_text(text, "mundo", "usuário"))

# Desfazer comandos novamente
editor.undo()
print(editor.get_text())  # Saída: "Olá, mundo! Este é um exemplo de texto."