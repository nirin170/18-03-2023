

# dnr = {
#     "1": "ishu",
#     "2": [1, 23, 45, 24, 24, 5421],
#     "3": ["dassd", "adwwww", "dasdw", "wde"],
#     "4": {"yes": "no", "black": "whit"},
#     "5": {"y": {'n': 'h', "z": [{"u": 'x'}]}}

# }


# for k in dnr:
#     if k == "5":
#         for l in dnr[k]:
#             if l=="y":
#                 for m in dnr[k][l]:
#                     if m=="z":
#                         for n in dnr[k][l][m]:
#                             for o in n:
#                                 if o=="u":
#                                     print(n[o])
# class Nitin:

#     def work(dict1):
#         for i in dict1:
#             if i == '5':
#                 if 'y' in dict1[i]:
#                     if 'k' in dict1[i]['y']:
#                         return "Scucces", dict1[i]['y']['k']


# n = Nitin
# l, m = n.work(dict1)
# print(m)


# dict1 ={
# "1" :"ishu",
# "2": [1, 23, 45, 24, 24, 5421],
# "3": ["dassd", "adwwww", "dasdw", "wde"],
# "4": {"yes": "no", "black": "whit"},
# "5": {"y": {'n': 'h', "k": [{"u": 'x'}]}}

# }


# def om(dict1):
#     for n in dict1:
#         if n == "1":
#             print(dict1["1"])
# nitin = om(dict1)
# print(nitin)


# sentence = "is2 Thi1s T4est 3a"
# # def order(sentence):
# x = sentence.split()
# # print(x)
# for i in x:
#     for v in i:
#         # if v.isdigit():
#         v = sorted(x, key=lambda r: int(''.join(filter(str.isdigit, r))))
#         o=" ".join(v)
# print(o)

# print(m)


# string = "4of Fo1r pe6ople g3ood th5e the2"
# words = string.split()  # split the string into words
# print(words)
# # sort the words based on the numbers in them
# sorted_words = sorted(words, key=lambda w: int(''.join(filter(str.isdigit, w))))
# print(sorted_words)
# sorted_string = ' '.join(sorted_words)
# # print(sorted_string)


# a = ['k','a','p','i','l']
# temp = a
# for i, v in enumerate(a):
#     print(i)
#     # temp[(len(a)-1)-i] = a[i]


# a = temp
# print(a)


# s="ABC"
# m=list(s.split())
# # print(m)
# def permutation(m):
#     permList = permutation(m)
#     for i in list(permList):
#         print(''.join(i))


sentence = "Hey fellow warriors "
# def spin_words(sentence):
# Your code goes here
s = sentence.split()
new = ""
for i in s:
    if len(i) >= 5:
        new+=(i[::-1])
    else:
        new += i
    if s.index(i) + 1 < len(s):
        new += " "

print(new)
# b="".join(reversed(i[::-1]))
# b=sentence.replace(i[::-1])
# b="".join(i[::-1]+sentence)
# print(b)

# reversed=''.join(reversed(s))
