from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import User
from .models import Post
from .models import Answer
from .models import PostM
from .models import AnswerM
from .models import Zadanie_zamkniete
from .models import Zadanie_otwarte
from .models import zadanie_matematyczne
import random



def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'forum/index.html', context)

def register1(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'forum/register1.html', context)

def register2(request):
    Name = request.POST['Name']
    Password = request.POST['Password']
    if (Name=="" or Password=="" ):
        msg="Empty,try again"
    else:
        if(User.objects.filter(name=Name).count()==0):
            u = User(name=Name,password=Password)
            u.save()
            msg="User added"
        else:
            msg="User with that name exists,try again"
    context = {'msg': msg}
    return render(request, 'forum/register2.html', context)

def usersHOME(request, user_id):
    users = User.objects.filter(id=user_id)
    context = {'users': users}
    return render(request, 'forum/usersHome.html', context)

def user_at_forum(request, user_id):
    users = User.objects.filter(id=user_id)
    posts = Post.objects.all()
    postsM= PostM.objects.all()
    context = {'posts': posts,'users': users,'postsM': postsM}
    return render(request, 'forum/userFORUM.html', context)

def math_page(request, user_id):
    users = User.objects.filter(id=user_id)
    context = {'users': users}
    return render(request, 'forum/MATH_PAGE.html', context)

def math_page2(request, user_id):
    users = User.objects.filter(id=user_id)

    r=request.session.get('r')
    r2=request.session.get('r2')
    r3=request.session.get('r3')
    r4=request.session.get('r4')

    r=(random.randint(1,4))
    r2=(random.randint(1,4))
    r3=(random.randint(1,3))
    r4=(random.randint(1,3))

    request.session['r'] = r
    request.session['r2'] = r2
    request.session['r3'] = r3
    request.session['r4'] = r4
   
    zos=zadanie_matematyczne.objects.filter(nr_wersji=r).filter(rodzaj="otwarte")
    zzs=zadanie_matematyczne.objects.filter(nr_wersji=r2).filter(rodzaj="zamkniete")

    context = {'users': users,'zos': zos,'zzs': zzs}
    return render(request, 'forum/MATH_PAGE2.html', context)

def math_page3(request, user_id):
    users = User.objects.filter(id=user_id)

    r=request.session.get('r')
    r2=request.session.get('r2')
    r3=request.session.get('r3')
    r4=request.session.get('r4')

    zos=zadanie_matematyczne.objects.filter(nr_wersji=r).filter(rodzaj="otwarte")
    zzs=zadanie_matematyczne.objects.filter(nr_wersji=r2).filter(rodzaj="zamkniete")

    odpZ = request.POST.getlist('odpZ')
    odpO = request.POST.getlist('odpO')

    linki = []

    punktyZ=0
    punktyO=0
    punktyMAX=0
    x=0
    for zz in zzs:
      posts= PostM.objects.filter(zadanie=zz.id)
      for post in posts:
        linki.append(post)
      punktyMAX=punktyMAX+1
      if zz.odpowiedz == odpZ[x]:
        punktyZ=punktyZ+1
      x=x+1

    for zo in zos:
      posts= PostM.objects.filter(zadanie=zo.id)
      for post in posts:
        linki.append(post)
      punktyMAX=punktyMAX+2
      x=int(punktyO)/2
      if zo.odpowiedz == odpO:
        punktyO=punktyO+2
    
    punkty=punktyZ+punktyO
      

    context = {'users': users,'zos': zos,'zzs': zzs,'odpO': odpO,'odpZ': odpZ,'punktyMAX': punktyMAX,'punkty': punkty,'linki': linki}
    return render(request, 'forum/MATH_PAGE3.html', context)

def post(request, user_id,post_id):
    users = User.objects.filter(id=user_id)
    posts = Post.objects.filter(id=post_id)
    answers = Answer.objects.filter(post=post_id)
    context = {'posts': posts,'answers': answers,'users': users}
    return render(request, 'forum/posts.html', context)

def postM(request, user_id,post_id):
    users = User.objects.filter(id=user_id)
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(zadanie=post_id)
    context = {'postsM': postsM,'answersM': answersM,'users': users}
    return render(request, 'forum/postsM.html', context)

def add(request, user_id):
    users = User.objects.filter(id=user_id)
    temat = request.POST['temat']
    tresc = request.POST['tresc']
    for user in users:
        w=user
    error=""
    if (temat=="" or tresc==""):
        error="Empty,try again"
    else:
        q = Post(userP=w,subject=temat,text=tresc)
        q.save()
        error="Post added"

    context = {'users': users,'temat': temat,'tresc': tresc,'error': error}
    return render(request, 'forum/add.html', context)

def delete(request, user_id,post_id):
    users = User.objects.filter(id=user_id)
    posts = Post.objects.filter(id=post_id)
    posts.delete()
    context = {'users': users}
    return render(request, 'forum/delete.html', context)

def odp(request, user_id,post_id):
    users = User.objects.filter(id=user_id)
    posts = Post.objects.filter(id=post_id)
    answers = Answer.objects.filter(post=post_id)
    error=""
    for user in users:
        x=user
    for post in posts:
        y=post
    new_answer = request.POST['comment']
    if (new_answer==""):
        error="Empty,try again"
    else:
        a = Answer(post=y,userA=x,answer=new_answer)
        a.save()
    context = {'posts': posts,'answers': answers,'users': users,'new_answer': new_answer,'error': error}
    return render(request, 'forum/posts.html', context)

def delete_odp(request, user_id,post_id,answer_id):
    users = User.objects.filter(id=user_id)
    posts = Post.objects.filter(id=post_id)
    answers = Answer.objects.filter(id=answer_id)
    answers.delete()
    answers = Answer.objects.filter(post=post_id)
    context = {'posts': posts,'answers': answers,'users': users}
    return render(request, 'forum/posts.html', context)

def odpM(request, user_id,post_id):
    users = User.objects.filter(id=user_id)
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(zadanie=post_id)
    error=""
    for user in users:
        x=user
    for post in postsM:
        y=post
    new_answer = request.POST['comment']
    if (new_answer==""):
        error="Empty,try again"
    else:
        a = AnswerM(zadanie=y,userA=x,answer=new_answer)
        a.save()
    context = {'postsM': postsM,'answersM': answersM,'users': users,'new_answer': new_answer,'error': error}
    return render(request, 'forum/postsM.html', context)

def delete_odpM(request, user_id,post_id,answer_id):
    users = User.objects.filter(id=user_id)
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(id=answer_id)
    answersM.delete()
    answersM = AnswerM.objects.filter(zadanie=post_id)
    context = {'postsM': postsM,'answersM': answersM,'users': users}
    return render(request, 'forum/postsM.html', context)