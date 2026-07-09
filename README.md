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

```text
                           +----------------------+
                           |   User Story (.txt)  |
                           |  stories/login.txt   |
                           +----------+-----------+
                                      |
                                      |
                                      ▼
                    +----------------------------------+
                    | Agent 1 - Test Case Generator    |
                    |----------------------------------|
                    | • Analyze User Story             |
                    | • Generate ISTQB Test Cases      |
                    +----------------+-----------------+
                                     |
                                     ▼
                       output/test_cases.md
                                     |
                                     |
                                     ▼
                  +--------------------------------------+
                  | Agent 2 - Gherkin Generator          |
                  |--------------------------------------|
                  | • Read User Story                    |
                  | • Generate BDD Scenarios             |
                  +----------------+---------------------+
                                   |
                                   ▼
                      features/login.feature
                                   |
                                   |
                                   ▼
             +------------------------------------------+
             | Agent 3 - Playwright UI Generator        |
             |------------------------------------------|
             | • Read Feature File                      |
             | • Generate UI Automation                 |
             +----------------+-------------------------+
                              |
                              ▼
                     tests/login.spec.ts
                              |
                              |
                              ▼
          +----------------------------------------------+
          | Agent 4 - API Test Generator                 |
          |----------------------------------------------|
          | • Read Swagger/OpenAPI Specification         |
          | • Generate Playwright API Tests             |
          +----------------+-----------------------------+
                           |
                           ▼
                 api_tests/api.spec.ts
                           |
                           |
                           ▼
      +---------------------------------------------------------+
      | Agent 5 - QA Reviewer                                  |
      |---------------------------------------------------------|
      | • Analyze all generated artifacts                      |
      | • Evaluate test coverage                               |
      | • Detect missing scenarios                             |
      | • Identify functional risks                            |
      | • Recommend improvements                               |
      +----------------+----------------------------------------+
                       |
                       ▼
               reviews/final_review.md
```

---

## Workflow

```text
User Story
      │
      ▼
Test Case Generator
      │
      ▼
Gherkin Generator
      │
      ▼
Playwright UI Generator
      │
      ▼
API Test Generator
      │
      ▼
QA Reviewer
      │
      ▼
Final
```



### Estructura del proyecto

```text
qa-agent/
│
├── stories/
│   └── login.txt
│
├── output/
│   └── test_cases.md
│
├── features/
│   └── login.feature
│
├── tests/
│   └── login.spec.ts
│
├── api_specs/
│   └── swagger.json
│
├── api_tests/
│   └── api.spec.ts
│
├── reviews/
│   └── final_review.md
│
├── app.py
├── gherkin_agent.py
├── playwright_agent.py
├── api_test_agent.py
├── review_agent.py
│
├── .env
├── requirements.txt
└── README.md

```

## AI Agents Responsibilities

| Agent | Responsibility | Input | Output |
|--------|---------------|--------|--------|
| **Agent 1** | Test Case Generator | User Story | ISTQB Test Cases |
| **Agent 2** | Gherkin Generator | User Story | `.feature` File |
| **Agent 3** | Playwright Generator | Gherkin | UI Automation |
| **Agent 4** | API Generator | Swagger/OpenAPI | API Automation |
| **Agent 5** | QA Reviewer | All Generated Artifacts | QA Review Report |





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


---

# 

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/qa-agent.git
```

```bash
cd qa-agent
```

---

## 2. Crear un entorno virtual

Linux / macOS

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

---

## 3. Activar el entorno virtual

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## 4. Instalar dependencias

```bash
pip install openai python-dotenv
```

Opcionalmente,  `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 5. Configurar el archivo `.env`

Crear un archivo llamado:

```text
.env
```

con el siguiente contenido:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **el archivo `.env` a GitHub. Agrégalo al archivo `.gitignore`.**

---


# Ejecución

## Agente 1 - Test Case Generator

```bash
python app.py
```

Salida:

```text
output/test_cases.md
```

---

## Agente 2 - Gherkin Generator

```bash
python gherkin_agent.py
```

Salida:

```text
features/login.feature
```

---

## Agente 3 - Playwright Generator

```bash
python playwright_agent.py
```

Salida:

```text
tests/login.spec.ts
```

---

## Agente 4 - API Test Generator

```bash
python api_test_agent.py
```

Salida:

```text
api_tests/api.spec.ts
```

---

## Agente 5 - QA Reviewer

```bash
python review_agent.py
```

Salida:

```text
reviews/final_review.md
```

---

#  Dependencias

Actualmente el proyecto utiliza las siguientes librerías:

| Librería      | Propósito                                                        |
| ------------- | ---------------------------------------------------------------- |
| openai        | Comunicación con los modelos de OpenAI                           |
| python-dotenv | Lectura segura de variables desde `.env`                         |
| os            | Manejo de archivos y directorios (biblioteca estándar de Python) |

---

#  Archivo `requirements.txt`

En lugar de decirle a los usuarios que instalen los paquetes uno por uno, es mejor crear un archivo `requirements.txt`.

Dentro coloca:

```text
openai>=1.100.0
python-dotenv>=1.1.0
```

Luego cualquier persona podrá instalar todo con un solo comando:

```bash
pip install -r requirements.txt
```

---

#  Archivo `.gitignore`


Contenido recomendado:

```gitignore
# Virtual environment
venv/

# Environment variables
.env

# Python cache
__pycache__/
*.pyc

# macOS
.DS_Store

# VSCode
.vscode/

# JetBrains
.idea/

# Generated files
output/
reviews/
tests/
api_tests/
features/
```

---

## Recomendaciones adicionales, tener n cuenta que aqui se sube todo el proyecto porque es un ejemplo


* Añadir una licencia (`LICENSE`, por ejemplo MIT).
* Mejorar la estructura moviendo los agentes a una carpeta `agents/` en lugar de dejarlos en la raíz.
* Incluir un diagrama de arquitectura en el README.


### Cómo ejecutar los agentes

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

