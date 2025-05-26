# Função para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicita o número de termos ao usuário
num = int(input("Quantos termos da sequência de Fibonacci você deseja? "))

# Exibe a sequência
print(f"Sequência de Fibonacci até o {num}-ésimo termo:")
for i in range(num):
    print(fibonacci(i), end=" ")
