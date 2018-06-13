import unittest

from src.MeasurementsCollection import *


class TestGeneral(unittest.TestCase):
    def test_loadFromSingleMonitorTest(self):
        x = MeasurementsCollection([], '');
        rawMeasurements = [{'metric_id': 'CPU_USAGE', 'hostname': 'workstation1', 'data': [{'value': 1}]},
                           {'metric_id': 'RAM_USAGE', 'hostname': 'workstation1', 'data': [{'value': 100}]},
                           {'metric_id': 'CPU_USAGE', 'hostname': 'workstation2', 'data': [{'value': 2}]}];
        monitor = '0.0.0.0';
        measurements = {};
        measurements = x.loadFromSingleMonitor(measurements, monitor, rawMeasurements)
        self.assertEqual(measurements, {'CPU_USAGE': [[monitor, 'workstation1', 1], [monitor, 'workstation2', 2]],
                                        'RAM_USAGE': [[monitor, 'workstation1', 100]]});

if __name__ == '__main__':
    unittest.main()
