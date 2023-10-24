from palmier.message import messageParser
class Configure:
    def __init__(self,api_key,in_prompt_template='',mode='story',model_name='models/chat-bison-001',temp=0.7,)->None:
        self.api_key = api_key
        self.model_name = model_name
        self.mode =mode
        self.temp = temp
        if in_prompt_template=='':
                self.prompt_template ='''
                    You're a friendly bot that answers to the questions given as prompt \
                    Answer in detail \
                    Answer in a {mode} with list out of points if necessary \
                    This is the {prompt} from the user \
                '''
        else :
            self.prompt_template = in_prompt_template
    def __str__(self) -> str:
         return 'Successfully initialized the api...'
    def activate(self,prompt,context,examples):
        message=[]
        error_message='''
        Error : Can't import google.generativeai
                Make sure you have installed the package 
                pip install google-generativeai
        '''
        try:
             import google.generativeai as palm 
        except ImportError:
            print(error_message)
        defaults = {
        'model': self.model_name,
        'temperature': self.temp,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        }
        palm.configure(api_key=self.api_key)
        message.append(messageParser(self.prompt_template,self.mode,prompt))
        response = palm.chat(
             **defaults,
             context=context,
             examples=examples,
             messages=message,
        )
        message.append('NEXT REQUEST')
        print(response.last)
        