import json


class Config(object):
    """
    Represents configuration loaded from a given file
    """
    def __init__(self, path=None):
        """
        Initializes configuration and loaded data from file if path is given

        :param path: path to the configuration file
        :type path: str
        """
        self.config = {}
        if path is not None:
            self.loadFromFile(path)

    def loadFromFile(self, path):
        """
        Loads configuration data from file to which path is given

        :param path: path to the configuration file
        :type path: str
        :return: returns None
        """
        f = open(path, 'r')
        self.config = json.loads(f.read())
        f.close()

    def get(self, name, defaultValue=None):
        """
        Gets configuration value located under the given name

        :param name: Name of configuration value
        :param defaultValue: Default value returned \
        when needed value is undefined
        :type name: str
        :type defaultValue: None
        :return: returns configuration value or None if it's undefined
        """
        if name in self.config:
            return self.config[name]
        else:
            return defaultValue
