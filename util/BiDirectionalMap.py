class BiDirectionalMap:
    def __init__(self):
        # create a dictionary with default values
        self._wordToVal = dict() # word -> val 
        self._valToWord = dict() # val -> word

    def put(self, word: str) -> None:
        if word in self._wordToVal:
            # If word exists, don't do anything
            return None

        val = len(self._wordToVal)
        self._wordToVal[word] = val
        self._valToWord[val] = word
        

    def get_word(self, value: int) -> str:
        return self._valToWord[value]
        

    def get_value(self, word: str) -> int:
        return self._wordToVal[word]

    def __repr__(self):
        return str(self._wordToVal)

