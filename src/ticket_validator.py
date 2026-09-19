import re


def is_valid_ticket(ticket):
    """Return True if ticket matches the required format."""
    if not isinstance(ticket, str):
        raise TypeError("ticket must be a string")

    pattern = r"^TKT-\d{4}$"
    return re.match(pattern, ticket) is not None


def mask_ticket(ticket):
    """Mask the numeric portion of a valid ticket.

    Example:
        TKT-1234 -> TKT-****
    """
    if not is_valid_ticket(ticket):
        raise ValueError("ticket is not valid")

    prefix, number = ticket.split("-")

    if len(number) <= 2:
        masked_number = "*" * len(number)
    else:
        masked_number = number[:1] + "*" * (len(number) - 1)

    return f"{prefix}-{masked_number}"


def normalize_ticket(ticket):
    """Normalize a ticket by removing spaces and converting to uppercase."""
    if not isinstance(ticket, str):
        raise TypeError("ticket must be a string")

    cleaned = ticket.strip().upper()

    if not cleaned.startswith("TKT-"):
        cleaned = "TKT-" + cleaned

    return cleaned