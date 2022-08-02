from typing import Any


class BaseFuzzingError(Exception):
    """This exists so that clients can distinguish between exception classes."""


class ConflictingKeys(BaseFuzzingError):
    def __init__(
        self,
        key: str,
        operation_id: str = None,
        *args: Any,
    ) -> None:
        if operation_id:
            return super().__init__(
                f'There are multiple factory registrations for "{operation_id}" in "{key}".',
                *args,
            )

        return super().__init__(
            f'There are multiple factory registrations for "{key}".', *args
        )


class ConflictingHandlers(BaseFuzzingError):
    def __init__(
        self,
        key: str,
        *args: Any,
    ) -> None:
        return super().__init__(
            f'There are multiple handlers registered for "{key}".', *args
        )
