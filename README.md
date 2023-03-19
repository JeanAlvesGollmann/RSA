# RSA
Eu criei um código de criptografia RSA sem utilizar a biblioteca rsa do python, que transporta os dados para um código "Server" com base no protocolo UDP.

Para executar o código é necessário o uso de 2 bibliotecas:
1° A biblioteca para utilizar o protocolo UDP a biblioteca socket > pip install sockets
2° A biblioteca que busca números primos de 4096 bits no python a biblioteca pycryptodome > pip install pycryptodome

Processo:
- Assim que é iniciado o server, ele fica aguardando a entrada da chave publica
- O cliente por sua vez, quando é iniciado começa a gerar as chaves públicas e privadas para enviar os dados da pública para o server
- Após receber a chave, o Server começa a criptografar letra por letra da frase fixa no código e começa a enviar para o cliente
- O cliente ao receber aramazena os valores em uma lista
- No cliente é executado um loop pela lista para decriptografar todas os códigos da lista
- Assim que o código é decriptografado ele é convertido para a letra da tabela ascii e depois é adicionado em uma string para poder montar a frase completa emitida pelo Server.

