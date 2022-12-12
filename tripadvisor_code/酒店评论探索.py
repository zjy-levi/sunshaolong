import cv2
import numpy as np
import matplotlib.pyplot as plt
# import json
# from jsonpath import jsonpath
# import os
# from  urllib.request import urlretrieve
# with open(os.path.join(os.getcwd(),'sunshaolong\hoteldata\西安W酒店.json'),encoding='utf-8') as f:
#     review=json.load(f)
# # print(len(review))
# # print(review[0]['content'])
# photo_url={}
# for i in range(3):
#     photo_url[i]=jsonpath(review[i],'$..photos..original.url')
# 下载图片
# for j in range(len(photo_url[0])):  
#     urlretrieve(photo_url[0][j],os.path.join(os.getcwd(),f'sunshaolong\\測試圖片{j}.png'))
# 练练opencv
# 加载一个图片
img=cv2.imread(r'E:\code\python_code\BDManager\sunshaolong\0.png')
i=1
plt.figure(dpi=300)
for minVal in range(10,200,10):
    edges = cv2.Canny(img,minVal,200)
    plt.subplot(5,4,i)
    i+=1
    plt.title(minVal)
    plt.imshow(edges[:3000,:3000])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
