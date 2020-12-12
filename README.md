Clone a project and move to it:

    $ git clone https://github.com/Kouff/4bill.git
    $ cd 4bill
Create a [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip) and [activate](https://virtualenv.pypa.io/en/latest/user_guide.html#activators) it or skip this point.

Install the requirements:
    
    $ pip install -r requirements.txt
Run server:

    $ uvicorn main:app
or (Gunicorn doesn't work on windows)

    $ gunicorn -k uvicorn.workers.UvicornWorker main:app