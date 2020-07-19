<?php

use Illuminate\Database\Seeder;
use App\User;
use Illuminate\Support\Str;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
      DB::table('users')->delete();
        //
        $users = array(
          array(
            'name'          => 'Nurul Asyikin',
            'email'         => '98asyikin@gmail.com',
            'password'      =>  Hash::make('password'),
            'remember_token'=> Str::random(12),
          )
        );

        DB::table('users')->insert($users);

    }
}
