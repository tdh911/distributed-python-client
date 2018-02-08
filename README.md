# distributeddb-python-client
This is the front end client for our [DistributedDB project](https://github.com/rthotakura97/decentralized-database).

## Instructions
From the root of the directory you can run
```
python bin/client.py <method> --user <user> --filename <filename> --filepath <filepath> --secret-key <secret-key> --endpoint <endpoint>
```

You can choose between list-all, write, read, or delete. 

--endpoint is always optional, defaults to http://localhost:8080

### list-all
* Used to list all files you have in database
* Only requires --user arg

### read
* Used to read a file
* Requires --user, --secret-key, --filename

### write
* Used to write a file
* Requires --user, --secret-key, --filepath

### delete
* Used to delete a file
* Requires --user, --secret-key, --filename
