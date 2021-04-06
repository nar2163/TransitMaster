from flask import Flask

from flask import render_template
from flask import request, jsonify

import os, json

app = Flask(__name__)

trains = [
  {
    "id": 1,
    "train": "1",
    "img_link": "https://i.ibb.co/cT0qTB9/1-train.png",
    "info": "The 1 Train is the Broadway-7 Avenue local that runs uptown/downtown on the West Side of New York City.",
    "uptown": "Van Cortland Park/242nd",
    "downtown": "South Ferry"
  },
  {
    "id": 2,
    "train": "6",
    "img_link": "https://i.ibb.co/bRJTP7T/Screen-Shot-2021-04-02-at-10-45-20-PM.png",
    "info": "6 trains operate local at all times between Pelham Bay Park in the Bronx and Brooklyn Bridge–City Hall in Lower Manhattan.",
    "uptown": "Pelham Bay Park",
    "downtown": "Brooklyn Bridge - Chambers Street"
  },
  {
    "id": 3,
    "train": "A",
    "img_link": "https://i.ibb.co/4FvyQD1/A-train.png",
    "info": "The A train is the 8th Avenue express train that runs uptown to downtown on the west side of Manhttan.",
    "uptown": "Inwood 207th Street",
    "downtown": "Far Rockaway - Mott Avenue"
  },
  {
    "id": 4,
    "train": "L",
    "img_link": "https://i.ibb.co/FVwfhDJ/L-train.png",
    "info": "The L train runs East and West across 14th Street from 8th Avenue and into Brooklyn!",
    "uptown": "8th Avenue",
    "downtown": "Canarsie - Rockaway Beach"
  },
  {
    "id": 5,
    "train": "S",
    "img_link": "https://i.ibb.co/dBpV1Wt/S-train.png",
    "info": "The S Train is the shuttle train that connects Grand Central Terminal with Time Square!",
    "uptown": "42nd Street",
    "downtown": "42nd Street"
  },
]

easyQuiz = [
  {
    "id": 1,
    "question": "Let's go from Columbia University to Times Square!",
    "answer": [[1], [1, 6], [1, 7]]
  },
  {
    "id": 2,
    "question": "Let's go from 59th Street/Columbus Circle to Grand Central!",
    "answer": [[3, 5], [8, 5], [9, 5], [1, 5], [6, 5], [7, 5]]
  },
  {
    "id": 3,
    "question": "Let's go from the Met on 82nd and Fifth Avenue to Union Square!",
    "answer": [[2]]
  },
  {
    "id": 4,
    "question": "Let's go from 8th Avenue at 14th Street to Union Square!",
    "answer": [[4]]
  },
  {
    "id": 5,
    "question": "Let's go from Grand Central to Times Square!",
    "answer": [[5]]
  }
]

hardQuiz = [
  {
    "id": 1,
    "question": "Let's go from Union Square to Columbia University!",
    "answer": [[4, 1]]
  },
  {
    "id": 2,
    "question": "Let's go from West4th to Grand Central!",
    "answer": [[1, 5], [3, 5]]
  },
  {
    "id": 3,
    "question": "Let's go from Columbus Circle 59th Street to the Met on 85th and 5th Avenue!",
    "answer": [[1, 5, 2], [3, 5, 2]]
  },
  {
    "id": 4,
    "question": "Let's go from Union Square to the Cloisters (far upper west side)!",
    "answer": [[4, 3], [4, 1]]
  },
  {
    "id": 5,
    "question": "Let's go from the World Trade Center to Grand Central Station!",
    "answer": [[1, 5], [3, 5]]
  }
]

loadCommand = 0
indexLoad = 0
quizIndex = 0
quizScore = 0
quizChoice = 0
currentAnswer = []



@app.route('/')

def home():
    return render_template('home.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex)

@app.route('/learn/', methods=['GET', 'POST'])

def learn():
  return render_template('learn.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex)
 
@app.route('/quiz/', methods=['GET', 'POST'])

def quiz():
  
  tempQuiz = None

  if quizChoice == 1:
    tempQuiz = easyQuiz
  elif quizChoice == 2:
    tempQuiz = hardQuiz
  return render_template('quiz.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=tempQuiz, quizIndex=quizIndex)

@app.route('/update_quiz_choice', methods=['GET', 'POST'])

def update_quiz_choice():
  global quizChoice

  request_data = request.get_json()
  print(request_data)
  updated_choice = request_data['updated_choice']
  quizChoice = updated_choice

  print(quizChoice)

  return jsonify(data=quizChoice)

@app.route('/view/<int:index_id>', methods=['GET', 'POST'])

def view(index_id):
  return render_template('view.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex)

@app.route('/learn/save_index', methods=['GET', 'POST'])

def save_index():
  global indexLoad

  request_data = request.get_json()
  print(request_data)
  updated_index = request_data['updated_index']
  indexLoad = updated_index

  print(indexLoad)

  return jsonify(data=indexLoad)

@app.route('/quiz/update_answer', methods=['GET', 'POST'])

def update_answer():
    global quizIndex
    global currentAnswer

    request_data = request.get_json()
    print(request_data)
    updated_answer = request_data['updated_answer']
    
    print(updated_answer)

    currentAnswer = updated_answer

    return jsonify(data=currentAnswer)

@app.route('/correctness', methods=['GET'])

def correctness():
  global currentAnswer
  global quizIndex
  global quizChoice
  currQuiz = None

  if quizChoice == 1:
    currQuiz = easyQuiz
  elif quizChoice == 2:
    currQuiz = hardQuiz

  question = currQuiz[quizIndex]
  realAnswer = question['answer']
  currentAnswer.sort()
  correct = 0

  for curr in realAnswer:
    curr.sort() 
    print(curr) 
    if(curr == currentAnswer):
      correct = 1
      break

  return jsonify(data=correct)

@app.route('/quiz/save_quiz_index', methods=['GET', 'POST'])

def save_quiz_index():
  global quizIndex
  global quizScore

  request_data = request.get_json()
  print(request_data)

  quizIndex = request_data['updated_index'] + 1

  print(quizIndex)

  return jsonify(data=quizIndex)
  
  
@app.route('/get_quiz_index', methods=['GET'])

def get_quiz_index():
  global quizIndex
  return jsonify(data=quizIndex)

@app.route('/update_quiz_score', methods=['GET'])

def update_quiz_score():
  global quizScore
  quizScore += 1
  print(quizScore)
  return jsonify(data=quizScore)

@app.route('/get_quiz_score', methods=['GET'])

def get_quiz_score():
  global quizScore
  print(quizScore)
  return jsonify(data=quizScore)

@app.route('/results', methods=['GET', 'POST'])

def results():
  global quizScore
  global quizIndex
  tempScore = quizScore
  print("inside results page")
  quizScore = 0
  quizIndex = 0

  return render_template("results.html", trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex, quizScore=tempScore)
