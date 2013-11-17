from lib.wsdl import Wsdl
import config
import os
for file in os.listdir(config.res+"/wsdl"):
    wsdl=Wsdl(config.res+"/wsdl/"+file)
    print wsdl.operation
    exit()