bird_words = 'hoooowe yyyooouuu duoooiiine'
#bird_words = 'hieeelalaooo'
#bird_words = 'aaa bo cy da eee fe'

def translate(phrase: str) -> str:
    result = ''
    vowels = "aeiouy"

    i = 0
    while i < len(phrase):
        result += phrase[i]
        print("input: ["+phrase[i]+"], i="+str(i))
        if phrase[i].isspace():
            print("found space, keep it")
            i += 1
        elif vowels.count(phrase[i]) > 0:
            i += 3
        else:
            i += 2
    return result

print(translate(bird_words))