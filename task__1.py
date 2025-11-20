#task 1 : chatbot with rule based responses

import datetime

print("Chatbot:Hello!Type 'bye' to exit")

while True:

    user_input = input("You:").lower()
    if user_input == 'bye':
        print("Chatbot:Goodbye!")
        break
    elif 'date' in user_input.lower():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Chatbot:The current date is {current_date}")
    elif 'time' in user_input.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot:The current time is {current_time}")
    elif 'hello' in user_input.lower():
        print("Chatbot:Hello! How can I assist you?")
    elif 'how are you' in user_input.lower():
        print("Chatbot:I'm just a program, but thanks for asking!")
    elif 'weather' in user_input.lower():
        print("Chatbot:I'm sorry, I can't provide weather updates right now.")
    elif 'joke' in user_input.lower():
        print("Chatbot:Why did the scarecrow win an award? Because he was outstanding in his field!")
    elif 'help' in user_input.lower():
        print("Chatbot:I can tell you the current date and time. Just ask!")
    elif 'thank you' in user_input.lower() or 'thanks' in user_input.lower():
        print("Chatbot:You're welcome!")
    elif 'created you' in user_input.lower() or 'who made you' in user_input.lower():
        print("Chatbot:I was created by a team of developers.")
    else:
        print("Chatbot:I'm sorry, I can only tell you the current time or say goodbye.")
    









