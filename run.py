import config
import os
from lib.plotter import Plot

plotter = Plot()
#p.__wsdl__(config.res+"/test.wsdl")
wsdls=[]
for _file in os.listdir(config.res+"/wsdl"):
    wsdls.append(config.res+"wsdl/"+_file)

# first draw all wsdls
for wsdl in [ wsdls[0],wsdls[1],wsdls[2]]:
    print wsdl
    plotter.__wsdl__(wsdl)

for wsdl1 in [ wsdls[0],wsdls[1],wsdls[2]]:
    for wsdl2 in [ wsdls[0],wsdls[1],wsdls[2]]:
        plotter.wsdl_connect(wsdl1,wsdl2)

#for wsdl1 in wsdls:
#    for wsdl2 in wsdls:
#        if wsdl1!=wsdl2:
#            plotter.wsdl_connect(wsdl1,wsdl2)
plotter.show()
