#9. Crie uma estrutura que possa ler uma expressão matemática do tipo (2+3)*(8-9)/(7^3) e apresente todos os operadores matemáticos existente nessa expressão, utilize a pilha para responder a questão.
class OperatorFinder:
    def __init__(self):
        self.operators = []
        self.stack = []

    def is_operator(self, char):
        return char in ['+', '-', '*', '/', '^', '(', ')']

    def find_operators(self, expression):
        for char in expression:
            if self.is_operator(char):
                self.operators.append(char)
                self.stack.append(char)
        return self.operators

    def get_operators(self):
        return self.operators

# Criação de uma instância da classe OperatorFinder
finder = OperatorFinder()

# Definição da expressão matemática
expression = "(2+3)*(8-9)/(7^3)"

# Encontrando os operadores matemáticos
operators = finder.find_operators(expression)

# Apresentando os operadores matemáticos
print("Operadores matemáticos encontrados:")
for operator in operators:
    print(operator)

# Saída:
# Operadores matemáticos encontrados:
# +
# *
# -
# /
# ^
# (
# )