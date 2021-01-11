from PhoneTest.DAQ import DAQ

def main(channel):
    d = DAQ(channel)
    data = d.read()
    d.close()
    return data


# data = main("Dev1/ai0")

# f = open("Results.csv", "w")
# f.write(str(data))
# f.close()


d = DAQ("Dev1/ai0")
data = d.read_multiple_samples(2)
d.close()
print(data)