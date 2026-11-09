# Barbearia Navalha Urbana — MVP

Sistema de agendamento autónomo e controlo de bancada mobile-first voltado à eficiência operacional de microempreendimentos locais, alinhado ao **ODS 8 (Trabalho Digno e Crescimento Económico)**.

---

## Tecnologias Utilizadas
* **Backend:** Python 3.11+, Flask, Flask-WTF, SQLAlchemy
* **Frontend:** Jinja2 Templates, Tailwind CSS (Mobile-First, WCAG 2.1 AA)
* **Base de Dados:** PostgreSQL (Produção) / SQLite (Testes)
* **Qualidade e Testes:** Pytest, Flake8, GitHub Actions (CI)

---

## Estrutura do Projeto
\\\	ext
barbearianavalha/
+-- app/
¦   +-- controllers/      # Rotas públicas e de gestão
¦   +-- models/           # Modelação relacional e entidades
¦   +-- services/         # Regras de negócio (ex: BookingService com bloqueio atómico)
¦   +-- static/           # Estilos e assets estáticos
¦   +-- templates/        # Telas Jinja2 acessíveis (WCAG 2.1 AA)
+-- tests/
¦   +-- unit/             # Testes unitários das regras de negócio
¦   +-- integration/      # Testes de rotas, formulários e base de dados
+-- .github/workflows/    # Pipeline de CI (build, lint e testes)
+-- .gitignore
+-- requirements.txt
+-- README.md
\\\

---
