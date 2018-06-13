class ResponseError(RuntimeError):
    """
    Represents HTTP error which occurs \
    during doing requests to external servers
    """
    def __init__(self, code, message):
        """
        Initializes response error

        :param code: HTTP error code
        :param message: Message returned by external server
        :type code: int
        :type message: str
        """
        self.code = code
        self.message = message

    def __str__(self):
        """
        Converts this error to string

        :return: returns string representation of this error
        :rtype: str
        """
        return self.message
