# Chat_Room
Esse é um projeto de chatroom  simples usando `sockets` escrito em `python`. 

O servidor pede por um username quando o cliente se conecta ao chatroom e aceita a conexão. 
Após faz o broadcasts informando da entrada do novo cliente para todos outros clientes conectados no momento.
Tambem informa quando qualquer cliente entra ou sai do chat, realizando o broadcast das situação de entrada/saida.

O servidor atua fazendo o broadcast das mensagens dos clientes para os outros clientes, conectando-os em um chatroom, o servidor não atua como cliente, somente como conector e faz o papel de broadcast.
