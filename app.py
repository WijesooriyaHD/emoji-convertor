
def emoji_convertor(sentence):

    words=sentence.split(" ")

    emoji={
        
        ";)":"🙂",
        ":-(":"😠",
        ";(":"😒"
    }

    output=""

    for word in words:
        output=output+emoji.get(word,word)+" "

    return output


print( )
print("Enter a sentence with an emoji. Available emojis are shown below.")
print()
print("   ;)   ;(  :-(   ")
print( )
print()


sentence=input('Enter your message : ')
print("converted mesaage : "+emoji_convertor(sentence))
print()

