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

    def loadFromSingleMonitor(self, measurements, monitorUrl, rawMeasurements):
        """
        Loads last measurements from single monitor

        :param measurements: all measurements given until now
        :param monitorUrl: url of the monitor
        :param rawMeasurements: raw measurements from monitor
        :type measurements: dict
        :type monitorUrl: str
        :type rawMeasurements: dict
        :return: returns all measurements including given from this one monitor
        :rtype: dict
        """
        for measurement in rawMeasurements:
            if not self._checkKeyError('metric_id', measurement) \
                    or not self._checkKeyError('hostname', measurement) \
                    or not self._checkKeyError('data', measurement):
                continue
            if not self._checkDataField(measurement):
                continue
            metricId = measurement['metric_id']
            if metricId not in measurements:
                measurements[metricId] = []
            measurements[metricId].append(
                [monitorUrl,
                 measurement['hostname'],
                 measurement['data'][-1]['value']]
            )
        return measurements

    def _checkKeyError(self, keyName, measurement):
        if 'hostname' not in measurement.keys():
            print(f'Warning: Entry doesn\'t have key \'{keyName}\'')
            return False
        else:
            return True

    def _checkDataField(self, measurement):
        if len(measurement['data']) < 1:
            print(
                'Warning: Data section in your entry doesn\'t have any value'
            )
            return False
        else:
            return True

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
                self.request.getMeasurements(monitorUrl, self.authToken)
            )
        return measurements
