class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"
        # including the '!r' after the self.name will automatically put the
        # string inside quotes. It internally calls the __repr__ method of
        # self.name.

    def disconnect(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining.)"

    def print_pages(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("USB Printer", "USB", 500)
printer.print_pages(20)
print(printer)
printer.disconnect()
printer.print_pages(30)



# printer = Device("Printer", "Bluetooth")
# print(printer)
# printer.disconnect()
