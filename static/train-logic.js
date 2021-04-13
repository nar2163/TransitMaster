let currentAnswer = [];
let currentTrains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
let allTrains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

$(document).ready(function(){

    $(".draggable").draggable({
        revert: "invalid",
        zIndex: 300,
    });

    $( "#answer-bucket" ).droppable({
        accept: ".train-drag",
        activeClass: "dark-pink",
        hoverClass: "darkest-pink",
        drop: function( event, ui ) {
            $( this )
            {
                console.log("i'm inside");
                $(this).addClass("dropped");
                let id = ui.draggable.attr("id");
                $(this).removeClass("dropped");
                updateCurrentArraysAnswer(id);
                updateCurrentAnswer(currentAnswer);
                deleteUI();
                loadCurrQuiz(currentTrains, currentAnswer, trains);
            }
        }
    });

    $("#train-bucket").droppable({
        accept: ".answer-drag",
        activeClass: "dark-blue",
        hoverClass: "darkest-blue",
        drop: function( event, ui ) {
            $( this )
            {
                $(this).addClass("dropped");
                let id = ui.draggable.attr("id");
                $(this).removeClass("dropped");
                updateCurrentArraysTrains(id);
                updateCurrentAnswer(currentAnswer);
                deleteUI();
                loadCurrQuiz(currentTrains, currentAnswer, trains);
            }
        }
    });

    display_trains(trains, loadCommand, indexLoad, quiz, quizIndex, wrongAnswer)
});

function display_trains(trains, loadCommand, indexLoad, quiz, quizIndex, wrongAnswer)
{
    if(loadCommand == 0)
    {
        loadHome();
    } else if(loadCommand == 1)
    {
        loadLearn(trains)
    } else if(loadCommand == 2)
    {
        loadView(trains, indexLoad)
    } else if(loadCommand == 3)
    {
        loadQuiz(trains, quiz, quizIndex, currentAnswer)
    } else if(loadCommand == 4)
    {
        currentTrains = allTrains;
        loadResults(trains, quiz, quizScore, wrongAnswer)
    }

}

function updateCurrentArraysAnswer(id)
{
    let tempIndex = 0;
    let tempTrain;

    console.log("id: " + id);
    for(tempIndex; tempIndex < currentTrains.length; tempIndex++)
    {
        tempTrain = currentTrains[tempIndex];
        if(tempTrain == id)
        {
           break; 
        }
    }

    //console.log(tempTrain);
    currentAnswer.push(tempTrain);

    const index = currentTrains.indexOf(parseInt(id));
    if (index > -1) {
        currentTrains.splice(index, 1);
    }
    //console.log("currentTrains in updateCurrentArrayAnswer:");
    //console.log(currentTrains);
    //console.log("currentAnswer in updateCurrentArrayAnswer:");
    //console.log(currentAnswer);
}

function updateCurrentArraysTrains(id)
{
    let tempIndex = 0
    let tempTrain;

    for(tempIndex; tempIndex < currentAnswer.length; tempIndex++)
    {
        tempTrain = currentAnswer[tempIndex];
        if(tempTrain == id)
        {
            break;
        }
    }
    
    currentTrains.push(tempTrain);
    const index = currentAnswer.indexOf(parseInt(id));
    if (index > -1) {
        currentAnswer.splice(index, 1);
    }

    console.log("currentTrains:");
    console.log(currentTrains);
    console.log("currentAnswer:");
    console.log(currentAnswer);
}

function deleteUI()
{
    let tempBucket = document.getElementById("answer-bucket");
    tempBucket.innerHTML = '';
    tempBucket = document.getElementById("train-bucket");
    tempBucket.innerHTML = '';
    tempBucket = document.getElementById("train-bucket1");
    tempBucket.innerHTML = '';
    tempBucket = document.getElementById("train-bucket2");
    tempBucket.innerHTML = '';
}

function loadHome()
{
    let quizParent = document.getElementById("quiz-link");
    quizParent.addEventListener("click", showQuizDiv);
    let easyLink = document.getElementById("easy-link");
    let hardLink = document.getElementById("hard-link");
    easyLink.addEventListener("click", function(){
        quizChosen(1);
    }, false);
    hardLink.addEventListener("click", function(){
        quizChosen(2);
    }, false);
}

function showQuizDiv()
{
    let quizDiv = document.getElementById("quiz-options");
    let quizMain = document.getElementById("quiz-main");
    quizDiv.style = "display:block;";
    quizMain.style = "display:none;";
}

function quizChosen(choice)
{
    choice_to_server = {
        "updated_choice": choice
    }

    $.ajax({
        type: 'POST',
        url: 'update_quiz_choice',
        data: JSON.stringify(choice_to_server),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function(result){
            console.log(result)
        },
        error: function(request, status, error){
            console.log('Error');
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

function loadResults(trains, quiz, quizScore, wrongAnswer)
{
    console.log("wrongAnswers: " + wrongAnswer);
    console.log(quizScore);
    let resultsDiv = document.getElementById("final-score");
    resultsDiv.innerHTML = "You got a " + quizScore + " out of 5";
    let comment;
    if(quizScore < 3)
    {
        comment = "Keep trying! Here's what you got wrong!"
    } else {
        comment = "Wow you really are a Transit Master! Congrats!"
    }
    let commentDiv = document.createElement("div");
    commentDiv.innerHTML += comment;
    commentDiv.classList.add("question-text");
    resultsDiv.appendChild(commentDiv);

    let wrongAnswersDiv = document.getElementById("wrong-answers");

    let index = 0;

    /**for(index; index < wrongAnswer.length; index++)
    {
        let tempObject = quiz[wrongAnswer[index]];
        let tempAnswer = tempObject.answer;
        let tempQuestion = tempObject.question;
        let tempDiv = document.createElement("div");
        tempDiv.innerHTML += tempQuestion.toString();
        let innerIndex = 0;
        for(innerIndex; innerIndex < tempAnswer.length; innerIndex++)
        {
            let tempImageDiv = document.createElement("div");
            let currAnswer = tempAnswer[innerIndex];
            let secondInnerIndex = 0;
            for(secondInnerIndex; secondInnerIndex < currAnswer.length; secondInnerIndex++)
            {

            }

        }
        wrongAnswersDiv.appendChild(tempDiv);
    }**/
}

function loadLearn(trains)
{
    console.log(trains);
    let train_list = document.getElementById("train-main");
    console.log(train_list);
    train_list.innerHTML = '';
    let index = 0;

    for(index; index < 9; index++){
        let tempObject = trains[index];
        let trainImg = tempObject.img_link;
        let id = tempObject.id;
        newDiv = document.createElement("div");
        newDiv.className = "card col-lg-4";    
        newRowHTML = "<a href='/view/" + id + "' onclick='updateIndex(" + index + ")'><img class='card-img-top card-img-size' src='" + trainImg + "' alt='Broadway Show Poster Image'></a>";
        newDiv.innerHTML += newRowHTML;
        train_list.appendChild(newDiv);
    }

    train_list = document.getElementById("train-main2");
    train_list.innerHTML = '';

    for(index; index < 17; index++){
        let tempObject = trains[index];
        let trainImg = tempObject.img_link;
        let id = tempObject.id;
        newDiv = document.createElement("div");
        newDiv.className = "card col-lg-3";    
        newRowHTML = "<a href='/view/" + id + "' onclick='updateIndex(" + index + ")'><img class='card-img-top card-img-size' src='" + trainImg + "' alt='Broadway Show Poster Image'></a>";
        newDiv.innerHTML += newRowHTML;
        train_list.appendChild(newDiv);
    }

    train_list = document.getElementById("train-main3");
    train_list.innerHTML = '';

    for(index; index < 22; index++)
    {
        let tempObject = trains[index];
        let trainImg = tempObject.img_link;
        let id = tempObject.id;
        newDiv = document.createElement("div");
        newDiv.className = "card col-lg-12";    
        newRowHTML = "<a href='/view/" + id + "' onclick='updateIndex(" + index + ")'><img class='card-img-top card-img-size' src='" + trainImg + "' alt='Broadway Show Poster Image'></a>";
        newDiv.innerHTML += newRowHTML;
        train_list.appendChild(newDiv);
    }
}

function loadView(trains, indexLoad)
{
    console.log(trains);
    let tempObject = trains[indexLoad];

    let subway_logo = document.getElementById("subway-logo");
    newDiv = document.createElement("div");
    newDiv.className = "card col-lg-2";
    newDiv.innerHTML = "<img class='card-img-top card-img-size' src='" + tempObject.img_link + "'>";
    subway_logo.appendChild(newDiv);

    let subway_description = document.getElementById("subway-description");
    subway_description.innerHTML += "<p>" + tempObject.info + "</p>";

    let subway_laststops = document.getElementById("subway-laststops");
    subway_laststops.innerHTML += "<p> Uptown:" + tempObject.uptown + "</p><p> Downtown: " + tempObject.downtown + "</p>";
    
    //console.log(tempObject.hot_spots);
    
    let subway_map = document.getElementById("subway-map");
    subway_map.innerHTML += "<img src='" + tempObject.route_img + "'/>";

    let hot_spots = tempObject.hot_spots;
    let hot_spot_ids = tempObject.hot_spot_id;

    let index = 0;
    
    for(index; index < hot_spots.length; index++)
    {
        let tempArr = hot_spots[index];
        console.log(tempArr);
        newDiv = document.createElement("div");
        newDiv.id = hot_spot_ids[index];
        newDiv.style = "height: 50px; width: 50px; position:absolute; left:" + (tempArr[0] - 10) + "px; top:" + tempArr[1] + "px; color: black";
        //newDiv.style.display = 'none';
        //newDiv.innerHTML += "<p>XXX</p>";
        document.getElementById("view-main").appendChild(newDiv);

        //color: #ecd525 opacity: 0
        

        newDiv.onmouseover = function(e) { 
            let circleDivId = this.id;
            console.log(circleDivId);
            circleDiv = document.createElement("div");
            circleDiv.id = circleDivId + "circle";
            circleDiv.innerHTML = circleDivId.toString();
            circleDiv.style += "height: 100px; width: 100px; background-color: none; color: black; border-radius: 50%; position:absolute; left:" + (tempArr[0] - 10) + "px; top:" + tempArr[1] + "px;";
            //console.log(circleDiv);
            document.getElementById("view-main").appendChild(circleDiv);
            newCard = document.createElement("div");
            let boxTest = document.getElementById("popup");
            console.log(boxTest);
            if(boxTest != null)
            {
                console.log("i'm inside");
                boxTest.innerHTML = '';
            }
            newCard.id = circleDivId + "card";
            newCard.className = "card col-lg-12";
            imgLink = tempObject.hot_spot_img[circleDivId.toString()];
            newCard.innerHTML = "<img class='card-img-top card-img-size' src='" + imgLink + "'>";
            newCard.innerHTML += "<div class='card-body'>" + circleDivId.toString() + "</div>";
            document.getElementById("popup").appendChild(newCard);
    
        };

        newDiv.onmouseout = function(e) {
            let temp = document.getElementById(this.id + "circle");
            temp.remove();
            //temp = document.getElementById(this.id + "card");
            //temp.remove();
        };

    }

    let back = document.createElement("button");
    back.innerHTML = "back";   
    back.addEventListener("click", function(){
        history.back();
    });
    subway_description.appendChild(back);
 
}

function loadQuiz(trains, quiz, quizIndex)
{
    let train_bucket = document.getElementById("train-bucket");
    let question_bucket = document.getElementById("question");
    let index = 0;

    updateScoreUI();

    for(index; index < trains.length; index++)
    { 

        if(index >= 6 && index < 13)
        {
            train_bucket = document.getElementById("train-bucket1");
        } else if(index >= 13)
        {
            train_bucket = document.getElementById("train-bucket2");
        }

        let tempTrain = trains[index];
        console.log(trains);
        let card1 = document.createElement("div");
        card1.classList.add("container");
        card1.classList.add("draggable");
        card1.classList.add("train-drag");
        card1.id = tempTrain.id;
        card1.innerHTML = "<img src='" + tempTrain.img_link + "' height='70' width='60'>";
        train_bucket.appendChild(card1);
        $(".draggable").draggable({revert: true, zIndex: 300});
        console.log(card1);
        
    }

    let currentQuestion = quiz[quizIndex];
    
    question_bucket.innerHTML = '<p>' + currentQuestion.question + '<p>';
}

function loadCurrQuiz(currentTrains, currentAnswer, trains)
{
    let train_bucket = document.getElementById("train-bucket");
    let answer_bucket = document.getElementById("answer-bucket");
    let index = 0;
    let innerIndex = 0;
    let tempTrain;

    /**console.log("loadQuiz currentTrains:");
    console.log(currentTrains);
    console.log("loadQuiz currentAnswer:");
    console.log(currentAnswer);**/

    updateScoreUI();

    for(index; index < currentTrains.length; index++)
    {
        for(innerIndex; innerIndex < trains.length; innerIndex++)
        {
            tempTrain = trains[innerIndex];
            if(tempTrain.id == currentTrains[index])
            {
                break;
            }

        }
        
        if(index >= 6 && index < 12)
        {
            train_bucket = document.getElementById("train-bucket1");
        } else if(index >= 12)
        {
            train_bucket = document.getElementById("train-bucket2");
        }

        innerIndex = 0;
        let card1 = document.createElement("div");
        card1.classList.add("container");
        card1.classList.add("draggable");
        card1.classList.add("train-drag");
        card1.id = tempTrain.id;
        card1.innerHTML = "<img src='" + tempTrain.img_link + "' height='70' width='60'>";
        train_bucket.appendChild(card1);
        $(".draggable").draggable({revert: true, zIndex: 300}); 
    }

    index = 0;
    innerIndex = 0;

    console.log("current Answer:");
    console.log(currentAnswer);

    for(index; index < currentAnswer.length; index++)
    {

        for(innerIndex; innerIndex < trains.length; innerIndex++)
        {
            tempTrain = trains[innerIndex];
            if(tempTrain.id == currentAnswer[index])
            {
                break;
            }

        }
        
        innerIndex = 0;
        let card1 = document.createElement("div");
        card1.classList.add("container");
        card1.classList.add("draggable");
        card1.classList.add("answer-drag");
        card1.id = tempTrain.id;
        card1.innerHTML = "<img src='" + tempTrain.img_link + "' height='70' width='60'>";
        answer_bucket.appendChild(card1);
        $(".draggable").draggable({revert: true, zIndex: 300}); 

    }
}

$("#submit-answer").click(function(){

    $.get('/correctness', function(data)
    {
        if(data.data)
        {
            alert("Correct!");
            updateQuizScore();
            updateQuizIndex();
            /**$.get('/save_quiz_index', function(data)
            {
                console.log(data.data);
            });**/
        } else {
            alert("Incorrect!");
            updateWrongAnswers();
            updateQuizIndex();
            /**$.get('/save_quiz_index', function(data)
            {
                console.log(data.data);
            });**/
        }
    });

});

function updateWrongAnswers()
{
    $.get('/save_wrong_answer', function(data)
    {
        console.log(data.data);
    });
}

function updateQuizScore()
{
    $.get('/update_quiz_score', function(data)
    {
        console.log(data.data);
    });
}

function updateScoreUI()
{
    $.get('/get_quiz_score', function(data)
    {
        let scoreDiv = document.getElementById("score");
        scoreDiv.classList.add("centerStuff");
        scoreDiv.innerHTML = "SCORE: " + data.data + "/5";
    });
}

function updateIndex(index)
{
    index_to_server = {
        "updated_index": index
    }

    $.ajax({
        type: 'POST',
        url: 'save_index',
        data: JSON.stringify(index_to_server),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function(result){
            console.log(result)
        },
        error: function(request, status, error){
            console.log('Error');
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

function updateQuizIndex()
{
    index_to_server = {
        "updated_index": quizIndex
    }

    console.log("quiz index: ");
    console.log(quizIndex);
    console.log(index_to_server);
    $.ajax({
        type: 'POST',
        url: 'save_quiz_index',
        data: JSON.stringify(index_to_server),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function(result){
            console.log(result.data)
            if(result.data > 4)
            {
                console.log("should load result")
                window.location.href= "/results"
            } else {
                window.location.href= "/quiz"
            }
        },
        error: function(request, status, error){
            console.log('Error');
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

function updateCurrentAnswer(answer)
{
    answer_to_server = {
        "updated_answer": answer
    }

    //let tempTest = document.getElementById("answer-bucket");
    //let tempTestArr = tempTest.getElementsByTagName("div")
    //console.log(tempTestArr);

    $.ajax({
        type: 'POST',
        url: 'update_answer',
        data: JSON.stringify(answer_to_server),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        success: function(result){
            console.log(result)
        },
        error: function(request, status, error){
            console.log('Error');
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}