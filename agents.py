import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env
load_dotenv()

# Get API key securely
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def run_agent(user_input):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced medical doctor. Based on the user's query, "
                    "you should infer which medical specialist (e.g., cardiologist, neurologist) is most suitable. "
                    "Then provide a helpful answer in simple language. "
                    "Only give health-related suggestions, not final diagnoses or prescriptions."
                ),
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()
