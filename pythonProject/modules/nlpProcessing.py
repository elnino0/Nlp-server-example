from nltk import pos_tag, ne_chunk, download
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize


def init_nltk():
    download('punkt')
    download('averaged_perceptron_tagger')
    download('maxent_ne_chunker')
    download('words')
    download('vader_lexicon')


def sentiment_analyze(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)


def tokenization(text):
    return word_tokenize(text)


def part_of_speach(text):
    return pos_tag(tokenization(text))


def named_entity_recognition(text):
    return extract_ne(text)


def extract_ne(text):
    tags = part_of_speach(text)
    tree = ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )


init_nltk()
