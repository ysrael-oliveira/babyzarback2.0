# Babyzar 2.0

Babyzar combina Baby (Bebê) + Bazar e visa simplificar o controle de roupas dos bebês, que facilmente se perdem. Os pais poderão então registrar qual valor de compra e já sugerir um valor de venda, facilitando o uso sustentável de roupas e permitindo a geração de uma renda extra para que os pais possam comprar fraldas.
A nova versão do projeto apresenta uma ferramenta de atualização de preços, bem como uma ferramenta de conversão para moeda estrangeiras, visando atingir os mercados de Argentina, Estados Unidos e Europa.

## Índice

1. [Sobre]
2. [Arquitetura]
3. [Execução]
4. [Tecnologias usadas]
5. [Autor]

## Sobre
Este projeto é uma API que visa controlar as roupas de um bebê, podendo ser usada por pais para ter o estoque de roupas e desde já planejar a venda das mesmas. Ela permite adicionar, remover e consultar as roupas que estão no banco de dados, bem como atualizar o preço das mesmas

## Arquitetura

![Arquitetura do MVP](<Arquitetura-MVP.png>)

A Interface constitui um sistema de registro de peças disponíveis para a venda, que se comunica com um módulo API que permite a inserção de novas peças, a deleção de peças já vendidas, a atualização de preço de peça e a listagem de todas as peças disponíveis. A Interface se comunica ainda com a Currency Data API, que retorna o cálculo em tempo real do preço da peça selecionada em moeda estrangeira.

A [Currency Data API] (https://apilayer.com/marketplace/currency_data-api?utm_source=apilayermarketplace&utm_medium=featured) é uma api externa que permite o cálculo do câmbio de moedas, de acordo com a cotação em tempo real. No presente projeto, foi utilizada a requisição GET da rota /convert, que permite converter um valor para outra moeda.

A API externa utilizada é gratuita até o limite de 100 utilizações, após cadastro prévio. A APIKey utilizada foi incluída na submissão do MVP, não sendo necessário cadastro adicional.

## Execução (através do Docker)
1. Navegue para o diretório referente a pasta babyzar_api
   ```
   $ cd babyzar_api
   ```
2. Certifique-se de ter o [Docker] (https://docs.docker.com/) instalado e em execução na sua máquina.
    Primeiramente, execute o comando para construção da imagem (confirme que está no mesmo diretório da Dockerfile):
    ```
    $ docker build -t nome_da_imagem .  
    ```
    Em seguida, execute a imagem através do comando:
    ```
    $ docker run -p 5000:5000 nome_da_imagem 
    ```
3. Em um navegador, abra o endereço http://localhost:5000/ para acessar o swagger da aplicação.

## Tecnologias usadas
Python
Flask
SQLAlchemy
Docker

## Autor
Ysrael Oliveira
