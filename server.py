from flask import Flask

from flask import render_template
from flask import request, jsonify

import os, json

app = Flask(__name__)

trains = [
  {
    "id": 1,
    "train": "1",
    "img_link": "https://i.ibb.co/2kjjjr1/1-train.png",
    "route_img": "https://i.ibb.co/b5kHLMC/123-train-route.png",
    "info": "The 1 Train is the Broadway-7 Avenue local that runs uptown/downtown on the West Side of New York City.",
    "uptown": "Van Cortland Park/242nd",
    "downtown": "South Ferry",
    "hot_spots": [[940, 60], [890, 320], [900, 415], [925, 560], [960, 605], [980, 740], [1060, 960]],
    "hot_spot_id": ["Van Courtland Park", "Columbia University", "96th Street", "Columbus Circle", "Times Square", "Christopher Street", "South Ferry"],
    "hot_spot_img": {"Van Courtland Park" : "https://i.ibb.co/VB3CgmG/OLYMPUS-DIGITAL-CAMERA.jpg", "Columbia University" : "https://i.ibb.co/b11FPF3/columbia.png", "96th Street" : "https://i.ibb.co/Lgf7kd0/96th.jpg", "Columbus Circle" : "https://i.ibb.co/QdfLmx4/Columbus-Circle.jpg", "Times Square" : "https://i.ibb.co/8D9hDF0/Times-Square.jpg", "Christopher Street" : "https://i.ibb.co/6H9Vz5L/west4.jpg", "South Ferry" : "https://i.ibb.co/vBXSpz5/southferry.jpg"}
  },
  {
    "id": 2,
    "train": "2",
    "img_link": "https://i.ibb.co/hYrfBXN/2-train.png",
    "route_img": "https://i.ibb.co/b5kHLMC/123-train-route.png",
    "info": "The 2 Train is the Broadway-7 Avenue express that runs uptown/downtown on the West Side of New York City.",
    "uptown": "Wakefield - 241 Street",
    "downtown": "New Lots Avenue",
    "hot_spots": [[940, 60], [890, 320], [900, 415], [925, 560], [960, 605], [980, 740], [1060, 960]],
    "hot_spot_id": ["Van Courtland Park", "Columbia University", "96th Street", "Columbus Circle", "Times Square", "Christopher Street", "South Ferry"],
    "hot_spot_img": {"Van Courtland Park" : "https://i.ibb.co/VB3CgmG/OLYMPUS-DIGITAL-CAMERA.jpg", "Columbia University" : "https://i.ibb.co/b11FPF3/columbia.png", "96th Street" : "https://i.ibb.co/Lgf7kd0/96th.jpg", "Columbus Circle" : "https://i.ibb.co/QdfLmx4/Columbus-Circle.jpg", "Times Square" : "https://i.ibb.co/8D9hDF0/Times-Square.jpg", "Christopher Street" : "https://i.ibb.co/6H9Vz5L/west4.jpg", "South Ferry" : "https://i.ibb.co/vBXSpz5/southferry.jpg"}
  },
  {
    "id": 3,
    "train": "3",
    "img_link": "https://i.ibb.co/cDbSD9g/3-train.png",
    "route_img": "https://i.ibb.co/b5kHLMC/123-train-route.png",
    "info": "The 1 Train is the Broadway-7 Avenue local that runs uptown/downtown on the West Side of New York City.",
    "uptown": "Van Cortland Park/242nd",
    "downtown": "South Ferry",
    "hot_spots": [[940, 60], [890, 320], [900, 415], [925, 560], [960, 605], [980, 740], [1060, 960]],
    "hot_spot_id": ["Van Courtland Park", "Columbia University", "96th Street", "Columbus Circle", "Times Square", "Christopher Street", "South Ferry"],
    "hot_spot_img": {"Van Courtland Park" : "https://i.ibb.co/VB3CgmG/OLYMPUS-DIGITAL-CAMERA.jpg", "Columbia University" : "https://i.ibb.co/b11FPF3/columbia.png", "96th Street" : "https://i.ibb.co/Lgf7kd0/96th.jpg", "Columbus Circle" : "https://i.ibb.co/QdfLmx4/Columbus-Circle.jpg", "Times Square" : "https://i.ibb.co/8D9hDF0/Times-Square.jpg", "Christopher Street" : "https://i.ibb.co/6H9Vz5L/west4.jpg", "South Ferry" : "https://i.ibb.co/vBXSpz5/southferry.jpg"}
  },
  {
    "id": 4,
    "train": "4",
    "img_link": "https://i.ibb.co/v3fWZbn/4-train.png",
    "route_img": "https://i.ibb.co/nj7yPmC/456-train-route.png",
    "info": "The 4 train runs express under Lexington Avenue on the East Side of Manhattan.",
    "uptown": "Woodlawn",
    "downtown": "New Lots Avenue",
    "hot_spots": [[1095, 350], [1095, 480], [1090, 615], [1090, 740], [1070, 950]],
    "hot_spot_id": ["110th Street", "86th Street", "Grand Central", "Spring Street", "Brooklyn Bridge"],
    "hot_spot_img": {"110th Street" : "https://i.ibb.co/Sx358yc/OLYMPUS-DIGITAL-CAMERA.jpg", "86th Street" : "https://i.ibb.co/r7PwDsV/Met.jpg", "Grand Central" : "https://i.ibb.co/YWnc8xg/Grand-Central.jpg", "Spring Street" : "https://i.ibb.co/C684ncq/Spring-Street.jpg", "Brooklyn Bridge" : "https://i.ibb.co/3RdrMGL/Brooklyn-Bridge-Manhattan.jpg"}
  },
  {
    "id": 5,
    "train": "5",
    "img_link": "https://i.ibb.co/R9ZbJZZ/5-train.png",
    "route_img": "https://i.ibb.co/nj7yPmC/456-train-route.png",
    "info": "The 5 train runs express under Lexington Avenue on the East Side of Manhattan.",
    "uptown": "Eastchester - Dyre Avenue",
    "downtown": "Flatbush Avenue - Brooklyn College",
    "hot_spots": [[1095, 350], [1095, 480], [1090, 615], [1090, 740], [1070, 950]],
    "hot_spot_id": ["110th Street", "86th Street", "Grand Central", "Spring Street", "Brooklyn Bridge"],
    "hot_spot_img": {"110th Street" : "https://i.ibb.co/Sx358yc/OLYMPUS-DIGITAL-CAMERA.jpg", "86th Street" : "https://i.ibb.co/r7PwDsV/Met.jpg", "Grand Central" : "https://i.ibb.co/YWnc8xg/Grand-Central.jpg", "Spring Street" : "https://i.ibb.co/C684ncq/Spring-Street.jpg", "Brooklyn Bridge" : "https://i.ibb.co/3RdrMGL/Brooklyn-Bridge-Manhattan.jpg"}
  },
  {
    "id": 6,
    "train": "6",
    "img_link": "https://i.ibb.co/r7dmH5S/6-train.png",
    "route_img": "https://i.ibb.co/nj7yPmC/456-train-route.png",
    "info": "6 trains operate local at all times between Pelham Bay Park in the Bronx and Brooklyn Bridge–City Hall in Lower Manhattan.",
    "uptown": "Pelham Bay Park",
    "downtown": "Brooklyn Bridge - Chambers Street",
    "hot_spots": [[1095, 350], [1095, 480], [1090, 615], [1090, 740], [1070, 950]],
    "hot_spot_id": ["110th Street", "86th Street", "Grand Central", "Spring Street", "Brooklyn Bridge"],
    "hot_spot_img": {"110th Street" : "https://i.ibb.co/Sx358yc/OLYMPUS-DIGITAL-CAMERA.jpg", "86th Street" : "https://i.ibb.co/r7PwDsV/Met.jpg", "Grand Central" : "https://i.ibb.co/YWnc8xg/Grand-Central.jpg", "Spring Street" : "https://i.ibb.co/C684ncq/Spring-Street.jpg", "Brooklyn Bridge" : "https://i.ibb.co/3RdrMGL/Brooklyn-Bridge-Manhattan.jpg"}
  },
  {
    "id": 7,
    "train": "A",
    "img_link": "https://i.ibb.co/85Ny3Qx/a-train.png",
    "route_img": "https://i.ibb.co/cNwmcQf/ACE-train-route.png",
    "info": "The A train is the 8th Avenue express train that runs uptown to downtown on the west side of Manhttan.",
    "uptown": "Inwood 207th Street",
    "downtown": "Far Rockaway - Mott Avenue",
    "hot_spots": [[900, 100], [925, 550], [940, 590], [1010, 740], [1160, 890]],
    "hot_spot_id": ["207th Street", "Columbus Circle", "Times Square", "West 4th", "Chambers Street"],
    "hot_spot_img" : {"207th Street" : "https://i.ibb.co/GTW7ZDm/207.jpg", "Columbus Circle" : "https://i.ibb.co/QdfLmx4/Columbus-Circle.jpg", "Times Square" : "https://i.ibb.co/8D9hDF0/Times-Square.jpg", "West 4th" : "https://i.ibb.co/6H9Vz5L/west4.jpg", "Chambers Street" : "https://i.ibb.co/ThjXXR9/chambers.jpg" }
  },
  {
    "id": 8,
    "train": "C",
    "img_link": "https://i.ibb.co/SBn5k9X/c-train.png",
    "route_img": "https://i.ibb.co/cNwmcQf/ACE-train-route.png",
    "info": "The C train is the 8th Avenue local train that runs uptown to downtown on the west side of Manhttan.",
    "uptown": "168th Street",
    "downtown": "Euclid Avenue",
    "hot_spots": [[900, 100], [925, 550], [940, 590], [1010, 740], [1160, 890]],
    "hot_spot_id": ["207th Street", "Columbus Circle", "Times Square", "West 4th", "Chambers Street"],
    "hot_spot_img" : {"207th Street" : "https://i.ibb.co/GTW7ZDm/207.jpg", "Columbus Circle" : "https://i.ibb.co/QdfLmx4/Columbus-Circle.jpg", "Times Square" : "https://i.ibb.co/8D9hDF0/Times-Square.jpg", "West 4th" : "https://i.ibb.co/6H9Vz5L/west4.jpg", "Chambers Street" : "https://i.ibb.co/ThjXXR9/chambers.jpg" }
  },
  {
    "id": 9,
    "train": "E",
    "img_link": "https://i.ibb.co/LkSrLm6/e-train.png",
    "route_img": "https://i.ibb.co/cNwmcQf/ACE-train-route.png",
    "info": "The E train is the 8th Avenue local train that runs between Queens and the West Side of Manhattan.",
    "uptown": "Jamiaca - 179th Street",
    "downtown": "World Trade Center",
    "hot_spots": [[900, 100], [925, 550], [940, 590], [1010, 740], [1160, 890]],
    "hot_spot_id": ["207th Street", "Columbus Circle", "Times Square", "West 4th", "Chambers Street"],
    "hot_spot_img" : {"207th Street" : "https://i.ibb.co/GTW7ZDm/207.jpg", "Columbus Circle" : "https://i.ibb.co/QdfLmx4/Columbus-Circle.jpg", "Times Square" : "https://i.ibb.co/8D9hDF0/Times-Square.jpg", "West 4th" : "https://i.ibb.co/6H9Vz5L/west4.jpg", "Chambers Street" : "https://i.ibb.co/ThjXXR9/chambers.jpg" }
  },
  {
    "id": 10,
    "train": "B",
    "img_link": "https://i.ibb.co/vc632yz/b-train.png",
    "route_img": "https://i.ibb.co/88Rp9Ws/BDFM-train-route.png",
    "info": "The B train runs local under 6th Avenue in the Center and West Side of Manhattan",
    "uptown": "Bedford Park Blvd",
    "downtown": "Brighton Beach"
  },
  {
    "id": 11,
    "train": "D",
    "img_link": "https://i.ibb.co/WvLYVSp/d-train.png",
    "route_img": "https://i.ibb.co/88Rp9Ws/BDFM-train-route.png",
    "info": "The D train runs express under 6th Avenue in the Center and West Side of Manhattan, ",
    "uptown": "Norwood - 205th Street",
    "downtown": "Coney Island - Stillwell Avenue"
  },
  {
    "id": 12,
    "train": "F",
    "img_link": "https://i.ibb.co/FwbSbqm/f-train.png",
    "route_img": "https://i.ibb.co/88Rp9Ws/BDFM-train-route.png",
    "info": "The F train runs local under 6th Avenue in the center of Manhattan.",
    "uptown": "Jamiaca - 179th Street",
    "downtown": "Coney Island - Stillwell Avenue"
  },
  {
    "id": 13,
    "train": "M",
    "img_link": "https://i.ibb.co/N9yW2fw/m-train.png",
    "route_img": "https://i.ibb.co/88Rp9Ws/BDFM-train-route.png",
    "info": "The M train runs express under 6th Avenue in the center of Manhattan.",
    "uptown": "Forrest Hills - 71 Avenue",
    "downtown": "Middle Village - Metropolitan Avenue"
  },
  {
    "id": 14,
    "train": "N",
    "img_link": "https://i.ibb.co/41x9Qk8/n-train.png",
    "route_img": "https://i.ibb.co/crvr6GM/NQR-train-route.png",
    "info": "The N train runs through the center of Manhattan between Brooklyn and Queens",
    "uptown": "Astoria - Ditmars Blvd",
    "downtown": "Coney Island - Stillwell Avenue"
  },
  {
    "id": 15,
    "train": "Q",
    "img_link": "https://i.ibb.co/3vPBWvw/q-train.png",
    "route_img": "https://i.ibb.co/crvr6GM/NQR-train-route.png",
    "info": "The Q train runs through the center of Manhattan and then on the East side to 96th Street",
    "uptown": "96th Street",
    "downtown": "Coney Island - Stillwell Avenue"
  },
  {
    "id": 16,
    "train": "R",
    "img_link": "https://i.ibb.co/jJVMVMb/r-train.png",
    "route_img": "https://i.ibb.co/crvr6GM/NQR-train-route.png",
    "info": "The R train runs through the center of Manhattan between Brooklyn and Queens",
    "uptown": "Whitehall Street",
    "downtown": "Bay Ridge - 95th Street"
  },
  {
    "id": 17,
    "train": "W",
    "img_link": "https://i.ibb.co/XXNZXrN/w-train.png",
    "route_img": "https://i.ibb.co/crvr6GM/NQR-train-route.png",
    "info": "The W train runs through the center of Manhattan and then on the East side to 96th Street",
    "uptown": "Astoria - Ditmars Avenue",
    "downtown": "Whitehall Street"
  },
  {
    "id": 18,
    "train": "7",
    "img_link": "https://i.ibb.co/G9NXsR0/7-train.png",
    "route_img": "https://i.ibb.co/yWBFyWD/7-train-route.png",
    "info": "The 7 train runs across midtown Manhattan and into Queens",
    "uptown": "34th Street - 11th Avenue",
    "downtown": "Flushing - Main Street"
  },
  {
    "id": 19,
    "train": "L",
    "img_link": "https://i.ibb.co/7jDLv62/L-train.jpg",
    "route_img": "https://i.ibb.co/v4tL9sv/L-train-route.png",
    "info": "The L train runs under 14th Street across Manhattan and into Brooklyn",
    "uptown": "8th Avenue",
    "downtown": "Canarsie - Rockaway Parkway"
  },
  {
    "id": 20,
    "train": "S",
    "img_link": "https://i.ibb.co/KrcsdG1/s-train.png",
    "route_img": "https://i.ibb.co/FKqddnj/S-train-route.png",
    "info": "The S train connects Times Square/42nd Street and Grand Central Station",
    "uptown": "Times Square/42nd Street",
    "downtown": "Grand Central Station"
  }

]

easyQuiz = [
  {
    "id": 1,
    "question": "Let's go from Columbia University to Times Square!",
    "answer": [[1], [1, 2], [1, 3]]
  },
  {
    "id": 2,
    "question": "Let's go from 59th Street/Columbus Circle to Grand Central!",
    "answer": [[7, 20], [8, 20], [1, 20], [2, 20], [3, 20]]
  },
  {
    "id": 3,
    "question": "Let's go from the Met on 82nd and Fifth Avenue to Union Square!",
    "answer": [[6]]
  },
  {
    "id": 4,
    "question": "Let's go from 8th Avenue at 14th Street to Union Square!",
    "answer": [[19]]
  },
  {
    "id": 5,
    "question": "Let's go from Grand Central to Times Square!",
    "answer": [[20]]
  }
]

hardQuiz = [
  {
    "id": 1,
    "question": "Let's go from Union Square to Columbia University!",
    "answer": [[19, 1]]
  },
  {
    "id": 2,
    "question": "Let's go from West 4th to Grand Central!",
    "answer": [[7, 20], [8, 20], [9, 20]]
  },
  {
    "id": 3,
    "question": "Let's go from Columbus Circle 59th Street to the Met on 85th and 5th Avenue!",
    "answer": [[1, 5, 2], [3, 5, 2]]
  },
  {
    "id": 4,
    "question": "Let's go from Union Square to the Cloisters (far upper west side)!",
    "answer": [[19, 8, 7], [19, 7], [19, 9, 7], [14, 7]] 
  },
  {
    "id": 5,
    "question": "Let's go from the World Trade Center to Grand Central Station!",
    "answer": [[1, 20], [2, 20], [3, 20]]
  }
]

loadCommand = 0
indexLoad = 0
quizIndex = 0
quizScore = 0
quizChoice = 0
wrongAnswer = []
currentAnswer = []



@app.route('/')

def home():
    return render_template('home.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex, wrongAnswer=wrongAnswer)

@app.route('/learn/', methods=['GET', 'POST'])

def learn():
  return render_template('learn.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex, wrongAnswer=wrongAnswer)
 
@app.route('/quiz/', methods=['GET', 'POST'])

def quiz():
  
  tempQuiz = None

  if quizChoice == 1:
    tempQuiz = easyQuiz
  elif quizChoice == 2:
    tempQuiz = hardQuiz
  return render_template('quiz.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=tempQuiz, quizIndex=quizIndex, wrongAnswer=wrongAnswer)

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
  return render_template('view.html', trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex, wrongAnswer=wrongAnswer)

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

@app.route('/save_wrong_answer', methods=['GET', 'POST'])

def save_wrong_answer():
  global quizIndex
  global wrongAnswer

  print("quizIndex:")
  print(quizIndex)
  wrongAnswer.append(quizIndex)
  print(wrongAnswer)

  return jsonify(data=wrongAnswer)

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
  global wrongAnswer
  tempScore = quizScore
  tempWrongAnswer = wrongAnswer
  print("inside results page")
  print(wrongAnswer)
  quizScore = 0
  quizIndex = 0
  wrongAnswer = []

  return render_template("results.html", trains=trains, loadCommand=loadCommand, indexLoad=indexLoad, quiz=easyQuiz, quizIndex=quizIndex, quizScore=tempScore, wrongAnswer=tempWrongAnswer)
