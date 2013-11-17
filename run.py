import config
import os
from lib.plotter import Plot
from lib.wsdl import Wsdl
plotter = Plot()
#p.__wsdl__(config.res+"/test.wsdl")
wsdls=[]
id=1
#for _file in os.listdir(config.res+"/wsdl"):
#    wsdls.append(Wsdl(config.res+"wsdl/"+_file))
#for _file in [config.res+"wsdl/BookAuthor.wsdl",config.res+"wsdl/author_bookprice_service.wsdl"]:
for _file in os.listdir(config.res+"/wsdl"):
    wsdls.append(Wsdl(config.res+"wsdl/"+_file,id))
    id+=1

# first draw all wsdls
for wsdl in wsdls:
    plotter.__wsdl__(wsdl)

for wsdl1 in wsdls:
    for wsdl2 in wsdls:
        plotter.wsdl_connect(wsdl1,wsdl2)

#for wsdl1 in wsdls:
#    for wsdl2 in wsdls:
#        if wsdl1!=wsdl2:
#            plotter.wsdl_connect(wsdl1,wsdl2)
plotter.show()
