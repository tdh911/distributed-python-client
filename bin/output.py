import prettytable

FILEPATH = "../output/"
def format_output(json_data):
    method = json_data['method']

    if method == "list-all":
        table = prettytable.PrettyTable()
        table.add_column("Files", json_data['data']) 

        print table

    elif method == "read" or method == "write" or method == "delete":
        print method + " operation was successful"
        print

        if method == "read":
           write_file(json_data['data']) 

def write_file(file_string):
    filepath = FILEPATH + json_data['filename']

    with open(filepath, 'wb') as f:
        f.write(file_string)


