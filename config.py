# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'JeremyZhaoXu'

# The repository to add this issue to
REPO_OWNER = 'JeremyZhaoXu'
REPO_NAME = 'ArXivDaily_GalaxyFormation'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/astro-ph/new'

KEYWORD_LIST = [
    # sims / SAM / trees
    "COLIBRE", "EAGLE", "FLAMINGO", "GALFORM", "semi-analytic",
    "merger tree", "halo finder", "HBT", "hydrodynamical simulation",
    "cosmological simulation", "subgrid", "zoom-in simulation",
    # line 1: high-z descendants
    "descendant", "high-redshift", "high redshift", "z>10", "z > 10",
    "UV-bright", "UV luminosity function",
    # line 2: halo mass definition / HMF / GSMF
    "halo mass function", "halo mass definition", "M_{200", "stellar mass function",
    # line 3: AGN chemical evolution
    "AGN feedback", "chemical evolution", "quenching",
]
KEYWORD_EX_LIST = [
    "exoplanet", "protoplanetary", "brown dwarf", "standard candle",
    "X-ray binar", "solar corona", "planetary system",
]
