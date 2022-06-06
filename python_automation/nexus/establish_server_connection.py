import serial.tools.list_ports


def connection_test():
    ports = serial.tools.list_ports.comports()
    serial_inst = serial.Serial()

    port_list = []

    for onePort in ports:
        port_list.append(str(onePort))
        print(str(onePort))

connection_test()
