import unittest
import sys

from PyQt4.Qt import *

from orangecontrib.crystal.diffraction.DiffractionSetupSweeps import DiffractionSetupSweeps
from orangecontrib.crystal.diffraction.Diffraction import Diffraction
from orangecontrib.crystal.diffraction.GeometryType import BraggDiffraction
from orangecontrib.crystal.widgets.diffraction.PlotViewer1D import PlotViewer1D


@unittest.skip("Blocking QT test")
class PlotViewer1DTest(unittest.TestCase):
    def testPlotViewer(self):
        appl = QApplication(sys.argv)
        ow = PlotViewer1D()
        ow.show()
        diffraction_setup = DiffractionSetupSweeps(BraggDiffraction(),
                                             "Si",
                                             thickness=0.0100 * 1e-2,
                                             miller_h=1,
                                             miller_k=1,
                                             miller_l=1,
                                             asymmetry_angle=3,
                                             energy=10000,
                                             angle_deviation_min= -100.0e-6,
                                             angle_deviation_max=100e-6,
                                             angle_deviation_points=50)

        diffraction = Diffraction()
        res = diffraction.calculateDiffraction(diffraction_setup)

        plot_data_1d = res.asPlotData1D()
        ow.setPlots(plot_data_1d)
        appl.exec_()