<?php

require("dbc.php");

function getUserData($id){
  $q = mysql_query("SELECT * FROM 'users' WHERE 'id'=".$id);
  while($r = mysql_fetch_assoc($q))
  {
    $array['id'] = $r['id'];
    $array['name'] = $r['name'];
    $array['password'] = $r['password'];
    $array['remember_token'] = $r['remember_token'];
    $array['created_at'] = $r['created_at'];
    $array['updated_at'] = $r['updated_at'];
    $array['email'] = $r['email'];
  }

  return $array;
}



 ?>
