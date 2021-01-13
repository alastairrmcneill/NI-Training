from phone_test.DAQ import DAQ
from phone_test.File_IO import File_IO

d = DAQ("Dev1/ai0")
f = File_IO("Results")

data = d.read()
print(data)
f.write_csv(data)
f.write_txt(data)



data = d.read_multiple_samples(10)
print(data)

def main(channel):
    d = DAQ(channel)
    data = d.read()
    d.close()
    return data