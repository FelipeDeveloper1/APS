# Função de chave para garantir que a chave tenha 16 caracteres
def ajusta_chave(chave):
    return chave.ljust(16, ' ').encode('utf-8')[:16]

# Função de XOR para simular a nossas cifragem
def cifra_xor(mensagem, chave):
    chave = ajusta_chave(chave)
    # Converte a mensagem e a chave para uma lista de bytes
    mensagem_bytes = mensagem.encode('utf-8')
    resultado = bytearray()
    
    # XOR entre cada byte da mensagem e da chave que iremos colocar
    for i in range(len(mensagem_bytes)):
        resultado.append(mensagem_bytes[i] ^ chave[i % len(chave)])  # A chave é repetida se for menor do que o que precisamos
    
    return bytes(resultado)

# Função para decifrar, que é o mesmo processo de cifrar
def decifra_xor(mensagem_cifrada, chave):
    chave = ajusta_chave(chave)
    resultado = bytearray()
    
    # XOR entre cada byte da mensagem cifrada e da chave que iremos colocar
    for i in range(len(mensagem_cifrada)):
        resultado.append(mensagem_cifrada[i] ^ chave[i % len(chave)])  # A chave é repetida se for menor do que o que precisamos
    
    return bytes(resultado).decode('utf-8')

# Função principal onde podemos escrever a mensagem e a chave
def main():
    mensagem = input("Digite a mensagem que deseja cifrar: ")
    chave = input("Digite a chave (até 16 caracteres): ")

    # Cifra a mensagem
    mensagem_cifrada = cifra_xor(mensagem, chave)
    print(f"Mensagem cifrada: {mensagem_cifrada.hex()}")  # Vai exibir a mensagem cifrada

    # Decifra a mensagem que escrevemos
    mensagem_decifrada = decifra_xor(mensagem_cifrada, chave)
    print(f"Mensagem decifrada: {mensagem_decifrada}")

# Chama a função principal
if __name__ == "__main__":
    main()
