<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
Auth::routes();

Route::group(['middleware' => ['auth','admin']], function () {

  Route::get('/role-fetchuser','Admin\FetchController@fetch');
});

Route::get('/', function () {
    return view('welcome');
});

Route::resource('admin', 'UserBController');
//Route::get('/first', function () {
    //return view ('first');
//});

// for new Welcome
Route::get('/welcome', function () {
    return view('welcome');
});


//for login
//Route::get('/main','MainController@index');
//Route::post('/main/checklogin', 'MainController@checklogin');
//Route::get('main/successlogin','MainController@successlogin');
//Route::get('main/logout','MainController@logout');

//for button redirect to the next page
//Route::get('/main')


//for quizzes
Route::get('/quiz', function () {
    return view ('quiz');
});
Route::get('/firstQ', function () {
    return view ('firstQ');
});
Route::get('/secQ', function () {
    return view ('secQ');
});
Route::get('/MUKA', function () {
    return view ('MUKA');
});

Route::view('adminuser','adminuser');
Route::post('adminuser','ListController@list');

//Route::view('adminedit','adminedit');
//Route::post('adminedit','UpdateController@update');

//Route::view('/adminuser','adminuser');
//Route::post('adminuser','UpdateController@update');

//Route::view('adminupdate','adminupdate');
//Route::post('adminupdate','UpdateController@update');

//register
Route::post('/store', "UserController@store");
Route::post('/keeps', "AdminController@keeps");
Route::post('/list', "ListController@list");
Route::post('/update', "UpdateController@update");
//Route::view('/register','register');
Route::view('/registration','registration');

//userProfile
Route::get('/userProfile', function () {
    return view ('userProfile');
});

//for login
Route::view('/login','login');
Route::post('/logs', "UserController@logs");

//for admin login
Route::view('/adminedit','adminedit');
Route::post('/keeps', "AdminController@keeps");

Route::view('/adminuser','adminuser');
Route::post('/list', "ListController@list");

Route::resource('adminuser', 'UpdateController')->names([
    'update' => 'adminuser.update',
    // ...
]);

Route::view('/list','list');
Route::post('/update', "UpdateController@update");

Route::get('/hello', function () {
    return view ('hello');
});

//question.blade.php
Route::get('/question', function () {
    return view ('question');
});

//skintype
Route::get('/skintype', function () {
    return view ('skintype');
});

Route::get('/rb', function () {
    return view('rb');
});

Route::get('/testing', function () {
    return view('testing');
});

//dashboard userProfile
Route::get('/dashboard', function () {
    return view('dashboard');
});

//dashboard admin
Route::get('/admindashboard', function () {
    return view('admindashboard');
});

Route::get('/register', function () {
    return view('register');
});

Route::get('/adminuser', function () {
    return view('adminuser');
});

Route::get('/adminedit', function () {
    return view('adminedit');
});

Route::get('/admintips', function () {
    return view('admintips');
});

Route::get('/usertips', function () {
    return view('usertips');
});

Route::get('adminskintype', function () {
    return view('adminskintype');
});

Route::get('adminskincare', function () {
    return view('adminskincare');
});

Route::get('adminroutine', function () {
    return view('adminroutine');
});

Route::get('adminoily', function () {
    return view('adminoily');
});

Route::get('adminoilyroutine', function () {
    return view('adminoilyroutine');
});

Route::get('adminnorroutine', function () {
    return view('adminnorroutine');
});

Route::get('adminnorroutinen', function () {
    return view('adminnorroutinen');
});

Route::get('adminoilycleanser', function () {
    return view('adminoilycleanser');
});

Route::get('admindry', function () {
    return view('admindry');
});

//skincareCategory
Route::get('/oilyskincareCategory', function () {
    return view('oilyskincareCategory');
});

Route::get('/dryskincareCategory', function () {
    return view('dryskincareCategory');
});

Route::get('/senskincareCategory', function () {
    return view('senskincareCategory');
});

Route::get('/norskincareCategory', function () {
    return view('norskincareCategory');
});

Route::get('/comskincareCategory', function () {
    return view('comskincareCategory');
});

Route::get('/skincareroutine', function () {
    return view('skincareroutine');
});

Route::get('/comcleanserd', function () {
    return view('comcleanserd');
});

Route::get('/cleanser', function () {
    return view('cleanser');
});

Route::get('/drycleanser', function () {
    return view('drycleanser');
});

Route::get('/dryroutine', function () {
    return view('dryroutine');
});

Route::get('/dryroutinen', function () {
    return view('dryroutinen');
});

Route::get('/sencleanser', function () {
    return view('sencleanser');
});

Route::get('/norcleanser', function () {
    return view('norcleanser');
});

Route::get('/comcleanser', function () {
    return view('comcleanser');
});

Route::get('/oilytoner', function () {
    return view('oilytoner');
});

Route::get('/drytoner', function () {
    return view('drytoner');
});

Route::get('/sentoner', function () {
    return view('sentoner');
});

Route::get('/nortoner', function () {
    return view('nortoner');
});

Route::get('/comtoner', function () {
    return view('comtoner');
});

Route::get('/comtonerd', function () {
    return view('comtonerd');
});

Route::get('/oilymoist', function () {
    return view('oilymoist');
});

Route::get('/drymoist', function () {
    return view('drymoist');
});

Route::get('/senmoist', function () {
    return view('senmoist');
});

Route::get('/normoist', function () {
    return view('normoist');
});

Route::get('/commoist', function () {
    return view('commoist');
});

Route::get('/commoistd', function () {
    return view('commoistd');
});

Route::get('/oilymask', function () {
    return view('oilymask');
});

Route::get('/drymask', function () {
    return view('drymask');
});

Route::get('/senmask', function () {
    return view('senmask');
});

Route::get('/normask', function () {
    return view('normask');
});

Route::get('/commask', function () {
    return view('commask');
});

Route::get('/commaskd', function () {
    return view('commaskd');
});

Route::get('/oilyex', function () {
    return view('oilyex');
});

Route::get('/dryex', function () {
    return view('dryex');
});

Route::get('/senex', function () {
    return view('senex');
});

Route::get('/norex', function () {
    return view('norex');
});

Route::get('/comex', function () {
    return view('comex');
});

Route::get('/comexd', function () {
    return view('comexd');
});

Route::get('/oilysun', function () {
    return view('oilysun');
});

Route::get('/drysun', function () {
    return view('drysun');
});

Route::get('/sensun', function () {
    return view('sensun');
});

Route::get('/norsun', function () {
    return view('norsun');
});

Route::get('/comsun', function () {
    return view('comsun');
});

Route::get('/comsund', function () {
    return view('comsund');
});

Route::get('/oilyeye', function () {
    return view('oilyeye');
});

Route::get('/dryeye', function () {
    return view('dryeye');
});

Route::get('/seneye', function () {
    return view('seneye');
});

Route::get('/noreye', function () {
    return view('noreye');
});

Route::get('/comeye', function () {
    return view('comeye');
});

Route::get('/comeyed', function () {
    return view('comeyed');
});

Route::get('/oilyeyeD', function () {
    return view('oilyeyeD');
});

Route::get('/oilyeyeD1', function () {
    return view('oilyeyeD1');
});
//Route::get('/main','MainController@index');
//for login

//Route::view('/login','login');
//Route::post('/logs', "UserController@logs");

Route::get('/skin2', function () {
    return view('skin2');
});
