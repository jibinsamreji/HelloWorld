def emoji_converter(message):
    words = message.split(' ')
    print(words)

    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# emoji - cntrl+command+space

message = input("> ")
print(emoji_converter(message))

