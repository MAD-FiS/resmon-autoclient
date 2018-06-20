import getpass
from time import sleep
from src.Config import Config
from src.request.Request import Request
from src.request.ResponseError import ResponseError
from src.MeasurementsCollection import MeasurementsCollection
from src.View import View


class Client(object):
    """
    Client which offers basic methods of the application
    """
    def __init__(self, configFile, limit, register):
        """
        Initializes client with a given parameters

        :param configFile:
        :param limit:
        :param register:
        :type configFile: str
        :type limit: int
        :type register: bool
        """
        self.userData = {
            'username': None,
            'password': None
        }
        try:
            self.config = Config(configFile)
            self.request = Request()
            self.collection = None
            self.view = View(limit)
            self.registerMode = register
        except OSError:
            filename = configFile
            print(f"InitError: Configuration file {filename} can\'t be found!")
            exit(1)

    def loadUserData(self):
        """
        Loads username and password from keyboard when it's typed by user

        :return: returns None
        """
        try:
            self.userData['username'] = input('username: ')
            self.userData['password'] = getpass.getpass('password: ')
        except KeyboardInterrupt:
            print()
            print("You broke execution of ResMon client manually")
            exit(0)

    def login(self):
        """
        Provides functionality of log in on JWT authorization server

        :return: returns login response parsed as JSON
        """
        print("Please type your username and password "
              "to be logged on authorization server")
        self.loadUserData()
        return self.request.login(
            self.config.get('auth'),
            self.userData['username'],
            self.userData['password']
        )

    def register(self):
        """
        Provides functionality of registration on JWT authorization server

        :return: returns registration response parsed as JSON
        """
        print("Please type new username and password "
              "to be registered on authorization server")
        self.loadUserData()
        password2 = getpass.getpass('retype password: ')
        if self.userData['password'] != password2:
            print("Error: You didn't enter the same passwords. "
                  "Please try it again.")
            exit(0)
        return self.request.register(
            self.config.get('auth'),
            self.userData['username'],
            self.userData['password']
        )

    def displayLoop(self):
        """
        Displays online results in a neverending loop

        :return: returns None
        """
        if self.collection is None:
            print("You didn't prepare measurement collection")
            exit(1)
        try:
            while True:
                try:
                    measurements = self.collection.get()
                    self.view.display(measurements)
                    sleep(1)
                except ResponseError as error:
                    print("LoadDataError: " + str(error))
        except KeyboardInterrupt:
            print()
            print("ResMon client has been closed successfully")
            pass

    def run(self):
        """
        Runs the client

        :return: returns None
        """
        loginResult = {}
        try:
            if self.registerMode:
                loginResult = self.register()
            else:
                loginResult = self.login()
        except ResponseError as error:
            print("AuthError: "+str(error)+". Please try to log in again.")
            exit(1)
        authToken = loginResult['access_token']
        self.collection = MeasurementsCollection(
            self.config.get('monitors'),
            authToken
        )

        self.displayLoop()
        exit(0)
