# nam = {
#     "k" :8 ,
#     "k1":[1,2,3],
#     "k2":{"y1":45},
#     "k3":{"l1":3,"l2":45,"l3":[1,2,3,4]}
# }
# def jiju(f):
#     for g in f:
#         if "k3" == g:
#             return f[g]

# t=jiju(nam)
# print(t)


# source_arry = [5, 8, 6, 3, 4]
# odd_numbers = sorted([n for n in source_arry if n%2])
# c = 0
# res = []
# for i in source_arry:
#     if i %2:
#         res.append(odd_numbers[c])
#         c += 1
#     else:
#         res.append(i)
# print (res)


# sum=0
# for i in source_arry:
#     if i%2!=0:
#         sum=i
#         print(sum)

# string="camelCasing"

# def split_camel_case(string):
# Add a space before each capital letter
# def break_camel_case(s):
#     return ''.join([' ' + c if c.isupper() else c for c in s])

# # You can use this function to split a given string that is in camel case format, like this:

# # ```python
# s = "camelCasing"
# result = break_camel_case(s)
# print(result) # Output: "camel Casing"


# result = ""
# for char in string:
#     if char.isupper():
#         result += ""
#         result += char
# # Capitalize the first letter of each word
#     result = result.strip().title()
# print (result)

# n="8384051670982648262526513498362389583"
# sum = 0
# gum=0
# num=0
# for i in str(n):
#     # if int(i)>1:
#     sum += int(i)
# # print(sum)
# for b in str(sum):
#     gum+=int(b)
# for m in str(gum):
#     num+=int(m)
# print(num)



url = "http://github.com/carbonfive/raygun"
# def domain_name(url):
m=url.split('/')
print(m)
