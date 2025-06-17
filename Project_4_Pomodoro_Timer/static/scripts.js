let workTime = 25 * 60;
let shortBreak = 5 * 60;
let longBreak = 15 * 60;
let reps = 0;
let timer;
let timeLeft = workTime;
let isWorkSession = true; 

function updateDisplay(seconds) {
    const min = Math.floor(seconds / 60).toString().padStart(2, '0');
    const sec = (seconds % 60).toString().padStart(2, '0');
    document.getElementById("timer").innerText = `${min}:${sec}`;
}

function startTimer() {
    reps++;
    const sound = document.getElementById("alarmSound");
    sound.play();
    if (reps % 8 === 0) {
        timeLeft = longBreak;
        isWorkSession = false;
        document.getElementById("title").innerText = "Long Break";
        document.getElementById("title").style.color = "red";
    } else if (reps % 2 === 0) {
        timeLeft = shortBreak;
        isWorkSession = false;
        document.getElementById("title").innerText = "Short Break";
        document.getElementById("title").style.color = "blue";
    } else {
        timeLeft = workTime;
        isWorkSession = true;
        document.getElementById("title").innerText = "Work";
        document.getElementById("title").style.color = "green";
    }

    runTimer();
}

function runTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateDisplay(timeLeft);
        } else {
            clearInterval(timer);

            if (isWorkSession) {
                document.getElementById("checkmarks").innerText += "✔ ";
            }

            startTimer();
            
        }
    }, 1000);
}

function resetTimer() {
    clearInterval(timer);
    reps = 0;
    timeLeft = workTime;
    isWorkSession = true;
    updateDisplay(timeLeft);
    document.getElementById("title").innerText = "Pomodoro Timer";
    document.getElementById("title").style.color = "#2F4F4F";
    document.getElementById("checkmarks").innerText = "";
}
