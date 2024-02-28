import json
import time
from PostingLists import PostingsList
from heapq import heapify, heappush, heappop
from math import log, sqrt
import pickle

document_number = 12202


def read_json(path):
    file = open(path)
    datas = json.load(file)
    file.close()
    return datas


news_in = []


def in_news(num, datas):
    for i in range(num):
        if not datas.get(str(i)) is None:
            news_in.append(i)


map_doc = PostingsList()


def preprocess(datas):
    for i in news_in:
        if i % 1000 == 0:
            print((i / document_number) * 100, "percentage")
        if datas.get(str(i)) is None:
            continue
        content = datas[str(i)]['content']
        content = tokenizer(content)
        position = 0
        for word in content:
            map_doc.add(word, str(i), position)
            position += 1

    db = map_doc.map
    dbfile = open('postings', 'ab')
    pickle.dump(db, dbfile)
    dbfile.close()


datas = None


def search_query(string):
    string = normalizer(string)
    token_query = tokenizer(string)
    count = dict()
    word_count = 0
    for word in token_query:
        word_count += 1
        if count.get(word) is None:
            count[word] = 0
        count[word] += 1

    word_count = sqrt(word_count)
    have_token = []

    use_champion_list = False  # change to use champion list
    for word in count.keys():
        count[word] /= word_count
        if use_champion_list:
            have_token += map_doc.give_champion_list(word)
        else:
            have_token += map_doc.get_list_word(word)

    have_token = list(dict.fromkeys(have_token))
    token_query = list(dict.fromkeys(token_query))

    heap = []
    heapify(heap)
    returned_doc = 3  # change to give more result
    max_size = returned_doc

    for i in have_token:
        score = 0
        for word in token_query:
            score += map_doc.get_weight(i, word) * count[word]
        heappush(heap, (score, i))
        if len(heap) > max_size:
            heappop(heap)

    candidates = []
    while len(heap):
        candidates.append(heappop(heap))
    candidates = list(reversed(candidates))
    for candidate in candidates:
        index = candidate[1]
        print(datas[index]['title'], " ", datas[index]["url"])
        print(datas[index]['content'])


from NTF import tokenizer, delete_negharesh, normalizer

if __name__ == "__main__":

    datas = read_json("IR_data_news_12k.json")

    in_news(document_number, datas)
    map_doc.set_valid_news(news_in)

    preprocess(datas)
    stop_word = map_doc.find_word_with_most_freq_and_del()

    map_doc.calcute_weight(document_number)
    map_doc.create_champion_list(20)

    db = map_doc.map
    dbfile = open('postings', 'ab')
    pickle.dump(db, dbfile)
    dbfile.close()
    print(100, "percentage")

    while True:
        query = input("متن مورد نظر خود را برای حستحو وارد کنید:")
        search_query(query)
