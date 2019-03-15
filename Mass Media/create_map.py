import pymongo
from pymongo import MongoClient
from collections import Counter
import pickle as pk
import pandas as pd
from scipy import spatial
from sklearn.preprocessing import normalize

art_client = MongoClient('mongodb://10.237.27.104:27017/')
art_db = art_client['media-db']

x = art_db.articles.find({})

city_map={}
state_map={}
total_map = {}
i=0
for art in x:
    i+=1
    try:
        ent=art['entities']
    except:
        continue
    for en in ent:
        if(en['type']=="City"):
            if en['name'].lower() in city_map.keys():
                city_map[en['name'].lower()].append(art['_id'])
            else:
                city_map[en['name'].lower()] = []
                city_map[en['name'].lower()].append(art['_id'])
            if en['name'].lower() in total_map.keys():
                total_map[en['name'].lower()].append(art['_id'])
            else:
                total_map[en['name'].lower()] = []
                total_map[en['name'].lower()].append(art['_id'])
        if(en['type']=="ProvinceOrState"):
            if en['name'].lower() in state_map.keys():
                state_map[en['name'].lower()].append(art['_id'])
            else:
                state_map[en['name'].lower()] = []
                state_map[en['name'].lower()].append(art['_id'])
            if en['name'].lower() in total_map.keys():
                total_map[en['name'].lower()].append(art['_id'])
            else:
                total_map[en['name'].lower()] = []
                total_map[en['name'].lower()].append(art['_id'])
    if(i%100000==0):
        # file1 = open("/Users/abhishekyadav/Documents/Study/BTP/city_to_article/city_map_big.pk",'wb')
        # file2 = open("/Users/abhishekyadav/Documents/Study/BTP/city_to_article/state_map_big.pk",'wb')
        # file3 = open("/Users/abhishekyadav/Documents/Study/BTP/city_to_article/total_map_big.pk",'wb')
        # pk.dump(city_map,file1)
        # pk.dump(state_map,file2)
        # pk.dump(total_map,file3)
        # file1.close()
        # file2.close()
        # file3.close()
        print(i)


file1 = open("/Users/abhishekyadav/Documents/Study/BTP/city_to_article/city_map_big.pk",'wb')
file2 = open("/Users/abhishekyadav/Documents/Study/BTP/city_to_article/state_map_big.pk",'wb')
file3 = open("/Users/abhishekyadav/Documents/Study/BTP/city_to_article/total_map_big.pk",'wb')
pk.dump(city_map,file1)
pk.dump(state_map,file2)
pk.dump(total_map,file3)
file1.close()
file2.close()
file3.close()