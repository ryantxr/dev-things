# PHP Project Things

Add these tools and configuration to all PHP projects.

    composer require --dev "phpstan/phpstan=*"
    composer require --dev "squizlabs/php_codesniffer=*"
    composer require --dev phpunit/phpunit ^9.5

## What are these things?

PHPStan is a static analyzer and it identifies potential code problems.
Run it and fix what it complains about.

PHP Code sniffer enforces a particular coding style.
The coding style it enforces is specific to 3iT/RMT

Infection is a mutator tool that attempts to determine the quality of unit tests.
It works by injecting errors into the code to see if a unit test will detect the error.

## Where do I put these files?

Put files in the same folder/directory where composer.json lives.

## Composer json file

Assuming that source code is located in "src" add this to composer.json

```json
    "scripts": {
        "phpcs": "phpcs src",
        "phpcbf": "phpcbf",
        "phpstan": "phpstan analyze src -c phpstan.neon --level=3 --no-progress -vv --memory-limit=-1",
        "phpunit": "phpunit",
        "phpdbg": "phpdbg -qrr vendor/bin/infection",
        "infection": "XDEBUG_MODE=coverage infection --min-msi=50 --min-covered-msi=50 --log-verbosity=all",
        "coverage": "XDEBUG_MODE=coverage phpunit --coverage-text --coverage-html ./var/coverage/html --coverage-clover ./var/coverage/clover.xml",
        "ci:pack": [
            "@phpcs", "@phpstan", "@phpunit", "@infection", "@coverage"
        ]
    },
```

## infection.json

Create a file named `infection.json` and put this content into it.

```json
{
    "timeout": 1,
    "source": {
        "directories": [
            "src"
        ]
    },
    "logs": {
        "text": "var/infection/text.log",
        "summary": "var/infection/summary.log",
        "debug": "var/infection/debug.log",
        "perMutator": "var/infection/perMutator.md",
        "stryker": {
            "badge": "main"
        }
    },
    "mutators": {
        "@default": true
    }
}
```

## .gitignore

Add the following to `.gitignore`.

    .phpunit.result.cache

## Finally

You can run these scripts from composer like this:

    composer phpcs
    
    composer phpstan
    
    composer phpunit
    
    composer infection
