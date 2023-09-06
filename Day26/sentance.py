sentence = "What is the Airspeed velocity of an Unladen Swallow?"
word_list = sentence.split()  # Split the sentence into words
print(word_list)

result = {word:len(word) for word in word_list}
print(result)