-----------------------------------
# Local setup

### Install poetry (package manager)
### Download [poetry](https://link):
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`


### Setup path
To get started you need Poetry's bin directory ($HOME/.poetry/bin) in your `PATH` environment variable. Next time you log in this will be done automatically. Add entry in PATH variable in `~/.bash_rc` file.


### Apply changes to current terminal

`source $HOME/.poetry/env`

`source ~/.bashrc`


### Install project dependencies:
`poetry install`

### Run app using this command:    
`AUTHENTICATION=jwt DATABASE_URL=localhost POSTGRES_USER=postgres POSTGRES_PASSWORD=dbuser@123 uvicorn main:app --reload`

### Access app using url:   
  [ http://localhost:8000/](http://localhost:8000/)


-----------------------------------
# Build Docker Image

### Using Dockerfile
   `docker build -t python-fastapi .`

### Using Docker Compose
   `docker-compose build`


### Access app using url:   
  [ http://localhost:8001/](http://localhost:8001/)


-----------------------------------
# Create/Run app as docker container
### Run with docker command:
   `docker run -d --name python-fastapi-c -p 8001:80 -e AUTHENTICATION=jwt -e DATABASE_URL=localhost -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=dbuser@123 python-fastapi`
#### Access app using url:   
  [ http://localhost:8001/](http://localhost:8001/)


### Run with docker-compose - local:  
`docker-compose -d up`

### Run with docker-compose - qa:  
`docker-compose -d -f docker-compose-qa.yml up --build`

### Run with docker-compose - prod:  
`docker-compose -d -f docker-compose-prod.yml up --build`

#### Access app using url:   
  [ http://localhost:8002/](http://localhost:8002/)


-----------------------------------
# Verify
### To check the docker container status:    
`docker ps`

### Accessing logs
`docker logs -f python-fastapi`   
(or)   
`docker logs -f {container_name}` 