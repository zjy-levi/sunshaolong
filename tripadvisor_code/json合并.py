import os
import json
from jsonpath import jsonpath
import pandas as pd
def mergejson(filename):
    j_all={}
    for i in os.scandir():#扫盘
        if i.name.split('.')[-1] =='json':#json格式
            with open(f'{i.name}','r',encoding='utf-8') as f:
                a=json.load(f)
                j_all[i.name.split('.')[0]]=a
    # jsonall=json.dumps(str(j_all))
    # print('评论数量：',jsonpath(jsonall,'$[0:]..'))
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(j_all,f,ensure_ascii=False)

def construct_traindata():
    # 获取评分和评论信息
    review=[]
    rating=[]
    title=[]
    # kind=[]
    for i in os.scandir():#扫盘
        if i.name.split('.')[-1] =='json':#json格式
            with open(f'{i.name}','r',encoding='utf-8') as f:
                a=json.load(f)
                review.extend(jsonpath(a,'$[*].content'))
                rating.extend(jsonpath(a,'$[*].rating'))
                title.extend(jsonpath(a,'$[*].title'))
                # kind.extend(jsonpath(a,'$[*].'))
    print(len(review),len(rating))
    df=pd.DataFrame({'title':title,'review':review,"rating":rating})
    # df.to_csv('评论与评分.csv')
    # 特征转换 
    df['label']=df['rating'].apply(lambda x:trans(x))
    # print(df['label'].head())
    df.to_csv('评论与评分.csv')
    return df
def trans(df):
    if df==4 or df==5:
        return 1
    # if df==3:
    #     return 0
    else :
        return -1
if __name__ == '__main__':
    os.chdir(os.path.join(os.getcwd(),'sunshaolong\hoteldata'))
    filename='all酒店.json'
    # mergejson(filename)
    # 获取评分和评论信息
    df=construct_traindata()
    
    