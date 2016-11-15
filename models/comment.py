from File import File

class Comment(object):
    '''
    object Comment implementation
    '''

    @classmethod
    def get_file_comments(cls, path):
        try:
            file_ = File(path)
            cls.parse
