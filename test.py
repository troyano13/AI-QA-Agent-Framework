from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Crear cliente OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

try:
    # Obtener lista de modelos disponibles
    models = client.models.list()

    print("Conexión exitosa")
    print(f"Cantidad de modelos: {len(models.data)}")
    print("\nModelos GPT disponibles:\n")

    # Mostrar únicamente los modelos GPT
    for model in models.data:
        if "gpt" in model.id.lower():
            print(model.id)

except Exception as e:
    print(f"ERROR: {e}")
