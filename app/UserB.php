<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class UserB extends Model
{
    protected $fillable = ['name', 'email', 'password'];
}
