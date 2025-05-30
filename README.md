
# Desafio DevOps 2025

## Estrutura do Projeto

Este projeto consiste em duas aplicações:
- **Node.js** (porta 3000) com cache de 10 segundos.
- **Flask (Python)** (porta 5005) com cache de 60 segundos.

## Como executar

1. Clone este repositório:
```bash
git clone <repo-url>
cd devops-desafio
```

2. Execute os containers:
```bash
docker-compose up --build
```

## Rotas disponíveis

### Aplicação Node.js
- `GET /ping` → texto fixo
- `GET /time` → hora do servidor (cache 10s)

### Aplicação Flask
- `GET /ping` → texto fixo
- `GET /time` → hora do servidor (cache 60s)

## Observações
- Cada aplicação está containerizada com Docker.
- A estrutura está preparada para futuras melhorias como Redis, Prometheus, CI/CD etc.
