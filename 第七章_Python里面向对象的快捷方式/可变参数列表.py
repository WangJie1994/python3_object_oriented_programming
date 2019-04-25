def get_links(*links):
    for link in links:
        print(link)


get_links('www.baidu.com')
get_links('www.taobao.com', 'www.baidu.com')


class Options:
    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, item):
        return self.options[item]


options = Options(username='dusty', password='drowssap', debug=True)
print(options['debug'])
print(options['port'])
print(options['username'])

import shutil
import os.path


def augmented_move(target_folder, *filenames, verbose=False, **specific):
    """
    move
    :param target_folder:
    :param filenames:
    :param verbose:
    :param specific:
    :return:
    """

    def print_verbose(message, filename):
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == 'ignore':
                print_verbose("ignoring {0}", filename)
            elif specific[filename] == 'copy':
                print_verbose("copying {0}", filename)
                shutil.copyfile(filename, target_path)
        else:
            print_verbose("moving {0}", filename)
            shutil.move(filename, target_path)


augmented_move("move here", "one", "two")
augmented_move("move here", "one", "two", verbose=True)
augmented_move("move here", "one", "two", two="move", verbose=True, one="copy")
