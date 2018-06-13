import unittest

from src.View import *


class TestGeneral(unittest.TestCase):
    def test_loadFromSingleMonitorTest(self):
        x = View(2)
        monitor = '0.0.0.0'
        measurements = x.prepare(
            {'CPU_USAGE': [[monitor, 'workstation1', 2],
                           [monitor, 'workstation2', 3],
                           [monitor, 'workstation3', 1]]})
        self.assertEqual(measurements,
            {'CPU_USAGE': [[monitor, 'workstation2', 3],
                           [monitor, 'workstation1', 2]]})


if __name__ == '__main__':
    unittest.main()
