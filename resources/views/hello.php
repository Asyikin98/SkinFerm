<?php

if(isset($_POST['edit_btn']))
{
  $id = $_POST['edit_id'];
  //echo $id;
  $query = "SELECT * FROM users WHERE id='$id' ";
  $connection = mysqli_connect("localhost","root","","testing");
  $query_run = mysqli_query($connection, $query);
  //echo "kau ke";
  //readfile("http://localhost/fyp/fyp/public/adminedit");
}


 ?>
