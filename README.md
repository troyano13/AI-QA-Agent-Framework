# AI-QA-Agent-Framework

### AI QA Agent Framework

v1.0

Framework de agentes de Inteligencia Artificial para automatización y aseguramiento de calidad (QA).

### Descripción

Este proyecto implementa una arquitectura de 5 agentes especializados de QA utilizando Python + OpenAI API.

El objetivo es transformar una historia de usuario en un conjunto completo de artefactos de pruebas:

* Casos de prueba ISTQB

* Escenarios Gherkin

* Automatización Playwright UI

* Automatización de APIs basada en Swagger/OpenAPI

* Revisión automática de cobertura y riesgos

### Arquitectura

User Story

stories/login.txt

Agent 1

### Test Case Generator

Genera casos de prueba ISTQB

Salida

output/test_cases.md

Markdown

Agent 2

### Gherkin Generator

Convierte historias a Gherkin

Salida

features/login.feature

.feature

Agent 3

### Playwright UI Generator

Genera automatización UI

Salida

tests/login.spec.ts

TypeScript

Agent 4

### API Test Generator

Genera pruebas API desde Swagger

Salida

api_tests/api.spec.ts

Playwright API

Agent 5

### QA Reviewer Agent

Analiza todos los artefactos generados

Cobertura

Riesgos

Mejoras

Score QA

Salida

reviews/final_review.md

Reporte

### Estructura del proyecto

qa-agent/
├── stories/
│   └── login.txt
├── output/
│   └── test_cases.md
├── features/
│   └── login.feature
├── tests/
│   └── login.spec.ts
├── api_specs/
│   └── swagger.json
├── api_tests/
│   └── api.spec.ts
├── reviews/
│   └── final_review.md
├── app.py
├── gherkin_agent.py
├── playwright_agent.py
├── api_test_agent.py
└── review_agent.py


### Tecnologías utilizadas

| Tecnología      | Uso                          |
| --------------- | ---------------------------- |
| Python 3.14     | Lógica de los agentes        |
| OpenAI API      | Generación con LLMs          |
| python-dotenv   | Manejo seguro de API Keys    |
| Playwright      | Automatización UI y API      |
| Gherkin         | Definición de escenarios BDD |
| Swagger/OpenAPI | Especificación de APIs       |

### Instalación

Comandos

Copiar

Configurar el archivo .env

### Cómo ejecutar

| Agente                  | Comando                    |
| ----------------------- | -------------------------- |
| Test Case Generator     | python app.py              |
| Gherkin Generator       | python gherkin_agent.py    |
| Playwright UI Generator | python playwright_agent.py |
| API Test Generator      | python api_test_agent.py   |
| QA Reviewer             | python review_agent.py     |

### Flujo completo

Historia Usuario

1

Test Cases

2

Gherkin

3

Playwright UI

4

Playwright API

5

QA Review

Reporte Final

### Resultado final

El framework genera automáticamente:

*  Casos de prueba ISTQB

*  Escenarios Gherkin

*  Automatización Playwright UI

*  Automatización de APIs

* Análisis de cobertura

* Identificación de riesgos

* Score de calidad QA

### Autor

Alexandra Troyano

QA Automation Engineer | SDET | AI QA Enthusiast

PythonOpenAI

PlaywrightAI Agents

