Clone a project and move to it:

    $ git clone https://github.com/Kouff/4bill.git
    $ cd 4bill
    $ git checkout with_docker
Build and run docker container:

    $ docker-compose up -d --build
    
Urls:
* http://127.0.0.1:8000/request/<amount> - where **amount** is some integer.

Stop docker container:

    $ docker-compose down