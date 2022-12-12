import pandas as pd
import os
from jieba import lcut
from jieba import posseg as pseg
# from bertopic import BERTopic
from imblearn.over_sampling import SMOTE,BorderlineSMOTE

from sklearn.model_selection import train_test_split
# os.chdir("E:\code\python_code\BDManager\sunshaolong\model\stopwords-master")
# lst=[]
# for i in os.scandir():
#     if i.name.split('.')[-1]=='txt':
#         with open(i.name,'r',encoding='utf-8') as f:
#             lst.extend(f.readlines())
#         # break
# s=pd.Series(lst)
# # s=s.str.replace('\n','')
# print(s[:5])
# with open('my_dict.txt','w',encoding='utf-8') as f:
#     f.writelines(s)
def clean_text_nval(text):
    '''
    jieba分词词性选择：
    名词（不要人名）
    动词类
    形容词类
    成语（如果有的话）
    '''
    words= pseg.lcut(text)
    return ' '.join([i for i,f in words if len(i)>=2 and (f=='n' or f.startswith('v') or f.startswith('a') or f.startswith('l'))])
def over_smote_(X, y):
    """
    功能: 二分类过采样，以smote举例。
    why: 当正负样本比例相差过大时，一般为1：20以内。举例：如果正负样本为1：99，那么相当于告诉模型只要判断为负，则正确率就为99%，那么模型就会这么做。
    X: 数据X（df型/无label）
    y: 数据y（df型/label）
    num: 过采样的个数
    reture: 
        X_resampled: 过采样后的X
        y_resampled: 过采样后的y
    """
    ss = pd.Series(y).value_counts()
    smote = SMOTE(random_state=2019)  # radom_state为随机值种子，1:ss[1]+表示label为1的数据增加多少个
    # adasyn = ADASYN(sampling_strategy={0:ss[0],1:ss[1]+800},random_state=2019) # 改变正样本数量参数
    X_resampled, y_resampled = smote.fit_resample(X, y)
    # print("过采样个数为：", num)
    # check_num_X = X_resampled.shape[0] - X.shape[0]
    # check_num_y = y_resampled.shape[0] - y.shape[0]
    # if (check_num_X == check_num_y) and (check_num_X == num):
    #     print("过采样校验：成功")
        # return X_resampled, y_resampled
    # else:
    #     print("过采样校验：失败")
    print(len(X_resampled))

if __name__ == '__main__':
    data=pd.read_csv(r'E:\code\python_code\BDManager\sunshaolong\model\topic2vec数据.csv',index_col=0)
    X=data.iloc[:,:-1]
    y=data.iloc[:,-1]
    X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    random_state=0,
                                                    test_size=0.2)
    smo=SMOTE(random_state=0)
    print('采样前：',X.shape[0])
    print(y_train.value_counts())
    X__train,y__train = smo.fit_resample(X_train,y_train)
    print('采样后：',data.shape[0])
    print(y__train.value_counts())  



    

