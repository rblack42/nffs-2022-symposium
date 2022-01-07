import pint
u = pint.UnitRegistry()

class StdAtmosphere(object):

    def __init__(self):

        pass

    def density(self, elevation):
        return (elevation / 10) * u.ounce/u.ft**3

