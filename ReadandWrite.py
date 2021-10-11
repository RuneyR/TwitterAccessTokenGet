import os

# Program script will create 2 files. One for consumer key and secret. The other for creating generated tokens.
# Program will also read from Consumer file for OAUTH.
cKeys = 'ConsumerKeys.txt'
aKeys = 'AccessKeys.txt'
global fileEmpty


def check_ck_file():
    global fileEmpty
    try:
        fileEmpty = os.stat(cKeys).st_size == 0
    except OSError:
        print("File not found.Creating txt.Write down keys within the file. File location=program was run.\n")
        consumerFileWrite = open(cKeys, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(cKeys, "a")
        consumerFileWrite.write("Please write Consumer key and Consumer Token, in order and on separate lines, "
                                "no spaces, below. This file should only be 3 lines long.\nReplace this line with "
                                "Consumer Key! \nReplace this line with Consumer Token!")
        consumerFileWrite.close()


def get_consumer_keys():
    cfr = open(cKeys, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck


def write_token(access_token, access_secret):
    akw = open(aKeys, "w")
    akw.write(access_token + "\n" + access_secret)
    akw.close()
    print("Access Tokens have been written. Delete file after using. Tokens will remain the same until revoked on "
          "Twitters Account Security settings. Check " + aKeys)
