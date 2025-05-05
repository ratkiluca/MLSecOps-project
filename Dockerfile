# 1. Alap python image
FROM python:3.10-slim

# 2. Mappa beállítás
WORKDIR /app

# 3. Csak a szükséges fájlokat másoljuk be
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Projekt fájlok bemásolása
COPY . .

# 5. Port expozíció (REST API)
EXPOSE 8000

# 6. API indítása
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
