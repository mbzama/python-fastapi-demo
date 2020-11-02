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




# Build/Run using Docker

### Build docker image with Dockerfile
   `docker build -t python-fastapi .`

### Run app with docker container
   `docker run -d --name python-fastapi-c -p 8001:80 python-fastapi`

### Access app using url:   
  [ http://localhost:8001/](http://localhost:8001/)



# Build/Run using Docker Compose
### Build image using docker-compose file:    
`docker-compose -f docker-compose-qa.yml build`

### Run with local environment:  
`docker-compose -d -f docker-compose-local.yml up --build`

### Run with qa environment:  
`docker-compose -d -f docker-compose-qa.yml up --build`

### Run with prod environment:  
`docker-compose -d -f docker-compose-prod.yml up --build`


### Access app using url:   
  [ http://localhost:8002/](http://localhost:8002/)


# Verify
### To check the docker container status:    
`docker ps`

### Accessing logs
`docker logs -f python-fastapi`   
(or)   
`docker logs -f {container_name}` 