def contar_letra_a(texto):
    # Converte o texto completo para minúsculo e conta a letra 'a'
    return texto.lower().count('a')

# Exemplo de uso
texto = input("Digite uma string: ")
quantidade = contar_letra_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes.")
