import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from wordcloud import WordCloud
import jieba as jb

matplotlib.rcParams['font.family'] = 'Times New Roman'
plt.style.use('dark_background')


def plot_most_frequent(common_words):
    # rows = len(common_words/10) #一张图画十个
    data = np.zeros(len(common_words))
    words = []
    for ii in range(len(common_words)):
        print(common_words[ii])
        words.append(common_words[ii][0])
        data[ii] = common_words[ii][1]

    plt.figure(figsize=(20, 5))
    plt.bar(range(len(data)), data, width=0.4)
    plt.xticks(range(len(data)), words, rotation=90)
    plt.title('词频图 (名词与动词)')
    plt.xlabel('词')
    plt.ylabel('频次')
    plt.savefig('result\word_frequent.png', dpi=600, bbox_inches='tight')
    plt.show()

    # data = data.reshape((-1, 10))

    # plt.figure(figsize=(5, 10))
    # for ii in range(data.shape[0]):
    #     plt.subplot(data.shape[0], 1, ii+1)
    #     plt.bar(range(len(data[ii])), data[ii], width=0.4)
    #     plt.ylim([0, common_words[0][1] + 30])
    # plt.show()

    return 0


def words_cloud(comments):
    # pass
    wcd = WordCloud(
                    background_color='black',
                    repeat=False,
                    max_words=100,
                    height=400,
                    width=500,
                    mask=None,
                    max_font_size=50,
                    min_font_size=10,
                    colormap='Reds',
                    mode='RGBA'
    )
    comments = ' '.join(comments)
    ss = ' '.join(jb.lcut(comments))
    wcd.generate(ss)
    wcd.to_image()
    wcd.to_file('result\wordCloud.png')
    print('+++++ 词云已经生成完毕 +++++')
    return 0


def sentiment_distribution(sentiments, comments, up=0.95, down=0.05):
    pos = 0
    neg = 0
    for s, t in zip(sentiments,  comments):
        if s > up:
            print(round(s, 3), t)
            pos += 1
        elif s < down:
            print(round(s, 3), t)
            neg += 1
    print(pos, neg)
    # plt.plot(range(len(sentiments)), sorted(sentiments))
    plt.scatter(range(len(sentiments)), sentiments, s=0.4)
    plt.scatter(range(len(sentiments)), sorted(sentiments), s=0.2, marker='*')
    plt.ylim([0, 1.1])
    plt.ylabel('Sentiment')
    plt.savefig('result\sentiment.png', dpi=1080, bbox_inches='tight')
    plt.show()

    return 0
