# Usa una imagen oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto que Gunicorn usará
EXPOSE 8080

# Usa Gunicorn para correr la app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "guess_game:app"]