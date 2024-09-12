def pertence_fibonacci(numero):
    # Inicializando os primeiros números da sequência de Fibonacci
    a, b = 0, 1
    # Se o número for 0 ou 1, ele pertence à sequência
    if numero == 0 or numero == 1:
        return True

    # Gera a sequência de Fibonacci até encontrar um número maior ou igual ao informado
    while b < numero:
        a, b = b, a + b

    # Verifica se o número é igual ao último número gerado
    return b == numero

# Exemplo de uso
numero = int(input("Digite um número para o Fibonacci: "))
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
