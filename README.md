
# Desafio DevOps 2025

## Estrutura do Projeto

Este projeto consiste em duas aplicações:
- **Node.js** (porta 3000) com cache de 10 segundos.
- **Flask (Python)** (porta 5000) com cache de 60 segundos.

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

## Pontos de Melhoria

### Técnicos:

- Substituir cache local por Redis em produção, permitindo consistência entre múltiplas instâncias.
- Adicionar testes automatizados e CI/CD via GitHub Actions ou GitLab CI.
- Utilizar NGINX como gateway reverso para centralizar acesso e log.

### Estruturais:

- Uso de uma ferramenta de observabilidade robusta (Prometheus/Grafana).
- Containerização com imagens leves (Alpine, Slim).
- Refatorar os códigos para separar responsabilidades (MVC, blueprints, etc.).

---

## Atualizações de Infraestrutura e Código

### Fluxo de Atualização do Código:

1. Desenvolvedor faz alterações localmente.
2. Commit + Push para o repositório.
3. Pipeline de CI é acionado (testes, lint, build).
4. Nova imagem é gerada e enviada para o Docker Registry.
5. Produção é atualizada com:
   ```bash
   docker-compose pull && docker-compose up -d
