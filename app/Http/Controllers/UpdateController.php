<?php
namespace App\Http\Controllers;
session_start();
use Illuminate\Http\Request;

class UpdateController extends Controller
{
  function update(Request $req)
  {

    if(isset($_POST[updatebtn]))
    {
      $id = $_POST['edit_id'];
      $name = $_POST['edit_name'];
      $email = $_POST['edit_email'];
      $password = $_POST['edit_password'];

      $query = "UPDATE users SET name='$name', email='$email', password='$password' WHERE id='$id' ";
      $connection = mysqli_connect("localhost","root","","testing");
      $query_run = mysqli_query($connection, $query);

      if($query_run)
      {
        $_SESSION['success'] = "Your Data is Updated";
        header('Location: adminuser');
      }
      else
      {
        $_SESSION['status'] = "Your Data is NOT Updated";
        header('Location: adminuser');
      }
    }
  }
}
?>
