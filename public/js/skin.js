function submitAnswer(){
  var total = 6;

  //get user input
  var q1 = document.forms["skinQuiz"]["q1"].value;
  var q2 = document.forms["skinQuiz"]["q2"].value;
  var q3 = document.forms["skinQuiz"]["q3"].value;
  var q4 = document.forms["skinQuiz"]["q4"].value;
  var q5 = document.forms["skinQuiz"]["q5"].value;
  var q6 = document.forms["skinQuiz"]["q6"].value;

  //validation
  for(i =1; i <= total; i++){
    if(eval("q" + i) == null || eval("q" + i) == ''){
      alert ("You missed question " +i);
      return false;
    }
  }

  //set skin type
  var man = document.getElementById("q1a").checked;
  var women = document.getElementById("q1b").checked;
  var under20 = document.getElementById("q2a").checked;
  var above20 = document.getElementById("q2b").checked;
  var above31 = document.getElementById("q2c").checked;
  var above41 = document.getElementById("q2d").checked;

//oily
  var oily1 = document.getElementById("oilyalready").checked;
  var oily2 = document.getElementById("oilywhole").checked;
  var oily3 = document.getElementById("acne").checked;
  var oily4 = document.getElementById("large").checked;

//dry
  var dry1 = document.getElementById("drytight").checked;
  var dry2 = document.getElementById("drywhole").checked;
  var dry3 = document.getElementById("irritated").checked;
  var dry4 = document.getElementById("medium").checked;

//Normal
  var nor1 = document.getElementById("good").checked;
  var nor2 = document.getElementById("oilypart").checked;
  var nor3 = document.getElementById("pores").checked;
  var nor4 = document.getElementById("small").checked;

//Sensitive
  var sen1 = document.getElementById("drytight").checked;
  var sen2 = document.getElementById("drywhole").checked;
  var sen3 = document.getElementById("irritated").checked;
  var sen4 = document.getElementById("medium").checked;

//com
  var com1 = document.getElementById("somespot").checked;
  var com2 = document.getElementById("oilypart").checked;
  var com3 = document.getElementById("pores").checked;
  var com4 = document.getElementById("visible").checked;

  //start
  if (man == "" || women == "")
  {
    if (under20 == "" || above20 == "" || above31 == "" || above41 == "")
    {
      if (oily1 == "" && oily2 == "" && oily3 == "" && oily4 == "")
      {
        alert ("Oily Skin");
        window.location = "oilyskincareCategory";
        return false;
      }
      else if (dry1 == "" && dry2 == "" && dry3 == "" && dry4 == "")
      {
        alert ("Dry Skin");
        window.location = "dryskincareCategory";
        return false;
      }
      else if (nor1 == "" && nor2 == "" && nor3 == "" && nor4 == "")
      {
        alert ("Normal Skin");
        window.location = "norskincareCategory";
        return false;
      }
      else if (sen1 == "" && sen2 == "" && sen3 == "" && sen4 == "")
      {
        alert ("Sensitive Skin");
        window.location = "senskincareCategory";
        return false;
      }
      else if (com1 == "" && com2 == "" && com3 == "" && com4 == "")
      {
        alert ("Combination Skin");
        window.location = 'comskincareCategory';
        return false;
      }
      else
      {
        alert ("Skin");
      }
    }
    else
    {
      alert ("pediaaaaa");
    }
  }

  //display results
  var results = document.getElementById('results');
  results.innerHTML = '<h3>You scored out of <br> <a href=\"dashboard">Dashboard</a><h3>';
  alert('You score '+score+' out of ' +total);
  return false;
}
