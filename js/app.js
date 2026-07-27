function updateClock(){

    let now = new Date();

    document.getElementById("clock").innerHTML = now.toLocaleString();

}

setInterval(updateClock,1000);

updateClock();

const enterBtn = document.getElementById("enterBtn");
const welcomeBox = document.getElementById("welcomeBox");

console.log(enterBtn);
console.log(welcomeBox);

enterBtn.onclick = function () {

    console.log("Button Clicked");

    welcomeBox.style.display = "none";

}