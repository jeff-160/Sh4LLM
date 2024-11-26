from chatterbot import ChatBot

chatbot = ChatBot(
    "chatbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
)

while True:
    query = input("> ")
    if query == "exit":
        break
    else:
        print(f"Sh4LLM: {chatbot.get_response(query)}")