Reproducing these results
=========================

To reproduce this results:

- For the smaller tournaments: :code:`./update.sh 100 0`

- For the large tournaments::

    python run_noisy.py  # Creates a data set in the folder data/
    python run_std.py  # Creates a data set in the folder data/
    python run_probend.py  # Creates a data set in the folder data/

    python analyse_noisy.py  # Analyses the corresponding data set
    python analyse_std.py  # Analyses the corresponding data set
    python analyse_probend.py  # Analyses the corresponding data set
