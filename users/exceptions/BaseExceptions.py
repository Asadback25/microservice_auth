


class BaseAppException(Exception):
    status_code = 400
    default_message = "Application error"
    default_code = "error"

    def __init__(self, message=None, code=None):
        self.message = message or self.default_message
        self.code = code or self.default_code
        super().__init__(self.message)

    def to_dict(self):
        return {
            "error": {
                "message": self.message,
                "code": self.code
            }
        }