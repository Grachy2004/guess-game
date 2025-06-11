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

CMD ["gunicorn", "-b", "0.0.0.0:8080", "guess_game:app"]

