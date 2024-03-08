# use: run from command line 'python3 open-ai-client.py ARG' where ARG is a
# multi word topic / sentence / question / prompt

import openai

from sys import argv

openai.organization = "" # requires account
openai.api_key = ""      # requires account

if len(argv) < 2:
    exit(0)

topic_array = []
for topic in argv[1:]:
    topic_array.append(topic)

topic = " ".join(topic_array)

prompt = topic
engine = "text-davinci-003"
max_tokens = 1000

response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=max_tokens).choices[0].text
print(response)

