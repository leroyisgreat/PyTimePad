import sys
import argparse
import string

# TODO: 
#       -- Implement file operators
#       -- Write documentation
#       -- Implement other cycling options:
#           -- upper + digit cycling (mod 36)
#           -- upper + lower cycling (mod 52)
#           -- upper + lower + digit cycling (mod 62)

# A shift function, curried to allow the switch of encrypt/decrypt and still
#   be used in a call to map. This is the best Python 2.7 has to offer.
def shift(decrypt):

    def shift_((char, shift)):
        if (decrypt):
            s_i = -int(shift)
        else:
            s_i = int(shift)

        if (char in string.ascii_letters):
        # For letters...
            c_i = ord(string.upper(char)) - ord('A')
            p_i = c_i + s_i
            return chr(ord('A') + (p_i % 26))
        elif (char in string.digits):
        # For numbers...
            c_i = ord(char) - ord('0')
            p_i = c_i + s_i
            return chr(ord('0') + (p_i % 10))
        else:
        # Echo anything that shouldn't be shifted
            return char

    return shift_


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt",
                    help="set the operand to be decryption, rather than encryption",
                    action="store_true")

# File I/O
#parser.add_argument("-if", "--input_file",
#                    help="set a given file to be read as the message to be encrypted/decrypted",
#                    type=str)
#parser.add_argument("-of", "--output_file",
#                    help="set a given file to be writen as the encrypted/decrypted message to",
#                    type=str)
#parser.add_argument("-kf", "--key_file",
#                    help="set a given file to be read as the key",
#                    type=str)

# Cycling settings
#modulo = parser.add_argument_group('cycle pattern')
#modulo.add_argument("-m36", "--modulo_36",
#                    help="set the OTP cycling to be uppercase letters and digits",
#                    action='store_true')
#modulo.add_argument("-m52", "--modulo_52",
#                    help="set the OTP cycling to be uppercase and lowercase letters",
#                    action='store_true')
#modulo.add_argument("-m62", "--modulo_62",
#                    help="set the OTP cycling to be uppercase and lowercase letters, and digits",
#                    action='store_true')

parser.add_argument("k", type=int, help="conversion key")
args = parser.parse_args()

msg = list(raw_input())
key = list(str(args.k))

if (len(msg) > len(key)):
    parser.error("Error: message length greater than key length.")

pre = zip(msg, key)
pst = map(shift(args.decrypt), pre)


print('%s' % ''.join(pst))
