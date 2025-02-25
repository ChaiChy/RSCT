import typer
import serial
import serial.tools.list_ports
from tabulate import tabulate
import packetizer

def get_modules():

    TARGET_VID = 0xf00d
    TARGET_PID = 0xbabe

    list_of_modules = []

    available_system_ports = serial.tools.list_ports.comports()

    for io_module in available_system_ports:
        if io_module.vid == TARGET_VID and io_module.pid == TARGET_PID:
            list_of_modules.append({"serial_id" : io_module.serial_number, "comport" : io_module.device})
    
    return list_of_modules

def print_modules_in_table(list_of_modules):
    table_rows = []
    for i, module in enumerate(list_of_modules, start=0):
        table_rows.append([f"Module {i}", module["serial_id"], module["comport"]])

    headers = ["Module", "Serial ID", "Com Port"]

    print(tabulate(table_rows, headers=headers, tablefmt="fancy_grid"))

# rsct = random server cli thingy
rsct = typer.Typer()

@rsct.command()
def ls_modules():
    print_modules_in_table(get_modules())

@rsct.command()
def write_do(serial_id: int, do_state: str):
    do_state_int = int(do_state, 0)
    if do_state_int > 1023 or do_state_int < 0:
        print("DO state must have a value between 0 and 1023!")

    available_modules = get_modules()

    if len(available_modules) == 0:
        print(f"No module present ): ")
        return 
    
    for module in available_modules:
        if int(module["serial_id"]) == serial_id:
            try: 
                transceiver = serial.Serial(module["comport"], 115200)
                transceiver.write(packetizer.digital_out_set_state(serial_id, do_state_int))
            except serial.SerialException as e:
                print(f"Failed to open or write to {module['comport']}: {e}")

            response = transceiver.readline().decode().strip()
            print(f"Received: {response}")
            return
    
    print(f"No module with serial id: {serial_id} present ):")

@rsct.command()
def read_do(serial_id: int):
    
    available_modules = get_modules()

    if len(available_modules) == 0:
        print(f"No module present ): ")
        return 
    
    for module in available_modules:
        if int(module["serial_id"]) == serial_id:
            try: 
                transceiver = serial.Serial(module["comport"], 115200)
                transceiver.write(packetizer.digital_out_read_state(serial_id))
            except serial.SerialException as e:
                print(f"Failed to open or write to {module['comport']}: {e}")

            response = transceiver.readline().decode().strip()
            print(f"Received: {response}")
            return
    
    print(f"No module with serial id: {serial_id} present ):")


if __name__ == "__main__":
    rsct()
