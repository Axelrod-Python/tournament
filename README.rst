.. image:: https://badge.waffle.io/Axelrod-Python/Axelrod.svg?label=ready&title=Ready
    :target: https://waffle.io/Axelrod-Python/Axelrod


.. image:: https://coveralls.io/repos/Axelrod-Python/Axelrod/badge.svg
    :target: https://coveralls.io/r/Axelrod-Python/Axelrod

.. image:: https://img.shields.io/pypi/v/Axelrod.svg
    :target: https://pypi.python.org/pypi/Axelrod

.. image:: https://travis-ci.org/Axelrod-Python/Axelrod.svg?branch=packaging
    :target: https://travis-ci.org/Axelrod-Python/Axelrod

|Join the chat at https://gitter.im/Axelrod-Python/Axelrod|

Results
=======

This repository contains Python code that reproduces the
tournament. To run the tournament, you simply need to:

::

    $ python run_axelrod

This automatically outputs a ``svg`` file with the results. You can see
the results from the latest run of the tournament here:

.. figure:: http://axelrod-python.github.io/tournament/assets/strategies_boxplot.svg
   :alt:

You can see the results from the latest run of the tournament here with
the cheating strategies (which manipulate/read what the opponent does):

.. figure:: http://axelrod-python.github.io/tournament/assets/all_strategies_boxplot.svg
   :alt:

Also the pairwise performance of each strategy versus all others:

.. figure:: http://axelrod-python.github.io/tournament/assets/strategies_payoff.svg
   :alt:

Please do contribute :)

Note that you can run ``python run_axelrod -h`` for further
options available: for example, cheating strategies can be excluded for
faster results by running:

::

    $ python run_axelrod --xc --xa

You can also run the tournament in parallel (below will run 4 parallel
processes):

::

    $ python run_axelrod -p 4

You can run with all available CPUs with:

::

    $ python run_axelrod -p 0

To re run the full set of results and output them to the `assets` directory
simply run::

    $ ./update_results.sh 0 100  # Runs with all CPUS and 100 repetitions

**Note that this uses the installed version of the axelrod library.**
If you want to keep things tidy you can create a virtualenv and install the
latest version of the library like so::

    $ virtualenv env
    $ source env/bin/activate
    $ pip install git+https://github.com/Axelrod-Python/Axelrod@master

If you have the Axelrod repository locally you can also run::

    $ pip install path_to_axelrod

If you have already installed :code:`axelrod` you can add the `-U` tag to update
to the latest version of master::

    $ pip install git+https://github.com/Axelrod-Python/Axelrod@master -U

or::

    $ pip install path_to_axelrod  -U
