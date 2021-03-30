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

class Zadanie_otwarte(models.Model):
    nr_zadania=models.IntegerField()
    nr_wersji=models.IntegerField()
    tresc = models.CharField(max_length=200)
    odpowiedz = models.CharField(max_length=30)
    dzial=models.CharField(max_length=30)
    punkty=models.IntegerField()
    def __str__(self):
        return self.tresc

class Zadanie_zamkniete(models.Model):
    nr_zadania=models.IntegerField()
    nr_wersji=models.IntegerField()
    tresc = models.CharField(max_length=200)
    odp_a= models.CharField(max_length=40)
    odp_b= models.CharField(max_length=40)
    odp_c= models.CharField(max_length=40)
    odp_d= models.CharField(max_length=40)
    odpowiedz = models.CharField(max_length=40)
    dzial=models.CharField(max_length=30)
    punkty=models.IntegerField()
    def __str__(self):
        return self.tresc


   