import struct
from dataclasses import dataclass
from uuid import UUID


@dataclass
class SensorMessage:
    sensor_id: UUID
    data: float

    def to_bytes(self):
        """
        Convert the SensorMessage object to bytes. The format will be:
        - 16 bytes for the UUID (since UUID is 128 bits)
        - 8 bytes for the float (assuming double precision)

        Returns:
            bytes: The byte representation of the sensor message.
        """
        # Convert the UUID to bytes (16 bytes)
        sensor_id_bytes = self.sensor_id.bytes

        # Convert the float data to bytes (8 bytes using double precision)
        data_bytes = struct.pack('d', self.data)  # 'd' stands for double precision float

        # Return the concatenation of the sensor_id bytes and data bytes
        return sensor_id_bytes + data_bytes

    @classmethod
    def from_bytes(cls, message_bytes: bytes):
        """Create a SensorMessage instance from a byte string."""
        # Extract the first 16 bytes for UUID
        sensor_id_bytes = message_bytes[:16]
        # Extract the next 8 bytes for the float
        data_bytes = message_bytes[16:]

        # Convert bytes back to the original types
        sensor_id = UUID(bytes=sensor_id_bytes)
        data = struct.unpack('d', data_bytes)[0]  # 'd' for double precision float

        # Return a new SensorMessage instance
        return cls(sensor_id, data)
