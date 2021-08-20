# Apache2 Setup to use php-fpm

    <VirtualHost *:443>
        ServerName      example.com
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/sites/foo/webapp/app/webroot
        <Directory "/var/www/sites/foo/webapp/app/webroot">
                Options Indexes FollowSymLinks MultiViews
                AllowOverride All
                Order allow,deny
                Allow from all
                require all granted
        </Directory>
        <FilesMatch "\.php$">
             SetHandler "proxy:unix:/run/php/php7.4-fpm.sock|fcgi://localhost/"
        </FilesMatch>

        ErrorLog /var/www/sites/foo/logs/error.log
        CustomLog /var/www/sites/foo/logs/access.log combined
    </VirtualHost>
