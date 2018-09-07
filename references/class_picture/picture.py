import os
from PIL import Image as PilImage


class Image(object):
    def __init__(self, dir_entry):
        # NOTE: os.DirEntry is yielded by generator os.scandir(path='.')
        self.name = dir_entry.name
        self.path = dir_entry.path
        self.stat = dir_entry.stat()  # W.I.P

    def get_name(self):
        '''
        Signature: None -> String
        Purpose: Return a string showing name of object
        Examples: self.get_name() -> "ABC.png"
        '''
        return self.name

    def get_path(self):
        '''
        Signature: None -> String
        Purpose: Return a string showing path of object
        Examples: self.get_path() -> "./Pictures/ABC.png"
        '''
        return self.path

    def get_stat(self):
        '''
        Signature: None -> Dictionary
        Purpose: Return a dictionary showing stat of object
        Examples: self.get_stat() -> {}
        '''
        # Get file type
        name = self.get_name().split('.')
        type = name[-1].upper()

        stat = {
            'type': type,
            'size': self.stat.st_size,
            'created': self.stat.st_ctime,
            'accessed': self.stat.st_atime,
            'modified': self.stat.st_mtime
        }
        # TODO: Convert timestamp using lambda function and
        # datetime.time.fromtimestamp(timestamp / 1e3)
        return stat

    def get_resolution(self):
        '''
        Signature: None -> Tuple: (width, height)
        Purpose: Return a tuple showing resolution of object
        Examples: self.get_resolution() -> (1920, 1080)
        '''
        path = self.get_path()
        with PilImage.open(path) as image:
            return image.size

    def get_aspect_ratio(self):
        '''
        Signature: None -> Tuple (width, height)
        Purpose: Return a tuple that shows aspect ratio of object
        based on resolution provided by get_resolution()
        Examples: self.get_aspect_ratio() -> (16, 9)
        '''
        # TODO: Continue

    def add_watermark(self, logo):
        pass

    def __str__(self):
        '''Signature: None -> String
        '''
        return f'''\
Name: {self.get_name()}
Path: {self.get_path()}
Stat: {self.get_stat()}
Resolution: {self.get_resolution()}\
'''

    def __repr__(self):
        return ''' '''  # TODO: W.I.P


# Test
with os.scandir(path='/home/thang/Pictures') as dir_entries:
    for dir_entry in dir_entries:
        dir_entry = Image(dir_entry)
        print(dir_entry)
        input()
