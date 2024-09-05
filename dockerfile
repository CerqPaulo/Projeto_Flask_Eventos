# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# RUN apt-get update && apt-get install -y netcat


# Copie o conteúdo do projeto para o contêiner
COPY . .

# Exponha a porta em que a aplicação Flask rodará
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "main.py"]
