def countwords(sentences):
    word_count = 0
    in_word = False

    for char in sentences:
        if char.isspace():
            in_word = False
        elif not in_word:
            word_count +=1
            in_word = True    

    return word_count

sentence = input("Enter a sentence: ")
result = countwords(sentence)
print("Number of words:", result)