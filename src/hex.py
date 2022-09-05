import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        coded_string = []
        for c in x:
            coded_letter = hex(ord(c))
            coded_string.append(coded_letter)
        encoding = ''.join(coded_string)
        print(encoding)

    case "decode":
        # Implement the decoding here
        splitted = x.split('0x')[1:]
        decoded_string = []
        for n in splitted:
            decoded_letter = chr(int(n, base=16))
            decoded_string.append(decoded_letter)
        decoding = ''.join(decoded_string)
        print(decoding)
