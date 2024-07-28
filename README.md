# lildaq (WIP)

A lil' Data Acquisition System (DAQ) in the form of a lightweight CLI that collects serial input and dumps it with a timestamp to a local CSV file.  Built for Ardunio/IoT applications.  I built `lildaq` because I thought it would be cool if logging data from serial inputs from things like `Ardunio` projects was easier/more repeatable for me.  It would be even cooler if other folks get some use out of it too!


## Installation WIP

1. Clone this repository
2. Create a virtual environment (Optional, but recommended)
3. Install dependencies 

```
cd lildaq
pip install -r "setup/requirements.txt"
```
4. Log data to your heart's content!


## Usage WIP

### General Usage:

```
lildaq.py [-h] [-p PORT] [-o OUTPUT_PATH] [-b BAUD_RATE] [-e]
                 [-f FILE_HEADER [FILE_HEADER ...]] [-q]
```
to stop logging, hit **Ctrl-C**

### CLI Options
```
  -h, --help            show this help message and exit
  -p PORT, --port PORT  The serial port to monitor
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Local path to write the output file.
  -b BAUD_RATE, --baud_rate BAUD_RATE
                        The serial port baud raute in bps; default is 9600
  -e, --epoch_timestamps
                        If enabled, reports timestamps as epoch/UNIX
                        timestamps
  -f FILE_HEADER [FILE_HEADER ...], --file_header FILE_HEADER [FILE_HEADER ...]
                        List of column names to form the header; be sure to
                        check your Arduino setup first :)
  -q, --quiet           When flag is used, serial data will not be displayed
                        as it collects

```

A note about baudrates...
From the `pySerial` documentation:

```
The parameter baudrate can be one of the standard values: 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800, 9600, 19200, 38400, 57600, 115200. These are well supported on all platforms.

Standard values above 115200, such as: 230400, 460800, 500000, 576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000 also work on many platforms and devices.

Non-standard values are also supported on some platforms (GNU/Linux, MAC OSX >= Tiger, Windows). Though, even on these platforms some serial ports may reject non-standard values.
```

## Examples WIP



## Acknowledgements

This whole thing is just a wrapper for the very nicely built [pySerial](https://pyserial.readthedocs.io/en/latest/#), I really appreciate all their work.

[pyFiglet](https://github.com/pwaller/pyfiglet) Is another awesome library I used to make the text graphics in the CLI.  :)

