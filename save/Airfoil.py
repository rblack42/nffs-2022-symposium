import json
from .curve import Curve
class Airfoil(object):

    def __init__(self):
        self.airfoil = 'circular-arc-3%'
        self.data_dir = '../data'

    def show_curve(self, type):
        fn = '{}/{}-{}.json'.format(
            self.data_dir,
            self.airfoil, type)
        with open(fn,'r') as fin:
            curve_data = json.load(fin)
            for l in curve_data['datasetColl'][0]['data']:
                print(l['value'])


if __name__ == '__main__':
    a = Airfoil()
    a.show_curve('Cl')
