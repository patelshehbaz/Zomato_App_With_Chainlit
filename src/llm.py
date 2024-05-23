import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from src.config import instruction

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-4", api_key=OPENAI_API_KEY)

def ask_bot(user_message, instruction):
    template = """
    {instruction}

    Human: {user_message}
    AI:
    """
    prompt = PromptTemplate(input_variables=["instruction", "user_message"], template=template)
    prompt_text = prompt.format(instruction=instruction, user_message=user_message)
    
    response = llm.invoke(prompt_text)
    return response.content.strip()

if __name__ == "__main__":
    user_message = "hi how are you?"
    response = ask_bot(user_message, instruction)
    print(response)



