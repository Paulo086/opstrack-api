# OpsTrack API

API inicial do projeto OpsTrack, desenvolvida com Flask.

![CI](https://github.com/Paulo086/opstrack-api/actions/workflows/ci.yml/badge.svg)

## Executar localmente

```bash
pip install -r requirements.txt
python app.py
```

A aplicação fica disponível em `http://127.0.0.1:5000`.

## Testes e qualidade

Instale as dependências de desenvolvimento:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

Execute o lint:

```bash
flake8 app.py tests --count --max-line-length=88 --statistics
```

Execute os testes com cobertura mínima de 85%:

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=85
```

A integração contínua é executada automaticamente em pushes para `main` e em Pull Requests direcionados à `main`.
