##Basic Chatbot using NLTK

import nltk
from nltk.chat.util import Chat, reflections

#Define pairs of inputs and responses

pairs = [
    (r"hi|hello|hey" , ["Hello!", "Hi there!" , "Hey ! How can I assist you"]),
    (r"how are you?", ["I'm just a program, but I'm functioning perfectly!", "Doing great, thanks! How can I help?"]),
    (r"what is your name?", ["I'm a simple chatbot created to assist you. What's your name?"]),
    (r"my name is (.*)", ["Nice to meet you, %1! How can I assist you today?"]),
    (r"what can you do?", ["I can chat with you and answer simple questions. Try asking me something!"]),
    (r"(.*) your favorite (.*)", ["I don't have personal preferences, but I enjoy helping you!"]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "See you later! Take care!"]),
    (r"(.*)", ["I'm not sure I understand. Can you rephrase?"])
]

#cerate a chat object
chatbot = Chat(pairs,reflections)

#start the chatbot
def start_chat():
    print("chatbot : Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You : ").lower()
        if user_input == "bye":
            print("Chatbot : Good Bye! HAve a greate day")
            break
        else:
            response=chatbot.respond(user_input)
            print(f"Chatbot :{response}")

#Run the chatbot
if __name__=="__main__":
    start_chat()