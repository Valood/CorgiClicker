const scoreElement = document.getElementById('score');
const forceElement = document.getElementById('force');
const autoBoostElement = document.getElementById('autoBoost')
const clickerButton = document.getElementById('clicker');

const boosters = [
    {element: document.getElementById('ball'), price: 10, boost: 1},
    {element: document.getElementById('boomerang'), price: 100, boost: 5},
    {element: document.getElementById('toy'), price: 1000, boost: 10},
]
const autoBoosters = [
	{ element: document.getElementById('bone'), price: 10, boost: 1 },
	{ element: document.getElementById('food'), price: 100, boost: 5 },
	{ element: document.getElementById('steak'), price: 1000, boost: 10 },
]

let score = 0;
let force = 1;
let autoBoostForce = 0;

window.onload = function () {fetch(`/boost?username=${localStorage.username}`, {
    method: "get",
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
        score = result.corgies
        force = result.corgies_per_click
        autoBoostForce = result.corgies_per_second
        forceElement.textContent = `Корги за клик: ${force}`
        scoreElement.textContent = `У вас ${score} корги`;
        autoBoostElement.textContent = `Корги в секунду: ${autoBoostForce}`
        console.log(score)})}

console.log(123)


clickerButton.addEventListener('click', () => {
    score += force
    scoreElement.textContent = `У вас ${score} корги`;
    fetch('/boost',{
        method: "post",
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
        body: JSON.stringify({
            "username": localStorage.username,
            "corgies" : score,
            "corgies_per_click": force,
            "corgies_per_second": autoBoostForce
        })
    })
    console.log(score, force, autoBoostForce)
})

boosters.forEach((booster) => booster.element.addEventListener('click', () => {
    if(score >= booster.price){
        force += booster.boost;
        score -= booster.price;
        forceElement.textContent = `Корги за клик: ${force}`
        scoreElement.textContent = `У вас ${score} корги`;

    }
}))


intervalRef = setInterval(() => {
                score += autoBoostForce;
                scoreElement.textContent = `У вас ${score} корги`;
            }, 1000);

autoBoosters.forEach((booster) => booster.element.addEventListener('click', () => {
    if(score >= booster.price){
        clearInterval(intervalRef)
        autoBoostForce += booster.boost;
        autoBoostElement.textContent = `Корги в секунду: ${autoBoostForce}`;
        score -= booster.price;
        intervalRef = setInterval(() => {
                score += autoBoostForce;
                scoreElement.textContent = `У вас ${score} корги`;
            }, 1000);
    }
}))

