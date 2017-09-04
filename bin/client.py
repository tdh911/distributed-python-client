import parser
import urllib
import urllib2 as url
import json

DEFAULT_ENDPOINT = "http://localhost:8080"

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
        raise ValueError("Missing user!")

    if (not args.secret_key or not filename) and args.method != "list-all":
        raise ValueError("Does not contain all necessary arguments")
    
    http_args = {
            "method":args.method,
            "decentralized-db-user":args.user,
            "secret-key":args.secret_key,
            "filename":filename,
            "file":file_contents
    }

    data = urllib.urlencode(http_args)
    endpoint = args.endpoint if args.endpoint else DEFAULT_ENDPOINT
    request = url.Request(endpoint)
    resp = url.urlopen(request, data)

    json_data = json.load(resp)
    print json_data

if __name__ == "__main__":
    main()
