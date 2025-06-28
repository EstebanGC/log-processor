from events.log_event import LogEvent
from typing import Optional, Tuple

class BaseValidator:
    def __init__(self, next_validator: Optional["BaseValidator"] = None):
        self._next = next_validator

    def validate(self, event: LogEvent) -> Tuple[bool, str]:
        ok, reason = self._check(event)
        if not ok:
            return False, reason
        if self._next:
            return self._next.validate(event)
        return True, "OK"

    def _check(self, event: LogEvent) -> Tuple[bool, str]:
        raise NotImplementedError