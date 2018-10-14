# DTL-Register-Feedback

## Configurando o ambiente DEV

Requisitos para instalação:
<ul>
    <li>Docker</li>
    <li>Python 3.6.5 (Marcar a opção 'Add python to PATH')</li>
</ul>

### Rodando o projeto

Para a rodar o projeto sem instalar frameworks desnecessários na sua máquina, vamos usar o virtualenv para isolar o ambiente, mas antes vamos precisar do **pip**.

Use o comando `pip install virtualenv` no no seu terminal.

Após a instalação bem sucedidada, entre do diretório/pasta raiz do projeto e rode o comando `python -m venv DTL`.

Rode: `source/DTL/Scripts/activate` Caso o comando source não funcione, abra o terminal na pasta Scripts do projeto e abra o arquivo activate.bat

Com o ambiente virtual ativo, instale as dependências com o comando `pip install -r requeriments.txt`

Após a instalação rode na sequência 
* `python manage.py makemigrations`
* `python manage.py migrate`
* `docker-compose up`
* `python manage.py runserver`


Acesse: localhost:8000 e veja se o serviço está no ar.



## Acessando o banco de dados local
>**User**: postgres
<br>**Password**: admin
<br>**DB**: api_rest
<br>**Name**: api_rest
<br>**Port**: 5432

## Salvando dados via JS

Por motivos de segurança o google chrome bloqueia método POST, retornando uma mensagem de error no console `Allow-Control-Allow-Origin:`

Para resolver o problema, instale e ative este [plugin](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi)
