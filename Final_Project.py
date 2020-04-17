import random
import time
import string
import json


def getlowercase():
    return random.choice(string.ascii_lowercase)


def getuppercase():
    return random.choice(string.ascii_uppercase)


def getsymbol():
    syms = ['!', '@', '#', '$', '%']
    return str(random.randint(syms))


def getnum():
    return str(random.randint(1, 20))


defs = [getlowercase, getuppercase, getsymbol, getnum]


length = random.randint(12, 12)
pw = []

for x in range(length):
    index = random.randint(0, 3)
    pw.append(index)
pw_mask = ''.join(map(str, pw))


class Device:
    def __init__(self, wifi_ssid, wifi_password, device_id, firmware, device_type):
        self.wifi_ssid = wifi_ssid
        self.wifi_password = wifi_password
        self.device_id = device_id
        self.firmware = firmware
        self.device_type = device_type

    def new_device_set_up(self):
        file = open("Device_id.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n" + "Ssid: " + self.wifi_ssid + "\n" + "Password: "
                   + self.wifi_password + "pos_emulation: " + self.pos_emulation + "\n" + "----------------------------------------------------------\n")
        file.close()
        print("----------------------------------------------------------\n" + "Thingamajig: " + self.device_id + "\n" + "Wifi ssid: " + self.wifi_ssid + "\n" + "Wifi Password: "
              + self.wifi_password + "\n" + "pos_emulation: " + self.pos_emulation + "\n" + "Device type: " + self.device_type + "\n"
              + "----------------------------------------------------------" + "\n")
        file = open("Activation_Log.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n")
        file.close()


class Scanner(Device):
    def __init__(self, wifi_ssid, wifi_password, device_id, pos_emulation, firmware, device_type):
        super().__init__(wifi_ssid, wifi_password, device_id, firmware, device_type)
        self.device_type = device_type
        self.pos_emulation = pos_emulation


    def scanner_set_up(self):
        file = open("Device_id.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n" + "Ssid: " + self.wifi_ssid + "\n" + "Password: "
                   + self.wifi_password + "\npos_emulation: " + self.pos_emulation + "\nScanner Firmware: " + self.firmware + "\nDevice Type: Scanner" + "\n" + "----------------------------------------------------------\n")
        file.close()
        print(
            "----------------------------------------------------------\n" + "Thingamajig: " + self.device_id + "\n" + "Wifi ssid: " + self.wifi_ssid + "\n" + "Wifi Password: "
            + self.wifi_password + "\n" + "pos_emulation: " + self.pos_emulation + "\nScanner Firmware: " + self.firmware + "\nDevice Type: " + self.device_type + "\n"
            + "----------------------------------------------------------" + "\n")
        file = open("Activation_Log.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n")
        file.close()

    def update_device(self):
        self.device_id = {
            'Device ID': self.device_id,
            'SSID': self.wifi_ssid,
            'Password': self.wifi_password,
            'pos_emulation': self.pos_emulation,
            'firmware': self.firmware,
            'type': self.device_type
        }

        j = json.dumps(self.device_id)
        with open('COM0.json', 'w') as f:
            f.write(j)
            f.close()

    def erase_credentials(self):
        self.device_id = {
            'Device ID': 'N/A',
            'SSID': 'N/A',
            'Password': 'N/A',
            'pos_emulation': 'N/A',
            'firmware': 'N/A',
            'type': 'N/A'
        }

        j = json.dumps(self.device_id)
        with open('COM0.json', 'w') as f:
            f.write(j)
            f.close()



class Printer(Device):
    def __init__(self, wifi_ssid, wifi_password, device_id, pos_emulation, firmware, device_type):
        super().__init__(wifi_ssid, wifi_password, device_id, firmware, device_type)
        self.device_type = device_type
        self.pos_emulation = pos_emulation



    def printer_set_up(self):
        file = open("Device_id.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n" + "Ssid: " + self.wifi_ssid + "\n" + "Password: "
                   + self.wifi_password + "\npos_emulation: " + self.pos_emulation + "\nPrinter Firmware: " + self.firmware + "\nDevice Type: Printer" + "\n" + "----------------------------------------------------------\n")
        file.close()
        print(
            "----------------------------------------------------------\n" + "Thingamajig: " + self.device_id + "\n" + "Wifi ssid: " + self.wifi_ssid + "\n" + "Wifi Password: "
            + self.wifi_password + "\n" + "pos_emulation: " + self.pos_emulation + "\nScanner Firmware: " + self.firmware + "\nDevice Type: " + self.device_type + "\n"
            + "----------------------------------------------------------" + "\n")
        file = open("Activation_Log.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n")
        file.close()

    def update_device(self):
        self.device_id = {
            'Device ID': self.device_id,
            'SSID': self.wifi_ssid,
            'Password': self.wifi_password,
            'pos_emulation': self.pos_emulation,
            'firmware': self.firmware,
            'type': self.device_type
        }

        j = json.dumps(self.device_id)
        with open('COM0.json', 'w') as f:
            f.write(j)
            f.close()


class Display(Device):
    def __init__(self, wifi_ssid, wifi_password, device_id, firmware, device_type):
        super().__init__(wifi_ssid, wifi_password, device_id, firmware, device_type)
        self.device_type = device_type

    def display_set_up(self):
        file = open("Device_id.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n" + "Ssid: " + self.wifi_ssid + "\n" + "Password: "
                   + self.wifi_password + "\nDisplay Firmware: " + self.firmware + "\nDevice Type: Display" + "\n" + "----------------------------------------------------------\n")
        file.close()
        print(
            "----------------------------------------------------------\n" + "Thingamajig: " + self.device_id + "\n" + "Wifi ssid: " + self.wifi_ssid + "\n" + "Wifi Password: "
            + self.wifi_password + "\nDisplay Firmware: " + self.firmware + "\nDevice Type: " + self.device_type + "\n"
            + "----------------------------------------------------------" + "\n")
        file = open("Activation_Log.txt", "a")
        file.write("Thingamajig: " + self.device_id + "\n")
        file.close()







class Device:
    def __init__(self, ssid, password, id, firmware, type, pos, firmware_2):
        self.ssid = ssid
        self.password = password
        self.id = id
        self.firmware = firmware
        self.type = type
        self.pos = pos
        self.firmware_2 = firmware_2

    def update_wifi(self):
        self.id = {
            'Device ID': self.id,
            'SSID': self.ssid,
            'Password': self.password,
            'pos_emulation': "N/A",
            'firmware': self.firmware_2,
            'type': self.type,
            'pos': self.pos
        }

        j = json.dumps(self.device_id)
        with open('COM0.json', 'w') as f:
            f.write(j)
            f.close()


def main():
    choice ='0'
    while choice =='0':
        print("\nDevice Connected to COM0 Serial connection.")
        time.sleep(.5)
        print("\n-")
        time.sleep(.5)
        print("\n-")
        time.sleep(.5)
        print("\n-")
        time.sleep(.5)
        print("\n-")
        time.sleep(.5)
        print("\n-")
        print("Program Ready\n")
        for x in range(length):
            index = random.randint(0, 20)
            pw.append(index)
        pw_mask = ''.join(map(str, pw))
        print("1) Provision 2) Update Device on COM0 3) Update Flasher 4) Check Current Credentials 0) Main Menu 00) Exit Program ")
        print("Activation Code: " + pw_mask)
        first_choice = input("What will you be doing today? ")
        if first_choice == "1":
            print("Time to Provision a new device.")
            second_choice = input("1) Scanner 2) Printer 3) Display 0) Main Menu\nWhat kind of device will this be: ")
            if second_choice == "1":
                print("Printer Set up")
                print("Make sure to copy the activation code exactly.")
                new_scanner = input("Paste Activation code: ")
                if new_scanner == pw_mask:
                    new_scanner = Scanner(input("Network Name: "), input("Password: "), pw_mask,input("pos_emulation: "), input("Scanner_firmware: "), "Scanner")
                    new_scanner.scanner_set_up()
                    new_scanner.update_device()
                else:
                    print(
                        "That is either an expired or inactive code, Please contact activation@setup.com for a new code.")

            elif second_choice == "2":
                print("Printer Set up")
                print("Make sure to copy the activation code exactly.")
                new_printer = input("Paste Activation code: ")
                if new_printer == pw_mask:
                    new_printer = Printer(input("Network Name: "), input("Password: "), pw_mask, input("pos_emulation: "), input("printer_firmware: "), "Printer")
                    new_printer.printer_set_up()
                    new_printer.update_device()
                else:
                    print("That is either an expired or inactive code, Please contact activation@setup.com for a new code.")

            elif second_choice == "3":
                print("Display Set up")
                print("Make sure to copy the activation code exactly.")
                new_display = input("Paste Activation code: ")
                if new_display == pw_mask:
                    new_display = Display(input("Network Name: "), input("Password: "), pw_mask, input("Display_firmware: "), input("Device Type: "))
                    new_display.display_set_up()
                else:
                    print("That is either an expired or inactive code, Please contact activation@setup.com for a new code.")

        elif first_choice == "2":
            third_choice = input("1) ESP32 2) Update Wifi 3) Clear Credentials 0) Reboot ")
            if third_choice == "1":
                print("ESP32")
                fourth_choice = input("1) Erase Firmware 2) Update Firmware 0) Reboot ")
                if fourth_choice == "1":
                    print("")

                elif fourth_choice == "2":
                    print("Enter New Credentials\n")
                    new_printer = pw_mask
                    new_printer = Printer(input("Network Name: "), input("Password: "), pw_mask, input("pos_emulation: "), input("printer_firmware: "), "Printer")
                    new_printer.printer_set_up()

            elif third_choice == "2":
                print("Updating 328-Right from Firmware_server.txt\n")
                print("Enter New Credentials\n")
                new_printer = pw_mask
                new_printer = Printer(input("Network Name: "), input("Password: "), pw_mask, input("pos_emulation: "),
                                      input("printer_firmware: "), "Printer")
                new_printer.printer_set_up()
                time.sleep(.5)
                print("-\n")
                time.sleep(.5)
                print("-\n")
                time.sleep(.5)
                print("Firmware Updated\n")
                print("Rebooting...")
                time.sleep(2)

            elif third_choice == "3":
                print("Clear Credentials\n")
                device_001 = {
                    'Device ID': '',
                    'SSID': '',
                    'Password': '',
                    'pos_emulation': '',
                    'firmware': '',
                    'type': '',
                    'pos': '',
                }
                time.sleep(2)
                print("Credentials Cleared")

                j = json.dumps(device_001)
                with open('COM0.json', 'w') as f:
                    f.write(j)
                    f.close()
                time.sleep(.5)
                print("-\n")
                time.sleep(.5)
                print("-\n")
                time.sleep(.5)
                print("Credentials Erased\n")
                print("Rebooting...")
                time.sleep(2)

        elif first_choice == "3":
            print("Downloading Software...")
            time.sleep(.5)
            print("\n-")
            time.sleep(.5)
            print("\n-")
            time.sleep(.5)
            print("Updating Software...")
            print("\n-")
            time.sleep(.5)
            print("\n-")
            time.sleep(.5)
            print("\n-")
            time.sleep(.5)
            print("\n-")
            print("IOT Device Flasher V.1.0.0.2\n")
            print("Program will now Reboot")
            time.sleep(2)

        elif first_choice == "4":
            print("Current Device Credentials: ")
            device_002 = json.load(open('COM0.json'))
            print(device_002)

        elif first_choice == "0":
            print("Rebooting...")
            time.sleep(2)
            second_menu()

        elif first_choice == "00":
            print("Device Disconnected.")
            device_001 = {
                'Device ID': 'N/A',
                'SSID': 'N/A',
                'Password': 'N/A',
                'pos_emulation': 'N/A',
                'firmware': 'N/A',
                'type': 'N/A'
            }

            j = json.dumps(device_001)
            with open('COM0.json', 'w') as f:
                f.write(j)
                f.close()
            break

        else:
            print("The program has run into a bug. Attempting to Reboot...")
            time.sleep(2)


if __name__ == '__main__':
    main()
