import argparse
import parser
import requests
import output

def getFilename(path):
    if path is None:
        return None

    if "/" in path:
        return path.split("/")[-1]
    else:
        return path

def main():
    args = parser.get_args()

    file_contents = None
    if args.method == "write":
        # TODO: this is dangerous if the file is too large
        #       Read through file based off system memory
        with open(args.filepath, 'rb') as f:
            file_contents = f.read()

    filename = args.filename if args.filename else getFilename(args.filepath)

    if not args.user:
        raise argparse.ArgumentTypeError("Missing user!")

    if (not args.secret_key or not filename) and args.method != "list-all":
        raise argparse.ArgumentTypeError("Missing secret key or filename or filepath")

    http_args = {
            "method":args.method,
            "decentralized-db-user":args.user,
            "secret-key":args.secret_key,
            "filename":filename,
            "file":file_contents
    }

    resp = requests.get(args.endpoint, http_args)
    if resp.status_code != requests.codes.ok:
        resp.raise_for_status()

    json_data = resp.json()

    if args.method == "read":
        json_data['filename'] = filename

    output.format_output(json_data)

if __name__ == "__main__":
    main()
