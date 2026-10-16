FROM node:20

WORKDIR /app

RUN npm install --global pnpm@10.34.7
COPY package.json pnpm-lock.yaml .npmrc ./
RUN pnpm install --frozen-lockfile

COPY . .

ARG VITE_API_URL=http://0.0.0.0:8000/predict
ARG VITE_API_WORKS=true

ENV VITE_API_URL=${VITE_API_URL}
ENV VITE_API_WORKS=${VITE_API_WORKS}

EXPOSE 3000

CMD ["pnpm", "run", "dev"]
