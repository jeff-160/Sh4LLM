from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("chatbot")
trainer = ListTrainer(chatbot)

with open("corpus.txt", encoding="utf-8") as f:
    corpus = f.read().split("\n")

trainer.train(corpus)

print("=== Training complete ===")