from openai import OpenAI
from dotenv import load_dotenv
import os

# =====================================
# Cargar variables de entorno
# =====================================

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# =====================================
# Configuración
# =====================================

INPUT_FILE = "stories/login.txt"
OUTPUT_FILE = "features/login.feature"

# =====================================
# Validar existencia de la historia
# =====================================

if not os.path.exists(INPUT_FILE):
    print(f"ERROR: No existe {INPUT_FILE}")
    exit()

# =====================================
# Leer historia
# =====================================

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    story = file.read()

# =====================================
# Prompt
# =====================================

prompt = f"""
Actúa como QA Automation Engineer Senior.

Analiza la siguiente historia de usuario.

Genera un archivo Gherkin profesional.

Reglas:

- Utiliza sintaxis Gherkin válida.
- Incluye Feature.
- Incluye Background si aplica.
- Incluye escenarios positivos.
- Incluye escenarios negativos.
- Incluye escenarios borde.
- Devuelve únicamente código Gherkin.
- No agregues explicaciones.

Historia:

{story}
"""

# =====================================
# Llamada OpenAI
# =====================================

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

gherkin = response.output_text

# =====================================
# Validación
# =====================================

if not gherkin.strip():
    print("ERROR: GPT devolvió contenido vacío")
    exit()

# =====================================
# Crear carpeta si no existe
# =====================================

os.makedirs("features", exist_ok=True)

# =====================================
# Guardar feature
# =====================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(gherkin)

# =====================================
# Mostrar resultado
# =====================================

print("\n===== FEATURE GENERADO =====\n")
print(gherkin)

print("\n===========================\n")

print(f"Archivo guardado: {OUTPUT_FILE}")
