from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, length + 1))

        return 0