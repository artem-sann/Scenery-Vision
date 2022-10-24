with open("descriptions.txt", "r") as f:
    DESCRIPTIONS = [description.stri for description in f.readlines()]

UPLOAD_FOLDER = 'out'
ALLOWED_EXTENSIONS = set(['zip', 'rar', '7z'])
ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

SECRET_KEY = "B1BB7B836CFA2600E09DAE1243DD4ECCA7F23E55"
SESSION_TYPE = "filesystem"
SERVER_FILE_PATH = "upload_file"
PORT = 3350
