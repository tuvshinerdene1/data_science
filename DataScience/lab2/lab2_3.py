def wordCounter(sentence):
    wordcount = {}
    for word in sentence.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    
    for word in wordcount:
        if wordcount[word] > 1:
            print(f"{word} : {wordcount[word]}")




def main():
    wordCounter("the cat and the dog and the bird and cat")

if __name__ == "__main__":
    main()