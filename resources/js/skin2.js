function submitAnswer()
{
  var q1a = document.getElementById("q1a");
  var q1b = document.getElementById("q1b");

  if(q1a.checked==true)
    alert("You are man"+q1a);
  if else(q1b.checked==true)
    alert("You are woman"+q1b);
  else
    alert("Pick your gender");


    var man = document.getElementById("q1a").checked;
    var women = document.getElementById("q1b").checked;

    var q3 = getElementsByName("q3");
    var q4 = getElementsByName("q4");
    var q5 = getElementsByName("q5");
    var q6 = getElementsByName("q6");


    if (women == "" && q2 == "q2a" && q3 == "q3b" && q4 == "q4a" && q5 == "q5a" && q6 == "q6d")
      alert ("Oily Skin");
    else
      alert ("Jawab la");
  //display results

   return false;

}

if (oily1 == "" && oily2 == "" && oily3 == "" && oily4 == "")
{
  alert ("Oily Skin");
  return false;
}
else
{
  alert ("Skin");
}
else if (dry1 == "" && dry2 == "" && dry3 == "" && dry4 == "")
{
  alert ("Dry Skin");
  return false;
}
else if (nor1 == "" && nor2 == "" && nor3 == "" && nor4 == "")
{
  alert ("Normal Skin");
  return false;
}
else if (sen1 == "" && sen2 == "" && sen3 == "" && sen4 == "")
{
  alert ("Sensitive Skin");
  return false;
}
else if (com1 == "" && com2 == "" && com3 == "" && com4 == "")
{
  alert ("Combination Skin");
  return false;
}
