import random
from utils import *


class Wordle:
    def __init__(self, word_len: int = 5, limittopwords: int = 10_000):
        self.word_len = word_len
        self.words = self.generate_words(word_len, limittopwords)

    def generate_words(self, word_len: int = 5, limittopwords: int = 10_000):

        # build data:
        words = []
        file_dir = './data/words_frequency.txt'
        with open(file_dir) as f:
            for line in f:
                word, frequency = line.split(', ')
                frequency = int(frequency)
                words.append((word.upper(), frequency))

        # sort date:
        words = sorted(words, key=lambda w: w[1], reverse=True)

        # limit top words:
        words = words[:limittopwords]

        # filter data:
        # 5 harfiha
        words = list(filter(lambda w: len(w[0]) == word_len, words))

        # delete frequencies:
        words = [w[0] for w in words]

        return words

    def run(self):
        # valid_char
        # invalid_position
        # invalid_char

        # word selection:
        random.seed(43)
        selected_word = random.choice(self.words)
        num_try = 6
        success = False

        # run:
        while num_try:
            guess_word = input(
                f'Enter a {self.word_len} letter word (or q to exit): ').upper()
            if guess_word == 'Q':
                break

            # word length
            if len(guess_word) != self.word_len:
                print(f'word must have {self.word_len} letters')
                continue
                # vaghti continue mishe dg nmiad payin k
                # bekhad ye count hesab she

            # check if grey
            if guess_word not in self.words:
                print_grey('input is not a word')
                print()
                continue

            # check wordle
            for gw, sw in zip(guess_word, selected_word):
                if gw == sw:
                    print_success(f' {gw} ')
                elif gw in selected_word:
                    print_warning(f' {gw} ')
                else:
                    print_error(f' {gw} ')
            if guess_word == selected_word:
                print(colored('\n Congratulations ! ',
                      'blue', attrs=['bold', 'blink']))
                success = True
                break
            print()
            num_try -= 1
        if not success:
            print_error(f'You Failed! The word was {selected_word}')
