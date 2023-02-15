
import spacy

nlp = spacy.load('en_core_web_md')

# open file
# read contents and store as dictionary

movies= {}
sentences = open("movies.txt").readlines()

sentence_to_compare = """Planet Hulk with the description 
'Will he save their world or destroy it?' When the Hulk 
becomes too dangerous for the Earth, the Illuminati trick 
Hulk into a shuttle and launch him into space to a planet 
where the Hulk can live in peace. Unfortunately, Hulk land 
on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# store the data for similarity and append to list, then sort to find the highest similarity.

data = []
model_sentence = nlp(sentence_to_compare)

# iterate through the dictionary

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    movies.update({sentence: similarity})
    data.append(similarity)

# store the largest num and match item in movie
data = sorted(data)
largestnum = data[-1]

# print result

for key in movies:
    if movies[key] == largestnum:
        print("Most similar movie:", key, movies[key])











