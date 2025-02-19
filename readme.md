# RSCT 
Random Server CLI Thingy provides an easy interface for users to mess around with the I/O modules :)

## Getting Started
Run this to install all dependencies uwu:
```bash
$ poetry install
```

##  Examples
1. List all available I/O modules:
```bash
$ python rsct.py ls-modules

# output
╒══════════╤═════════════╤══════════════╕
│ Module   │ Serial ID   │ Com Port     │
╞══════════╪═════════════╪══════════════╡
│ Module 0 │ 0x1         │ /dev/ttyACM1 │
├──────────┼─────────────┼──────────────┤
│ Module 1 │ 0x2         │ /dev/ttyACM0 │
╘══════════╧═════════════╧══════════════╛
```

2. Configire digital output state of module with a serial id of 0x1:

```bash
# set do 0 to High
$ python rsct.py write-do 0x1 0b0000000001

# output
Received: received val: 1


# set do 10, 9, 8, 7, 6 to High
$ python rsct.py write-do 0x1 0b1111100000

# output
Received: received val: 992
```

