class File_IO:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def write_csv(self, data):
        f = open(self.file_name + ".csv", "w")
        f.write(data)
        f.close()

    def write_txt(self, data):
        f = open(self.file_name + ".txt", "w")
        f.write(data)
        f.close()