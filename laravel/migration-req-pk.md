# Disable SQL_REQUIRE_PRIMARY_KEY in migrations

Sometimes artisan will generate a migration that adds the primary after making the table.
If SQL_REQUIRE_PRIMARY_KEY is enabled for that database, the migration will fail.
The solution is to check for it and if it is enabled, turn it off.

    <?php

    use Illuminate\Database\Migrations\Migration;
    use Illuminate\Support\Facades\DB;

    class YourCustomMigration extends Migration
    {
        /**
         * Run the migrations.
         *
         * @return void
         */
        public function up()
        {
            // Check if sql_require_primary_key is enabled
            $requirePrimaryKey = DB::select("SHOW GLOBAL VARIABLES LIKE 'sql_require_primary_key'");
            $isRequirePrimaryKeyEnabled = $requirePrimaryKey[0]->Value == 'ON' ? true : false;
    
            // Temporarily disable sql_require_primary_key if it's enabled
            if ($isRequirePrimaryKeyEnabled) {
                DB::statement("SET sql_require_primary_key=OFF");
            }
    
            // Your migration logic here
    
            // Re-enable sql_require_primary_key if it was initially enabled
            if ($isRequirePrimaryKeyEnabled) {
                DB::statement("SET sql_require_primary_key=ON");
            }
        }
    
        /**
         * Reverse the migrations.
         *
         * @return void
         */
        public function down()
        {
            // Your logic here to revert the migration
        }
    }

