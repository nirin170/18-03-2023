dict1 = {
    "21": "work ",
    "22": "chutiyaa kaam ni krna",
    "23": "print statement chutiya",
    "24": "chutiya hrkte psnd nhi",
    "25": {"1": "work", "2": {'1': "hello", '2': 'world'}},
    "26": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "27": [{"4": 32, "5": 45}, {"4": 35, "5": 45}, {"4": 40, "5": 45}, ],
    "28": "aws",
    "29": "xyzsx",
    "30": "1234",

}

for a in dict1:
    if a=="25":
        for b in dict1[a]:
            if b=="2":
                for c in dict1[a][b]:
                    if c=="2":
                        # print(dict1[a][b][c])
                        
                        
                        
                        
                        for d in dict1:
                            if d=="27":
                                for e in dict1[d]:
                                    for f in e:
                                        if f =="4":
                                            print(e[f])


# find 25th value in 2
# find value of 4 in of 27 key

# def mess(dict1, ky):
#     # l = []
#     for i in dict1[ky]:
#         print(i["4"])
#         # l.append(i["4"])
#         # return l


# mess(dict1, "27")
# # print("we")


# ############ SIMPLEST WAY: ###########

# c=dict1["25"]["2"]
# print("The value of key 25 is:",c)




dict1 = {
    "21": "work ",
    "22": "chutiyaa kaam ni krna",
    "23": "print statement chutiya",
    "24": "chutiya hrkte psnd nhi",
    "25": {"1": "work", "2": {'1': "hello", '2': {"3":"vau1","4":"work1"}}},
    "26": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    "29": [{"4": 32, "5": [{"6":"890"},{"6":"890"}]},{"4": 32, "5": [{"6":"890"},{"6":"890"}]} ,{"4": 32, "5": [{"6":"890"},{"6":"890"}]}  ],
    "28": "aws",
    "34": "xyzsx",
    "30": "1234",
    "1":1

}