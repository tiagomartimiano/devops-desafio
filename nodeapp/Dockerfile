
FROM node:18-alpine
WORKDIR /app
COPY index.js .
RUN npm install express node-cache
EXPOSE 3000
CMD ["node", "index.js"]
