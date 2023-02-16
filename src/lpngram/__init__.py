# __init__.py

"""
lpngram __init__.py
"""

# Version of the lpngram package
__version__ = "0.2"  # sync with setup.py
__author__ = "Tiago Tresoldi"
__email__ = "tiago.tresoldi@lingfil.uu.se"

# Build the namespace
from lpngram.ngrams import NgramModel

from lpngram.ngrams import (
    bigrams,
    fourgrams,
    get_all_ngrams,
    get_all_ngrams_by_order,
    get_all_posngrams,
    get_n_ngrams,
    get_posngrams,
    get_skipngrams,
    trigrams,
)

from lpngram.smoothing import (
    certaintydegree_dist,
    ele_dist,
    laplace_dist,
    lidstone_dist,
    mle_dist,
    random_dist,
    sgt_dist,
    smooth_dist,
    uniform_dist,
    wittenbell_dist,
)

# TODO: add __all__
