# TDD com Python e Django

## Configurações Iniciais
1. Download do [Python 3](https://www.python.org/downloads/).
2. Instale o [Geckodriver](https://github.com/cristianpenteado/tdd-django/wiki/Configura%C3%A7%C3%A3o-Geckodriver-e-Firefox).
3. Crie um [ambiente virtual](https://docs.python.org/pt-br/3/tutorial/venv.html#creating-virtual-environments).
4. Faça o clone: `git clone git@github.com:cristianpenteado/tdd-django.git`.
5. Entre na pasta do repositório: `cd tdd-django/`.
6. Ative o [ambiente virtual](https://docs.python.org/pt-br/3/tutorial/venv.html#creating-virtual-environments).
7. Atualize o pip: `python -m pip install --upgrade pip`
8. Instale as dependências: `pip install -r requirements.txt`

### Comandos úteis
- Execussão do servidor Django: `python manage.y  runserver`
- Execussão dos testes funcionais: `python functional_tests.py`
- Execussão dos testes de unidade: `python manage.py test`
- Execussão das migrations: `python manage.py makemigrations`
- Criação do arquivo db.sqlite3 `python manage.py migration`