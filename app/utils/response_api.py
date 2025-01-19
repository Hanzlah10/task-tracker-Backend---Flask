class apiResponse():
    def __init__(self, status_code, message, data):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.success = True if status_code <= 200 else False


        