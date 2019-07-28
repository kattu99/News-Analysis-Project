import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def pre_process_lines(lines):
    for line in lines:
        tokens = word_tokenize(line)
        token = [w.lower() for w in tokens]
        transformation = str.maketrans('','', string.punctuation)
        stripped = [w.translate(transformation) for w in token]
        words = [word for word in stripped if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if w not in stop_words]

# An ensemble model
# use a keras embeddings model, check performance
# use a naive bayes model as a sanity check to make sure we're doing the right thing
