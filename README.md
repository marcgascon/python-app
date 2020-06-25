# python-app

- [Description](#desc)
- [Usage](#usage)
- [Software Requirements](#swreq)
- [Why this solution?](#whysol)

<a name="desc"></a>
## Description
A simple HTTP reverse proxy made with nginx serving a python API

<a name="usage"></a>
## Usage
1. Download this github repository.
2. Make sure you have docker and docker-compose installed and build the project:<br>
```
docker-compose build
```
3. Run the app<br>
```
docker-compose up -d
```
4. Now it's time to test that it's working:<br>
```
$ curl -L http://127.0.0.1/hello
{"hello": "world"}

$ curl -L http://127.0.0.1/test
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```
5. Finally, don't forget to stop the running containers:
```
docker-compose down --remove-orphans
```

<a name="swreq"></a>
## Software Requirements
The software requirements for running this application are:
* Docker
* docker-compose cli

<a name="whysol"></a>
## Why this solution?
To do this project I used docker and docker-compose because:
* Docker images are immutable, so if you test something locally then you can be sure that you will run the same in production with a proper deployment.
* Docker and docker-compose can be run in any OS, so it's easier for other people to continue developing it without issues on the environment setup.
* docker-compose provides you the ability of linking containers easily.
