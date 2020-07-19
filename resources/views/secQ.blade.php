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
                color: black;
                font-family: Georgia, serif;
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
                      color: Black;
                    }


                    .round {
                      border-radius: 80%;
                    }

        </style>
    </head>
    <body>
        <div class="flex-center position-ref full-height">
            <div class="content">

                <form>

                  <p> My T-Zone.. </p>
                  <div class="cssradio">
                    <input type="radio" name="t-zone" id="radio11"/>
                    <label for="radio11"> Oily/Shiny the whole face </label>
                    <input type="radio" name="t-zone" id="radio12"/>
                    <label for="radio12"> Oily/Shiny a part of face </label>
                    <br/>
                    <input type="radio" name="t-zone" id="radio13"/>
                    <label for="radio13"> Dry the whole face </label>
                    <input type="radio" name="t-zone" id="radio14"/>
                    <label for="radio14"> Dry  a part of face </label>

                    <p> What is your top skin concern? </p>
                      <input type="radio" name="concern" id="radio15"/>
                      <label for="radio15"> Acne </label>
                      <input type="radio" name="concern" id="radio16"/>
                      <label for="radio16"> Anti-aging </label>
                      <input type="radio" name="concern" id="radio17"/>
                      <label for="radio17"> Dryness/Hydration </label>
                      <br/>
                      <input type="radio" name="concern" id="radio18"/>
                      <label for="radio18"> Pigmentation </label>
                      <input type="radio" name="concern" id="radio19"/>
                      <label for="radio19"> Oil control/Pores </label>

                    <p> Which best describe your pores? </p>
                      <input type="radio" name="pores" id="radio20"/>
                      <label for="radio20"> Medium Size </label>
                      <input type="radio" name="pores" id="radio21"/>
                      <label for="radio21"> Large/Medium Size & only visible on T-Zone </label>
                      <br/>
                      <input type="radio" name="pores" id="radio22"/>
                      <label for="radio22"> Small & Not Visible </label>
                      <input type="radio" name="pores" id="radio23"/>
                      <label for="radio23"> Large & Visible </label>

                  </div>

                  <hr/>

                  <a href="http://localhost/fyp/fyp/public/MUKA" class="next round">Submit</a>
                </form>



            </div>
        </div>

    </body>
</html>
