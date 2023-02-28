# Find Log Files and Rotate them

Searches through sub directories looking for log files
and uses logrotate to rotate them.

    #!/bin/bash

    # Set the path to search for log directories
    LOG_PATH="/path/to/logs"

    # Loop through each directory in the log path
    find "$LOG_PATH" -type d | while read DIR; do
        # Check if the directory contains a 'logs' subdirectory
        if [ -d "$DIR/logs" ]; then
            # If the 'logs' subdirectory exists, check if it contains access.log
            if [ -f "$DIR/logs/access.log" ]; then
                # If access.log exists, check if the access_logrotate.conf file exists
                if [ ! -f "$DIR/logs/access_logrotate.conf" ]; then
                    # If the access_logrotate.conf file doesn't exist, create it with default options
                    echo "$DIR/logs/access.log {
        daily
        rotate 14
        compress
        delaycompress
        missingok
        notifempty
        create 0644 user group
    }" > "$DIR/logs/access_logrotate.conf"
                fi
                # Rotate the access.log file using logrotate
                logrotate -s "$DIR/logs/access_logrotate.state" -f "$DIR/logs/access_logrotate.conf" "$DIR/logs/access.log"
            fi
            # Check if the 'logs' subdirectory contains error.log
            if [ -f "$DIR/logs/error.log" ]; then
                # If error.log exists, check if the error_logrotate.conf file exists
                if [ ! -f "$DIR/logs/error_logrotate.conf" ]; then
                    # If the error_logrotate.conf file doesn't exist, create it with default options
                    echo "$DIR/logs/error.log {
        daily
        rotate 14
        compress
        delaycompress
        missingok
        notifempty
        create 0644 user group
    }" > "$DIR/logs/error_logrotate.conf"
                fi
                # Rotate the error.log file using logrotate
                logrotate -s "$DIR/logs/error_logrotate.state" -f "$DIR/logs/error_logrotate.conf" "$DIR/logs/error.log"
            fi
        fi
    done
