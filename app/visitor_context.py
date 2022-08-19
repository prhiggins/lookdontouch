from dataclasses import dataclass

@dataclass
class VisitorContext:
    ip_address: str = None
    cookies: list[str] = None
    user_agent: str = None
    other_headers: dict[str] = None