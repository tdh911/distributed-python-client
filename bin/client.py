import parser
import urllib
import urllib2 as url

DEFAULT_ENDPOINT = "http://localhost:8080"

def main():
    args = parser.get_args()

    # TODO: this is dangerous if the file is TOO large
    with open(args.filepath, 'rb') as f:
        file_contents = f.read()

    endpoint = args.endpoint if args.endpoint else DEFAULT_ENDPOINT
    request = url.Request(endpoint)
    http_args = {
            "method":args.mode,
            "decentralized-db-user":args.user,
            "secret-key":args.secret_key,
            "filename":args.filename,
            "file":file_contents
        }

    data = urllib.urlencode(http_args)
    resp = url.urlopen(request, data)

    out = resp.read()
    print out 

if __name__ == "__main__":
    main()
