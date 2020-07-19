<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Welcome To MUKA</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet">

        <!-- Styles -->
        <style>
            html, body {
                background-image: url('{{asset("../public/2.jpg")}}');
                background-size: auto;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
                //background-color: #fff;
                color: #800000;
                font-family: Georgia, serif;
                font-style: italic;
                font-weight: 100;
                height: 100vh;
                margin: 0;
            }

            p{
              border-style: solid;
              border-width: medium;
              border-color: white;
              background-color: white;
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
            }

            .title {
                font-size: 74px;
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

        </style>
    </head>
    <body>
        <div class="flex-center position-ref full-height">
            <div class="content">
                <p class="title m-b-md">
                    Welcome to MUKA
                </p>
                <button class="button" onclick="window.location='http://localhost/fyp/fyp/public/quiz'">Let's Quiz</button>
                <button class="button button2" onclick="window.location='http://localhost/fyp/fyp/public/main'">Log In</button>
            </div>
        </div>

    </body>
</html>
