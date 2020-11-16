import pandas as pd
import numpy as np
import csv

class System(object):
    def __init__(self,name=None,Number_Monomers=None,Number_Moles=None):
        if name!=None:
            self.name=name
        else:
            print("ERROR::Please set the name for the system")
        if Number_Monomers!=None:
            self.Number_Monomers=Number_Monomers
        if Number_Moles!=None:
            self.Number_Moles=Number_Moles


        # mass for atoms
        self.mass={"C":12.011000,'H':1.008000}

    