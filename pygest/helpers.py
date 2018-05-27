import os

def get_results(path):
    result_tuples = []
    for root, dirs, files in os.walk(path, topdown=True):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            record = {'note': ""}
            try:
                file_parts = file.split('.')
                file_base = file_parts[0]
                file_extn = file_parts[1]
                if file_extn == 'json':
                    file_set = "json"
                    if os.path.isfile(os.path.join(root, file_base + ".tsv")):
                        file_set += ", tsv"
                    if os.path.isfile(os.path.join(root, file_base + ".log")):
                        file_set += ", log"
                    # Only log results if all three parts exist.
                    if file_set == "json, tsv, log":
                        # Get result properties from path.
                        directories = root.split(os.sep)
                        for directory in directories:
                            key_values = directory.split('_')
                            for key_value in key_values:
                                try:
                                    kv = key_value.split('-')
                                    record['note'] += "\nfound {} to be {}".format(kv[0], kv[1])
                                    record[kv[0]] = kv[1]
                                except IndexError:
                                    pass
                        # Get result properties from file name.
                        key_values = file_base.split('_')
                        for key_value in key_values:
                            try:
                                kv = key_value.split('-')
                                record[kv[0]] = kv[1]
                            except IndexError:
                                pass
                        record['root'] = root
                        record['file'] = file
                        result_tuples.append(record)
            except IndexError:
                # not a file with a . and extension, ignore it
                pass
    return result_tuples

