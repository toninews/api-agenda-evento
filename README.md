## Projeto desenvolvido no curso Desenvolvedor Contratado

# api-agenda-evento
Api de Agenda de Evento para criação, listagem, edição e deleção de um evento.

# Passo a passo para roda aplicação

Foi utilizado o Python 3.10

### Instalar as dependências
```
pip install -r requirements-dev.txt
```

### Subir a base de dados PosgreSQL
```
docker-compose up -d
```

### Executar aplicação
```
python manage.py runserver
```

### Documentação da API

A documentação da API está disponível em `http://127.0.0.1:8000/swagger/`

# Convenções de códigos e testes

### Rodar convenção de código:
```
flake8
```

### Rodar testes
```
pytest
```

OBS: Ambos foram implementados no CI (Github Actions)