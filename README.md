# Enriquece Metadados de Veículos via API acesso à APIExterna da Viacep e API da OpenAI
# API Back End - Responsável pelo armazenamento , recuperação das informações de Veículos na base de dados SqlLignt
# Data: 13/04/2025
# Por: Ronaldo Ramos da Costa.
Este pequeno projeto faz parte da entrega do MVP da Disciplina **Arquitetura de Software** 



## Arquitetura da Solução: 
[![Sou uma imagem](Arquitetura_aplicacao.png)](/)


## Situação Problema


Diversos sistemas envolvendo o cadastramento de Metadados, muitas vezes são incompletos e possuem grande dificuldade para encontrar  informações relevantes que possam garantir a completude de uma gama de dados necessários para o bom funcionamento do negócio. A dificuldade de encontrar informações, pode ser apoiada com o uso de APIs e com o uso de Inteligência Artificial.


##  Objetivo


Este experimento tem o objetivo não só utilizar API's externas, para busca externa da localização de um CEP vinculado a um Automóvel, mas como também utilizar a API da OpenAIi - Inteligência Artificial , para complementar informações cruzadas de Automóveis x Localização a partir do CEP , encontrando valores de venda praticados na região geográfica do veículo, bem como obter o  valor de custo de um seguro Anual do automóvel na região do Cep.

Além disso, uma outra busca na IA , coleta informações complementares sobre a Localização do veículo, incluindo Estado, Cidade e rua, trazendo uma percepção que pode justificar algum critério relacionado ao custo do seguro do veículo.


##  Escopo do MVP


Todas as informações utilizadas por este FRON-END são armazenadas no banco de dados acessando a  API de Back-End via Swagger utilizando  5 rotas: GET Lista de Automóveis para o grid, GET único para pesquisa por "Modelo de Automóvel", POST para inserção de Automóvel, e PUT para Atualização de um Automóvel.

As informações cadastradas são recuperadas em grade popdendo ser pesquisadas, editadas, atualizadas , excluídas neste Front End.

Este Front-End também busca informações de CEP na API gratuita da VIACEP, para recuperar informações de uma região a partir do CEP informado.

Este Front-End, como Cenário secundário e complementar busca informações via uso de 4 rotas GET na API da OpenAI (ChatGPT), agregando informações  sobre:
    1) As características impactantes do automóvel
    2) O valor de mercado médio na região recuperada via pesquisa do cep 
    3) O valor de seguro anual para o automóvel na região recuperada via pesquisa do CEP.
    4) Caracteristicas da região envolvendo a Cidade , o bairro e o logradouro da região recuperada via pesquisa do CEP
Também é possível editar estas informações no front end, viabilizando complementar e adicionar qualquer informação relevante.


Este projeto valida o conceito de que é possível enriquecer dados a partir do uso de APIS e Inteligência Artificial. Será de grande importância, pois me apoiará a planejae e desenvolver um serviço de busca de dados e enriquecimento de informações associadas ao Business de Petroleo e Gás, cuja demanda e carência de informações é muito grande.

O MVP contempla o cadastro e recuperação de  atributos vinculados a um automóvel, Regiao pesquisada via CEP e Resultado da Busca de informações complementares na API da OpenAI.


**Funcionalidades do Escopo do MVP**
Este FRONT-END apresenta os modelos cadastrados,viabiliza pesquisa pelo nome do modelo e realiza inclusão/alteração/exclusão/recuperação automóveis a partir do uso da grade que lista os automóveis cadastrados na base de dados. ESTE FRONT_END acessa as seguintes APIS:
    1) MINERA_VEICULO_APP_API-MAIN (BACKEND PRINCIPAL - CENÁRIO 1)
    2) VIACEP (ACESSO EXTERNO - CENÁRIO 1)
    3) BUSCA_DADOS_OPENAI (BACKEND SECUNDÁRIO) 


---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

Não é necessário utilizar nenhuma chave da Open API neste arquivo de Front-End, pois ele solicita e recebe informações do Backend  "BUSCA_DADOS_OPENAI", que é o responsável pela soculta. Este backend sim deverá acessar o serviço via chave.
---

## --------------------------------------------------------------------------------------------------
## Como executar:

## 1-Modo de desenvolvimento:

Basta fazer o download do projeto e abrir o arquivo index.html no seu browser.

## --------------------------------------------------------------------------------------------------

## 2-Utilizando o Docker 

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t nome_da_sua_imagem .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -d -p 8080:80 nome_da_sua_imagem
```

Uma vez executando, para acessar o front-end, basta abrir o [http://localhost:8080/#/](http://localhost:8080/#/) no navegador.




### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).


