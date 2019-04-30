import pandas as pd
msg=pd.read_csv('train_1500.txt',encoding="utf-8", names=['message','label'])
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
xtrain=msg.message
ytrain=msg.labelnum
#print(ytrain[:100])

#with open("train_label.txt",'a', encoding="utf-8") as f:
#    f.write(ytrain)

#f.close()
msg1=pd.read_csv('test.txt', names=['message','label'])
msg1['labelnum']=msg1.label.map({'pos':1,'neg':0})
xtest=msg1.message
ytest=msg1.labelnum

#with open("test_label.txt",'a', encoding="utf-8") as f:
#    f.write(ytest)
#f.close()
#from sklearn.model_selection import train_test_split
#xtrain,xtest,ytrain,ytest=train_test_split(x,y)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
xtrain_dtm=cv.fit_transform(xtrain)
xtest_dtm=cv.transform(xtest)
df=pd.DataFrame(xtrain_dtm.toarray(),columns=cv.get_feature_names())
#print(df)

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(xtrain_dtm,ytrain)
pred=clf.predict(xtest_dtm)
#print(xtest)
#print(pred)
from sklearn import metrics
print(metrics.confusion_matrix(ytest,pred))
print("precision",metrics.precision_score(ytest,pred))
print(metrics.recall_score(ytest,pred))
print("accuracy",metrics.accuracy_score(ytest,pred))

#aspects = {
#        "food": ['bread','cooking','cuisine','drink','food','meal','foodstuff','meat','snack','eatable','fruits','dish'],
#        "location": ['location','place','area','neighborhood','spot', 'region','venue'],
#        "amenities":[ 'amenitites','luxuries', 'conveniences', 'niceities','facility', 'comfort'],
#        "staff": ['staff','team', 'official','work force','security','waiter','reception','servent','maid'],
#        "cleanliness":['clean','sanitation','tidyness','neatness','fresh','organised'],
#        "customer_support": ['help','support'],
#        "quietness":['calm','silent','cool','quiet','patient'],
#        "affordability":['cheap','affordable','expensive','lavish','extravagant','economical','feasible','budget'],
#        "view":['view','look','scene','sight','landscape','panaroma','seascape','vision'],
#        "payment":['payment','card','amount','bill','cheque','cash','money','deposit','refund'],
#        "wifi":['wifi','internet','net','speed','network']
#        }
#flag=[]
#hotels=["hotel1.txt","hotel2.txt","hotel3.txt","hotel4.txt"]
#for hotel in hotels:
#    file = open(hotel, "r", encoding="utf-8")  
#    for line in file:
#        for word in line.split():
#            for i in aspects:
#                for j in aspects[i]:
#                    if j == word:
#                        if i in flag:
#                            continue
#                        f = open(hotel+"_"+i+".txt", "a",encoding="utf-8")
#                        #a = line.replace(' ,pos\n', ',pos\n')
#                        #b = a.replace(' ,neg\n',',neg\n')
#                        f.write(line)
#                        f.close()
#                        flag.append(i)
#        flag=[]
#    file.close()     
average_sentiment={}
hotel1_average={}
hotel2_average={}
hotel3_average={}
hotel4_average={}
list1=["hotel1","hotel2","hotel3","hotel4"]
list2=["affordability","amenities","cleanliness","customer_support","food","location","quietness","staff","view","payment","wifi"]
for i in list1:
    for j in list2:
        file = open(i+"_"+j+".txt", "r", encoding="utf-8") 
        p=0
        c=0
        for line in file:
            c=c+1
            line=[line]
            t=cv.transform(line)
            predicted=clf.predict(t)
            if predicted==1:
                p=p+1
        average_sentiment[i+"_"+j]=round((p/c)*100,4)
        file.close()
    if i=='hotel1':
        hotel1_average=average_sentiment
    if i=='hotel2':
        hotel2_average=average_sentiment
    if i=='hotel3':
        hotel3_average=average_sentiment
    if i=='hotel4':
        hotel4_average=average_sentiment
    average_sentiment={}
    
print("----------------------------------------------------")
print("nn")
print(hotel1_average)
print("----------------------------------------------------")
print("nn")
print(hotel2_average)
print("----------------------------------------------------")
print("nn")
print(hotel3_average)
print("----------------------------------------------------")
print("nn")
print(hotel4_average)


#i=0
#hotel1_average=[]
#hotel2_average=[]
#hotel3_average=[]
#hotel4_average=[]
#
#
#for q, p in average_sentiment.items():
#    i=i+1
#    if i in range[1, 12]:
#        hotel1_average.append(p)
#    if i in range[12, 23]:
#        hotel1_average.append(p)
"""
str="hot"
str=[str]
t=cv.transform(str)
predicted=clf.predict(t)
print(predicted)
"""