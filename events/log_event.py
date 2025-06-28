from __future__ import annotations
from datetime import datetime
from typing import Any, Dict

#Clase base LogEvent
class LogEvent:
    #Campos: id, tipo de evento, momento exacto del evento
    required_fields = {"user_id", "event_type", "timestamp"}

    def __init__(self, *, user_id: int, event_type: str,
                 timestamp: datetime, raw: Dict[str, Any]):
        self.user_id = user_id
        self.event_type = event_type
        self.timestamp = timestamp
        self.raw = raw                      

    #Validador retornando true
    def is_valid(self) -> bool:
        return True

    #Serializando el evento
    def to_dict(self) -> Dict[str, Any]:
        d = vars(self).copy()
        d["timestamp"] = self.timestamp.isoformat()
        return d