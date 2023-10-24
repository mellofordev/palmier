'''
A test code for the palmier package
'''
from palmier import api
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')
config = api.Configure(api_key,temp=0.8)

while True:
    prompt = input("Prompt >>")
    config.activate(prompt,'Youre chatting with a human',[['Hello bot','hi how can i help you!']])