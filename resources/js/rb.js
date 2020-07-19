//try try je

function fQuestion0(){
  document.body.style.backgroundColor = "lightBlue";
  document.getElementById("questionToAsk").innerHTML = "Which yours team?";
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fQuestion1()'> East </button> <button onclick = 'fQuestion2()'> West </button>";

}

function fQuestion1(){
  document.body.style.backgroundColor = "Blue";
}

function fQuestion2(){
  document.body.style.backgroundColor = "Yellow";
}
