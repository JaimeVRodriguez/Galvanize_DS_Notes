## Docker

### Run a New Container
Start new Container from an Image
`docker run IMAGE`
`docker run nginx`

... and assign it a name
`docker run --name CONTAINER IMAGE`
`docker run --name web nginx`

... and map a port
`docker run -p HOSTPORT:CONTAINERPORT IMAGE`
`docker run -p 8080:80 nginx`

... and start container in back


#### Tips
"Interactice Terminal"
`-it`  or  `-i -t`
`docker run --name <name> -it -d <container> bin/bash`

Execute
`docker exec -it <name> bash`

Leave Container
`exit`

Ports
Computer : Container
`-p 8888:8888` 

Volume
Computer directory :Container
`-v <directory>:/home`

Run Example
```docker
docker run --name pgserv -d \
-p 5432:5432 \
-v "$PWD":/home/data \
-e POSTGRES_PASSWORD='galvanize' \
skylarenglish/galvanize:galv_db
```

Execute to access postgres
```docker
docker exec -it pgserv psql -U postgres
```

List Databases
	`-l` or `--list`

Connect to Postgres SQL Databases
`-c` or `--connect`

