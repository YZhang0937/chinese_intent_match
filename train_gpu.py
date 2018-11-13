from core.nn import nn


def siam(paths):
    paths['dnn_siam_average'] = prefix + 'model/dnn/siam_average.h5'
    paths['cnn_siam_parallel'] = prefix + 'model/cnn/siam_parallel.h5'
    paths['cnn_siam_serial'] = prefix + 'model/cnn/siam_serial.h5'
    paths['rnn_siam_plain'] = prefix + 'model/rnn/siam_plain.h5'
    paths['rnn_siam_stack'] = prefix + 'model/rnn/siam_stack.h5'
    paths['rnn_siam_bi'] = prefix + 'model/rnn/siam_bi.h5'
    paths['rnn_siam_attend'] = prefix + 'model/rnn/siam_attend.h5'
    paths['rnn_siam_bi_attend'] = prefix + 'model/rnn/siam_bi_attend.h5'
    nn(paths, 'dnn', 'siam_average', 10, 'train')
    nn(paths, 'dnn', 'siam_average', 10, 'dev')
    nn(paths, 'cnn', 'siam_parallel', 10, 'train')
    nn(paths, 'cnn', 'siam_parallel', 10, 'dev')
    nn(paths, 'cnn', 'siam_serial', 10, 'train')
    nn(paths, 'cnn', 'siam_serial', 10, 'dev')
    nn(paths, 'rnn', 'siam_plain', 10, 'train')
    nn(paths, 'rnn', 'siam_plain', 10, 'dev')
    nn(paths, 'rnn', 'siam_stack', 10, 'train')
    nn(paths, 'rnn', 'siam_stack', 10, 'dev')
    nn(paths, 'rnn', 'siam_bi', 10, 'train')
    nn(paths, 'rnn', 'siam_bi', 10, 'dev')
    nn(paths, 'rnn', 'siam_attend', 10, 'train')
    nn(paths, 'rnn', 'siam_attend', 10, 'dev')
    nn(paths, 'rnn', 'siam_bi_attend', 10, 'train')
    nn(paths, 'rnn', 'siam_bi_attend', 10, 'dev')


def join(paths):
    paths['dnn_join_flat'] = prefix + 'model/dnn/join_flat.h5'
    paths['cnn_join_parallel'] = prefix + 'model/cnn/join_parallel.h5'
    paths['cnn_join_serial'] = prefix + 'model/cnn/join_serial.h5'
    paths['rnn_join_plain'] = prefix + 'model/rnn/join_plain.h5'
    paths['rnn_join_stack'] = prefix + 'model/rnn/join_stack.h5'
    paths['rnn_join_bi'] = prefix + 'model/rnn/join_bi.h5'
    nn(paths, 'dnn', 'join_flat', 10, 'train')
    nn(paths, 'dnn', 'join_flat', 10, 'dev')
    nn(paths, 'cnn', 'join_parallel', 10, 'train')
    nn(paths, 'cnn', 'join_parallel', 10, 'dev')
    nn(paths, 'cnn', 'join_serial', 10, 'train')
    nn(paths, 'cnn', 'join_serial', 10, 'dev')
    nn(paths, 'rnn', 'join_plain', 10, 'train')
    nn(paths, 'rnn', 'join_plain', 10, 'dev')
    nn(paths, 'rnn', 'join_stack', 10, 'train')
    nn(paths, 'rnn', 'join_stack', 10, 'dev')
    nn(paths, 'rnn', 'join_bi', 10, 'train')
    nn(paths, 'rnn', 'join_bi', 10, 'dev')


if __name__ == '__main__':
    paths = dict()
    prefix = 'core/'
    paths['train_clean'] = prefix + 'data/train_clean.csv'
    paths['dev_clean'] = prefix + 'data/dev_clean.csv'
    paths['pad_train'] = prefix + 'feat/nn/pad_train.pkl'
    paths['pad_dev'] = prefix + 'feat/nn/pad_dev.pkl'
    paths['train_label'] = prefix + 'data/train_label.txt'
    paths['dev_label'] = prefix + 'data/dev_label.txt'
    paths['embed'] = prefix + 'feat/nn/embed.pkl'
    siam(paths)
    join(paths)
