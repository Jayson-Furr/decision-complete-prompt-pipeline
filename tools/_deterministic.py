from __future__ import annotations
import os
from datetime import datetime, timezone

DEFAULT_GENERATED_AT_UTC = "2026-06-27T00:00:00Z"


def generated_at_utc() -> str:
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).isoformat().replace("+00:00", "Z")
    return os.environ.get("DP_PIPELINE_GENERATED_AT_UTC", DEFAULT_GENERATED_AT_UTC)
