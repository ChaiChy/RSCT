import struct

def digital_out_set_state(serial_id: int, digital_out_state: int):
    """
    Take a number between 0 and 1023 and pack it with a specified serial id as a struct byte object.
    :param bools: integer between 0 and 1023.
    :return: A 16-bit integer (0 to 65535) representing those booleans.
    """
    if digital_out_state > 1023 or digital_out_state < 0:
        raise ValueError("Value must be between 0 or 1023.")
    
    rw_command = 0b1 # 1 for write command

    payload = ((serial_id & 0x1F) << 11) | rw_command << 10 | (digital_out_state & 0x3FF)

    payload &= 0xFFFF
    return struct.pack("<H", payload)  # Pack as little-endian 16-bit integer

def digital_out_read_state(serial_id: int):
    """
    Read the digital out module pin state with the specified serial id.
    :param bools: integer between 0 and 31 (serial id is 5 bits wide)
    :return: A 16-bit integer (0 to 65535) representing those booleans
    """

    rw_command = 0b0 # 1 for write command

    payload = ((serial_id & 0x1F) << 11) | rw_command << 10 | 0 & 0x3FF

    payload &= 0xFFFF
    return struct.pack("<H", payload)  # Pack as little-endian 16-bit integer
