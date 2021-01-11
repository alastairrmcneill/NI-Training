from PhoneTest.DAQ import DAQ


def main(channel):
    d = DAQ(channel)
    data = d.read()
    d.close()

    return data


data = main("Dev1/ai0")

f = open("Result.csv", "w")
f.write(str(data))
f.close()



