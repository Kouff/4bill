# Web-Limiter

Task here -> https://drive.google.com/file/d/14fkG-ESH2XZsJmA2diORvmc6KIlrE4qM/view

Web framework: Starlette.

The repository has branches:
* master (without docker)
* with_docker (this code but in docker container)
* with_docker_and_redis (this code but in docker container and using redis instead of dict from python)

Clone a project and move to it:

    $ git clone https://github.com/Kouff/Web-Limiter.git
    $ cd 4bill
Create a [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip) and [activate](https://virtualenv.pypa.io/en/latest/user_guide.html#activators) it or skip this point.

Install the requirements:
    
    $ pip install -r requirements.txt
Run server:

    $ uvicorn main:app
or (Gunicorn doesn't work on windows)

    $ gunicorn -k uvicorn.workers.UvicornWorker main:app
    
Urls:
* http://127.0.0.1:8000/request/<amount> - where **amount** is some integer.
