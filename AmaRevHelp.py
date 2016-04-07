# -*- coding: utf-8 -*-
# amazon helpfulness rating regression and classification
# reading the data into pandas dataframe
import pandas as pd
import gzip


def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

Redf = getDF('reviews_Movies_and_TV.json.gz')

Medf = getDF('meta_Movies_and_TV.json.gz')

Redf['votes']=[k[1] for k in Redf.helpful]

Redf1 = Redf.ix[[i for i,k in enumerate(Redf.helpful) if k[1]>=k[0] and 10<k[1]<=10000 ]]

Redf1 = Redf1.reset_index()

Redf1['helprate']=[k[0]/float(k[1]) for k in Redf1.helpful]

Redf1['year']=[int(k.split()[2]) for k in Redf1.reviewTime]

plt.hist(Redf1.helprate,bins=10)
plt.xlabel('Helpfulness-Rating')
plt.ylabel('No. of reviews')

Redf1.groupby('overall').helprate.mean().plot(kind='bar')
plt.xlabel('Review-Rating')
plt.ylabel('Helpfulness-Ratio')

