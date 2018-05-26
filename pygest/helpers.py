import os

def get_results(path):
    results = []
    result_tuples = []
    for root, dirs, files in os.walk(path, topdown=True):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            record = {'note': ""}
            try:
                if file.split('.')[1] in ['json', 'log', 'tsv']:
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
                    record['root'] = root
                    record['file'] = file
                    result_tuples.append(record)
                    results.append(os.path.join(root, file))
            except IndexError:
                # not a file with a . and extension, ignore it
                pass
    return result_tuples

