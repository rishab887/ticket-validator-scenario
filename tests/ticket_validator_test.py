import pytest

from src.ticket_validator import (
    is_valid_ticket,
    mask_ticket,
    normalize_ticket,
)


def test_is_valid_ticket_true():
    assert is_valid_ticket("TKT-1234") is True


def test_is_valid_ticket_false():
    assert is_valid_ticket("ABC-1234") is False


def test_is_valid_ticket_type_error():
    with pytest.raises(TypeError):
        is_valid_ticket(1234)


def test_mask_ticket_invalid():
    with pytest.raises(ValueError):
        mask_ticket("INVALID")


# This test is intentionally disabled.
# DO NOT enable it yet.
#
# def test_mask_ticket_basic():
#     result = mask_ticket("TKT-1234")
#     assert result == "TKT-****"