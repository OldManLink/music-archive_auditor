from typing import Optional

def format_bytes(size_bytes: int) -> str:
    kb = 1024
    mb = kb * 1024
    gb = mb * 1024

    if size_bytes >= gb:
        return f"{size_bytes / gb:.1f} GB"

    if size_bytes >= mb:
        return f"{size_bytes / mb:.1f} MB"

    return f"{size_bytes / kb:.1f} KB"

def pluralize(count: int, singular: str, plural: Optional[str] = None) -> str:
    if abs(count) == 1:
        return singular

    return plural if plural is not None else singular + "s"
