from uuid import UUID


def safe_uuid_to_str(value: UUID):
    return str(value) if value else None
