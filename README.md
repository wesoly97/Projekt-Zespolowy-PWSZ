# CYRKIELEK
> Cyrkielek is a portal designed for secondary school students to help them prepare for their matriculation exams. Students can solve the final exam worksheets, draw individual exam questions and check their progress in the statistics section. The site distinguishes between user roles (admin and normal user)
## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Contact](#contact)
## General info
This project was done in agroup of nine, in an agile methodology.
We were divided into two groups which were responsible for the frontend and backend, I belonged to the backend group.
We divided all tasks into weekly sprints. 
During the project we used tools such as github, MongoDb Atlas and jira. My tasks included:
- Creating a module for adding open and closed questions for a user with administrator rights (database CRUD).
- Calculation and sending to the home page of statistics such as: number of active users, number of worksheets solved, number of matriculation questions.
- Create a function that calculates the percentage statistics of the mathematical sections mastered. It is updated after each solved worksheet. The data is then downloaded and displayed in the user statistics tab. 
- Creation of a single matriculation task draw module. The user can select the mathematics department and the type of question (open/closed).
- Use of the mathquill framework for entering mathematical symbols.
- Uploading images needed for tasks and displaying them later.
## Screenshots
view of main page:
![Example screenshot](./imagesOfCyrkielek/index.PNG)
![Example screenshot](./imagesOfCyrkielek/index2.PNG)
Login form:
![Example screenshot](./imagesOfCyrkielek/loginForm.PNG)
Register Form:
![Example screenshot](./imagesOfCyrkielek/registerForm.PNG)
User panel for user with admin privileges:
![Example screenshot](./imagesOfCyrkielek/userPanelAdmin.PNG)
User panel for user without admin privileges:
![Example screenshot](./imagesOfCyrkielek/userPanelUser.PNG)
Add open question module:
![Example screenshot](./imagesOfCyrkielek/openQuestionModule.PNG)
Add close question module:
![Example screenshot](./imagesOfCyrkielek/closeQuestionModule.PNG)
User stats module:
![Example screenshot](./imagesOfCyrkielek/userStats.PNG)
Single question draw settings view:
![Example screenshot](./imagesOfCyrkielek/oneQuestionSettings.PNG)
Open question drawn:
![Example screenshot](./imagesOfCyrkielek/oneQuestionDrawn.PNG)
Close question drawn:
![Example screenshot](./imagesOfCyrkielek/oneCloseQuestionDrawn.PNG)
the set of questions drawn up:
![Example screenshot](./imagesOfCyrkielek/setDrawn.PNG)
![Example screenshot](./imagesOfCyrkielek/setDrawn2.PNG)
View after examination:
![Example screenshot](./imagesOfCyrkielek/setAfterCheck.PNG)
Forum:
![Example screenshot](./imagesOfCyrkielek/forum.PNG)
## Technologies
* Django - version 3.2.6
* Jquery - version 3.6.0
* Bootstrap - version 4.6.0
* Katex - version 0.10.1
* Mathquill - version 8.0
* Virtual Keyboard - version 1.30.3
* mongoDB - version 5.0
* djongo - version 1.3.6
* dnspython - version 2.1.0
## Setup
Before you run the server please use these commands:

```

$ cd forum/mysite/
$ python -m django --version
$ pip install djongo
$ pip install dnspython
$ python manage.py makemigrations
$ python manage.py migrate

```

To run this project, first run the server:
```

$ cd forum/mysite/
$ py manage.py runserver

```
## Status
Project is: _no longer continue_ 
## Contact
>Created by [Piotr Brac](https://github.com/Krokus-lab),[Mikołaj Wesołek](https://github.com/wesoly97), [Adrian Kleyna](https://github.com/adriankleyna), [Damian Jancewicz](https://github.com/dilejt),[Hubert Drzymalski](https://github.com/HubertDrzymalski),[Szymon Doerfer](https://github.com/Saymon1998), [Łukasz Szymański](https://github.com/szyman-9), [Łukasz Sinica](https://github.com/LukaszSinica),[Kacper Pańkiewicz](https://github.com/kacperPankiewicz)- feel free to contact us!
