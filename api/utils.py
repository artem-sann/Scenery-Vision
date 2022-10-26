from config import *


def batch_splitter(iterable, batch_size):
    """
    Splits an iterable into batches of some batch_size.
    Args:
        iterable (any iterable): iterable to split
        batch_size (int): size of one batch
    Yields:
        list: array of batch size
    """
    iterable_length = len(iterable)

    for i in range(0, iterable_length, batch_size):
        yield iterable[i:min(i + batch_size, iterable_length)]


def allowed_file(filename):
    return any([extension in filename for extension in ALLOWED_EXTENSIONS])
