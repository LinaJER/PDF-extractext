from fastapi import HTTPException, status


class AppException(HTTPException):
    def __init__(
        self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    ):
        self.message = message
        super().__init__(status_code=status_code, detail=message)


class NotFoundException(AppException):
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            message=f"{resource} not found", status_code=status.HTTP_404_NOT_FOUND
        )


class ValidationException(AppException):
    def __init__(self, message: str):
        super().__init__(message=message, status_code=status.HTTP_400_BAD_REQUEST)
