#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
planets = sns.load_dataset("planets")
planets.head()


# In[3]:


df = planets.copy()


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[8]:


df.dtypes


# In[9]:


df.shape


# In[10]:


df.columns


# In[12]:


df.describe().T


# In[13]:


df.head()


# In[14]:


#hiç eksik gözlem var mı?


# In[15]:


df.isnull().values.any()


# In[16]:


#hangi değişkende kaçar tane var


# In[17]:


df.isnull().sum()


# In[18]:


df["orbital_period"].fillna(0, inplace = True)


# In[19]:


df.isnull().sum()


# In[21]:


df = planets.copy()
df.head()


# In[22]:


df.isnull().sum()


# In[23]:


kat_df = df.select_dtypes(include = ["object"])


# In[24]:


kat_df.head()


# In[25]:


kat_df.method.unique()


# In[26]:


kat_df["method"].value_counts().count()


# In[27]:


kat_df["method"].value_counts()


# In[29]:


df["method"].value_counts().plot.barh();


# In[30]:


df_num = df.select_dtypes(include = ["float64", "int64"])


# In[31]:


df_num.head()


# In[34]:


df_num.describe().T


# In[35]:


df_num["distance"].describe()


# In[47]:


print("Ortalama: " + str(df_num["distance"].mean()))
print("Dolu Gözlem Sayısı: " + str(df_num["distance"].count()))
print("Maksimum Değer: " + str(df_num["distance"].max()))
print("Minimum Değer: " + str(df_num["distance"].min()))
print("Medyan: " + str(df_num["distance"].median()))
print("Standart Sapma: " + str(df_num["distance"].std()))


# In[48]:


diamonds = sns.load_dataset('diamonds')
df = diamonds.copy()
df.head()


# In[49]:


df.info()


# In[53]:


df.describe().T


# In[54]:


df.head()


# In[55]:


df["cut"].value_counts()


# In[56]:


df["color"].value_counts()


# In[57]:


#ordinal tanımlama
from pandas.api.types import CategoricalDtype


# In[58]:


df.cut.head()


# In[59]:


df.cut = df.cut.astype(CategoricalDtype(ordered = True))


# In[60]:


df.cut.head(1)


# In[61]:


cut_kategoriler = ["Fair", "Good", "Very Good", "Premium", "Ideal"]


# In[63]:


df.cut =  df.cut.astype(CategoricalDtype(categories = cut_kategoriler, ordered = True))


# In[64]:


df.cut.head(1)


# In[65]:


#barplot


# In[67]:


(df["cut"]
 .value_counts()
 .plot.barh()
 .set_title("Cut Değişkeninin Sınıf Frekansları"));


# In[79]:


sns.barplot(x = "cut", y = df.cut.index , data = df);


# In[69]:


df.head()


# In[70]:


sns.catplot(x = "cut", y = "price", data = df);


# In[80]:


sns.barplot( x= "cut", y = "price", hue= "color", data = df);


# In[81]:


df.groupby(["cut","color"])["price"].mean()


# In[82]:


sns.distplot(df.price, kde = False);


# In[83]:


get_ipython().run_line_magic('pinfo', 'sns.distplot')


# In[87]:


sns.distplot(df.price, bins = 5, kde = False);


# In[88]:


sns.distplot(df.price);


# In[91]:


sns.distplot(df.price, hist = False);


# In[92]:


df["price"].describe()


# In[93]:


sns.kdeplot(df.price, shade = True);


# In[97]:


(sns.
 FacetGrid(df,
               hue = "cut",
               height = 5,
               xlim = (0,10000))
.map(sns.kdeplot, "price", shade = True)
 .add_legend()
);


# In[102]:


sns.catplot(x = "cut", y= "price", hue = "color", kind = "point", data = df);


# In[103]:


tips = sns.load_dataset("tips")
df = tips.copy()
df.head()


# In[104]:


df.tail()


# In[106]:


df.describe().T


# In[107]:


df["sex"].value_counts()


# In[108]:


df["smoker"].value_counts()


# In[109]:


df["day"].value_counts()


# In[110]:


df["time"].value_counts()


# In[111]:


sns.boxplot(x = df["total_bill"])


# In[115]:


sns.boxplot(x = df["total_bill"], orient = "v");


# In[116]:


#çaprazlamalar


# In[117]:


df.describe().T


# In[118]:


#hangi günler daha afzla kazanıyoruz


# In[119]:


sns.boxplot(x = "day", y = "total_bill", data = df);


# In[120]:


sns.boxplot(x = "time", y = "total_bill", data = df);


# In[121]:


sns.boxplot(x = "size", y = "total_bill", data = df);


# In[123]:


sns.boxplot(x = "day", y = "total_bill", hue = "sex", data = df);


# In[124]:


#violin


# In[125]:


sns.catplot(y = "total_bill", kind = "violin", data = df);


# In[ ]:




