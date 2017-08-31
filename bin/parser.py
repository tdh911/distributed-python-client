import argparse

CHOICES = ["list-all", "write", "read", "delete"]
def get_parser():
    parser = argparse.ArgumentParser(description="Make call to decentralized db")

    parser.add_argument("mode", choices=CHOICES)

    parser.add_argument("--user", "--public-key", dest="user", help="The public key associated with a user")
    parser.add_argument("--endpoint", dest="endpoint", default="http://localhost:8080", help="Where decentralized db is running")
    
    parser.add_argument("--filepath", dest="filepath", help="The path to the file you want to write")
    parser.add_argument("--filename", dest="filename", help="The file you want to read")
    parser.add_argument("--secret-key", dest="secret_key", help="Secret key associated with the file")

    return parser

def get_args():
    return get_parser().parse_args()
