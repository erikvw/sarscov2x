|pypi| |travis| |codecov| |downloads|


sarscov2x
=========

This is a sample application for use in a talk on how to configure your python project to use TravisCI.

Installing the sample application
---------------------------------

If you want, you can install the Django app. To do so, follow the steps below.

Install conda, check the docs for your OS::

    https://docs.conda.io/en/latest/miniconda.html

After the installation, create an environment using ``conda``::

    conda create -n edc python=3.8

Activate your new environment::

    conda activate edc

Clone this repo into a folder, for example, ``projects``::

    mkdir ~/projects
    cd  ~/projects
    git clone https://github.com/erikvw/sarscov2x.git

Navigate into the repo and install the requirements::

    cd ~/projects/sarscov2x
    pip install -U -r requirements.txt

This is a simple Django application so::

    python manage.py migrate
    python manage.py createsuperuser

Start up the test webserver::

    python manage.py runserver

Open your browser and navigate to::

    http://localhost:8000


References::

    https://docs.travis-ci.com/user/tutorial/

    https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github

.. |pypi| image:: https://img.shields.io/pypi/v/sarscov2x.svg
    :target: https://pypi.python.org/pypi/sarscov2x
    
.. |travis| image:: https://travis-ci.com/erikvw/sarscov2x.svg?branch=develop
    :target: https://travis-ci.com/erikvw/sarscov2x
    
.. |codecov| image:: https://codecov.io/gh/erikvw/sarscov2x/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/erikvw/sarscov2x

.. |downloads| image:: https://pepy.tech/badge/sarscov2x
   :target: https://pepy.tech/project/sarscov2x
