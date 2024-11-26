from chatterbot import ChatBot

chatbot = ChatBot(
    "chatbot",
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    database_uri = 'sqlite:///db.sqlite3',
    logic_adapters = [
        {
            "import_path": "chatterbot.logic.BestMatch"
        }
    ]
)

while True:
    query = input("> ").strip()

    if len(query):
        print(f"Sh4LLM: {chatbot.get_response(query)}")
