# dev-things
Links to dev things of interest

## GIT pub/priv keys

Tell GIT which keys to use.

```
export GIT_SSH_COMMAND="ssh -i ~/.ssh/KEY_FILE_GOES_HERE -F /dev/null" git clone REPO
```
After the clone has happened, you can set the command in git config

In .git/config, add the following to the \[core\] section:
```
   sshCommand = ssh -i ~/.ssh/KEY_FILE_GOES_HERE -F /dev/null
```

## PHP Helper Functions

https://github.com/ryantxr/php-helper

Some utility functions for PHP.

## Admin LTE

https://adminlte.io Admin theme with lots of features

https://github.com/jeroennoten/Laravel-AdminLTE Laravel installable

## Laravel Eloquent Join

Adds join capabilities to Eloquent models.

https://github.com/fico7489/laravel-eloquent-join

## Tumblr API

https://www.tumblr.com/docs/en/api/v2

## Bootstrap-Vue

https://bootstrap-vue.js.org/

## Carbon

https://carbon.nesbot.com

Date and time class for PHP.

## PHP PSR

https://www.php-fig.org

## ION Icons

https://ionicons.com/

## HTTP Statuses

https://httpstatuses.com

## Laravel API Auth
https://github.com/erjanmx/laravel-api-auth

Dead simple auth for APIs.

## Phone Number Handling
https://github.com/giggsey/libphonenumber-for-php

A PHP library for parsing, formatting, storing and validating international phone numbers. This library is based on Google's libphonenumber.

## MailHog

https://github.com/mailhog/MailHog

SMTP testing

## Bandwidth

https://dev.bandwidth.com

Send SMS

## Alpha Vantage

https://www.alphavantage.co

Stock quotes API

