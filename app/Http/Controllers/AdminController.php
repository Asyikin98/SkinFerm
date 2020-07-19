<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\URL;
use Illuminate\Support\Facades\DB;
session_start();

class AdminController extends Controller
{
    public function keeps(request $request)
    {

      //session_start();
      $name=$request->input('name');
      $password=$request->input('password');
      $data= DB::select('select id from admin where name=? and password =?' ,[$name,$password]);

      if(count($data))
      {
        //echo '<a href="http://localhost/fyp/fyp/public/quiz">Let Quizm</a>';
        readfile("http://localhost/fyp/fyp/public/admindashboard");
        //header("Location: http://localhost/fyp/fyp/public/quiz");
        //$_SESSION("userid")=$name;
        //readfile("http://localhost/fyp/fyp/public/dashboard");
        exit();
      }
      else
      {
        echo "Error";
      }

    }





}
?>
