#!/bin/env/python

import os

try:
    from contextlib import suppress
except ImportError:
    from contextlib import contextmanager
    @contextmanager
    def suppress(*exceptions):
        try:
            yield
        except exceptions:
            pass

from distutils.sysconfig import get_python_lib
from subprocess import call


if __name__ == '__main__':
    # chdir to the site-packages directory so the report lists relative paths
    dot_coverage_path = os.path.join(os.getcwd(), '.coverage')
    os.chdir(get_python_lib())
    with suppress(OSError):
        os.remove('.coverage')
    os.symlink(dot_coverage_path, '.coverage')

    # create a report from the coverage data
    if 'TRAVIS' in os.environ:
        rc = call('coveralls')
        # don't fail test if coveralls submission failed
        raise SystemExit(None)
    else:
        rc = call(['coverage', 'report'])
        raise SystemExit(rc)
