#10. Palíndromos são palavras, frases ou sequências que mantêm sua mesma forma quando invertidos. Por exemplo, a palavra "radar" é um palíndromo, pois se você a ler de trás para frente, ela ainda será "radar". Construa um programa que possa ler uma palavra ou frase e dizer se ela é um Palíndromo, use a estrutura de pilha para responder essa questão.
class PalindromeChecker:
    def __init__(self):
        self.stack = []

    def is_palindrome(self, word):
        # Remover espaços e converter para minúsculas
        word = word.replace(" ", "").lower()

        # Empilhar os caracteres da palavra
        for char in word:
            self.stack.append(char)

        # Desempilhar os caracteres e comparar com a palavra original
        reversed_word = ""
        while self.stack:
            reversed_word += self.stack.pop()

        # Verificar se a palavra é um palíndromo
        return word == reversed_word

    def check_palindrome(self, word):
        if self.is_palindrome(word):
            print(f"A palavra '{word}' é um palíndromo.")
        else:
            print(f"A palavra '{word}' não é um palíndromo.")

# Criação de uma instância da classe PalindromeChecker
checker = PalindromeChecker()

# Definição da palavra ou frase
word = "radar"

# Verificar se a palavra é um palíndromo
checker.check_palindrome(word)

# Saída:
# A palavra 'radar' é um palíndromo.