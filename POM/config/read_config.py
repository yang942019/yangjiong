import configparser
import os


def read_fig(section, option):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data = configparser.ConfigParser()
    data.read(os.path.join(base_dir, 'config.ini'))
    return data.get(section, option)


if __name__ == '__main__':
    print(read_fig('TEST_SERVER', 'url'))
