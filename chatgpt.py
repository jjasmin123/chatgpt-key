API_KEY = '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'
import openai
import os
os.environ['OPENAI_Key'] = API_KEY
openai.api_keys = os.environ['OPENAI_Key']

keep_prompting = True
while keep_prompting:
    prompt=input('What is your question? Type exit if you are done!')
    if prompt == 'exit':
        keep_prompting = False
    else:
        response=openai.Completion.create(engine='gpt-4', prompt=prompt, max_tokens = 200)
        print(response['choices'][0]['text'])