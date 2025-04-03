import socket

def servidor_udp():
    # Criando o socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Definindo o endereço e a porta para escutar
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    print("Servidor esperando mensagens na porta 12345...")

    while True:
        # Recebendo a mensagem
        data, client_address = server_socket.recvfrom(4096)
        print(f"Recebido: {data.decode()} de {client_address}")  # Corrigido: agora estamos chamando o método decode()

        # Enviando uma resposta
        response = f"Mensagem recebida: {data.decode()}"
        server_socket.sendto(response.encode(), client_address)

# Rodando o servidor UDP
servidor_udp()
