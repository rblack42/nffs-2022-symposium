import pint
u = pint.UnitRegistry()


class Rubber(object):

    def __init__(self):
        self.k_m = 30000 * u.inch

    def get_registry(self):
        return u

    def E(self, weight):
        return weight * self.k_m


