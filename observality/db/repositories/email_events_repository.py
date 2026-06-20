from json import dumps

from typing import Any
from observality.db import get_engine, create_tables, utc_now

def store_email_event(
    level: str,
    event: str,
    message: str,
    logger: str | None = None,
    recipient: str | None = None,
    subject: str| None = None,
    duration_ms: float | None = None,
    cpu_percent: float | None = None,
    memory_percent: float | None = None,
    process_memory_mb: float | None = None,
    error: str| None = None,
    file: str| None = None,
    line: str| None = None,
    function: str | None = None,
    **extra: Any,
) -> None:
    create_tables()

    engine = get_engine()

    row = {
        "created_at": utc_now(),
        "level" : level.upper(),
        "event" : event,
        "message" : message,
        "logger" : logger,
        "recipient" : recipient,
        "subject" : subject,
        "duration_ms" : duration_ms,
        "cpu_percent" : cpu_percent,
        "memory_percent" : memory_percent,
        "process_memory_mb" : process_memory_mb,
        "error" : error,
        "file" : file,
        "line" : line,
        "function" : function,
        "extra_json" : dumps(extra, ensure_ascii=False, default=str),
    }
