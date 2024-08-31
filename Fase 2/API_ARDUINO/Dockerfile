#### CREACIÓN DE IMÁGENES A PARTIR DE UNA APLICACIÓN 
#### Se construye desde la imagen de node corriendo en ALPINE (distro liviana de Linux)
FROM node:19.2-alpine3.16

# cd app
WORKDIR /app

# Destino: /app
COPY package.json ./

# Instalar las dependencias
# se ejecuta en la construcción de la imagen
RUN npm install

# PARA COPIAR TODO EL DIRECTORIO ACTUAL
COPY . .

# Comando run de la imagen
# se ejecuta cuando la imagen se monta y se arranca en el contenedor
# similar a 'command' de docker-compose
CMD [ "npm", "run", "start"]