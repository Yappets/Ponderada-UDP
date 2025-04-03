
# Comunicação UDP - Cliente e Servidor

Este projeto implementa a comunicação entre um **cliente** e um **servidor** utilizando o protocolo **UDP**. O cliente envia uma mensagem para o servidor, e o servidor responde com uma confirmação. O código foi escrito em **Python**.

## Como Executar o Código

### 1. Instalações Necessárias
Certifique-se de ter o **Python** instalado na sua máquina. Você pode verificar a instalação do Python com o seguinte comando:

```bash
python --version
```

### 2. Passos para Executar o Código
Para executar o código, você precisará rodar tanto o servidor quanto o cliente em terminais separados. Siga os passos abaixo:

#### Executando o Servidor
1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `server.py` está localizado. Se você estiver no mesmo diretório que o arquivo, use o comando `cd` para navegar para o diretório correto.
3. Execute o servidor com o seguinte comando:

   ```bash
   python server.py
   ```

4. Você verá a seguinte mensagem no terminal do servidor:

   ```
   Servidor esperando mensagens na porta 12345...
   ```

Isso significa que o servidor está aguardando por mensagens na porta 12345.

#### Executando o Cliente
1. Abra outro terminal ou prompt de comando (não feche o terminal do servidor).
2. Navegue até o diretório onde o arquivo `cliente.py` está localizado.
3. Execute o cliente com o seguinte comando:

   ```bash
   python cliente.py
   ```

4. Você verá a resposta do servidor no terminal do cliente:

   ```
   Resposta do servidor: Mensagem recebida: Olá, servidor!
   ```

### 3. Fluxo de Comunicação
- O servidor escuta as mensagens na porta 12345.
- O cliente envia uma mensagem ao servidor, no caso "Olá, servidor!".
- O servidor recebe a mensagem, a imprime no terminal e envia uma resposta de volta ao cliente.

