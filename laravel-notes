# Laravel Notes

Notes on installing and setting up Laravel.

## Migrations

Some databases require all tables to have a primary key. 
Therefore, always modify the password_resets migration to include one.

```
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;
use Illuminate\Support\Facades\DB; // <<<<< ---- add this
return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('password_resets', function (Blueprint $table) {
            // This is needed because DigitalOcean requires primary keys for all tables.
            // This command only turns that off for the session while the table 
            // is being created.
            DB::statement('SET SESSION sql_require_primary_key = 0'); // <<<<<< --- add this
            $table->unsignedBigInteger('id')->primary();
            $table->string('email')->index();
            $table->string('token');
            $table->timestamp('created_at')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('password_resets');
    }
};
```
