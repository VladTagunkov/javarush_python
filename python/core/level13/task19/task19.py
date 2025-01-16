# API от OpenAI

# Напишите программу, которая использует OpenAI API для получения ответа от модели ChatGPT.

# Напишите тут ваш код
import openai 

api_key = input("Enter your key: ")
your_prompt = input('Enter your prompt: ')
openai.api_key = api_key 

resp = openai.Completion.create(
    engine = 'text-davinci-003',
    prompt = your_prompt,
    max_token = 400)

print(resp.choices[0].text.strip())