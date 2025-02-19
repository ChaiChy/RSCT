import struct

def digital_out_packet_config(digital_out_states: int):
    """
    Take a number between 0 and 1023 and pack it as a struct byte object.
    :param bools: integer between 0 and 1023.
    :return: A 16-bit integer (0 to 65535) representing those booleans.
    """
    if digital_out_states > 1023 or digital_out_states < 0:
        raise ValueError("Value must be between 0 or 1023.")

    value = digital_out_states & 0xFFFF   # Mask to ensure it's within 16 bits
    return struct.pack("<H", value)  # Pack as little-endian 16-bit integer
