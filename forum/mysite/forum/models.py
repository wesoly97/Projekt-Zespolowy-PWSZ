from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    numer_kontaktowy = models.CharField(max_length=15,blank=True)
    szkola = models.CharField(max_length=100,blank=True)
    ranga = models.CharField(max_length=40,blank=True)
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
    url = models.CharField(max_length=200,blank=True,null=True)
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
    url = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.tresc

class zadanie_matematyczne(models.Model):
    nr_zadania=models.IntegerField()
    nr_wersji=models.IntegerField()
    rodzaj=models.CharField(max_length=30)
    zestaw= models.CharField(max_length=40,blank=True)
    tresc = models.CharField(max_length=200)
    odp_a= models.CharField(max_length=40,blank=True)
    odp_b= models.CharField(max_length=40,blank=True)
    odp_c= models.CharField(max_length=40,blank=True)
    odp_d= models.CharField(max_length=40,blank=True)
    rozwiazanie= models.CharField(max_length=200,blank=True)
    odpowiedz = models.CharField(max_length=40)
    dzial=models.CharField(max_length=30,blank=True)
    punkty=models.IntegerField()
    url = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.tresc

class PostM(models.Model):
    zadanie = models.ForeignKey(zadanie_matematyczne, on_delete=models.CASCADE)
    tresc =  models.CharField(max_length=200)
    def __str__(self):
        return self.zadanie

class AnswerM(models.Model):
    zadanie = models.ForeignKey(PostM, on_delete=models.CASCADE)
    userA = models.ForeignKey(User, on_delete=models.CASCADE)
    answer =  models.CharField(max_length=200)
    def __str__(self):
        return self.answer

class Podejscie(models.Model):
    user = models.IntegerField(blank=True)
    numeryZadanZamknietych = models.CharField(max_length=70)
    numeryZadanOtwartych = models.CharField(max_length=70)
    odpowiedzi = models.CharField(max_length=200)
    punkty=models.IntegerField();
    def __str__(self):
        return self.punkty
   