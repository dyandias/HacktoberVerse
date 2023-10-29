from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)

trainer.train([
    "Hi",
    "Hello",
    "How are you?",
    "I'm doing well, thank you.",
    "That's good to hear.",
    "Thank you."
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")