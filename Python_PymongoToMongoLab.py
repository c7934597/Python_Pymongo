from pymongo import MongoClient

#本機連線
#uri = "mongodb://localhost:27017/"

#連線到雲端資料庫MongoLab
uri="mongodb://test:test123@ds119273.mlab.com:19273/games"
client = MongoClient(uri)
db = client.get_database("games")
collect = db.get_collection("books")

#把每筆資料都印出來
for post in collect.find():
    print(post)

#query的應用
post1 = collect.find_one({'pubId': 'OA'})
print(end="\n")
print(post1)

post2 = collect.find_one({'_id': 1})
print(end="\n")
print(post2)

title = post1['title']
print(end="\n")
print(title)

# 創造新post物件
post3 = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"]}

# 寫進去集合
post_id = collect.insert_one(post3).inserted_id  #加入文檔的ID方便辨識
print (post_id)