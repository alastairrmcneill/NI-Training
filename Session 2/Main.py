from phone_test.DAQ import DAQ

def example(channel):
    d = DAQ(channel)
    data = d.read()
    d.close()
    return data

