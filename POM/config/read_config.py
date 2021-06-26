import configparser


def read_fig(path, section, option):
    data = configparser.ConfigParser()
    data.read(path)
    return data.get(section, option)


if __name__ == '__main__':
    read_fig('TEST_SERVER', 'url')