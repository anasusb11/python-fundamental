message = input("Enter the text with emoji: ")

emoji_map = {
    ":)" : "😊",
    ":D" : "😁",
    ":|" : "😐",
    ":(" : "🙁"
}

output = ""
words = message.split(" ")

for word in words:
    output += emoji_map.get(word, word) + " "

print(output)