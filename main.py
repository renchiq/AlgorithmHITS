import math

data = {
    'abc.ru': {
        'adjacency': ['xyz.com'],
        'hub': 1,
        'auth': 1
    },
    'xyz.com': {
        'adjacency': ['abc.ru', 'yui.kz'],
        'hub': 1,
        'auth': 1
    },
    'yui.kz': {
        'adjacency': ['xyz.com', 'klm.ua'],
        'hub': 1,
        'auth': 1
    },
    'klm.ua': {
        'adjacency': ['yui.kz'],
        'hub': 1,
        'auth': 1
    }
}

for step in range(4):
    norm = 0
    for page in data:
        data[page]['auth'] = 0
        for adj_page in data[page]['adjacency']:
            data[page]['auth'] += data[adj_page]['hub']
        norm += data[page]['auth'] ** 2
    norm = math.sqrt(norm)

    for page in data:
        data[page]['auth'] = data[page]['auth'] / norm

    norm = 0
    for page in data:
        data[page]['hub'] = 0
        for adj_page in data[page]['adjacency']:
            data[page]['hub'] += data[adj_page]['auth']
        norm += data[page]['hub'] ** 2
    norm = math.sqrt(norm)

    for page in data:
        data[page]['hub'] = data[page]['hub'] / norm

_ = [print(key, value) for key, value in data.items()]