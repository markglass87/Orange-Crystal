"""
Class to plot arbitrary matrix given as numpy array.
"""

from orangecontrib.crystal.util.PlotGeneratorSetting import PlotGeneratorSetting
from orangecontrib.crystal.util.PlotGenerator import PlotGenerator
from orangecontrib.crystal.util.PlotData1D import PlotData1D


class NumpyPlotGenerator(PlotGenerator):
    def __init__(self, numpy_array, column_names):
        super(NumpyPlotGenerator, self).__init__()

        if len(numpy_array.shape) != 2:
            raise Exception("Only matrices are supported (2D numpy array)")
            
        self._array = numpy_array
        self._column_names = column_names

    def _defaultSettings(self):
        default_settings = list()

        default_settings.append(PlotGeneratorSetting("Axis X", "Axis X", self._column_names, self._column_names[0]))
        default_settings.append(PlotGeneratorSetting("Axis Y", "Axis Y", self._column_names, self._column_names[-1]))

        return default_settings

    def _plots(self):
        column_name_x = self._settingByName("Axis X").value()
        index_x = self._column_names.index(column_name_x)

        column_name_y = self._settingByName("Axis Y").value()
        index_y = self._column_names.index(column_name_y)

        plot = PlotData1D("%s %s" % (column_name_x, column_name_y),
                          column_name_x,
                          column_name_y)
        plot.setX(self._array[:,index_x])
        plot.setY(self._array[:,index_y])

        return [plot]