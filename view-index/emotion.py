from cnsenti import Sentiment

senti = Sentiment(pos='dict/pos.txt',
                  neg='dict/neg.txt',
                  merge=False,  # 是否融合 cnsenti 自带词典和用户导入的自定义词典
                  encoding='utf-8')


def prop(txt: str):
    res = senti.sentiment_count(txt)
    pos = res["pos"]
    neg = res["neg"]
    return {"pos_prop": pos / (pos + neg), "neg_prop": neg / (pos + neg)}
