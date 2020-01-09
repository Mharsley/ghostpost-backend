from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    boast = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        # return f"{self.title} - {self.author}"
        return f"{self.title}"