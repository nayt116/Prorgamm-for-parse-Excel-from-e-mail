import os

class Create_diraction:
    def __init__(self, diraction:str):
        self.dir = diraction


    def creat_dir(self):
        os.mkdir(self.dir)