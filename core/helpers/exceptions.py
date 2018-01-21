class TimeoutReachedException(Exception):
    def __init__(self, seconds):
        super().__init__()
        self._seconds = seconds

    @property
    def seconds(self):
        return self._seconds

    def __str__(self):
        return ('Timeout reached after {}s,\
                unable to connect to resource'.format(self.seconds))
