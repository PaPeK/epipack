"""
Provides an API to define deterministic epidemiological models.
"""

import numpy as np 

from epipack import DeterministicEpiModel

class DeterministicSIRXModel(DeterministicEpiModel):
    """
    An SIRX model derived from :class:`epipack.deterministic_epi_models.DeterministicEpiModel`.
    """

    def __init__(self, R0, recovery_rate, quarantine_rate, containment_rate, population_size=1.0):

        infection_rate = R0 * recovery_rate

        DeterministicEpiModel.__init__(self, list("SIRXH"), population_size)

        self.set_quadratic_rates([
                ("S", "I", "S", -infection_rate),
                ("S", "I", "I", +infection_rate),
            ])
        self.add_transition_processes([
                ("S", containment_rate, "H"),
                ("I", recovery_rate, "R"),
                ("I", containment_rate+quarantine_rate, "X"),
            ])

class DeterministicSEIRXModel(DeterministicEpiModel):
    """
    An SEIRX model derived from :class:`epipack.deterministic_epi_models.DeterministicEpiModel`.
    """

    def __init__(self, R0, recovery_rate, symptomatic_rate, quarantine_rate, containment_rate, population_size=1.0):

        infection_rate = R0 * recovery_rate

        DeterministicEpiModel.__init__(self, list("SEIRXH"), population_size)

        self.set_quadratic_rates([
                ("S", "I", "S", -infection_rate),
                ("S", "I", "E", +infection_rate),
            ])
        self.add_transition_processes([
                ("E", symptomatic_rate                ,"I"),
                ("S", containment_rate               ,"H"), 
                ("I", recovery_rate                  ,"R"),
                ("I", containment_rate+quarantine_rate,"X")
            ])

class DeterministicSEIRModel(DeterministicEpiModel):
    """
    An SEIR model derived from :class:`epipack.deterministic_epi_models.DeterministicEpiModel`.
    """

    def __init__(self, R0, recovery_rate, symptomatic_rate, population_size=1.0):

        infection_rate = R0 * recovery_rate

        DeterministicEpiModel.__init__(self, list("SEIR"), population_size)

        self.set_quadratic_rates([
                ("S", "I", "S", -infection_rate),
                ("S", "I", "E", +infection_rate),
            ])
        self.add_transition_processes([
                ("E", symptomatic_rate, "I"),
                ("I", recovery_rate, "R"),
            ])

class DeterministicSEIRSModel(DeterministicEpiModel):
    """
    An SEIRS model derived from :class:`epipack.deterministic_epi_models.DeterministicEpiModel`.
    """

    def __init__(self, R0, recovery_rate, symptomatic_rate, waning_immunity_rate, population_size=1.0):

        infection_rate = R0 * recovery_rate

        DeterministicEpiModel.__init__(self, list("SEIR"), population_size)

        self.set_quadratic_rates([
                ("S", "I", "S", -infection_rate),
                ("S", "I", "E", +infection_rate),
            ])
        self.add_transition_processes([
                ("E", symptomatic_rate     , "I"),
                ("I", recovery_rate        , "R"),
                ("R", waning_immunity_rate , "S"),
            ])


if __name__=="__main__":    # pragma: no cover
    epi = DeterministicEpiModel(list("SEIR"))
    print(epi.compartments)
    print()
    epi.add_transition_processes([
            ("E", 1.0, "I"),
            ("I", 1.0, "R"),
            ])
    print(epi.linear_rates)
    epi.set_quadratic_rates([
            ("S", "I", "S", -1.0),
            ("S", "I", "E", +1.0),
            ])
    print()
    for iM, M in enumerate(epi.quadratic_rates):
        print(epi.get_compartment(iM), M)

