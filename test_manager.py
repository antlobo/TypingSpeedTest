from random import choices


class TestManager:
    def __init__(self):
        self.wordlist = []
        self.words_per_min = 0
        self.chars_per_min = 0
        self.wrong_words = []

    def retrieve_words_from_file(self, file: str, num_words: int) -> str:
        """
        Updates the wordlist with the new words retrieved from the file passed and returns the words chosen in a string
        :param file: string of the path to the file with words
        :param num_words: integer with the number of the words to select from the file
        :return: a string with all the words selected
        """
        with open(file, mode="r") as file:
            words = [line.replace("\n", "") for line in file]
        self.wordlist = choices(words, k=num_words)
        return " ".join(self.wordlist)

    def check_words_against_wordlist(self, typed_words: list) -> None:
        """
        Checks the list of words passed against the wordlist retrieved from file and updates the values of
        words_per_min, chars_per_min and wrong_words
        :param typed_words: a list with the typed words by the user
        :return: it doesn't return a value
        """
        self.words_per_min = sum([len(wl) for wl, tw in zip(self.wordlist, typed_words) if wl == tw]) // 5
        self.chars_per_min = sum([len(tw) for tw in typed_words])
        self.wrong_words = [wl for wl, tw in zip(self.wordlist, typed_words) if wl != tw]
