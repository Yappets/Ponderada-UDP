# client.py
import socket

def cliente_udp():
    # Criando o socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Definindo o endereço do servidor
    server_address = ('localhost', 12345)

    try:
        # Enviando uma mensagem para o servidor
        message = "Olá, servidor!"
        client_socket.sendto(message.encode(), server_address)

        # Recebendo a resposta do servidor
        data, server = client_socket.recvfrom(4096)
        print(f"Resposta do servidor: {data.decode()}")

    finally:
        client_socket.close()

# Rodando o cliente UDP
cliente_udp()
