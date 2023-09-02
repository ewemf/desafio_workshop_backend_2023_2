# desafio_workshop_backend_2023_2
Fábrica de Software 2023.2 - Desafio Workshop BackEnd

# API de uma Loja de Jogos

Esta é uma API que demonstra o funcionamento das 4 operações(get, post, put e delete), usando o Django Rest Framework sobre uma loja de jogos. Nesta API, estamos lidando com três entidades principais (serializers, que converte objetos em representações JSON e vice-versa.): "Jogo", "Desenvolvedor" e "Cliente".

Baixe os arquivos e utilize uma IDE. Crie um ambiente virtual no terminal e ative ele, baixe os arquivos necessários que estão listados no 'requirements.txt' e inicie o servidor. A API usa um banco de dados SQLite. 

- Você fornece os detalhes do jogo no corpo da solicitação, como o título, desenvolvedor, gênero, plataforma e preço. E também do desenvolvedor (nome e sede) e do cliente (nome, endereço e telefone). Permite listar todos os jogos disponíveis na loja de jogos ou obter detalhes de um jogo específico com base em seu ID e também permite excluir um jogo da loja de jogos com base em seu ID.
