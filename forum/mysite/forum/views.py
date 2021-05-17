from django.core.paginator import Paginator
from django.db.models import Max

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import User
from .models import Post
from .models import Answer
from .models import PostM
from .models import AnswerM
from .models import Zadanie_zamkniete
from .models import Zadanie_otwarte
from .models import zadanie_matematyczne
from .models import Score
from .models import Zrodlo
import random
from datetime import date, datetime
from django.core.files.storage import FileSystemStorage
import re
import json
from django.http.response import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from numpy.core.defchararray import upper
import time


#####################################################
#                                                   #
#   Funkcja sprawdzająca czy user jest zalogowany   #
#                                                   #
#####################################################
def is_user_authenticated(request):
    try:
        if request.session['logged_user'] == 0 or request.session['logged_user'] == "0" or not request.session['logged_user']:
            return False
        else:
            return True
    except KeyError:
        return False


#####################################################
#                                                   #
#      Funkcja zwracająca id zalogowanego usera     #
#                                                   #
#####################################################
def auth_user_id(request):
    if is_user_authenticated(request):
        return request.session['logged_user']
    else:
        return "User not authenticated"


#####################################################
#                                                   #
#   Funkcja zwracająca range zalogowanego usera     #
#                                                   #
#####################################################
def auth_user_rank(request):
    if is_user_authenticated(request):
        user = User.objects.filter(id=auth_user_id(request))[0]
        return user.ranga
    else:
        return 0


#####################################################
#                                                   #
#      Funkcja dodająca nowy post do zadania        #
#                                                   #
#####################################################
def addNewPost(NumberTask,nrWersji):
    taskAdded = zadanie_matematyczne.objects.get(nr_zadania=NumberTask,nr_wersji=nrWersji)
    newPost=PostM(zadanie=taskAdded,tresc=taskAdded.tresc)
    newPost.save()


#####################################################
#                                                   #
#      Funkcja zamieniajaca format dla mathjax      #
#                                                   #
#####################################################
def replace(text):
    newtext=text.replace('\ ',' ')
    newtext=newtext+" "
    newtext=newtext.replace(' \\',' $\\')
    newtext=newtext.replace('} ','}$ ')
    list=re.findall(r'\s[1-z]+[-^]', newtext)
    for i in list:
       newtext = newtext.replace(i,' $'+i[1:len(i)])
    count=newtext.count('$')
    if(count==1):
        newtext=newtext+"$"
    list2=re.findall(r'.*?\$(.*)$.*', newtext)
    # for j in list2:
    #    tmp=j
    # #    newSubString=tmp.replace(' ','\ ')
    #    newtext = newtext.replace(j,newSubString)
    return newtext

#####################################################
#                                                   #
#          Funkcja zwracająca aktualną datę         #
#                                                   #
#####################################################

def current_date():
    now = datetime.now() # current date and time
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time

#####################################################
#                                                   #
#          Funkcja do statystyk                     #
#                                                   #
#####################################################
def addStatistics(questionList,answerList,stats):
    count=0
    for question in questionList:
        if(upper(question['dzial'])=="GEOMETRIA"):
            stats['GEOMETRIA'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['GEOMETRIA'][1]+=1
        if(upper(question['dzial'])=="TRYGONOMETRIA"):
            stats['TRYGONOMETRIA'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['TRYGONOMETRIA'][1]+=1
        if(upper(question['dzial'])=="ALGEBRA"):
            stats['ALGEBRA'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['ALGEBRA'][1]+=1
        if(upper(question['dzial'])=="LOGARYTMY"):
            stats['LOGARYTMY'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['LOGARYTMY'][1]+=1
        if(upper(question['dzial'])=="POTEGOWANIE"):
            stats['POTEGOWANIE'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['POTEGOWANIE'][1]+=1
        if(upper(question['dzial'])=="PIERWIASTKOWANIE"):
            stats['PIERWIASTKOWANIE'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['PIERWIASTKOWANIE'][1]+=1
        if(upper(question['dzial'])=="FUNKCJE"):
            stats['FUNKCJE'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['FUNKCJE'][1]+=1        
        if(upper(question['dzial'])=="PRAWDOPODOBIENSTWO"):
            stats['PRAWDOPODOBIENSTWO'][0]+=1
            if(question['odpowiedz']==answerList[count]):
                stats['PRAWDOPODOBIENSTWO'][1]+=1      
        count+=1
    return stats

def index(request):
    users = User.objects.all()
    userNumber = User.objects.aggregate(Max('id'))
    questionNumber = zadanie_matematyczne.objects.aggregate(Max('id'))
    doneSet = Score.objects.aggregate(Max('id'))
    context = {'users': users,'numberUsers':userNumber['id__max'],'NumberQuestion':questionNumber['id__max'],'NumberDone':doneSet['id__max']}
    return render(request, 'forum/index.html', context)

def login(request):
    if is_user_authenticated(request):
        return redirect('usersHOME', user_id=auth_user_id(request))
    else:
        context = {'error': ''}

    return render(request, 'forum/login.html', context)


def login_user(request):
    if request.POST:
        try:
            user = User.objects.filter(name=request.POST['login'], password=request.POST['password'])[0]
        except IndexError:
            context = {'cont': "Hfdhshfd", 'error': "Błędne dane logowania"}
            return render(request, 'forum/login.html', context)
        request.session['logged_user'] = user.id
        return redirect('usersHOME', user_id=auth_user_id(request))
    else:
        return redirect('login')


def logout(request):
    request.session['logged_user'] = "0"
    return redirect('index')


def register1(request):
    if is_user_authenticated(request):
        return redirect('usersHOME', user_id=auth_user_id(request))
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'forum/register1.html', context)


def addQuestionView(request, user_id):
    if auth_user_rank(request) != 'admin' and auth_user_rank(request) != 'moderator':
        return render(request, 'forum/error.html', context={'error': 'Brak uprawnień'})
    users = User.objects.filter(id=user_id)

    context = {'users': users}
    
    return render(request, 'forum/addQuestionOpen.html', context)


def addQuestionViewClosedQuestion(request, user_id):
    if auth_user_rank(request) != 'admin' and auth_user_rank(request) != 'moderator':
        return render(request, 'forum/error.html', context={'error': 'Brak uprawnień'})
    users = User.objects.filter(id=user_id)
    context = {'users': users}
    return render(request, 'forum/addQuestionClose.html', context)


def addQuestionOpenToDatabase(request):
    if auth_user_rank(request) != 'admin' and auth_user_rank(request) != 'moderator':
        return render(request, 'forum/error.html', context={'error': 'Brak uprawnień'})
    NumberTask = request.POST['numberTask']
    section = request.POST['section']
    set = request.POST['set']
    NumberPoints = request.POST['NumberPoints']
    inputQuestion = request.POST['inputQuestion']
    inputAnswer = request.POST['inputAnswer']
    solution = request.POST['solution']
    inputQuestion=replace(inputQuestion)
    if 'image' in request.FILES:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = 'images/'+fs.url(filename)
    else:
        uploaded_file_url = ""
    version = zadanie_matematyczne.objects.filter(nr_zadania=NumberTask)
    ver=version.aggregate(Max('nr_wersji'))
    if version.exists():
        newVersion=ver['nr_wersji__max']+1
    else:
        newVersion=1
    
    newQuestion=zadanie_matematyczne(nr_zadania=NumberTask,nr_wersji=newVersion,rodzaj="otwarte",zestaw=set,tresc=inputQuestion,odp_a="",odp_b="",odp_c="",odp_d="",rozwiazanie=solution,odpowiedz=inputAnswer,dzial=section,punkty=NumberPoints,url=uploaded_file_url)
    newQuestion.save()

    addNewPost(NumberTask,newVersion)

    users = User.objects.filter(id=request.POST["user_id"])
    nameNew='{% url "addQuestionOpenToDatabase" %}'
    context = {'users': users}
    return render(request, 'forum/addQuestionOpen.html', context)

def addQuestionCloseToDatabase(request):
    if auth_user_rank(request) != 'admin' and auth_user_rank(request) != 'moderator':
        return render(request, 'forum/error.html', context={'error': 'Brak uprawnień'})
    NumberTask = request.POST['numberTask']
    section = request.POST['section']
    set = request.POST['set']
    NumberPoints = request.POST['NumberPoints']
    inputQuestion = request.POST['inputQuestion']
    inputAnswer = request.POST['inputAnswer']
    inputAnswerA = request.POST['inputAnswerA']
    inputAnswerB = request.POST['inputAnswerB']
    inputAnswerC = request.POST['inputAnswerC']
    inputAnswerD = request.POST['inputAnswerD']
    inputQuestion=replace(inputQuestion)
    if 'image' in request.FILES:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(fs.url(filename))
        uploaded_file_url = 'images/'+fs.url(filename)
    else:
        uploaded_file_url = ""
    version = zadanie_matematyczne.objects.filter(nr_zadania=NumberTask)
    ver=version.aggregate(Max('nr_wersji'))
    if version.exists():
        newVersion=ver['nr_wersji__max']+1
    else:
        newVersion=1
    

    newQuestion=zadanie_matematyczne(nr_zadania=NumberTask,nr_wersji=newVersion,rodzaj="zamkniete",zestaw=set,tresc=inputQuestion,odp_a=inputAnswerA,odp_b=inputAnswerB,odp_c=inputAnswerC,odp_d=inputAnswerD,rozwiazanie="",odpowiedz=inputAnswer,dzial=section,punkty=NumberPoints,url=uploaded_file_url)
    newQuestion.save()

    addNewPost(NumberTask,newVersion)

    users = User.objects.filter(id=request.POST["user_id"])
    nameNew='{% url "addQuestionOpenToDatabase" %}'
    context = {'users': users}
    return render(request, 'forum/addQuestionClose.html', context)

def register2(request):
    Name = request.POST['Name']
    Password = request.POST['Password']
    Email = request.POST['Email']
    SchoolName = request.POST['SchoolName']
    City = request.POST['City']
    ContactNumber = request.POST['ContactNumber']
    
    if (Name=="" or Password=="" or Email=="" or SchoolName=="" or City=="" or ContactNumber==""):
        msg="Empty,try again"
    else:
        if(User.objects.filter(name=Name).count()==0):
            u = User(name=Name,password=Password,ranga="user",numer_kontaktowy=ContactNumber,email=Email,miasto=City,szkola=SchoolName)
            u.save()
            msg="User added"
        else:
            msg="User with that name exists,try again"
    context = {'msg': msg}
    return render(request, 'forum/register2.html', context)

def usersHOME(request, user_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})

    users = User.objects.filter(id=auth_user_id(request))
    context = {'users': users, 'role': auth_user_rank(request)}
    return render(request, 'forum/usersHome.html', context)


def user_at_forum(request, user_id):
    users = User.objects.filter(id=auth_user_id(request))

    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1

    page_post_checked = page_number
    page_post_to_check = page_number

    postsToPaginate = Post.objects.all()
    postsPaginated = Paginator(postsToPaginate, 5)
    posts = postsPaginated.get_page(page_number)

    postsToChcekMToPaginate=PostM.objects.filter(stan="check")
    postsToChcekMPaginated = Paginator(postsToChcekMToPaginate, 5)

    if int(page_post_to_check) > postsToChcekMPaginated.num_pages:
        page_post_to_check = postsToChcekMPaginated.num_pages

    postsToChcekM = postsToChcekMPaginated.get_page(page_post_to_check)

    postsChechedToPaginate=PostM.objects.filter(stan="")
    postsChechedPaginated = Paginator(postsChechedToPaginate, 5)

    if int(page_post_checked) > postsChechedPaginated.num_pages:
        page_post_checked = postsChechedPaginated.num_pages

    postsCheched = postsChechedPaginated.get_page(page_post_checked)
    context = {'posts': posts,'users': users, 'postsToChcekM': postsToChcekM,'postsCheched': postsCheched, 'range': range(posts.paginator.num_pages)}
    return render(request, 'forum/userFORUM.html', context)


def math_page2(request, user_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))

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
   
    zos=zadanie_matematyczne.objects.filter(id=225)|zadanie_matematyczne.objects.filter(id=230)
    zzs=zadanie_matematyczne.objects.filter(id=201)|zadanie_matematyczne.objects.filter(id=181)|zadanie_matematyczne.objects.filter(id=180)
    
    context = {'users': users,'zos': zos,'zzs': zzs}
    return render(request, 'forum/MATH_PAGE2.html', context)

def math_page3(request, user_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))

    r=request.session.get('r')
    r2=request.session.get('r2')
    r3=request.session.get('r3')
    r4=request.session.get('r4')

    zos=zadanie_matematyczne.objects.filter(id=225)|zadanie_matematyczne.objects.filter(id=230)
    zzs=zadanie_matematyczne.objects.filter(id=201)|zadanie_matematyczne.objects.filter(id=181)|zadanie_matematyczne.objects.filter(id=180)

    #odpZ = request.POST.getlist('odpZ')
    odpZ=[]
    odpO = request.POST.getlist('odpO')

    linki = []
    
    punktyZ=0
    punktyO=0
    punktyMAX=0
    x=0

    dzisiaj = datetime.now()#pobieram dzisiejsza date
    data_wyslania_testu = dzisiaj.strftime("%Y-%m-%d %H:%M:%S")

    tasks_close=''
    odp_zamkniete=''

    tasks_open=''
    odp_otwarte=''
    

    for zz in zzs:
      posts= PostM.objects.filter(zadanie=zz.id)
      for post in posts:
        linki.append(post)
      punktyMAX=punktyMAX+1
      flexRadioDefaultNumber="flexRadioDefault"+str(x)
      my_answer = request.POST[flexRadioDefaultNumber]
      odpZ.append(my_answer)
      if zz.odpowiedz == my_answer:
        punktyZ=punktyZ+1
      tasks_close+=str(zz.id)+' '
      odp_zamkniete+=my_answer+ ' '
      x=x+1

    x=0

    for zo in zos:
      posts= PostM.objects.filter(zadanie=zo.id)
      for post in posts:
        linki.append(post)
      punktyMAX=punktyMAX+2
      if zo.odpowiedz == odpO[x]:
        punktyO=punktyO+2
      tasks_open+=str(zo.id)+' '
      odp_otwarte+=odpO[x]+ '\n'
      x=x+1  
      
    
    punkty=punktyZ+punktyO
      
    newScore=Score(id_user_id=user_id, data_testu=data_wyslania_testu, id_zad_otwartych=tasks_open, odp_otwarte=odp_otwarte,
    id_zad_zamknietych=tasks_close, odp_zamkniete=odp_zamkniete, punkty=punkty)
    newScore.save()
    context = {'users': users,'zos': zos,'zzs': zzs,'odpO': odpO,'odpZ': odpZ,'punktyMAX': punktyMAX,'punkty': punkty,'linki': linki}
    return render(request, 'forum/MATH_PAGE3.html', context)

def post(request, user_id,post_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    posts = Post.objects.filter(id=post_id)
    answers = Answer.objects.filter(post=post_id)
    context = {'posts': posts,'answers': answers,'users': users, 'role': auth_user_rank(request), 'auth_user_id': auth_user_id(request)}
    return render(request, 'forum/posts.html', context)

def postM(request, user_id,post_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(zadanie=post_id)
    context = {'postsM': postsM,'answersM': answersM,'users': users, 'role': auth_user_rank(request), 'auth_user_id': auth_user_id(request)}
    return render(request, 'forum/postsM.html', context)

def add(request, user_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    temat = request.POST['temat']
    tresc = request.POST['tresc']
    tresc = replace(tresc)
    for user in users:
        w=user
    error=""
    if (temat=="" or tresc==""):
        error="Empty,try again"
    else:
        q = Post(userP=w,subject=temat,text=tresc,date=current_date())
        q.save()
        error="Post added"

    context = {'users': users,'temat': temat,'tresc': tresc,'error': error}
    return render(request, 'forum/add.html', context)

def delete(request, user_id,post_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    posts = Post.objects.filter(id=post_id)
    posts.delete()
    context = {'users': users}
    return render(request, 'forum/delete.html', context)

def odp(request, user_id,post_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
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
        new_answer=replace(new_answer)
        a = Answer(post=y,userA=x,answer=new_answer,date=current_date())
        a.save()
        return redirect('post', user_id=auth_user_id(request), post_id=post_id)
    context = {'posts': posts, 'answers': answers, 'users': users,  'new_answer': new_answer, 'error': error}
    return render(request, 'forum/posts.html', context)

def delete_odp(request, user_id,post_id,answer_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    posts = Post.objects.filter(id=post_id)
    answers = Answer.objects.filter(id=answer_id)
    answers.delete()
    answers = Answer.objects.filter(post=post_id)
    return redirect('post', user_id=auth_user_id(request), post_id=post_id)

def odpM(request, user_id,post_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(zadanie=post_id)
    error=""
    for user in users:
        x=user
    for post in postsM:
        y=post
        y.stan="check"
        y.save()
    new_answer = request.POST['comment']
    if (new_answer==""):
        error="Empty,try again"
    else:
        a = AnswerM(zadanie=y,userA=x,answer=new_answer,date=current_date())
        a.save()
        return redirect('postM', user_id=auth_user_id(request), post_id=post_id)
    context = {'postsM': postsM,'answersM': answersM,'users': users,'new_answer': new_answer,'error': error}
    return render(request, 'forum/postsM.html', context)

def delete_odpM(request, user_id,post_id,answer_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(id=answer_id)
    answersM.delete()
    answersM = AnswerM.objects.filter(zadanie=post_id)
    return redirect('postM', user_id=auth_user_id(request), post_id=post_id)

def userPanel(request, user_id):
    users = User.objects.filter(id=user_id)
    context = {'users': users}
    return render(request, 'forum/userPanel.html', context)
     
def score(request, user_id):
    start_time = time.monotonic()
    users = User.objects.filter(id=user_id)
    score = Score.objects.filter(id_user_id=user_id)
    openQuestion=[]
    closeQuestion=[]
    listOfOpenQuestionIds=[]
    listOfCloseQuestionIds=[]
    listOfCloseQuestionAnswer=[]
    listOfOpenQuestionAnswer=[]
    sumOfTask=0
    sumOfCorrectTask=0
    stats={
        "GEOMETRIA":[0,0],
        "TRYGONOMETRIA":[0,0],
        "ALGEBRA":[0,0],
        "LOGARYTMY":[0,0],
        "POTEGOWANIE":[0,0],
        "PIERWIASTKOWANIE":[0,0],
        "FUNKCJE":[0,0],
        "PRAWDOPODOBIENSTWO":[0,0],
    }

    resultStats={
        "GEOMETRIA":'0',
        "TRYGONOMETRIA":'0',
        "ALGEBRA":'0',
        "LOGARYTMY":'0',
        "POTEGOWANIE":'0',
        "PIERWIASTKOWANIE":'0',
        "FUNKCJE":'0',
        "PRAWDOPODOBIENSTWO":'0',
        "ZDOBYTE":'0',
    }
    for question in score:
        for id in list(question.id_zad_otwartych.split(" "))[:-1]:
            listOfOpenQuestionIds.append(id)
        for id in list(question.id_zad_zamknietych.split(" "))[:-1]:
            listOfCloseQuestionIds.append(id)
        for id in list(question.odp_zamkniete.split(" "))[:-1]:
            listOfCloseQuestionAnswer.append(id)
        for id in list(question.odp_otwarte.split("\n"))[:-1]:
            listOfOpenQuestionAnswer.append(id)
    for openQuestionId in listOfOpenQuestionIds:
        openQuestion.append(zadanie_matematyczne.objects.values('dzial','odpowiedz').get(id=openQuestionId))
    for closeQuestionId in listOfCloseQuestionIds:
        closeQuestion.append(zadanie_matematyczne.objects.values('dzial','odpowiedz').get(id=closeQuestionId))
    stats=addStatistics(openQuestion,listOfOpenQuestionAnswer,stats)
    stats=addStatistics(closeQuestion,listOfCloseQuestionAnswer,stats)

    sumOfTask=sum(stats[dzial][0] for dzial in stats)
    sumOfCorrectTask=sum(stats[dzial][1] for dzial in stats)

    resultStats['GEOMETRIA'] = ( round((stats['GEOMETRIA'][1] / stats['GEOMETRIA'][0])*100)) if stats['GEOMETRIA'][1] != 0 else 0
    resultStats['TRYGONOMETRIA'] = ( round((stats['TRYGONOMETRIA'][1] / stats['TRYGONOMETRIA'][0])*100 )) if stats['TRYGONOMETRIA'][1] != 0 else 0
    resultStats['ALGEBRA'] = ( round((stats['ALGEBRA'][1] / stats['ALGEBRA'][0])*100 )) if stats['ALGEBRA'][1] != 0 else 0
    resultStats['LOGARYTMY'] = ( round((stats['LOGARYTMY'][1] / stats['LOGARYTMY'][0])*100) ) if stats['LOGARYTMY'][1] != 0 else 0
    resultStats['POTEGOWANIE'] = ( round((stats['POTEGOWANIE'][1] / stats['POTEGOWANIE'][0])*100) ) if stats['POTEGOWANIE'][1] != 0 else 0
    resultStats['PIERWIASTKOWANIE'] = round(( (stats['PIERWIASTKOWANIE'][1] / stats['PIERWIASTKOWANIE'][0])*100 )) if stats['PIERWIASTKOWANIE'][1] != 0 else 0
    resultStats['POTEGOWANIE'] = ( round((stats['POTEGOWANIE'][1] / stats['POTEGOWANIE'][0])*100 )) if stats['POTEGOWANIE'][1] != 0 else 0
    resultStats['FUNKCJE'] = ( round((stats['FUNKCJE'][1] / stats['FUNKCJE'][0])*100 )) if stats['FUNKCJE'][1] != 0 else 0
    resultStats['PRAWDOPODOBIENSTWO'] = ( round((stats['PRAWDOPODOBIENSTWO'][1] / stats['PRAWDOPODOBIENSTWO'][0])*100 )) if stats['PRAWDOPODOBIENSTWO'][1] != 0 else 0
    resultStats['ZDOBYTE'] = ( round((sumOfCorrectTask / sumOfTask)*100 )) if sumOfCorrectTask != 0 else 0
    print('seconds: ', time.monotonic() - start_time)
    context = {'users':users, 'score':score,'Stats':resultStats}
    return render(request, 'forum/userScore.html',context)
  
def scoreDetails(request, user_id):
    users = User.objects.filter(id=user_id)
    score = Score.objects.filter(id=user_id)
    nzO=[]
    nzZ=[]
    oZZ=[]
    oOO=[]
    pytZ=[]
    pytO=[]
    odpZZ=[]
    for s in score:
        nzO = list(s.id_zad_otwartych.split(" "))
        nzZ = list(s.id_zad_zamknietych.split(" "))
        oZ = list(s.odp_zamkniete.split(" "))
        oO = list(s.odp_otwarte.split("\n"))
        
        
        for nr in nzZ[:-1]:
            x=str(zadanie_matematyczne.objects.filter(id=nr).values('tresc'))[22:-4]
            x=x.replace('\\\\',' \\')
            pytZ.append(x)
        for nr in nzO[:-1]:
            x=str(zadanie_matematyczne.objects.filter(id=nr).values('tresc'))[22:-4]
            x=x.replace('\\\\',' \\')
            pytO.append(x)
        for o in oZ[:-1]:
            oZZ.append(o)
        for o in oO[:-1]:
            oOO.append(o)

        for r in nzZ[:-1]:
            odpA=str(zadanie_matematyczne.objects.filter(id=r).values('odp_a'))[22:-4]
            odpB=str(zadanie_matematyczne.objects.filter(id=r).values('odp_b'))[22:-4]
            odpC=str(zadanie_matematyczne.objects.filter(id=r).values('odp_c'))[22:-4]
            odpD=str(zadanie_matematyczne.objects.filter(id=r).values('odp_d'))[22:-4]
            temp="A) "+odpA +"B) "+odpB +"C) "+odpC+"D) "+odpD
            temp=temp.replace('\\\\',' \\')
            odpZZ.append(temp)

    pytaniaZamkniete=zip(pytZ,odpZZ,oZZ)
    pytaniaOtwarte=zip(pytO,oOO)
    context = {'pytaniaZamkniete':pytaniaZamkniete, 'pytaniaOtwarte':pytaniaOtwarte}
    return render(request, 'forum/userScoreDetails.html',context)

def check(request, user_id,post_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    postsM = PostM.objects.filter(id=post_id)
    answersM = AnswerM.objects.filter(zadanie=post_id)
    for post in postsM:
        y=post
        y.stan=""
        y.save()
    context = {'postsM': postsM,'answersM': answersM,'users': users}
    return render(request, 'forum/postsM.html', context)

def history(request, user_id):
    score = Score.objects.filter(id_user_id=user_id)
    posts = Post.objects.filter(userP_id=user_id)
    answer = Answer.objects.filter(userA_id=user_id)
    answerM = AnswerM.objects.filter(userA_id=user_id)
    postsM= PostM.objects.all()
    
    nzO=[]
    nzZ=[]
    oZZ=[]
    oOO=[]
    pytZ=[]
    pytO=[]
    odpZZ=[]
    pytObrazkiZ=[]
    pytObrazkiO=[]
    for s in score:
        nzO = list(s.id_zad_otwartych.split(" "))
        nzZ = list(s.id_zad_zamknietych.split(" "))
        oZ = list(s.odp_zamkniete.split(" "))
        oO = list(s.odp_otwarte.split("\n"))
        
        
        for nr in nzZ[:-1]:
            x=str(zadanie_matematyczne.objects.filter(id=nr).values('tresc'))[22:-4]
            x=x.replace('\\\\',' \\')
            pytZ.append(x)
        for nr in nzO[:-1]:
            x=str(zadanie_matematyczne.objects.filter(id=nr).values('tresc'))[22:-4]
            x=x.replace('\\\\',' \\')
            pytO.append(x)
            pytObrazkiO.append(str(zadanie_matematyczne.objects.filter(id=nr).values('url'))[20:-4])
        for o in oZ[:-1]:
            oZZ.append(o)
        for o in oO[:-1]:
            oOO.append(o)

        for r in nzZ[:-1]:
            odpA=str(zadanie_matematyczne.objects.filter(id=r).values('odp_a'))[22:-4]
            odpB=str(zadanie_matematyczne.objects.filter(id=r).values('odp_b'))[22:-4]
            odpC=str(zadanie_matematyczne.objects.filter(id=r).values('odp_c'))[22:-4]
            odpD=str(zadanie_matematyczne.objects.filter(id=r).values('odp_d'))[22:-4]
            temp="A) "+odpA +"B) "+odpB +"C) "+odpC+"D) "+odpD
            temp=temp.replace('\\\\',' \\')
            odpZZ.append(temp)
            pytObrazkiZ.append(str(zadanie_matematyczne.objects.filter(id=r).values('url'))[20:-4])

    pytaniaZamkniete=zip(pytZ,odpZZ,oZZ,pytObrazkiZ)
    pytaniaOtwarte=zip(pytO,oOO,pytObrazkiO)
    context = {'pytaniaZamkniete':pytaniaZamkniete, 'pytaniaOtwarte':pytaniaOtwarte,'posts':posts,'answer':answer,'answerM':answerM,'postsM': postsM}
    return render(request, 'forum/history.html', context)

def oneTaskGenerate(request, user_id):
    users = User.objects.filter(id=user_id)
    context = {'users': users}
    return render(request, 'forum/oneTaskSettings.html', context)

def oneTaskGenerateSendSettings(request, user_id):
    questionType = request.POST['questionType']
    questionSection= request.POST['questionSection']
    question = list(zadanie_matematyczne.objects.filter(rodzaj=questionType, dzial=questionSection))
    random_item = random.choice(question)
    users = User.objects.filter(id=user_id)
    context = {'users': users,'singleQuestion':random_item}
    return render(request, 'forum/oneTaskShow.html', context)
def oneTaskCheckAnswer(request, user_id):
    sendAnswer=request.POST.get("answer","")
    questionId=request.POST.get("questionId","")
    question = zadanie_matematyczne.objects.filter(id=questionId)
    response_data={}
    print(question.values('odpowiedz')[0]['odpowiedz'])
    try:
        response_data['result']=question.values('odpowiedz')[0]['odpowiedz']
        if(question.values('odpowiedz')[0]['odpowiedz']==sendAnswer):
            response_data['message']='<div class="alert alert-success" role="alert"><h3>Twoja odpowiedź jest poprawna!</h3><a class="close">&times;</a></div>'
        else:
            response_data['message']='<div class="alert alert-danger" role="alert"><h3>Twoja odpowiedź nie jest prawidłowa!</h3><a class="close">&times;</a></div>'
    except:
        response_data['result']='Lipa'
        response_data['message']='cos poszlo nie tak'
    return JsonResponse(response_data)
