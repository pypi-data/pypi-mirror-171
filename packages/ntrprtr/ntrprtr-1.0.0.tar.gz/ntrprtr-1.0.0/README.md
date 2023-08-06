# Description

Interpret bytes through different customizable actions

# Configuration

In order to interpet the given bytes, you need to provide a ´.json´ file
with the following structure:

```json
[
    {
        "name": "Enter the name here..",
        "description": "Provide description here..",
        "start": 0,  // The start byte from where you want to interpret
        "end": 10,   // The end byte where interpreting shall stop
        "action": {  // There a 3 different actions at the moment. 
                     // --> Do only specify one action per object here.
                     // --> The actions are specified below.
        }
    }
]
```
The following actions are available:

```json
// Get the decimal value of the given bytes.
// Specify if you want to interpret it as little or big endian
{
    "type": "amount",
    "endianess": "little|big"
}

// Get the ascii representation of the given bytes.
{
    "type": "ascii"
}

// Compare the given bytes against your own values:
{
    "type": "equals",
    // Add as many objects as you want to the "cmp" list
    "cmp": [{
                // The value you want to compare with the given bytes
                "value": "1D1E", 
                // A description which will be added to the result, 
                // if the given bytes matches "value"         
                "description": "Compare 1"      
            },{
                "value": "1D1",
                "description": "Compare 2"
            }]
}
```

Just add as many interpreting objects as you want to the list. The output is a list of tuples. Look at the example section for an overview.



# Installation

`pip install ntrprtr`

# Example

Given bytes to interpret:

```
00 01 02 03 04 04 06 07 08 09 0A 0B 0C 0D 0E 0F 
68 61 6C 6C 6F 20 77 6F 72 6C 64 1B 1C 1D 1E 1F
```

Use the following `config.json`:

```json
[
    {
        "name": "first-bytes",
        "description": "This are the first three bytes",
        "start": 0,
        "end": 2,
        "action": {
            "type": "amount",
            "endianess": "little"
        }
    },
     {
        "name": "ascii-bytes",
        "description": "These are ascii values",
        "start": 16,
        "end": 26,
        "action": {
            "type": "ascii"
        }
    },
    {
        "name": "equals-bytes",
        "description": "Test if the given bytes equals my specified bytes",
        "start": 29,
        "end": 30,
        "action": {
            "type": "equals",
            "cmp": [{
                "value": "1D1E",
                "description": "Compare 1"
            },{
                "value": "1D1",
                "description": "Compare 2"
            }]
        }
    }
]
```

Use it programmatically:

```python
import json

from ntrprtr.ByteInterpreter import ByteInterpreter

configPath = "config.json"
pathToFile = "example.dd" # Contains the above bytes


fileHandle = open(pathToFile, "rb")
testBytes = fileHandle.read()

configHandle = open(configPath, encoding="utf8")
config = json.load(configHandle)

b = ByteInterpreter(testBytes, config)
result = b.interpret()
```

The result is a list of tuples:
```python
[
#     Name           Description          Action   Bytes                        ActionResult
    ('first-bytes', 'First three bytes', 'amount', bytearray(b'\x00\x01\x02'), '131328'), 
    ('ascii-bytes', 'Ascii values',      'ascii',  bytearray(b'hallo world'),  'hallo world'), 
    ('equals-bytes', 'Test equals',      'equals', bytearray(b'\x1d\x1e'),     'Compare 1')
]
```

# License

MIT