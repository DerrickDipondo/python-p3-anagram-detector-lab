class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, anagrams):
        # Sort letters of the word

        sorted_word = sorted(self.word)

        # Return  list of anagrams
        return [anagram for anagram in anagrams if sorted(anagram.lower()) == sorted_word and anagram.lower() != self.word]
    
