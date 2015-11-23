Topical
=======

Topical is a publish/subscribe based messaging system organised around topics.

Users may subscribe and unsubscribe to messages in a topic and post messages to
any topic (even those they are not subscribed to). They can also request to
receive any messages from a topic in order to read them. Once a user has 
received a message they will not receive it again.

Setup
=====

To run Topical, you will need Python 3 and the virtualenv tool.
To initialise the virtual environment and run topical:

    $ virtualenv --python=python3 venv
    $ . venv/bin/activate
    $ python3 setup.py develop
    $ topical

By default topical will run on port 8080, you can use the --port option
to change it if you already have software running on port 8080.

Disclaimer - this works on Ubuntu 15.10 but should also work on any other
environment with python3 and virtualenv available

Testing
=======

After activating the virtual environment, tests can be run with:

    $ python3 setup.py nosetests

This will run unit and acceptance tests and generate coverage reports
