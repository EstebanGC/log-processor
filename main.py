from datetime import datetime, timezone
from events.factory import EventFactory
from validators.validations import NotNullValidator, EventTypeValidator, ProductDetailsValidator

#Validators chain
validator_chain = NotNullValidator(
    EventTypeValidator(
        ProductDetailsValidator()
    )
)

#Eventos de prueba
raw_events = [
    #válido
    {
        "user_id": 1, "event_type": "product_view",
        "product_id": 101, "product_name": "Camisa Negra",
        "timestamp": datetime.now(timezone.utc).isoformat()
    },
    #falta product_id
    {
        "user_id": 2, "event_type": "add_to_cart",
        "quantity": 2, "price": 19.99,
        "timestamp": datetime.now(timezone.utc).isoformat()
    },
    #tipo desconocido
    {
        "user_id": 3, "event_type": "checkout",
        "timestamp": datetime.now(timezone.utc).isoformat()
    },
    #válido
    {
        "user_id": 4, "event_type": "add_to_cart",
        "product_id": 202, "quantity": 1, "price": 5.0,
        "timestamp": datetime.now(timezone.utc).isoformat()
    },
]


for idx, raw in enumerate(raw_events, start=1):
    evt = EventFactory.build(raw)
    valid, reason = validator_chain.validate(evt)
    tag = "Válido" if valid else "Inválido"
    print(f"[{idx}] {tag} – {reason}")
    if valid:
        print("     →", evt.to_dict())