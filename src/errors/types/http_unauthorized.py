class HttpUnauthorizedError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unautorized"
        self.status_code = 401
