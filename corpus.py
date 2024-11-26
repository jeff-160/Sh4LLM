import os

header = "3P3 Shalom: "

filter = [
    "3P3 Shalom left",
    "added 3P3 Shalom",
    "Messages and calls are end-to-end encrypted",
    "This message was deleted",
    "sticker omitted",
    "image omitted",
    "joined using this group's invite link",
    "was added"
]

corpus = []

for file in map(lambda name : f"chats\\{name}", os.listdir("chats")):
    with open(file, encoding="utf-8") as f:
        contents = [
            line[line.index(header) + len(header): ].replace("‎", "").strip()
            for line in f.readlines()
            if header in line and all(map(lambda x : x not in line, filter))
        ]
    
    corpus.extend(contents)
    
with open("corpus.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(corpus))