/*function loginInfo(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "EricMayIsTheBest" && password === "password1"){
        window.location.href = "ProfessorDashboard.html";
    } else if (username === "Jimmy" && password === "password2"){
    window.location.href = "StudentDashboard.html";
    } else { alert("Invalid username or password");}
}*/

let loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let username = document.getElementById("username");
  let password = document.getElementById("password");

  if (username.value == "" || password.value == "") {
    alert("Ensure you input a value in both fields!");
  } else {
    // perform operation with form input
    alert("This form has been successfully submitted!");
    console.log(
      `This form has a username of ${username.value} and password of ${password.value}`
    );

    username.value = "";
    password.value = "";
  }
});