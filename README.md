# Desafio Back-End Django CNAB 🐍🚀

Bem-vindo ao repositório do meu desafio back-end com Django enquanto eu estava na Kenzie Academy Brasil! Este projeto, chamado Banco de Dados CNAB, tem como objetivo facilitar o cadastro, leitura e localização de dados de arquivos CNAB.

## Funcionalidades ✨

- Cadastro de arquivo CNAB por cliente/loja.
- Listagem de cliente/loja com histórico de transações.

## Tecnologias Utilizadas 🛠️

- Python
- Django Rest Framework
- SQLite
- [DRF Espetacular](https://drf-espectacular.readthedocs.io/)

## Instalação 🚀

**1° Passo:** Crie seu ambiente virtual:

```bash
python -m venv venv
```

[Mais informações sobre ambientes virtuais](https://docs.python.org/3/library/venv.html)

**2° Etapa:** Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

**3° Passo:** Execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

**4° Passo:** Inicie o servidor:

```bash
python manage.py runserver
```

**5° Passo:** Acesse a aplicação em [http://localhost:8000/](http://localhost:8000/)

## Uso do Aplicativo 🚀

**Link do Servidor Comum:** [http://localhost:8000/](http://localhost:8000/)

**Cadastro CNAB:** Para fazer upload e registrar seu arquivo CNAB, adicione o sufixo `api/` ao link do servidor para acessar o formulário de envio. Após o envio, você receberá uma resposta de sucesso do servidor se tudo correr bem!

**Lista de Lojas e Transações:** Para listar todas as lojas e suas transações, adicione o sufixo `api/list/` ao link do servidor.

Divirta-se explorando o projeto! Contribuições e feedbacks são sempre bem-vindos. Vamos construir algo incrível juntos! 🚀😊
