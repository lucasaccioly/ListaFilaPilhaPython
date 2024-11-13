#6. Imagine que você está desenvolvendo um navegador web simplificado. Use uma pilha para armazenar o histórico de páginas visitadas pelos usuários e implementar as funcionalidades de voltar e avançar na navegação.
class Browser:
    def __init__(self):
        self.stack = []

    def visit(self, page):
        self.stack.append(page)

    def back(self):
        if len(self.stack) > 1:
            self.stack.pop()
            print(f"Voltando para: {self.stack[-1]}")
        else:
            print("Você está na página inicial!")

    def forward(self):
        if self.forward_stack:
            page = self.forward_stack.pop()
            self.stack.append(page)
            print(f"Avançando para: {page}")
        else:
            print("Você está na página mais recente!")

    def current_page(self):
        if self.stack:
            return self.stack[-1]
        else:
            return "Página inicial"

    def __init_forward_stack(self):
        self.forward_stack = []

    def __str__(self):
        return f"Página atual: {self.current_page()}"
    browser = Browser()

# Visitando páginas
browser.visit("reddit.com")
browser.visit("tumblr.com")
browser.visit("55chan.com")

print(browser)  

# Voltando para a página anterior
browser.back()
print(browser)  

# Avançando para a página seguinte
browser.forward()
print(browser)  

# Voltando para a página anterior novamente
browser.back()
browser.back()
print(browser)  

# Avançando para a página seguinte novamente
browser.forward()
browser.forward()
print(browser)  