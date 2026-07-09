from openai import OpenAI
from dotenv import load_dotenv
import os

# =====================================
# Configuración
# =====================================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

SWAGGER_FILE = "api_specs/swagger.json"
OUTPUT_FILE = "api_tests/api.spec.ts"

# =====================================
# Validar archivo
# =====================================

if not os.path.exists(SWAGGER_FILE):
    print(f"ERROR: No existe {SWAGGER_FILE}")
    exit()

# =====================================
# Leer swagger
# =====================================

with open(SWAGGER_FILE, "r", encoding="utf-8") as file:
    swagger = file.read()

# =====================================
# Prompt
# =====================================

prompt = f"""
Actúa como Senior QA Automation Engineer.

Analiza el siguiente Swagger/OpenAPI.

Genera pruebas API usando Playwright.

Reglas:

- Usa Playwright request context.
- Valida status code.
- Valida response body.
- Incluye escenarios positivos.
- Incluye escenarios negativos.
- Devuelve únicamente TypeScript.
- No agregues explicaciones.

Swagger:

{swagger}
"""

# =====================================
# OpenAI
# =====================================

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

code = response.output_text

if not code.strip():
    print("ERROR: GPT devolvió contenido vacío")
    exit()

# =====================================
# Crear carpeta
# =====================================

os.makedirs("api_tests", exist_ok=True)

# =====================================
# Guardar
# =====================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(code)

print("\n===== API TEST GENERADO =====\n")
print(code)

print("\n=============================\n")

print(f"Archivo guardado: {OUTPUT_FILE}")
