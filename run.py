import config
import os
from lib.plotter import Plot
from lib.wsdl import Wsdl
from lib import similarity

from lib.subPlotter import SubPlotter
plotter = Plot()
#wsdls=[]
#id=1
#for _file in os.listdir(config.res+"/wsdl"):
#     wsdls.append(Wsdl(config.res+"wsdl/"+_file,id))
#     id+=1

## first draw all wsdls
#for wsdl in wsdls:
#     plotter.__wsdl__(wsdl)
#
#for wsdl1 in wsdls:
#     for wsdl2 in wsdls:
#         plotter.wsdl_connect(wsdl1,wsdl2)
#print plotter.input_nodes
#print plotter.output_nodes
#plotter.save_sdg()
#print similarity.Similarity("_BOOK","book").value
plotter.load_sdg()
sub_plotter=SubPlotter(plotter,"book","author")
sub_plotter.show()

#plotter.show()
