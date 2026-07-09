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

# =====================================
# Archivos
# =====================================

STORY_FILE = "stories/login.txt"
TEST_CASES_FILE = "output/test_cases.md"
FEATURE_FILE = "features/login.feature"
UI_TEST_FILE = "tests/login.spec.ts"
API_TEST_FILE = "api_tests/api.spec.ts"

# =====================================
# Función utilitaria
# =====================================

def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    return "FILE NOT FOUND"

# =====================================
# Lectura
# =====================================

story = read_file(STORY_FILE)
test_cases = read_file(TEST_CASES_FILE)
feature = read_file(FEATURE_FILE)
ui_tests = read_file(UI_TEST_FILE)
api_tests = read_file(API_TEST_FILE)

# =====================================
# Prompt
# =====================================

prompt = f"""
Actúa como Principal QA Architect.

Debes revisar el trabajo realizado por varios agentes QA.

Analiza:

1. Historia de usuario
2. Casos de prueba
3. Gherkin
4. Automatización UI
5. Automatización API

Genera:

# Coverage Analysis

# Missing Scenarios

# Risks

# Automation Improvements

# Final Score (0-100)

# Recommendations

Historia:

{story}

Casos de prueba:

{test_cases}

Feature:

{feature}

UI Tests:

{ui_tests}

API Tests:

{api_tests}
"""

# =====================================
# OpenAI
# =====================================

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

review = response.output_text

# =====================================
# Guardar resultado
# =====================================

os.makedirs("reviews", exist_ok=True)

with open(
    "reviews/final_review.md",
    "w",
    encoding="utf-8"
) as file:
    file.write(review)

print("\n===== REVIEW =====\n")
print(review)

print("\n==================\n")
print("Review generado")
