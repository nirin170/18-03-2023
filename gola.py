# myfamily = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     }
# }
# for v in myfamily:
#     if v == {"name"}:
#         print("there is nothing")
# print(myfamily["child2"]["name"])




# result= {}
# students= int(input("enter the no. of students:"))
# i=0

# while i < students:
#     roll = int(input("enter the roll no:"))
#     marks = int(input("enter the marks:"))
#     result[roll] = marks
    
#     i= i + 1
    
# print ("do you want to display the results?")

# if input() == "yes":
#     print (result)
    
# else:
#     print("thank you!")
    
    
    
    
    




# Dik = {}

# Lodu = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]

# # Loop to add key-value pair
# # to dictionary
# for i in range(len(Lodu)):
	
# 	if Lodu[i][0] in Dik:
# 		Dik[Lodu[i][0]].append(Lodu[i][1])
# 	else:
# 		Dik[Lodu[i][0]]= []
# 		Dik[Lodu[i][0]].append(Lodu[i][1])
		
# print(Dik)






dict1 = {
    "1": "ishu",
    "2": [1, 23, 45, 24, 24, 5421],
    "3": ["dassd", "adwwww", "dasdw", "wde"],
    "4": {"yes": "no", "black": "whit"},
    "5": {"y": {'n': 'h', "k": [{"u": 'x'}]}}

}


class Nitin:

    def work(dict1):
        for i in dict1:
            if i == '5':
                if 'y' in dict1[i]:
                    if 'k' in dict1[i]['y']:
                        return "Scucces", dict1[i]['y']['k']


n = Nitin
l, m = n.work(dict1)
print(m)


# class nitin:
    
#     def kiki(dict1):
#         for i in dict1:
#             if "4" in dict1 :
#                 return "ghanta", dict1 [4]


# m= nitin
# print(m)