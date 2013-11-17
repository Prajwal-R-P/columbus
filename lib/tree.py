import config
from lib.wsdl import Wsdl
import os

class Tree():
    def __init__(self):
        for wsdl in os.listdir(config.res+"wsdl/"):
            pass