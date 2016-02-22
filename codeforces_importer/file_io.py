import os

WRITE_FLAGS = os.O_CREAT | os.O_WRONLY


def write_to_file(file_path, content):
    """Writes content to file at file_path. Creates file if not present, overwrites it otherwise.

    :param file_path: path of file
    :param content: content to be written
    """

    try:
        print 'writing to file ' + file_path
        file_handle = os.open(file_path, WRITE_FLAGS)
        with os.fdopen(file_handle, 'w') as file_obj:
            file_obj.write(content)
    except OSError as ex:
        print 'Error: ' + ex.strerror
        raise ex
    except ValueError as ex:
        print 'Error: ' + ex.message
        raise ex
