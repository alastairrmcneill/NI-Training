from PhoneTest.DAQ import DAQ

def main(channel):
    d = DAQ(channel)
    data = d.read()
    d.close()
    return data


