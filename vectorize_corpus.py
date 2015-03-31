from __future__ import unicode_literals, print_function

import logging
import itertools
import pickle

import numpy as np
import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim.parsing.preprocessing import STOPWORDS

def init_logging():
    logging.basicConfig(format="%(levelname)s : %(message)s", level=logging.INFO)
    logging.root.level = logging.INFO

def head(stream, n=10):
    # Return first 'n' elements of stream as plain list
    return list(itertools.islice(stream, n))

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

# IN PLACE OF iter_wiki method, because we use a TextCorpus, use get_texts()
def build_dictionary_and_clean(reviews):
    # Place any additional cleaning here in future
    return gensim.corpora.Dictionary([reviews])

def main():
    init_logging()
    with open('data/cleaned_reviews.pickle') as f:
	reviews = pickle.load(f)
    
    review_dict = build_dictionary_and_clean(reviews)
    print(review_dict.token2id)

    review_dict.save_as_text('data/review_dictionary.txt')

if __name__ == '__main__': main()
