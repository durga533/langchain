from dotenv import load_dotenv
import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env vars
load_dotenv()

# Initialize model with API key
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define question prompt
question = "I am preparing for DSA interview and practising questions. You are an expert at {language}. Help me fix the error: {error}"

prompt = ChatPromptTemplate.from_template(question)
prompt_value = prompt.invoke({"language": "java", "error": "; is missing"})

# Get answer from model
answer = model.invoke(prompt_value)
print(answer.content)
