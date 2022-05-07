# Laravel Redis

Redis facade. Make redis key value expire.

In lavavel, set a redis value which will expire in 5 seconds.

    Redis::set('somekey', 'somevalue', 'EX', 5);
    
In laravel, set a redis value which will expire in 100 milliseconds.

    Redis::set('somekey', 'somevalue', 'PX', 100);
    
Set a value if it does not exist. use NX to tell redis to set the key only if it does not already exist.

    Redis::set('somekey', 'somevalue', 'PX', 100, 'NX');
    
## Other Redis::set options
 
EX seconds -- Set the specified expire time, in seconds.

PX milliseconds -- Set the specified expire time, in milliseconds.

EXAT timestamp-seconds -- Set the specified Unix time at which the key will expire, in seconds.

PXAT timestamp-milliseconds -- Set the specified Unix time at which the key will expire, in milliseconds.

NX -- Only set the key if it does not already exist.

XX -- Only set the key if it already exist.

KEEPTTL -- Retain the time to live associated with the key.

GET -- Return the old string stored at key, or nil if key did not exist. An error is returned and SET aborted if the value stored at key is not a string.
