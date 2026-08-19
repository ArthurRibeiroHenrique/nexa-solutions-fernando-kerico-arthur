FROM python:3.12-slim
WORKDIR /app

# Copia o arquivo da pasta backend para o container
COPY backend/requirements.txt .

# Instala as dependências (Django, etc)
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código da pasta backend
COPY backend/ .