
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class MyWordCloud():
    def __init__(self, file_path):
        with open(file_path) as f:
            self.text = f.read()

    def run(self, file_name):
        wordcloud = WordCloud().generate(self.text)
        wordcloud.to_file(file_name)


if __name__ == '__main__':
    wc = MyWordCloud('src/data/movies2.txt')
    wc.run('output.png')
