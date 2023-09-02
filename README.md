# desafio_workshop_backend_2023_2
Fábrica de Software 2023.2 - Desafio Workshop BackEnd

# API de uma Loja de Jogos

Esta é uma API que demonstra o funcionamento das 4 operações(get, post, put e delete), usando o Django Rest Framework sobre uma loja de jogos, da qual apresenta o desenvolvedor do jogo e as informações do jogo, tendo também a opção de recolher os dados do cliente durante o processo de compra do jogo. Nesta API, lidei com três entidades principais (serializers, que traduz objetos em representações JSON e vice-versa.): "Jogo", "Desenvolvedor" e "Cliente".

# Instalação
- Baixe os arquivos diretamente do github e utilize uma IDE. Crie um ambiente virtual no terminal e ative ele, baixe os arquivos necessários que estão listados no 'requirements.txt' e inicie o servidor.

# Requisitos
- Python
- Django Rest Framework
- Ambiente Virtual
- Dependências do Projeto (está no arquivo: requirements.txt)

# Funcionalidades Principais
- Você fornece os detalhes do jogo no corpo da solicitação, como o título, desenvolvedor, gênero, plataforma e preço. E também do desenvolvedor (nome e sede) e do cliente (nome, endereço e telefone). Permite listar todos os jogos disponíveis na loja de jogos ou obter detalhes de um jogo específico com base em seu ID e também permite excluir as informações conseguidas com base em seu ID pelo acesso ao admin.
