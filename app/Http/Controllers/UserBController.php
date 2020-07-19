<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\UserB;

class UserBController extends Controller
{
    public function create()
    {
      return view('admin.create');
    }

    public function store(Request $request)
    {
      $this->validate($request, [
        'name'  =>  'required',
        'email' =>  'required',
        'password'  =>  'required'
      ]);
      $admin = new Admin([
        'name'  =>  '$request->get('name')',
        'email' =>  '$request->get('email')',
        'password'  =>  '$request->get('password')'
      ]);
      $admin->save();
      return redirect()->route('admin.create')->with('success',
        'Data Added');
    }
}
