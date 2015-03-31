from frequency import remove_stop_words
from gensim.utils import lemmatize as lem

'''
Parses and returns a list of the raw review text of a directory.
'''
import json
import os
import re, pickle


def get_list_of_raw_reviews(path):
    list_of_raw_reviews = []
    for filename in os.listdir(path):
	full_file_path = os.path.join(path, filename)
	with open(full_file_path) as f:
	    json_review = json.loads(f.read())

	list_of_raw_reviews.append(json_review['text'])

    return list_of_raw_reviews

def clean_reviews(path):
    reviews = get_list_of_raw_reviews(path)
    return lemmatize_reviews(remove_stop_words(reviews))

def lemmatize_reviews(reviews):
    lemmatized = [lem(review) for review in reviews]
    return [re.sub('/[A-Z]+', '', word) for revs in lemmatized for word in revs]

def main():
    clean_revs = clean_reviews(os.curdir)
    # pickle cleaned reviews
    with open(os.path.join('../../topic_modeling/data', 'cleaned_reviews.pickle'), 'wb') as pickled_reviews:
        pickle.dump(clean_revs, pickled_reviews)

if __name__ == "__main__": main()
