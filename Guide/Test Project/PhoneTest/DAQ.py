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
        return self.task.read()

    def close(self):
        self.task.close()
        
