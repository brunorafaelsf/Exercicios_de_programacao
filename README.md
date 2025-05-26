# Repositório de Estudos de Programação

Este repositório contém exemplos de códigos simples que estou criando enquanto estudo programação. Aqui, estou documentando os exercícios e desafios que estou resolvendo à medida que aprendo novas tecnologias e conceitos de programação.

## Tecnologias que estou aprendendo

- Python
- Lógica de Programação
- Algoritmos

## Exercícios de Programação

### Exemplo 1: Sequência de Fibonacci / Fatorial

Os códigos abaixo geram a sequência de Fibonacci e o calculo do fatorial de um numero.

#### Código:

```python
# Função para calcular o enésimo número de Fibonacci
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
