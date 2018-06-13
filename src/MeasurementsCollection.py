from src.request.Request import Request


class MeasurementsCollection(object):
    """
    Represents single collection of data grabbed from all monitors in one time
    """

    def __init__(self, monitors, authToken):
        """
        Initializes a collection

        :param monitors: list of known monitor url addresses
        :param authToken: authorization token
        :type monitors: list
        :type authToken: str
        """
        self.monitors = monitors
        self.authToken = authToken
        self.request = Request()

    def loadFromSingleMonitor(self, measurements, monitorUrl, authToken):
        """
        Loads last measurements from single monitor

        :param measurements: all measurements given until now
        :param monitorUrl: url of the monitor
        :param authToken: authorization token
        :type measurements: dict
        :type monitorUrl: str
        :type authToken: str
        :return: returns all measurements including given from this one monitor
        :rtype: dict
        """
        for measurement in self.request.getMeasurements(monitorUrl, authToken):
            metricId = measurement['metric_id']
            if metricId not in measurements:
                measurements[metricId] = []
            measurements[metricId].append(
                [monitorUrl,
                 measurement['hostname'],
                 measurement['data'][-1]['value']]
            )
        return measurements

    def get(self):
        """
        Loads last measurements from all known monitors
        :return: returns
        :rtype: dict
        """
        measurements = {}
        for monitorUrl in self.monitors:
            measurements = self.loadFromSingleMonitor(
                measurements,
                monitorUrl,
                self.authToken
            )
        return measurements
