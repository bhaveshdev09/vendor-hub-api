from enum import StrEnum

# The class `OrderStatus` is a string enumeration that represents the status of an order, with
# possible values of "pending", "completed", and "cancelled".


class OrderStatus(StrEnum):
    """string enumeration that represents the status of an order"""

    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
