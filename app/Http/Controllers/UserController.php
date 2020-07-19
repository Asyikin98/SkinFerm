<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\URL;
use Illuminate\Support\Facades\DB;
session_start();

class UserController extends Controller
{
    public function store(request $request)
    {
      //print_r($request->input());
      $name=$request->input('name');
      $email=$request->input('email');
      //$username=$request->input('username');
      $password=$request->input('password');
      DB::insert('insert into users(id,name,email,password) values(?,?,?,?)',[null,$name,$email,$password]);
      echo '<a href="quiz">Go!</a>';
      //header("location:quiz");

    }

    public function logs(request $request)
    {

      //session_start();
      $name=$request->input('name');
      $password=$request->input('password');
      $data= DB::select('select id from users where name=? and password =?' ,[$name,$password]);

      if(count($data))
      {
        header("location:quiz");
        //echo '<a href="http://localhost/fyp/fyp/public/quiz">Let Quizm</a>';
        //readfile("http://localhost/fyp/fyp/public/quiz");
        //header("Location: http://localhost/fyp/fyp/public/quiz");
        //$_SESSION("userid")=$name;
        //readfile("http://localhost/fyp/fyp/public/dashboard");
        exit();
      }
      else
      {
        echo "Please Register first";
      }

    }


}
?>
