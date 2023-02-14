import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Cat and Monkey have a high similarity. This is because they are both animals.
# Monkey and banana have a high similarity, due to Monkeys eating banana's. The similarity is not as high as monkey and cat.
# banana and cat have a low similarity.

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",  similarity)


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


word1 = nlp("house")
word2 = nlp("window")
word3 = nlp("door")
word4 = nlp("car")

print("My example")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word3))
print(word4.similarity(word2))

# house and window have a high similarity
# door and window have the highest similarity
# window and car have the lowest similarity, lower than expected

print("Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model'en_core_web_md'")

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# en_core_wed_sm has a much higher similarity results when compared with web_md
# for instance cat apple is 0.7 compared with 0.2.
