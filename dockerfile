# Imagen base
FROM python:3.10

# Directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 80

# Comando para correr la app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "guess_game:app"]

