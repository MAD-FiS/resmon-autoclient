import os
import tabulate


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
            outputMeasurements[metricId] = measurement
        return outputMeasurements

    def display(self, measurements):
        """
        Displays measurements from one moment

        :param measurements: Measurements ready to be displayed
        :type measurements: dict
        :return: returns None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Host list")
        print('---------------------------------')
        print()
        for (metricId, measurement) in self.prepare(measurements).items():
            print(tabulate.tabulate(
                measurement[:self.limit],
                headers=['Monitor', 'Host', metricId]
            ))
            print()
