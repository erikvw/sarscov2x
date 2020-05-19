|pypi| |travis| |codecov| 

sarscov2x
=========

This is a sample ``Django`` application for use in a talk on how to configure your python project to use TravisCI. The production Django app for this simple Coronavirus KAP tool (Knowledge, Attitudes, and Practice) is available at sarscov2_. The tool is currently being administered in Tanzania.

Installing the sample ``Django`` application
--------------------------------------------

If you want, you can install the Django app. When installed you can easily inspect the ``.travis.yml`` and ``tox.ini`` and perhaps run the tests locally. 

To do so, follow the steps below to create a python environment, install the dependencies, prepare the Django apps DB, create a user account, and loads a local test web server.

First, set up a python environment.

I use miniconda_ to build and manage my python environments. You will need to install miniconda_ so go to the the miniconda_ docs and select the installer for your OS.

After the installing miniconda_, open a terminal and create a new python environment using the ``conda`` command::

    conda create -n edc python=3.8

Your new python env is named "edc" and runs python 3.8.

Next, activate your new environment::

    conda activate edc

Next, clone the repo into a folder, for example, ``projects``::

    mkdir ~/projects
    cd  ~/projects
    git clone https://github.com/erikvw/sarscov2x.git

Navigate into the repo and install the requirements::

    cd ~/projects/sarscov2x
    pip install -U -r requirements.txt

This is a simple Django application that uses ``sqlite`` as the DB. To create the database::

    python manage.py migrate
    
Next, create your user account::

    # run and follow the prompts
    python manage.py createsuperuser

Next, start up the test webserver::

    python manage.py runserver

Lastly, open your browser and navigate to::

    http://localhost:8000

PEP8, tests, tox and TravisCI, code coverage
--------------------------------------------

TravisCI is just part of what can be used to simplify checking your code (flake8), running all your tests against multiple environments (tox and travis) while finally checking that your test coverage is still where you want it to be.

Together with TravisCI
++++++++++++++++++++++
* tox_ (pip install tox)
* flake8 (pip install flake8)
* others (black_, gitflow_, coverage_, codecov_)

Integration with GitHub
+++++++++++++++++++++++

https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github

Configuration
+++++++++++++

The config files involved:

* ``.travis.yml``: read by TravisCI. Sets up OS, environment, pre-test commands, tests, post-test commands
* ``tox.ini``: easy way to run your tests in a fresh environment locallay and to run a matrix of environments remotely on TravisCI
* ``setup.cfg``: specify ``flake8`` config. ``Flake8`` (PEP8 rules) is good to run before your tests. Less important if you use a formatter like ``black``.

The flow is:

* --> ``git push`` to GitHub repo
* --> repo change triggers TravisCI
* --> on TravisCI all tests pass (you hope)
* --> TravisCI hands over to CodeCov

And if all goes well, your badges turn green!


References::

    https://docs.travis-ci.com/user/tutorial/

    https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github
    
    https://docs.travis-ci.com/user/job-lifecycle/

.. |pypi| image:: https://img.shields.io/pypi/v/sarscov2x.svg
    :target: https://pypi.python.org/pypi/sarscov2x
    
.. |travis| image:: https://travis-ci.com/erikvw/sarscov2x.svg?branch=develop
    :target: https://travis-ci.com/erikvw/sarscov2x
    
.. |codecov| image:: https://codecov.io/gh/erikvw/sarscov2x/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/erikvw/sarscov2x

.. _miniconda: https://docs.conda.io/en/latest/miniconda.html

.. _tox: https://tox.readthedocs.io/en/latest/

.. _black: https://black.readthedocs.io/en/stable/

.. _gitflow: https://nvie.com/posts/a-successful-git-branching-model/

.. _coverage: https://coverage.readthedocs.io/en/coverage-5.1/

.. _codecov: https://codecov.io

.. _sarscov2: https://github.com/erikvw/sarscov2

