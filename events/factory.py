from .log_event import LogEvent
from .product_view import ProductViewEvent
from .subclasses import AddToCartEvent
from datetime import datetime
from typing import Any, Dict

#Funcion EventFactory: procesa los datos que recibe y los convierte a la forma correcta de ProductViewEvent y AddToCartEvent
class EventFactory:

    @staticmethod
    def build(raw: Dict[str, Any]) -> LogEvent:
        #Devolviendo la instancia correcta de los datos a ProductViewEvent y AddToCartEvent
        if isinstance(raw.get("timestamp"), str):
            raw["timestamp"] = datetime.fromisoformat(raw["timestamp"])

        etype = raw.get("event_type")
        common_kw = {
            "user_id": raw.get("user_id"),
            "timestamp": raw.get("timestamp"),
            "raw": raw,
        }

        if etype == "product_view":
            return ProductViewEvent(
                product_id=raw.get("product_id"),
                product_name=raw.get("product_name", ""),
                **common_kw
            )
        elif etype == "add_to_cart":
            return AddToCartEvent(
                product_id=raw.get("product_id"),
                quantity=raw.get("quantity", 1),
                price=raw.get("price", 0.0),
                **common_kw
            )
        #LogEvent por defecto
        return LogEvent(event_type=etype or "unknown", **common_kw)