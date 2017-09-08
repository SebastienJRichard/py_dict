import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def lookup_word(word):
    word = word.lower()
    try:
        answer = data[word]
    except KeyError:
        alt_word = get_close_matches(word, data.keys(), n=1)[0]
        if alt_word != None:
            ans = input(word + " not found. Did you mean " + alt_word  + "? [Y/N]")
            if ans == "Y":
                answer = data[alt_word]
            elif ans == "N":
                answer = "Sorry, can't find your word"
            else:
                answer = "I'm sorry Dave, I don't understand you."
        else:
            answer = "Word not found"
    return answer


word = input("Enter word: ")
data = lookup_word(word)
if type(data) == list:
    for entry in data:
        print(entry)
else:
    print(data)
