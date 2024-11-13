#7. Crie uma calculadora que avalia expressões matemáticas no formato Notação Polonesa Reversa (RPN). Use uma pilha para armazenar os operandos e operadores e realizar os cálculos.
class RPNCalculator:
    def __init__(self):
        self.stack = []

    def push_operand(self, operand):
        self.stack.append(operand)

    def push_operator(self, operator):
        if len(self.stack) >= 2:
            operand2 = self.stack.pop()
            operand1 = self.stack.pop()
            result = self._perform_operation(operand1, operand2, operator)
            self.stack.append(result)
        else:
            print("Erro: não há operandos suficientes para realizar a operação!")

    def get_result(self):
        if len(self.stack) == 1:
            return self.stack[0]
        else:
            print("Erro: a pilha não contém um resultado único!")
            return None

    def _perform_operation(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 != 0:
                return operand1 / operand2
            else:
                print("Erro: divisão por zero!")
                return None
        else:
            print("Erro: operador desconhecido!")
            return None
        calculator = RPNCalculator()

# Adicionando operandos e operadores à pilha
calculator.push_operand(2)
calculator.push_operand(3)
calculator.push_operator('+')
calculator.push_operand(4)
calculator.push_operator('*')

# Realizando os cálculos
print(calculator.get_result())  # Saída: 14.0