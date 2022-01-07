import json
import yaml
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class Curves(object):

    def __init__(self, datadir='../data'):
        cwd = os.getcwd()
        self.datapath = os.path.join(cwd,datadir)
        if not os.path.isdir(self.datapath):
            print("Bad data dir, exiting...")
            sys.exit(1)

    def load_data(self, dtype, name):
        """top level data load routine"""
        if dtype == 'airfoil':
            self.load_airfoil(name)
        elif dtype == 'model':
            self.load_model(name)
        else:
            print("bad load type, exiting...")
            sys.exit(1)

    def get_WAD_points(self, data):
        """extract curve points fro WAD data"""
        points = data['datasetColl'][0]['data']
        x = []
        y = []
        for p in points:
            x.append(p['value'][0])
            y.append(p['value'][1])
        return x,y

    def get_yaml_points(self,data):
        """extract CL,CD data points"""
        points = data['data']
        x = []
        y = []

        for p in points:
            x.append(p[0])
            y.append(p[1])
        return x,y

    def load_json_file(self,name):
        """read a JSON data file"""
        if os.path.isfile(name):
            try:
                with open(name,'r') as fin:
                    data = json.load(fin)
            except:
                return None
            return data
        return None

    def load_yaml_file(self,name):
        """load a YML data file"""
        if os.path.isfile(name):
            try:
                with open(name,'r') as fin:
                    data = yaml.safe_load(fin)
            except:
                return None
            return data
        return None

    def fit_curve(self,xd,yd):
        """Return a curve fit function using spline interpolation"""
        xi = np.array(xd)
        yi = np.array(yd)
        x = np.linspace(-6, 20, 50)
        order = 1
        s = interpolate.InterpolatedUnivariateSpline(xi, yi, k=order)
        return s


    def load_airfoil(self, name):
        print("loading airfoil", name)
        froot = os.path.join(self.datapath, 'airfoils', name)
        froot = os.path.abspath(froot)
        if not os.path.isdir(froot):
            print("Airfoil not installed", name)
            return

        # load Cl data
        yname = os.path.join(froot, 'CL.yml')
        jname = os.path.join(froot,'CL.json')
        if os.path.isfile(yname):
            CL = self.load_yaml_file(yname)
            x_cl, y_cl = self.get_yaml_points(CL)
            CLfit = self.fit_curve(x_cl, y_cl)
            print(CLfit(20))
        elif os.path.isfile(jname):
            CL = self.load_json_file(jname)
            x_cl, y_cl = self.get_WAD_points(CL)
            CLfit = self.fit_curve(x_cl, y_cl)
            print(CLfit(20))
        else:
            print("CL data file not found")
            return

        # load CD data
        yname = os.path.join(froot,'CD.yml')
        jname = os.path.join(froot,'CD.json')
        if os.path.isfile(yname):
            CD = self.load_yaml_file(yname)
            x_cd, y_cd = self.get_yaml_points(CD)
            CDfit = self.fit_curve(x_cd, y_cd)
            print(CDfit(20))

            print(CD)
        elif os.path.isfile(jname):
            CD = self.load_json_file(jname)
            x_cd, y_cd = self.get_WAD_points(CD)
            CDfit = self.fit_curve(x_cd, y_cd)
            print(CDfit(20))
        else:
            CD = None


    def load_model(self, name):
        print("loading model:", name)
        froot = os.path.join(self.datapath, 'models')
        froot = os.path.abspath(froot)

        # check for yml data
        yname = os.path.join(froot, name + '.yml')
        jname = os.path.join(froot,name + '.json')
        if os.path.isfile(yname):
            with open(yname,'r') as fin:
                data = yaml.safe_load(fin)
            print(data)
        elif os.path.isfile(jname):
            fname = froot + '/' + name + '.json'
            with open(fname,'r') as fin:
                data = json.load(fin)
                Mdata = data['data']
            print(Mdata)
        else:
            print("model not installed:", name)
            pass




if __name__ == '__main__':
    c = Curves()
    c.load_data('airfoil','circular-arc-3%')
    c.load_data('model','hodson-wart')
    c.load_data('airfoil','mcbride-b7')
    c.load_data('model','erbach-basic')


