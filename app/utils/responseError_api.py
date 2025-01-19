class apiError(Exception):
    def __init__(self, status_code, message = "Something went wrong",errors = [],stack = ""):
        super.__init__(message)
        self.status_code = status_code
        self.message = message
        self.errors = errors
        self.data = None
        self.stack = stack
        self.success = False