class InvalidCountError(Exception):
    def __int__(self, message):
        super().__init__(message)
        super().__init__(message)   # super().__init__("3자리숫자가 아닙니다.")