"""
Q9.9 Answer.
"""
import matplotlib.pyplot as plt
import wikipedia as w
from wordcloud import WordCloud, STOPWORDS

if __name__ == '__main__':
    wiki = w.page("Korea")
    text = wiki.content
    s_words = STOPWORDS.union({"south", "north", "korean", "world", "country"})
    wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words).generate(text)
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.show()
