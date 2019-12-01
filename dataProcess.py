import pandas as pd
from collections import Counter
import re
import jieba as jb
import jieba.posseg
import jieba.analyse as analyse
# from snownlp import SnowNLP
from snownlp import sentiment


from dataShow import plot_most_frequent, sentiment_distribution, words_cloud


def clean_str(texts):
    texts_copy = []
    for text in texts:
        # if math.isnan(text):
        if text.__class__.__name__ == 'float':  # 去掉一些nan值
            continue
        if text.startswith('回复@'):
            text = re.sub('回复@[^:].+:', '', text)
        text = re.sub('[。！!.]{3,}', '', text)
        if len(text) >= 4:
            texts_copy.append(text)
    return texts_copy


def word_frequence(texts, most_common=100):
    stop_words = [line.strip() for line in open('stopwords\哈工大停用词表.txt', 'r', encoding='utf-8').readlines()]
    c = Counter()
    for text in texts:
        cuted_text = jieba.posseg.cut(text)  # 带词性的分词
        for word, pos in cuted_text:
            if word not in stop_words and (pos.startswith('v') or pos.startswith('n')):
                c[word] += 1
    common_words = c.most_common(most_common)
    for common_tuple in common_words:
        print('s', common_tuple[0], 's', ' ', common_tuple[1], ' ', common_tuple[1]/len(texts))
    return common_words


def sentiment_analyse(texts):
    sentiments = []
    for text in texts:
        sentiments.append(sentiment.classify(text))
    return sentiments


def extract_tags(texts):
    document = ' '.join(texts)
    keywords_textrank = analyse.textrank(document, topK=30)
    # print(keywords)
    keywords_tfidf = analyse.tfidf(document, topK=30)
    # print(keywords)
    return keywords_textrank, keywords_tfidf


if __name__ == "__main__":
    df_comments = pd.read_csv('comments\comment_v1.csv')
    comments = df_comments['content']
    print(len(comments))
    comments = clean_str(comments)
    print(len(comments))
    print()
    print(comments[:50])
    extract_tags(comments[:100])
    commons = word_frequence(comments)
    words_cloud(comments)
    # plot_most_frequent(commons)
    # sentiments = sentiment_analyse(comments)
    # sentiment_distribution(sentiments, comments)
    #
    # for s, t in zip(sentiments, comments):
    #     pos = 0
    #     neg = 0
    #     if s>0.95:
    #         print(round(s, 3), t)
    #         pos += 1
    #     elif s<0.05:
    #         print(round(s, 3), t)
    #         neg += 1
    # print(pos, neg)
    # plt.plot(range(len(sentiments)), sorted(sentiments))
    # plt.show()
