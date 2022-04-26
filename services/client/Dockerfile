FROM node:18-slim

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm i -y && \
    npm install -D @swc/cli @swc/core

COPY . .

EXPOSE 3000
