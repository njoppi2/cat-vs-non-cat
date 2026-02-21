FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

ARG VITE_API_URL=http://0.0.0.0:8000/predict
ARG VITE_API_WORKS=true

ENV VITE_API_URL=${VITE_API_URL}
ENV VITE_API_WORKS=${VITE_API_WORKS}

EXPOSE 3000

CMD ["npm", "run", "dev"]
