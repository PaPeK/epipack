# -*- coding: utf-8 -*-
"""
Build, simulate, and analyze any polynomial epidemiological model.
"""

from .metadata import *

from .deterministic_epi_models import (
        DeterministicEpiModel,
        DeterministicSIModel,
        DeterministicSISModel,
        DeterministicSIRModel,
        DeterministicSIRSModel,
        DeterministicSEIRModel,
        DeterministicSEIRSModel,
        DeterministicSEIRXModel,
        DeterministicSIRXModel,
        )

from .stochastic_epi_models import (
        StochasticEpiModel,
        StochasticSIRModel,
        StochasticSISModel,
        )

from .symbolic_epi_models import (
        SymbolicEpiModel,
        )

from .network_models import (
        get_2D_lattice_links,
        )
