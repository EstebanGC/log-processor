from .base_validator import BaseValidator
from events.log_event import LogEvent
from events.subclasses import ProductViewEvent, AddToCartEvent

class NotNullValidator(BaseValidator):
    critical_fields = {"user_id", "event_type", "timestamp"}

    def _check(self, event: LogEvent):
        missing = [f for f in self.critical_fields if getattr(event, f) in (None, "")]
        return (not missing, f"Null fields: {missing}" if missing else "OK")


class EventTypeValidator(BaseValidator):
    allowed = {"product_view", "add_to_cart"}

    def _check(self, event: LogEvent):
        if event.event_type not in self.allowed:
            return False, f"Not supported type event: {event.event_type}"
        return True, "OK"


class ProductDetailsValidator(BaseValidator):
    def _check(self, event: LogEvent):
        if isinstance(event, (ProductViewEvent, AddToCartEvent)):
            if not getattr(event, "product_id"):
                return False, "product_id faltante o inválido"
        return True, "OK"