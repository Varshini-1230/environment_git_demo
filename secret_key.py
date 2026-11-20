import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('openai_apikey')
print(api_key)