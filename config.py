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

# Keywords to search
KEYWORD_LIST = ["galaxy formation", "satellite galaxy", "Milky Way", "simulation", "tidal disruption", "small-scale structure", "dwarf galaxy"]
# Keywords to exclude
KEYWORD_EX_LIST = ["interstellar medium", "molecular cloud", "AGN", "standard candle", "X-ray binar", "solar corona", "Instrumentation"]
# Note that the 'Keywords' above are actually searched in the abstract instead of the real keyword section. 
