//lepas je button tu ditekan maksudnya button yg pakai func ni so ini yg akan keluar
function fQuestion0(){
  document.body.style.backgroundColor = "yellow";
  document.getElementById("questionToAsk").innerHTML = "1. Your Gender? "; //untuk soalan
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fMan()'> Man </button> <button onclick = 'fWomen()'> women </button> <button onclick = 'fQuestion1()'> Next </button>";
  //document.getElementById("btnArea").innerHTML = "<button onclick = 'fQuestion1()'> Man </button>";
}
function fMan(){
  document.body.style.backgroundColor = "blue";
}
function fWomen(){
  document.body.style.backgroundColor = "red";
}

function fQuestion1(){
  document.getElementById("questionToAsk1").innerHTML = "2. How old are you?"; //untuk soalan
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fUnder()'> Under 20 </button> <button onclick = 'fUnder1()'> 20-30 </button> <button onclick = 'fUnder2()'> 31-40 </button> <button onclick = 'fUnder3()'> 41++ </button> <button onclick = 'fQuestion2()'> Next </button> <button onclick = 'fQuestion0()'> Back </button>";//ni untuk jawapan kepada soalan. kalau ada 3 jawapan buat tiga tiga
}

function fQuestion2(){
  document.getElementById("questionToAsk2").innerHTML = "3. When I woke in the morning. My skin feels... ";
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fDry()'> Dry & Tight </button> <button onclick = 'fOily()'> Oily already </button> <button onclick = 'fCombination()'> Oily in some spot, dry in other </button> <button onclick = 'fNormal()'> Good </button> <button onclick = 'fQuestion3()'> Next </button> <button onclick = 'fQuestion1()'> Back </button>";
}

function fQuestion3(){
  document.getElementById("questionToAsk3").innerHTML = "4. My T-ZOne... ";
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fOily()'> Oily/Shiny the whole face </button> <button onclick = 'fCombination()'> Oily/Shiny a part of face </button> <button onclick = 'fDry()'> Dry the whole face </button> <button onclick = 'fNormal()'> Dry a part of face </button> <button onclick = 'fQuestion4()'> Next </button> <button onclick = 'fQuestion2()'> Back </button>";
}

function fQuestion4(){
  document.getElementById("questionToAsk4").innerHTML = "5. What is your top skin concern? ";
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fOily()'> Acne </button> <button onclick = 'fDry()'> Anti-aging </button> <button onclick = 'fDry()'> Dryness/Hydration </button> <button onclick = 'fNormal()'> Pigmentation </button> <button onclick = 'fOily()'> Oil control/Pores </button> <button onclick = 'fQuestion5()'> Next </button> <button onclick = 'fQuestion3()'> Back </button>";
}

function fQuestion5(){
  document.getElementById("questionToAsk5").innerHTML = "6. Which best describe your pores?";
  document.getElementById("btnArea").innerHTML = "<button onclick = 'fNormal()'> Medium Size </button> <button onclick = 'fCombination()'> Large/Medium Size & only visible on T-Zone </button> <button onclick = 'fNormal()'> Small & Not visible </button> <button onclick = 'fOily()'> Large & Visible </button> <button onclick = 'fSubmit()'> Result </button> <button onclick = 'fQuestion4()'> Back </button>";
}

function fSubmit(){

var skintype;

   if (skintype == fNormal()){
     alert("You have Normal skin");
   }

   else if (skintype == fCombination()){
      alert("You have Combination skin");
    }

    else if (skintype == fOily()){
       alert("You have Oily skin");
     }

    else {
      alert("You have Dry skin");
    }

    return false;
}
