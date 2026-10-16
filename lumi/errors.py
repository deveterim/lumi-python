from typing import Optional

class LumiError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None, error_type: Optional[str] = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_type = error_type

class AuthenticationError(LumiError):
    pass

class InvalidRequestError(LumiError):
    pass

class RateLimitError(LumiError):
    pass

class InternalServerError(LumiError):
    pass
