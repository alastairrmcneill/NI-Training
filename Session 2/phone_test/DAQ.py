import nidaqmx

class DAQ:
    def __init__(self, channel):
        self.channel = channel
        self.task = None
        self.set_task()

    def set_task(self):
        self.task = nidaqmx.Task()
        self.task.ai_channels.add_ai_voltage_chan(self.channel)
    
    def read(self):
        data = self.task.read()
        return data

    def read_multiple_samples(self, number):
        data = self.task.read(number_of_samples_per_channel=number)
        return data

    def close(self):
        self.task.close()
        
        