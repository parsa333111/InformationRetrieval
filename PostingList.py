from math import log
from heapq import heappop, heappush, heapify


class PostingList:
    def __init__(self, word):
        self.freq_in_doc = dict()
        self.freq_in_unique_doc = 0
        self.freq_in_all = 0
        self.word = word
        self.list = dict()
        self.champion_list = []

    def add(self, id, position):
        self.freq_in_all += 1
        if self.freq_in_doc.get(id) is None:
            self.freq_in_doc[id] = 0
            self.freq_in_unique_doc += 1
            self.list[id] = list()
        self.freq_in_doc[id] += 1
        self.list[id].append(position)

    def tf(self, id):
        if self.freq_in_doc.get(id) is None:
            return 0
        else:
            freq = self.freq_in_doc[id]
            return 1 + log(freq, 10)

    def idf(self, N):
        return log(N / self.freq_in_unique_doc, 10)

    def get_list_word(self):
        answer = []
        for doc_id in self.list.keys():
            answer.append(doc_id)
        return answer

    def create_champion_list(self, size):
        answer = []
        heapify(answer)

        for i in self.list.keys():
            score = self.freq_in_doc[i]
            heappush(answer, (score, i))
            if len(answer) > size:
                heappop(answer)

        candidates = []
        while len(answer):
            candidates.append(heappop(answer))
        candidates = list(reversed(candidates))
        return candidates

    def getfreq(self):
        return self.freq_in_unique_doc

    def __str__(self):
        return "freq=" + str(self.freq_in_all) + "freq_in_unique_doc=" + str(self.freq_in_unique_doc) + " word=" + str(self.word) + " freq_in_doc=" + str(self.freq_in_doc) + " list=" + str(self.list)

