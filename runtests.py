#!/usr/bin/env python
import os
import django
import logging
import sys

from django.test.runner import DiscoverRunner

def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'coronavirus.settings'
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failfast = True if [t for t in sys.argv if t == "--failfast"] else False
    failures = DiscoverRunner(failfast=failfast, tags=tags).run_tests(
        ["coronavirus.tests"]
    )
    sys.exit(bool(failures))


if __name__ == "__main__":
    logging.basicConfig()
    main()
