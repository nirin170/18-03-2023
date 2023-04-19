

# dic = {
    
#     "1":"work",
#     "2":[{'4':"5","7":{"6":[1,2,3,4]}}]
    
    
    
    
# }






# for a in dic:
#     if a=="2":
#         for b in dic[a]:
#             for c in b:
#                 if c=="7":
#                     for d in b[c]:
#                         print(b[c][d])



from django.db import models

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    "THE TME RATE OF CHANGE IN INEAR MOMENTUM IS DIRECTLEY PROPORTATIONAL TO THE NET APPLIED FORC AND THIS FORCE TAKES PLACE IN THE DIRECTION OF APPLID FORCE"

