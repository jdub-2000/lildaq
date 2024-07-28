# lildaq.py
#
# a CLI for monitoring, and logging arduino/serial structured input
# designed to be flexible and easy to use for logging things quickly
# jdub_2000, 27JUL2024

import csv
import argparse
from pathlib import Path
import time

from pyfiglet import Figlet
import serial
from serial import serialutil as ser_u



def open_serial_connection(mon_port, baud_rate):

    try:
        ser = serial.Serial(
            port=mon_port,
            baudrate=baud_rate
        )

    except ser_u.SerialException as err:
        print(f"The Following Error occurred: {err}")
        print(f"Check and see if the device is connected properly.")
        exit()
    
    return ser
    

def generate_timestamp(use_epoch_time):

    t = time.localtime()

    if use_epoch_time:
        tme_str = time.mktime(t)
    else:
        tme_str = time.strftime("%Y-%m-%d %H:%M:%S", t)

    return tme_str


def main(mon_port, out_path, baud_rate, use_epoch_time, file_header, quiet_mode):
    
    print("")

    f = Figlet(font="rowancap")
    print(f.renderText("lilDAQ"))

    print("ver 0.1 ALPHA")
    print("27JUL2024\n")
    print(f"Use Epoch timestamps = {use_epoch_time}")
    print(f"Quiet Mode = {quiet_mode}")
    print(f"Baud Rate: {baud_rate} bps")
    print(f"Streaming serial data from port {mon_port} to {out_path.name}...\n")
    
    # TODO: General cleanup/DRY etc.
    # TODO: baud rate enums or datachecks, not continuous but discrete baud rates are accepted by pyserial
    # TODO: add optin to control time code fmt string
    # TODO: path vaildator/ warning for overwriting

    run = True
    ser = open_serial_connection(mon_port, baud_rate)

    with open(out_path, "w", newline="") as csv_file:

        csv_writer = csv.writer(csv_file)
        header = ["Timestamp"] + file_header
        csv_writer.writerow(header)

        while run == True:

            try:
                serial_data = ser.readline().decode().strip()
                tme_str = generate_timestamp(use_epoch_time=use_epoch_time)
                arr = serial_data.split(",")
                record = [tme_str] # initialize with timestamp, append N serial records

                for _ in arr:
                    record.append(_)

                if not quiet_mode:
                    print(f"{tme_str},{serial_data}")

                csv_writer.writerow(record)

            except KeyboardInterrupt:
                print("\nLogging stopped.")
                print("Exiting ...")
                run = False



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="lildaq.py",
        description="Montitor serial input and log data (like from Arduinos) to a CSV file.",
    )


    parser.add_argument(
        "-p",
        "--port",
        action="store",
        help="The serial port to monitor"
    )

    parser.add_argument(
        "-o",
        "--output_path",
        action="store",
        help="Local path to write the output file."
    )

    parser.add_argument(
        "-b",
        "--baud_rate",
        action="store",
        default=9600,
        help="The serial port baud raute in bps; default is 9600"
    )

    parser.add_argument(
        "-e",
        "--epoch_timestamps",
        action="store_true",
        help="If enabled, reports timestamps as epoch/UNIX timestamps"
    )

    parser.add_argument(
        "-f",
        "--file_header",
        nargs="+",
        action="store",
        help="List of column names to form the header; be sure to check your Ardunio setup first :)"
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="When flag is used, serial data will not be displayed as it collects"
    )

    args = parser.parse_args()

    mon_port = args.port
    out_path = Path(args.output_path)
    baud_rate = int(args.baud_rate)
    use_epoch_time = bool(args.epoch_timestamps)
    file_header = args.file_header
    quiet_mode = args.quiet

    main(mon_port, out_path, baud_rate, use_epoch_time, file_header, quiet_mode)