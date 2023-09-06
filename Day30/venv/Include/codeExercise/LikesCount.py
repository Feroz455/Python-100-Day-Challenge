facebook_post = [
    {"likes": 21, "Comments" : 2},
    {"likes": 13, "Comments" : 2, "Shares": 1},
    {"likes": 33, "Comments" : 8, "Shares": 3},
    {"Comments" : 4, "Shares": 2},
    {"Comments" : 1, "Shares": 1},
    {"likes": 19, "Comments" : 3},
]
total_likes = 0
total_comments = 0
total_shares = 0
for post in facebook_post:
    try:
        total_likes = total_likes + post["likes"]
    except KeyError:
        pass
    try:
        total_comments =total_comments + post["Comments"]
    except:
        pass
    try:
        total_shares= total_shares + post["Shares"]
    except:
        pass
        
print(total_likes)
print(total_comments)
print(total_shares)