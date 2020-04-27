import pickle


def write_pickle(filename, data):
    with open('{}.pickle'.format(filename), 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_pickle(filename):
    with open('{}.pickle'.format(filename), 'rb') as handle:
        b = pickle.load(handle)
    return b
