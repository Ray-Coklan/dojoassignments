class Call(object):
    def __init__(self,unique_id,name,number,time,reason):
        self.unique_id = unique_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print"id: {} name {} number {} time {} reason {}".format(self.unique_id, self.name,self.number,self.time,self.reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = len(self.calls)
    def add(self, unique_id, name, number, time, reason):
        new_call = Call(unique_id, name, number, time, reason)
        self.calls.append(new_call)
        return self
    def displayCalls(self):
        for x in self.calls:
            print x




call1 = Call('789','jonas','233444','3:54','schedule')
call1.display()
callcenter1 = CallCenter()
callcenter1.add('333', 'myname', '234', '90', 'complain').displayCalls()