import gpt4free 
from gpt4free import Provider

chat = []

while True:
    prompt = input("You: ")
    if prompt == 'q':
        break
    response = gpt4free.Completion.create(Provider.You, prompt=prompt, chat=chat, detailed=True, include_links=True)

    print("Bot:", response)

    chat.append({"question": prompt, "answer": response})
