from flask_pymongo import PyMongo
from flask import Flask
from flask.json import jsonify
from flask.templating import render_template
from bson.objectid import ObjectId
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['MONGO_URI']='mongodb+srv://user:lol990@cluster0.nvy9l.mongodb.net/DataBase?retryWrites=true&w=majority'
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/add_set")
def add_one():
    db.todos23.insert_one({ 
        "_id":1,
  "zestaw":{ 
        "pytanie1":{
    "tresc": "Wartość\:wyrażenia \:x^2-5x + 90:dla \:x= ZMIENNA1\:" ,
    "warianty": ["1-2\sqrt{3}", "3", "1+2\sqrt{3}", "1-2\sqrt{3}"], 
    "odpowiedzi": ["3", "1", "1+2 sqrt{3}", "1-2 sqrt{3}"], 
    "poziom trudności":1
  },
  "pytanie2": {
    "tresc": "Liczba\:ZMIENNA1\:jest\:równa" ,
    "warianty": ["\\frac{2^{25}*3^{40}}{30^{10}}", "\\frac{2^{60}*3^{40}}{36^{10}}", "\\frac{2^{50}*3^{60}}{36^{12}}", "\\frac{2^{50}*3^{40}}{36^{10}}"], 
    "odpowiedzi": ["2^{30} * 3^{20}", "6^{45}", "6^{70}", "2^{10} * 3^{20}"], 
    "poziom trudności":1
  },
  "pytanie3": {
    "tresc": "Liczba\:\\log_5(ZMIENNA1)\:jest\:równa" ,
    "warianty": ["\sqrt{100}", "\sqrt{150}", "\sqrt{80}", "\sqrt{140}"], 
    "odpowiedzi": ["\\frac{3}{2}", "2", "3", "\\frac{2}{3}"], 
    "poziom trudności":1
  },
  "pytanie4": {
    "tresc": "Cenę\:x\:pewnego\:towaru\:obniżono\:o\:ZMIENNA1\:i\:otrzymano\:cenę\:y.\:Aby\:przywrócić\:cenę\:x,\:nową\:cenę\:y\:należy\:podnieść\:o:" ,
    "warianty": ["20\%", "30\%", "10\%", "40\%"], 
    "odpowiedzi": ["25\%", "20\%", "15\%", "12\%"], 
    "poziom trudności":1
  },
  "pytanie5": {
    "tresc": "Zbiorem\:wszystkich\:rozwiązań\:nierówności\:3(ZMIENNA1)\:>\:2(3x-1)\:-\:12x\:jest\:przedział:" ,
    "warianty": ["1-x", "3-x", "x-1", "x-3"], 
    "odpowiedzi": ["(\\frac{-5}{3}, +nieskonczoność)", "(-nieskonczonosc, \\frac{5}{3})", "(\\frac{5}{3}, +nieskonoczonsc)", "(-nieskonczonosc, \\frac{-5}{3})"], 
    "poziom trudności":1
  },

  "pytanie6": {
    "tresc": "Suma\:wszystkich\:rozwiązań\:równania\:x(ZMIENNA1)(x+2)\:=\:0\:jest\:równa" ,
    "warianty": ["x-3", "3-x", "x-4", "x-5"], 
    "odpowiedzi": ["1", "0", "2", "3"], 
    "poziom trudności":1
  },

  "pytanie7": {
    "tresc": "Równanie\:x(ZMIENNA1)\:=\:(ZMIENNA1)^2\:w\:zbiorze\:liczb\:rzeczywistych" ,
    "warianty": ["x-2", "x-3", "x-4"], 
    "odpowiedzi": ["ma\:dokładnie\:jedno\:rozwiazanie:\:x =\:2", "nie\:ma\:rozwiązań", "ma\:dokładnie\:jedno\:rozwiązanie:\:x\:=\:0", "ma\:dokładnie\:dwa\:różne\:rozwiązania:\:x\:=\:1\:i\:x\:=\:2"], 
    "poziom trudności":1
  },

    "pytanie8": {
      "tresc": "Wartość\:wyrażenia \:x^2-10x\:+\:90:dla\:x=ZMIENNA1\:",
      "warianty": ["1-2\sqrt{3}", "3", "1+2\sqrt{3}", "1-2\sqrt{3}"],
      "odpowiedzi": ["1", "3", "1+2\sqrt{3}", "1-2\sqrt{3}"],
      "poziom trudności": 1
    },

    "pytanie9": {
      "tresc": "Funkcja\:f\:jest\:określona\:wzorem\:f(x)\:=\:ZMIENNA1\:+\:1\:dla\:każdej\:liczby\:rzeczywistej\:x.\:Liczba\:f(\\frac{1}{2})\:jest\:równa",
      "warianty": ["4^-x", "2^-x", "4^x", "2^x"],
      "odpowiedzi": ["\\frac{3}{2}", "\\frac{1}{2}", "3", "17"],
      "poziom trudności": 1
    },

    "pytanie10": {
      "tresc": "Proste\:o\:równaniach\:y\:=\:(m\:-\:2)x\:oraz\:y=\:\\frac{3}{4}x\:+\:7\:są\:równoległe.\:Wtedy",
      "warianty": ["m\:-\:2", "m\:-\:3", "m\:-\:4", "m\:-\:5"],
      "odpowiedzi": ["m=\\frac{11}{4}", "m=-\\frac{5}{4})", "m=\\frac{2}{3}", "m=\frac{10}{3}"],
      "poziom trudności": 1
    },

    "pytanie11": {
      "tresc": "Cenę\:x\:pewnego\:towaru\:obniżono\:o\:ZMIENNA1\:i\:otrzymano\:cenę\:y. \:Aby\:przywrócić\:cenę\:x,\:nową\:cenę\:y\:należy\:podnieść\:o",
      "warianty": ["20\%", "30\%", "10\%", "40\%"],
      "odpowiedzi": ["25\%", "20\%", "15\%", "12\%"],
      "poziom trudności": 1
    },

    "pytanie12": {
      "tresc": "Ciąg\:(a_{n}\:jest\:określony\:wzorem\:a_{n}\:=\:ZMIENNA1.\:Różnica\:a_{5}-a_{4}\:jest\:równa",
      "warianty": ["2n^{2}", "2n^{2}", "2n^{2}", "2n^{2}"],
      "odpowiedzi": ["18", "4", "20", "36"],
      "poziom trudności": 1
    },

    "pytanie13": {
      "tresc": "W\:ciągu\:arytmetycznym\:(a_{n}),\:określonym\:dla\:n\:>=\:1.\:czwarty\:wyraz\:jest\:równy\:3,\:a\:różnica\:tego\:ciągu\:jest\:równa\:5.\:Suma\: a_{1}\:+\:a_{2}\:+\:a_{3}\:+\:a_{4}\:jest\:równa",
      "warianty": ["", "", "", ""],
      "odpowiedzi": ["-18", "-42", "-36", "6"],
      "poziom trudności": 1
    },

    "pytanie14": {
      "tresc": "Punkt\:A\:=\:(\\frac{1}{3},-1)\:należy\:do\:wykresu\:funkcji\:liniowej\:f\:określonej\:wzorem\:f(x)\:=\:3x\:+\:b.\:Wynika\:stąd,\:że",
      "warianty": ["", "", ""],
      "odpowiedzi": ["-2", "2", "1", "-1"],
      "poziom trudności": 1
    },

    "pytanie15": {
      "tresc": "Prosta\:przechodząca\:przez\:punkty\:A\:=\:(3,-2)\:i\:B\:=\:(-1,6)\:jest\:określona\:równaniem",
      "warianty": ["", "", ""],
      "odpowiedzi": ["y=−2x+4", "y=−2x−8", "y=2x+8", "y=2x−4"],
      "poziom trudności": 1
    },
  "pytanie16":{
    "tresc": "Przekątna\:sześcianu\:ma\:długośc:ZMIENNA1\:.\:Pole\:powierzchni\:tego\:sześcianu\:jest\:równe: " ,
    "warianty": ["4\sqrt{3}", "3", "1+2\sqrt{3}", "1-2\sqrt{3}"], 
    "odpowiedzi": ["96", "24\sqrt{3}", "192", "16\sqrt{3}"], 
    "poziom trudności":1
  },  
  "pytanie17":{
    "tresc": "Cztery\:liczby\:2,\:3,\:a,\:8\:tworzące\:zestaw\:danych,\:są\:uporządkowane\:rosnąco.\:Mediana\:tego\:zestawu\:czterech\:danych\:jest\:równa\:medianie\:zestawu\:pięciu\:danych\:ZMIENNA1.\:Zatem: ",
    "warianty": ["5,3,6,8,2", "3", "1+2\sqrt{3}", "1-2\sqrt{3}"], 
    "odpowiedzi": ["a=7", "a=6", "a=5", "a=4"], 
    "poziom trudności":1
  },"pytanie18":{
    "tresc": "Ile\:jest\:wszystkich\:dwucyfrowych\:liczb\:naturalnych\:utworzonych\:z\:cyfr:ZMIENNA1",
    "warianty": ["1,3,5,7,9", "1,2,5,7,9", "1,4,5,7,9", "1,5,5,7,9"], 
    "odpowiedzi": ["20", "25", "15", "10"], 
    "poziom trudności":1
  },
  "pytanie19":{
    "tresc": "Punkt B\:jest\:obrazem\:punktu\:A=(ZMIENNA1)\:w\:symetrii\:względem\:początku\:układu\:współrzędnych.\:Długość\:odcinka\:AB\:jest\:równa:",
    "warianty": ["−3,5", "3,5", "1+2\sqrt{3},5", "1-2\sqrt{3},5"], 
    "odpowiedzi": ["2\sqrt{34}", "\sqrt{34}", "8", "12"], 
    "poziom trudności":1
  },},
  })
    return jsonify(message="success")
@app.route("/add_many")
def add_many():
    db.todosTest.insert_many([
        {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
        ])
    return jsonify(message="success")
@app.route("/index")
def index():
    set = db.todos23.find({"_id":1})
    return render_template('index.html',sets=set)
@app.route("/index2")
def index2():
    set = db.todos23.find({"_id":1})
    sets=[]
    for doc in set:
      sets.append({
      'zestaw':(doc['zestaw'])
      })
    return jsonify(sets)
@app.route("/")
def home2():
    set = db.todosTest.find()
    
if __name__ == "__main__":
    app.run(debug=True)    
