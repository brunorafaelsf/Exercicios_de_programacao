# Repositório de Estudos de Programação

Este repositório contém exemplos de códigos simples que estou criando enquanto estudo programação. Aqui, estou documentando os exercícios e desafios que estou resolvendo à medida que aprendo novas tecnologias e conceitos de programação.

## Tecnologias que estou aprendendo

- Python
- Lógica de Programação
- Algoritmos

## Exercícios de Programação

### Exemplo 1: Sequência de Fibonacci

O código abaixo gera a sequência de Fibonacci até o número desejado. O cálculo de Fibonacci é uma sequência onde cada número é a soma dos dois anteriores. A sequência começa com 0 e 1, e os números subsequentes são calculados dessa maneira.

#### Código:

```python
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
