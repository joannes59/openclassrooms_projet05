FROM python:3.11-slim

WORKDIR /code

# Copier dependencies
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le projet
COPY . .

# Port HuggingFace
EXPOSE 7860

# Lancer Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
