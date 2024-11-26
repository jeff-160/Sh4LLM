import os, re

names = [
    "3P3 Shalom: ",
    "Shalom Chai: ",
    "~ lom: "
]

filter = [
    "3P3 Shalom left",
    "added 3P3 Shalom",
    "Messages and calls are end-to-end encrypted",
    "This message was deleted",
    "sticker omitted",
    "image omitted",
    "joined using this group's invite link",
    "was added",
    "changed the group name"
]

corpus = []

for file in map(lambda name: f"chats\\{name}", os.listdir("chats")):
    with open(file, encoding = "utf-8") as f:
        contents = []

        for line in f.readlines():
            try:
                header = [
                    name
                    for name in names 
                    if line.find(name) != -1
                ][0]

                if all(map(lambda x: x not in line, filter)):
                    cleaned_line = re.sub(
                        r"@\w+", "", 
                        line[line.index(header) + len(header): ].replace("‎", "")
                    ).strip()

                    if len(cleaned_line):
                        contents.append(cleaned_line)
                        
            except:
                continue
    
    corpus.extend(contents)
    
with open("corpus.txt", "w", encoding = "utf-8") as f:
    f.write("\n".join(corpus))