# Instruções para Execução do Sistema de Mensagens (Sockets)

Este documento descreve como configurar e executar o servidor e os clientes (Envio e Recebimento) do sistema de chat distribuído.

## Pré-requisitos

* **Python 3.x** instalado.
* Os arquivos `server.py`, `cliente_envia.py` e `cliente_recebe.py` devem estar na mesma pasta ou acessíveis via terminal.

---

## Passo a Passo para Execução

Para o funcionamento correto, a ordem de execução dos terminais é fundamental.

### 1. Iniciar o Servidor
O servidor deve ser o primeiro a ser executado para que as portas de conexão fiquem abertas.
1.  Abra um terminal.
2.  Execute o comando:
    ```bash
    python server.py
    ```
3.  Você deverá ver a mensagem: `Servidor conectado`.

### 2. Iniciar o Cliente de Recebimento (Tela de Histórico)
Este cliente servirá como o seu "monitor" de mensagens.
1.  Abra um **segundo terminal**.
2.  Execute o comando:
    ```bash
    python cliente_recebe.py
    ```
3.  Este terminal enviará automaticamente a identificação `Ouvinte` e ficará aguardando mensagens.

### 3. Iniciar o Cliente de Envio
Este é o terminal onde você interagirá com o chat.
1.  Abra um **terceiro terminal**.
2.  Execute o comando:
    ```bash
    python cliente_envia.py
    ```
3.  O terminal exibirá a mensagem `Digite seu nome`. Insira seu nome e aperte **Enter**.
4.  Após a identificação, você verá o prompt `MSG: `. Digite sua mensagem e envie.

---

## Arquitetura do Teste
Para testar a comunicação entre múltiplos usuários, você pode abrir **mais terminais** de `cliente_envia.py`.

* **Terminal 1:** Servidor (Log de conexões).
* **Terminal 2:** Cliente Recebe (Visualiza todas as mensagens do grupo).
* **Terminal 3:** Cliente Envia (Usuário A).
* **Terminal 4:** Cliente Envia (Usuário B).

Tudo o que for digitado nos terminais de envio deverá aparecer em tempo real no terminal de recebimento, respeitando a ordem da fila protegida por **semáforos** no servidor.

---

##  Possíveis Erros

* **ConnectionRefusedError:** Certifique-se de que o `server.py` foi iniciado antes dos clientes e que a porta escolhida é a mesma em todos os arquivos.
* **Endereço já em uso:** Se você fechar e abrir o servidor muito rápido, a porta pode estar ocupada. Aguarde alguns segundos ou verifique se não há processos Python travados no Gerenciador de Tarefas.