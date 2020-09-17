#!/usr/bin/env python3
# coding: utf-8

import jieba.posseg as pesg
import math
import numpy as np
import sys
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


def test(s_position, d_position, ans_position):

    f1 = open(s_position, "rt", encoding = 'UTF-8')
    f2 = open(d_position, "rt", encoding = 'UTF-8')
    f3 = open(ans_position, "a+", encoding = 'UTF-8')

    txt1 = f1.read()
    txt2 = f2.read()

    simer = SimVsm()
    sim = simer.distance(txt1, txt2)
    print('查重结果为%.2f'%sim)

    f3.write(str("Similarity: %.2f"%sim)+'\n')
    f1.close()
    f2.close()
    f3.close()









