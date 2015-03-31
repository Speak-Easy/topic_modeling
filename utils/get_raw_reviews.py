'''
Parses and returns a list of the raw review text of a directory. 
'''
import json
import os

def get_list_of_raw_reviews(path):
    list_of_raw_reviews = []
    for filename in os.listdir(path):
	full_file_path = os.path.join(path, filename)
	with open(full_file_path) as f:
	    json_review = json.loads(f.read())

	list_of_raw_reviews.append(json_review['text'])

    return list_of_raw_reviews

def main():
    # If run directly, just print out the current
    # directories raw review text
    print get_list_of_raw_reviews(os.curdir)

if __name__ == "__main__": main()
