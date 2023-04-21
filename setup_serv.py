dict = {
    "setup": {
        "di size": 0,  # Size of discrete input block (8 bit)
        "co size": 0,  # Size of coils block (8 bit)
        "ir size": 0,  # Size of input registers block (16 bit)
        "hr size": 1,  # Size of holding registers block (16 bit)
        "shared blocks": True,  # share memory for all blocks (largest size wins)
        "defaults": {
            "value": {  # Initial values (can be overwritten)
                "bits": 0x01,
                "uint16": 122,
                "uint32": 67000,
                "float32": 127.4,
                "string": " ",
            },
            "action": {  # default action (can be overwritten)
                "bits": None,
                "uint16": None,
                "uint32": None,
                "float32": None,
                "string": None,
            },
        },
        "type exception": False,  # return IO exception if read/write on non boundary
    },
    "write": [   # allow write, efault is ReadOnly
        122  # start, end bytes, repeated as needed
    ],
    "float32": [  # Define 32 bit floats (2 registers == 4 bytes)
        [100,150],
        {"addr": 100, "value": 10.00}
    ],
}