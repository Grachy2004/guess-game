# Imagen base
FROM python:3.10

# Directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8080

# Comando para correr la app
CMD ["python", "guess_game.py"]
