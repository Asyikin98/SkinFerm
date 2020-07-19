<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Question</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet">

        <!-- Styles -->
        <style>
            html, body {
                background-image: url('{{asset("../public/8.jpg")}}');
                background-size: 1350px 630px;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
                //background-color: #fff;
                color: black;
                font-family: Georgia, serif;
                //font-style: italic;
                font-weight: 100;
                height: 100vh;
                margin: 0;
            }

            p{
              border-style: solid;
              border-width: medium;
              border-color: white;
              background-color: white;
              padding: 0 15px;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                text-align: center;
                font-size: 24px;
            }

            .title {
                font-size: 54px;
            }

            .links > a {
                color: #636b6f;
                padding: 0 25px;
                font-size: 13px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
            }

            /*.m-b-md {
                margin-bottom: 30px;
            }*/

            .button {
              background-color: #F0E68C; /* Green */
              border: none;
              color: black;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 18px;
              margin: 4px 2px;
              cursor: pointer;
            }
            .button2 {background-color: #F0E68C;} /* Blue */

            .cc-selector input{
              margin:0;padding:0;
              -webkit-appearance:none;
              -moz-appearance:none;
              appearance:none;
            }
            .man{background-image:url('{{asset("../public/9.png")}}');}
            .women{background-image:url('{{asset("../public/10.png")}}');}

            .cc-selector input:active +.drinkcard-cc{opacity: .15;}
            .cc-selector input:checked +.drinkcard-cc{
              -webkit-filter: none;
              -moz-filter: none;
              filter: grayscale(100%);
            }
            .drinkcard-cc{
              cursor:pointer;
              background-size:contain;
              background-repeat:no-repeat;
              display:inline-block;
              width:100px;height:70px;
              -webkit-transition: all 100ms ease-in;
              -moz-transition: all 100ms ease-in;
              transition: all 100ms ease-in;
                -webkit-filter: brightness(1.8) grayscale(0) opacity(.7);
                -moz-filter: brightness(1.8) grayscale(0) opacity(.7);
                filter: brightness(1.1) grayscale(0) opacity(.8);
              }
              .drinkcard-cc:hover{
                -webkit-filter: brightness(1.2) grayscale(.5) opacity(.9);
                -moz-filter: brightness(1.2) grayscale(.5) opacity(.9);
                filter: brightness(1.2) grayscale(.5) opacity(.9);
              }

              .cssradio input [type="radio"]{display: none; background: #fafafa; padding: 0 15px;}
              .cssradio label {
                padding: 10px;
                margin: 15px 10px 0 0;
                background: #800000;
                border-radius: 3px;
                display: inline-block;
                color: white;
                font-size: 19px;
                font-family: sans-serif;
                cursor: pointer;
              }
              .cssradio input:checked + label{
                background: #f08080;
                font-weight: bold;

              }

              a {
                  text-decoration: none;
                  display: inline-block;
                  padding: 8px 16px;
                }

              a:hover {
                background-color: #fff68f;
                color: black;
              }

              .next {
                      background-color: #20b2aa;
                      color: white;
                    }

                    .round {
                      border-radius: 80%;
                    }

        </style>
    </head>
    <body>
        <div class="flex-center position-ref full-height">
            <div class="content">
                <p class="title m-b-md">
                    Let's Start
                </p>

                <form action="/action_page.php">

                  <p>Your Gender: </p>
                  <div class="cc-selector">
                    <input type="radio" id="man" name="gender" value="man">
                    <label class="drinkcard-cc man" for="man"></label>
                    <input type="radio"  id="women" name="gender" value="women">
                    <label class="drinkcard-cc women"for="women"></label>
                  </div>

                  <p>How Old are You? </p>
                  <div class="cssradio">
                    <input type="radio" id="radio1" name="age" value="18">
                    <label for="radio1"> Under 18 </label>
                    <input type="radio" id="radio2" name="age"  value="24">
                    <label for="radio2"> 18-24 </label>
                    <input type="radio" id="radio3"  name="age" value="34">
                    <label for="radio3"> 25-34 </label>
                    <input type="radio" id="radio4" name="age" value="44">
                    <label for="radio4"> 35-44 </label>
                    <input type="radio" id="radio5" name="age" value="54">
                    <label for="radio5"> 45-54 </label>
                    <input type="radio" id="radio6" name="age" value="55">
                    <label for="radio6"> 55+ </label>

                  <p> When I woke up in the morning. My skin feels.. </p>
                    <input type="radio" id="radio7" name="feel">
                    <label for="radio7"> Dry & Tight </label>
                    <input type="radio" id="radio8" name="feel">
                    <label for="radio8"> Oily </label>
                    <input type="radio" id="radio9" name="feel">
                    <label for="radio9"> Oily in some spot, dry in other </label>
                    <input type="radio" id="radio10" name="feel">
                    <label for="radio10"> Good </label>
                  </div>

                  <hr/>

                  <a href="http://localhost/fyp/fyp/public/secQ" class="next round">&#8250;</a>
                </form>



            </div>
        </div>

    </body>
</html>
