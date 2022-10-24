from config import *


def allowed_file(filename):
    return any([extension in filename for extension in ALLOWED_EXTENSIONS])
