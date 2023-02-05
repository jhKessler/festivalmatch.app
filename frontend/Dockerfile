# pull official base image
FROM node:16-alpine
WORKDIR /app

COPY package.json .
COPY package-lock.json .
RUN npm ci --legacy-peer-deps

COPY . .
RUN npm run build
RUN npm install --global serve

CMD [ "serve", "-s", "build" ]