let nameInput = document.getElementById("username")
let passwordInput = document.getElementById("password")
let submitButton = document.getElementById("submitButton")
submitButton.addEventListener("click", setLocalStorage)
function registration() {
    fetch('/login', {
        method: "post",
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
        body: JSON.stringify({"username": nameInput.value,
                "password": passwordInput.value,})});

    console.log(nameInput.value, passwordInput.value)
}

function setLocalStorage(){
    localStorage.setItem("username", nameInput.value)
}
