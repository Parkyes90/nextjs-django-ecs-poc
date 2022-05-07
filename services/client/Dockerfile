FROM node:18-slim as builder

WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install --only=prod
RUN export PATH=/usr/src/app/node_modules/.bin:$PATH

COPY . ./

EXPOSE 3000

FROM builder as production
RUN npm run build
CMD npm run start

FROM builder as development
RUN npm install -D
