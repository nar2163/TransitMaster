let currentAnswer = [];
let currentTrains = [1, 2, 3, 4, 5];
let allTrains = [1, 2, 3, 4, 5];

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

    display_trains(trains, loadCommand, indexLoad, quiz, quizIndex)
});

function display_trains(trains, loadCommand, indexLoad, quiz, quizIndex)
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
        loadResults(quizScore)
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
    quizDiv.style = "display:block;";
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

function loadResults(quizScore)
{
    console.log(quizScore);
    let resultsDiv = document.getElementById("final-score");
    resultsDiv.innerHTML = "YOU GOT A " + quizScore + " out of 5";
}

function loadLearn(trains)
{
    console.log(trains);
    let train_list = document.getElementById("train-main");
    console.log(train_list);
    train_list.innerHTML = '';
    let index = 0;

    for(index; index < trains.length; index++){
        let tempObject = trains[index];
        console.log(tempObject);
        let trainImg = tempObject.img_link;
        let id = tempObject.id;

        newDiv = document.createElement("div");
        newDiv.className = "card col-lg-2";
        newRowHTML = "<a href='/view/" + id + "' onclick='updateIndex(" + index + ")'><img class='card-img-top card-img-size' src='" + trainImg + "' alt='Broadway Show Poster Image'></a>";
        newDiv.innerHTML += newRowHTML;
        train_list.appendChild(newDiv);

    }
}

function loadView(trains, indexLoad)
{
    console.log(trains);
    let view_main = document.getElementById("view-main");
    console.log(view_main);
    view_main.innerHTML = '';
    let tempObject = trains[indexLoad];
    view_main.innerHTML = "<img src='" + tempObject.img_link + "'>" 
    view_main.innerHTML += "<p>" + tempObject.train + "</p>";
    view_main.innerHTML += "<p>" + tempObject.info + "</p>";
    view_main.innerHTML += "<p>" + tempObject.uptown + "</p>";
    view_main.innerHTML += "<p>" + tempObject.downtown + "</p>";  
    console.log(tempObject);
}

function loadQuiz(trains, quiz, quizIndex)
{
    let train_bucket = document.getElementById("train-bucket");
    let question_bucket = document.getElementById("question");
    let index = 0;

    updateScoreUI();

    for(index; index < trains.length; index++)
    {
        let tempTrain = trains[index];
        let card1 = document.createElement("div");
        card1.classList.add("container");
        card1.classList.add("draggable");
        card1.classList.add("train-drag");
        card1.id = tempTrain.id;
        card1.innerHTML = "<img src='" + tempTrain.img_link + "' height='40' width='25'>";
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
        
        innerIndex = 0;
        let card1 = document.createElement("div");
        card1.classList.add("container");
        card1.classList.add("draggable");
        card1.classList.add("train-drag");
        card1.id = tempTrain.id;
        card1.innerHTML = "<img src='" + tempTrain.img_link + "' height='40' width='25'>";
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
        card1.innerHTML = "<img src='" + tempTrain.img_link + "' height='40' width='25'>";
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
            updateQuizIndex();
            /**$.get('/save_quiz_index', function(data)
            {
                console.log(data.data);
            });**/
        }
    });

});

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