# Ecommerce News Backend

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar el scraper periódicamente

```bash
python scheduler.py
```

## Ejecutar la API

```bash
uvicorn main:app --reload
```

## Endpoint
- `GET /news`: Devuelve las últimas noticias guardadas de ecommercetimes.com 