from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

with open("stories/login.txt", "r") as file:
    story = file.read()

prompt = f"""
Actúa como QA Senior ISTQB.

Genera:

1. Casos positivos
2. Casos negativos
3. Casos borde
4. Riesgos

Historia:

{story}
"""

response = client.chat.completions.create(
    model="gpt-5-mini",
    max_completion_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

result = response.choices[0].message.content

with open("output/test_cases.md", "w") as file:
    file.write(result)

print("Casos generados")

print(response.usage)
