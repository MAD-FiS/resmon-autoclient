import requests
from src.request.ResponseError import ResponseError


class Request:
    """
    Request offers all needed requests to both authorization server and monitor
    """
    def __init__(self):
        self.lastRequest = None

    def getResponse(self):
        """
        Abstract response analyzer. \
        It detects positive or negative result of request

        :return: returns response parsed as JSON if HTTP code is equal to 201
        """
        jsonData = self.lastRequest.json()
        if self.lastRequest.status_code != 201:
            raise ResponseError(
                self.lastRequest.status_code, jsonData['message']
            )
        else:
            return jsonData

    def login(self, serverUrl, username, password):
        """
        Method to get authorization token from JWT server

        :param serverUrl: Url of JWT authorization server
        :param username: Name of user who wants to be logged
        :param password: Password of user who wants to be logged
        :type serverUrl: str
        :type username: str
        :type password: str
        :return: returns response parsed as JSON (fields: message, auth_token)
        """
        self.lastRequest = requests.post(
            'http://' + serverUrl + '/login',
            json={'username': username, 'password': password}
        )
        return self.getResponse()

    def register(self, serverUrl, username, password):
        """
        Method to retister in JWT server

        :param serverUrl: Url of JWT authorization server
        :param username: Name of user who wants to be logged
        :param password: Password of user who wants to be logged
        :type serverUrl: str
        :type username: str
        :type password: str
        :return: returns response parsed as JSON (fields: message, auth_token)
        """
        self.lastRequest = requests.post(
            'http://' + serverUrl + '/registration',
            json={'username': username, 'password': password}
        )
        return self.getResponse()

    def getMeasurements(self, monitorUrl, authToken):
        """
        Method to get measurements from single monitor

        :param monitorUrl: Url of single monitor \
        from where are served measurements
        :param authToken: Authorization token given from JWT server
        :type monitorUrl: str
        :type authToken: str
        :return: returns response parsed as JSON
        """
        self.lastRequest = requests.get(
            'http://' + monitorUrl + '/measurements',
            headers={'Authorization': 'Bearer ' + authToken}
        )
        if self.lastRequest.status_code != 200:
            raise ResponseError(
                self.lastRequest.status_code,
                "You can't fetch data from monitor: "+monitorUrl
            )
        return self.lastRequest.json()
