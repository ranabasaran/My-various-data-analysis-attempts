#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("diabetes.csv")
data.head()


# In[2]:


seker_hastalari = data[data.Outcome == 1]
sagliklilar = data[data.Outcome == 0 ]

plt.scatter(sagliklilar.Age, sagliklilar.Glucose, color = "green", label = "sağlıklı", alpha = 0.4)
plt.scatter(seker_hastalari.Age, seker_hastalari.Glucose, color = "red", label = "diyabet hastası", alpha = 0.4)

plt.xlabel("Age")
plt.ylabel("Glucose")
plt.legend()
plt.show()


# In[3]:


y = data.Outcome.values 
x_ham_veri = data.drop(["Outcome"],axis = 1)

x = (x_ham_veri - np.min(x_ham_veri)) / (np.max(x_ham_veri) - np.min(x_ham_veri))

#önce 
print("Normalizasyon öncesi ham veriler:\n")
print(x_ham_veri.head())

#sonra 
print("\n\n\nNormalizasyon sonrası yapay zekaya eğitimi için verceğimiz veriler:\n")
print(x.head())


# In[4]:


#train ve test datamızı ayırıyoruz 

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1, random_state = 1)


#KNN modelini oluşturmadan önce en uygun k değerini bulalım

sayac = 1
for k in range(1,11):
    knn_yeni = KNeighborsClassifier(n_neighbors = k)
    knn_yeni.fit(x_train,y_train)
    print(sayac, "  ", "Doğruluk oranı: %", knn_yeni.score(x_test,y_test)*100)
    sayac += 1


# In[5]:


#modeli olusturabiliriz

knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train, y_train)
prediction = knn.predict(x_test)
print("K = 3 için test verilerimizin doğrulama testi sonucu", knn.score(x_test,y_test))


# In[6]:


# Yeni hasta tahmini
from sklearn.preprocessing import MinMaxScaler

# normalization yapıyoruz - daha hızlı normalization yapabilmek için MinMax  scaler kullandım
sc = MinMaxScaler()
sc.fit_transform(x_ham_veri)

new_prediction = knn.predict(sc.transform(np.array([[6,148,72,35,0,33.6,0.627,50]])))
new_prediction[0]



