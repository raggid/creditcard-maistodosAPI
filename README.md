# Credit Card API

Este projeto é um exemplo de uma possível implementação de uma API  
para gerenciamento de dados de cartões de crédito, que pode então ser  
utilizada em qualquer tipo de software que dependa desses dados.


**OBS: A documentação está escrita em português visando ser mais clara para o time,  
porém, se necessário, estou a disposição para fazer a tradução para o inglês.**


### Instruções de execução

Incluida neste projeto está uma configuração de containers do docker, utilizando docker compose, para facilidade de execução e uma futura implantação, dessa forma, para executar o projeto de forma facilitada é necessário ter tanto o [Docker](https://docs.docker.com/engine/)  quanto o [Docker Compose](https://docs.docker.com/compose/) instalados.

Para a instalação do Docker e Docker Compose siga as instruções específicas para a sua distribuição contidas em:
1. [Docker Installation](https://docs.docker.com/engine/install/).
2. [Docker Compose Install](https://docs.docker.com/compose/install/linux/#install-using-the-repository).
3. [Docker Non Root User](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

Finalizadas essas etapas, basta executar, estando na pasta raíz do projeto, o comando:
`docker compose up -d`

Este comando irá iniciar um container do banco de dados [Postgres](https://www.postgresql.org/), um container contendo a API, e um container contendo o [Adminer](https://www.adminer.org/) para realizar consultas básicas no banco de dados.

### Swagger e Openapi
A aplicação fornece uma documentação interativa atraves da especificação [OpenApi](https://www.openapis.org/) e da ferramenta [SwaggerUI](https://swagger.io/tools/swagger-ui/), que permite visualizar e interagir com os recursos da API pelo navegador.
Para abrir essa documentação, voce deve acessar no seu navegador o endereço:
`http://localhost:8000/docs`

Você deve ver a seguinte pagina:
![Alt text](images/image-1.png)
Aqui você encontra todas as rotas disponíveis na aplicação, vê exemplos de como realizar requisições a cada rota, e pode executar as requisições diretamente .

### Login

A aplicação possui proteção em todas as rotas de gerenciamento  de dados de cartões de cŕedito, utilizando o protocolo [OAuth2](https://oauth.net/2/) com esquema de autenticação por Usuário e Senha. Para realizar qualquer requisição a essas rotas, é necessário primeiro realizar o login.

Esse login pode ser realizado via documentação interativa ou realizando uma requisição utilizando ferramentas como [Curl](https://curl.se/) ou [Postman](https://www.postman.com/).

##### Documentação Interativa
Na documentação interativa, basta realizar a requisição a rota `/api/v1/login/access-token` do grupo Login.
Clique no botão:
![Alt text](images/image-3.png)
Preencha os dados `username` e `password` com os dados:
username: admin@mail.com
password: superpass
![Alt text](images/image-4.png)
E clique no botão Execute
![Alt text](images/image-5.png)

No corpo da resposta você vai encontrar um `access_token` e um `token_type`.
![Body with Token](images/image-6.png)
Este `access_token` deve ser enviado em todas as requisições de cartão de crédito, no header da requisição.

**Importante: Este processo deve ser realizado para a obtenção do token a ser utilizado em requisições realizadas por fora da documentação interativa.  
Para poder realizar as requisições pela própria documentação, basta realizar a autenticação provida pelo Swagger.**
![Authorize](images/image-7.png)
Utilizando o mesmo usuário e senha:

![Authorization](images/image-8.png)
![Authorized](images/image-9.png)


##### Postman, Thunder e Outros

Da mesma forma, basta realizar uma requisição do tipo `POST` a rota `http://localhost:8000/api/v1/login/access-token` passando `username` e `password` como **Form** no corpo da requisição.
![Thunder Client](images/image-10.png)

### Realizando Requisições
Após ter realizado o login, basta utilizar o `access_token` como header de autorização em todas as requisições.

No Thunder Client, basta realizar uma requisição para qualquer rota de cartões de crédito, adicionando o token à aba **Auth** do tipo **Bearer**.
Como exemplo, vamos realizar uma requisição `GET` à rota `/api/v1/credit-card`, que vai nos devolver uma lista com todos os cartões cadastrados.

Configurando a autenticação:
![Alt text](images/image.png)
Resposta da requisição:
![Alt text](images/image-11.png)

Como alternativa, é possivel passar o header `Authorization` com o conteúdo `Bearer access_token` para realizar a autorização. Esta é a alternativa que deve ser utilizada em ferramentas de linha de comando como o `curl`.
![Alt text](images/image-12.png)

Exemplo utilizando o curl:
```console
curl --location 'http://localhost:8000/api/v1/credit-card' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTYzNTg3NzksInN1YiI6IjMifQ.fgiqmVNLmczFEHFXgcmmHqiUB4ub2KAXpEBHi3vVlZU'
```

**IMPORTANTE: Este token tem duração limitada e deve ser gerado novamente em caso de estar expirado.**

## Arquitetura, Bibliotecas e Motivações

Este projeto apresenta uma arquitetura simples, onde a aplicação responsável pelas requisições se comunica com um banco de dados POSTGRES em ambiente de "produção", e utiliza um banco SQLITE durante a execução dos testes.
![Alt text](images/image-13.png)

A aplicação em si foi desenvolvida utilizando a biblioteca [FastAPI](https://fastapi.tiangolo.com/), que favorece o desenvolvimento rapido de APIs de alta performance por fazer uso do [Starlette](https://www.starlette.io/), um framework que permite o desenvolvimento de serviços web assíncronos. 

Foi utilizada também a biblioteca [Pydantic](https://docs.pydantic.dev/latest/), integrada ao FastAPI, para a serialização, deserialização e validação dos dados das requisições e respostas da API. Com esta biblioteca podemos validar que todos os dados que entram na aplicação estão no formato esperado e com valores válidos, e da mesma forma podemos validar os dados de saída da API.

Utilizei [SQLAlchemy](https://www.sqlalchemy.org/) como [ORM](https://pt.wikipedia.org/wiki/Mapeamento_objeto-relacional) da aplicação, para permitir que as definições e operações de dados na aplicação sejam independentes do banco de dados utilizado, sendo possível trocar o banco quando necessário.

A biblioteca [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) foi utilizada para a geração de [Migrations](https://kenzie.com.br/blog/migrations/) de forma automatica, e para a atualização do esquema no banco de dados em caso de modificações nas tabelas. Dessa forma, não precisamos nos preocupar em fazer alterações direto no banco de dados, além de conseguirmos manter um histórico de modificações por meio das revisões geradas.

Para a criptografia de senhas foi utilizada a biblioteca [Passlib](https://passlib.readthedocs.io/en/stable/) com [Bcrypt](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html?highlight=bcrypt) como backend de criptografia. Para geração e decodificação do token de acesso foi utilizada a biblioteca [Python Jose](https://pypi.org/project/python-jose/). Essas bibliotecas em conjunto garantem a segurança da aplicação e das senhas de usuário, que não são mantidas em nossos bancos de dados.

Para testes foi utilizada a biblioteca [Pytest](https://docs.pytest.org/en/7.4.x/), além do módulo `TestClient` da Starlette para testes de integração.

Foi utilizado [Uvicorn](https://www.uvicorn.org/) como servidor da API, pois ele suporta aplicações que trabalham de forma assícrona.