import argparse
from src.Client import Client


class Application(object):
    """
    Main application class. It parses parameters and run client
    """
    version = '1.0'

    def __init__(self):
        """
        In constructor program arguments are parsed and client is prepared
        """
        arguments = self.parseArgs()
        self.client = Client(
            configFile=arguments.config,
            limit=arguments.limit,
            register=arguments.register
        )

    def parseArgs(self):
        """
        Parses all parameters given to the application during running it

        :return: returns data of all parsed parameters
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-c',
            '--config',
            type=str,
            default='config.json',
            help='Location where is stored JSON configuration file'
        )
        parser.add_argument(
            '-l',
            '--limit',
            type=int,
            default=10,
            help='Maximal limit of displayed hosts for every metric'
        )
        parser.add_argument(
            '--register',
            action='store_true',
            help='If it\'s set, then user can be registered \
            at start of the application. \
            In other case user has to be logged before using this.'
        )
        parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=('ResMon client '+Application.version)
        )
        return parser.parse_args()

    def run(self):
        """
        Client is started

        :return: returns None
        """
        self.client.run()
