# dev-things
Links to dev things of interest

## TailwindCSS installation
This installation process is for installing TailwindCSS standalone with zero
integration with any framework.
Tailwind is built in its own folder and it producess a css file which can be copied
to whatever site folder.

1. Make a folder for TailwindCSS.
2. Use NPM to install tailwindcss, postcss and autoprefixer.
3. Create tailwind configuration file.
4. Create a base tailwind.css file which will be used to generate the real css file.
5. Create a build script to run the build process
6. Add Tailwind as a PostCSS plugin.


```bash
# (step 1)
mkdir tailwindcss && cd tailwindcss && mkdir -p css
# (step 2)
npm install -D tailwindcss@latest postcss@latest postcss-cli@latest autoprefixer@latest
# (step 3)
npx tailwindcss init
# (step 4)
echo "@tailwind base;" > tailwind.css
echo "@tailwind components;" >> tailwind.css
echo "@tailwind utilities;" >> tailwind.css
# (step 5)
echo "echo building tailwind.css" > build
echo "echo ./node_modules/postcss-cli/bin/postcss tailwind.css -o css/tailwind.css" >> build
echo "./node_modules/postcss-cli/bin/postcss tailwind.css -o css/tailwind.css" >> build
chmod +x build
# (step 6)
echo "module.exports = {" > postcss.config.js
echo "  plugins: {" >> postcss.config.js
echo "    tailwindcss: {}," >> postcss.config.js
echo "    autoprefixer: {}," >> postcss.config.js
echo "  }" >> postcss.config.js
echo "}" >> postcss.config.js
```


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

## TailwindCSS StarterKit
https://www.creative-tim.com/learning-lab/tailwind-starter-kit/presentation open source components for TailwindCss

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

