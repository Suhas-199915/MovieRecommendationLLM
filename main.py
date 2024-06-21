from langchain_community.llms import GooglePalm
from dotenv import load_dotenv
import os
load_dotenv()
llm = GooglePalm(api_key=os.environ['GOOGLE_PALM_KEY'])

from langchain.chains.llm import LLMChain
from langchain.prompts.prompt import PromptTemplate

prompt_temp = """Recommend a movie in the {genre} and in {language}, translate the response in the same language"""

prompt = PromptTemplate(template=prompt_temp, input_variables=['genre', 'language'])

chain = LLMChain(llm=llm, prompt=prompt)
response = chain({'genre': 'Horror', 'language': 'Hindi'})



print(response['text'])


