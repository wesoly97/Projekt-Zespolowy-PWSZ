from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Post(models.Model):
    userP = models.ForeignKey(User, on_delete=models.CASCADE)
    subject =  models.CharField(max_length=50)
    text =  models.CharField(max_length=200)
    def __str__(self):
        return self.subject

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    userA = models.ForeignKey(User, on_delete=models.CASCADE)
    answer =  models.CharField(max_length=200)
    def __str__(self):
        return self.answer
