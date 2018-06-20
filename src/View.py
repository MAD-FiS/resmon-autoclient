import os
import tabulate
from colorama import Fore, Back, Style

class View(object):
    """
    Represents display layer of this application. \
    It determines how results can be displayed.
    """
    def __init__(self, limit=10):
        """
        Initialize display view

        :param limit: limit of displayed records
        :type limit: int
        """
        self.limit = limit

    def prepare(self, rawMeasurements):
        """
        Prepares given measurements to be good for displaying them
        :param rawMeasurements:
        :type rawMeasurements: dict
        :return: returns prepared measurements data
        :rtype: dict
        """
        outputMeasurements = {}
        for (metricId, measurement) in rawMeasurements.items():
            measurement.sort(key=lambda m: m[-1])
            measurement.reverse()
            measurement = measurement[:self.limit]
            outputMeasurements[metricId] = measurement
        return outputMeasurements

    def display(self, measurements):
        """
        Displays measurements from one moment

        :param measurements: Measurements ready to be displayed
        :type measurements: dict
        :return: returns None
        """
        self._clearScreen()
        print("Host list")
        print('---------------------------------')
        print()
        sortedMeasurements = sorted(self.prepare(measurements).items())
        for (metricId, measurement) in sortedMeasurements:
            print(tabulate.tabulate(
                measurement,
                headers=['Monitor', 'Host', Style.BRIGHT+Back.RED+Fore.CYAN+metricId+Style.RESET_ALL]
            ))
            print()
    def _clearScreen(self):
        if os.name in ('nt', 'dos'):
            os.system("cls")
        elif os.name in ('linux', 'osx', 'posix'):
            os.system("clear")
        else:
            print("\n") * 120