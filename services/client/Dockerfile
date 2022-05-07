FROM node:18-slim as builder

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

FROM builder as development
RUN npm install -D
CMD npm run dev

FROM builder as production
RUN npm run build
CMD npm run start
