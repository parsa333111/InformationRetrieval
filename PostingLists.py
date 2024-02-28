import sys

from PostingList import PostingList
from math import sqrt


class PostingsList:
    def __init__(self):
        self.all = 0
        self.weight = dict()
        self.map = dict()
        self.doc = dict()
        self.champion_list = dict()
        self.freq_with_word = []
        self.valid_news = []

    def set_valid_news(self, id_news):
        self.valid_news = id_news

    def add(self, word, id, position):
        if self.map.get(word) is None:
            posting = PostingList(word)
            self.all += 1
            self.map[word] = posting
        if self.doc.get(id) is None:
            self.doc[id] = dict()
        if self.doc[id].get(word) is None:
            self.doc[id][word] = 0
        self.doc[id][word] += 1
        self.map[word].add(id, position)

    def __str__(self):
        return []
        string = ""
        string += "{"
        for key in self.map.keys():
            string += key + ":" + self.map[key].__str__()
            string += ''
        string += "}"
        return string

    def score(self, id, word, N):
        score = self.tf(id, word) * self.idf(word, N)
        return score

    def tf(self, id, word):
        if self.map.get(word) is None:
            return 0
        return self.map[word].tf(id)

    def idf(self, word, N):
        if self.map.get(word) is None:
            return 0
        return self.map[word].idf(N)

    def calcute_weight(self, doc_num):
        for i in self.valid_news:
            self.weight[str(i)] = dict()
            size = 0
            for word in self.doc[str(i)].keys():
                score_word = self.idf(word, doc_num) * self.tf(str(i), word)
                self.weight[str(i)][word] = score_word
                size += score_word * score_word
            size = sqrt(size)
            for word in self.doc[str(i)].keys():
                self.weight[str(i)][word] /= size

    def get_weight(self, id, word):
        if self.weight[id].get(word) is None:
            return 0
        else:
            return self.weight[id][word]

    def get_list_word(self, word):
        if self.map.get(word) is None:
            return []
        answer = self.map[word].get_list_word()
        return answer

    def create_champion_list(self, size):
        for word in self.map.keys():
            self.champion_list[word] = self.map[word].create_champion_list(size)

    def give_champion_list(self, word):
        if self.champion_list.get(word) is None:
            return []
        can = self.champion_list[word]
        answer = []
        for item in can:
            answer.append(item[1])
        return answer

    def create_freq_word(self):
        for word in self.map.keys():
            self.freq_with_word.append([self.map[word].getfreq(), word])

    def find_word_with_most_freq_and_del(self):
        self.create_freq_word()
        self.freq_with_word.sort(reverse=True)
        answer = []
        for i in range(50):
            word = self.freq_with_word[i][1]
            freqq = self.freq_with_word[i][0]
            self.map.pop(word)
            answer.append(word)
        return answer
