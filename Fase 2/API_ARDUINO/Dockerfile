FROM node:lts-alpine

# cd app
WORKDIR /app

# Destino: /app
# COPY package.json ./

# Instalar las dependencias
# se ejecuta en la construcción de la imagen
#RUN npm config set registry https://registry.npmjs.org/
# RUN npm install

# PARA COPIAR TODO EL DIRECTORIO ACTUAL
COPY . .

# RUN npm install
RUN npm install --force

# Expone el puerto en el que la aplicación se ejecutará


EXPOSE 8080


# Comando run de la imagen
# se ejecuta cuando la imagen se monta y se arranca en el contenedor
# similar a 'command' de docker-compose
CMD [ "npm", "run", "start"]