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

FEATURE_FILE = "features/login.feature"
OUTPUT_FILE = "tests/login.spec.ts"

# =====================================
# Validar archivo feature
# =====================================

if not os.path.exists(FEATURE_FILE):
    print(f"ERROR: No existe {FEATURE_FILE}")
    exit()

# =====================================
# Leer feature
# =====================================

with open(FEATURE_FILE, "r", encoding="utf-8") as file:
    feature = file.read()

# =====================================
# Prompt
# =====================================

prompt = f"""
Actúa como Senior QA Automation Engineer.

Convierte el siguiente archivo Gherkin en código Playwright TypeScript.

Reglas:

- Utiliza Playwright Test.
- Usa test.describe().
- Usa test().
- Genera comentarios útiles.
- Usa buenas prácticas.
- Devuelve únicamente código TypeScript.
- No agregues explicaciones.

Feature:

{feature}
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

os.makedirs("tests", exist_ok=True)

# =====================================
# Guardar archivo
# =====================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(code)

print("\n===== PLAYWRIGHT GENERADO =====\n")
print(code)

print("\n==============================\n")

print(f"Archivo guardado: {OUTPUT_FILE}")
