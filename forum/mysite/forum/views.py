from django.db.models import Max
from django.http import HttpResponse,HttpResponseRedirect

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
import random
from datetime import date, datetime
from django.core.files.storage import FileSystemStorage
import re





#####################################################
#                                                   #
#   Funkcja sprawdzająca czy user jest zalogowany   #
#                                                   #
#####################################################
def is_user_authenticated(request):
    try:
        if request.session['logged_user'] == 0 or request.session['logged_user'] == "0":
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
    for j in list2:
       tmp=j
       newSubString=tmp.replace(' ','\ ')
       newtext = newtext.replace(j,newSubString)
    return newtext


def index(request):
    users = User.objects.all()
    context = {'users': users}
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
    if (Name=="" or Password=="" ):
        msg="Empty,try again"
    else:
        if(User.objects.filter(name=Name).count()==0):
            u = User(name=Name,password=Password,ranga="user")
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
    posts = Post.objects.all()
    postsM= PostM.objects.all()
    postsToChcekM=PostM.objects.filter(stan="check")
    postsCheched=PostM.objects.filter(stan="")
    context = {'posts': posts,'users': users,'postsM': postsM,'postsToChcekM': postsToChcekM,'postsCheched': postsCheched}
    return render(request, 'forum/userFORUM.html', context)

def math_page(request, user_id):
    if not is_user_authenticated(request):
        return render(request, 'forum/error.html', context={'error': 'Nie jesteś zalogowany'})
    users = User.objects.filter(id=auth_user_id(request))
    context = {'users': users}
    return render(request, 'forum/MATH_PAGE.html', context)

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

    odpZ = request.POST.getlist('odpZ')
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
      if zz.odpowiedz == odpZ[x]:
        punktyZ=punktyZ+1
      tasks_close+=str(zz.id)+' '
      odp_zamkniete+=odpZ[x]+ ' '
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
        a = Answer(post=y,userA=x,answer=new_answer)
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
        a = AnswerM(zadanie=y,userA=x,answer=new_answer)
        a.save()
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
    context = {'postsM': postsM,'answersM': answersM,'users': users}
    return render(request, 'forum/postsM.html', context)

def userPanel(request, user_id):
    users = User.objects.filter(id=user_id)
    context = {'users': users}
    return render(request, 'forum/userPanel.html', context)
     
def score(request, user_id):
    users = User.objects.filter(id=user_id)
    score = Score.objects.filter(id_user_id=user_id)
    context = {'users':users, 'score':score}
    return render(request, 'forum/userScore.html',context)
  
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
    context = {'pytaniaZamkniete':pytaniaZamkniete, 'pytaniaOtwarte':pytaniaOtwarte,'posts':posts,'answer':answer,'answerM':answerM}
    return render(request, 'forum/history.html', context)
