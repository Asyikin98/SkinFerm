<!DOCTYPE html>
<html>

	<head>
		<title>Skin Quiz</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<link rel="shortcut icon" href="../public/PurpleAdmin-Free-Admin-Template-master/assets/images/favicon1.ico">

		<link rel="stylesheet" href="../resources/sass/skin.css" type="text/css">
	</head>

	<body>
		<div id="container">
			<header>
				<h1>Skin Quiz</h1>
				<p>Discover your skin type</p>
			</header>
			<section>
				<div id="results"></div>
				<form name="skinQuiz" onsubmit="return submitAnswer()">
					<h3>1. Your Gender? </h3>
					<input type="radio" name="q1"  id="q1a" value="man" >Man<br>
					<input type="radio" name="q1"  id="q1b" value="women">Women<br>

					<h3>2. How old are you? </h3>
					<input name="q2" type="radio" value="Under 20" id="q2a">Under 20<br>
          <input name="q2" type="radio" value="20-30" id="q2b">20-30<br>
          <input name="q2" type="radio" value="31-40" id="q2c">31-40<br>
          <input name="q2" type="radio" value="41++" id="q2d">41++<br>

					<h3>3. When I woke in the morning. My skin feels... </h3>
					<input name="q3" type="radio" value="Dry & Tight" id="drytight">Dry & Tight<br>
          <input name="q3" type="radio" value="Oily already" id="oilyalready">Oily already<br>
          <input name="q3" type="radio" value="Oily in some spot, dry in other" id="somespot">Oily in some spot, dry in other<br>
          <input name="q3" type="radio" value="Good" id="good">Good<br>

					<h3>4. My T-ZOne... </h3>
					<input name="q4" type="radio" value="Oily/Shiny the whole face" id="oilywhole">Oily/Shiny the whole face<br>
          <input name="q4" type="radio" value="Oily/Shiny a part of face" id="oilypart">Oily/Shiny a part of face<br>
          <input name="q4" type="radio" value="Dry the whole face" id="drywhole">Dry the whole face<br>
          <input name="q4" type="radio" value="Dry a part of face" id="drypart">Dry a part of face<br>

					<h3>5. What is your top skin concern? </h3>
					<input name="q5" type="radio" value="Acne" id="acne">Acne<br>
          <input name="q5" type="radio" value="Rashes on skin" id="rashes">Rashes on skin<br>
          <input name="q5" type="radio" value="Dryness/Hydration" id="dryness">Dryness/Hydration<br>
          <input name="q5" type="radio" value="Easily irritated skin" id="irritated">Easily irritated skin<br>
          <input name="q5" type="radio" value="Oil control/Pores" id="pores">Oil control/Pores<br>

					<h3>6. Which best describe your pores? </h3>
					<input name="q6" type="radio" value="Medium Size" id="medium">Medium Size<br>
          <input name="q6" type="radio" value="Large/Medium Size & only visible on T-Zone" id="visible">Large/Medium Size & only visible on T-Zone<br>
          <input name="q6" type="radio" value="Small & Not visible" id="small">Small & Not visible<br>
          <input name="q6" type="radio" value="Large & Visible" id="large">Large & Visible<br>
					<br><br>
					<input type="submit" value="Submit Quiz">
				</form>
			</section>
			<footer>
				<p>Copyright &copy; 2020, All Right Reserved</p>
			</footer>
		</div>
		  <script src="../resources/js/skin.js"></script>
	</body>
</html>
