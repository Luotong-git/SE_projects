#!/usr/bin/env python3
# coding: utf-8

import jieba.posseg as pesg
import math
import numpy as np
import sys
#import psutil
import os


class SimVsm:
    '''比较相似度'''
    def distance(self, text1, text2):
        words1 = [word.word for word in pesg.cut(text1) if word.flag[0] not in ['u', 'x', 'w']]
        words2 = [word.word for word in pesg.cut(text2) if word.flag[0] not in ['u', 'x', 'w']]
        tfidf_reps = self.tfidf_rep([words1, words2])
        return self.cosine_sim(np.array(tfidf_reps[0]), np.array(tfidf_reps[1]))

    '''对句子进行tfidf向量表示'''
    def tfidf_rep(self, sents):
        sent_list = []
        df_dict = {}
        tfidf_list = []
        for sent in sents:
            tmp = {}
            for word in sent:
                if word not in tmp:
                    tmp[word] = 1
                else:
                    tmp[word] += 1
            tmp = {word:word_count/sum(tmp.values()) for word, word_count in tmp.items()}
            for word in set(sent):
                if word not in df_dict:
                    df_dict[word] = 1
                else:
                    df_dict[word] += 1
            sent_list.append(tmp)
        df_dict = {word :math.log(len(sents)/df+1) for word, df in df_dict.items()}
        words = list(df_dict.keys())
        for sent in sent_list:
            tmp = []
            for word in words:
                tmp.append(sent.get(word, 0))
            tfidf_list.append(tmp)
        return tfidf_list

    '''余弦相似度计算相似度'''
    def cosine_sim(self, vector1, vector2):
        cos1 = np.sum(vector1 * vector2)
        cos21 = np.sqrt(sum(vector1 ** 2))
        cos22 = np.sqrt(sum(vector2 ** 2))
        similarity = cos1 / float(cos21 * cos22)
        return similarity

def test():

    f1name = sys.argv[1]
    f2name = sys.argv[2]
    f3name = sys.argv[3]
    f1 = open(f1name, "rt", encoding = 'UTF-8')
    f2 = open(f2name, "rt", encoding = 'UTF-8')
    f3 = open(f3name, "a+", encoding = 'UTF-8')

    txt1 = f1.read()
    txt2 = f2.read()

    simer = SimVsm()
    sim = simer.distance(txt1, txt2)

    f3.write(str("Similarity: %.2f"%sim)+'\n')
    f1.close()
    f2.close()
    f3.close()

'''
def performence_test():

    f1 = open("文件路径", "rt", encoding='UTF-8')
    f2 = open("文件路径", "rt", encoding='UTF-8')
    f3 = open("文件路径", "a+", encoding='UTF-8')

    txt1 = f1.read()
    txt2 = f2.read()

    simer = SimVsm()
    sim = simer.distance(txt1, txt2)

    f3.write(str("Similarity: %.2f" % sim) + '\n')
    f1.close()
    f2.close()
    f3.close()
'''

if __name__=="__main__":
    test()
    #performence_test()
    # 性能分析
    #print(u'当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) )
    #print(u'当前进程的使用的CPU时间：%.4f s' % (psutil.Process(os.getpid()).cpu_times().user) )







