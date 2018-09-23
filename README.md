# DTL-Register-Feedback

## Configurando o ambiente DEV

Requisitos para instalação:
<ul>
    <li>Docker</li>
    <li>Python 3.6.5</li>
</ul>

### Rodando o projeto

Para a rodar o projeto sem instalar frameworks desnecessários na sua máquina, vamos usar o virtualenv para isolar o ambiente, mas antes vamos precisar do **pip**.

Use o comando `pip install virtualenv` no no seu terminal.

Após a instalação bem sucedidada, entre do diretório/pasta raiz do projeto e rode o comando `python3 -m venv DTL`.

Rode: `source/DTL/Scripts/activate`

Com o ambiente virtual ativo, instale as dependências com o comando `pip install -r requeriments.txt`

Após a instalação rode na sequência `python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`
`docker-compose up`

Acesse: localhost:8000 e veja se o serviço está no ar.