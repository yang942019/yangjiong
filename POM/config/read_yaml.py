import yaml


def read(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(stream=file, Loader=yaml.FullLoader)
    print(data)
    return data


if __name__ == '__main__':
    read('../data/login.yaml')
