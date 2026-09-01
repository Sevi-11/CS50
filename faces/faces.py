emoticons = {
    ":)" : "🙂",
    ":(" : "🙁",
    ":D": "😀"
}

text = input("Emoji Text: ")

for key, value in emoticons.items():

   text = text.replace(key, value)

print(text)