from uuid import UUID


def safe_uuid_to_str(value: UUID):
    """
    Safely converts a UUID object to a string representation.

    This function takes a UUID object and returns its string representation if the UUID is
    valid (i.e., not None). If the input value is None, the function returns None instead
    of raising an error. This ensures that the function handles cases where the UUID is
    missing or not provided without throwing an exception.

    Args:
        value (UUID): A UUID object to be converted to a string.

    Returns:
        Optional[str]: The string representation of the UUID if it is not None, otherwise None.
    """
    return str(value) if value else None
