# Função para calcular o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicita o número ao usuário
num = int(input("Digite um número para calcular o fatorial: "))

# Calcula e exibe o fatorial
print(f"O fatorial de {num} é: {fatorial(num)}")
