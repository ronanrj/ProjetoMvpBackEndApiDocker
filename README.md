# ProjetoMVP backEnd API
ProjetoMVP backEnd API - Este projeto faz parte da entrega para conclusão do mvp da sprint Arquitetura de Software do curso de pós graduação da PUC RIO.

O objetivo do projeto é um cadastro simples de auto escolas com relacionamento de carros e instrutores em uma base de dados sqlite e a contenerização utilizando docker.
A Api backend , quando solicitada pelos metodos POST e PUT , realiza uma conexão http-get , passando um cep válido, para a API externa ViaCEP (https://viacep.com.br/) , retornando o endereço completo e atualizando no banco de dados sqlite.

![image](https://github.com/ronanrj/ProjetoMvpBackEndApiDocker/assets/20301129/7ddb1d4e-1155-41bc-bdd1-95a013510329)



---
### Instalação
Foi utilizado o python 3.12.0

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

> Ambiente virtual Python

Cria o ambiente virtual com o comando
```
 python -m venv env
```

Após, ativar o ambiente com o comando no powershell
```
.\env\Scripts\Activate.ps1
```

Após, será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

```
(env)$ pip install -r requirements.txt
---
### Executando o servidor


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

---
### Acesso no browser

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t back-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 back-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.



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
