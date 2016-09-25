#!/usr/bin/python
import sys
import re
log = "./log/senseface_gpu.INFO"
def synch_time(log_path, item):
    time = []
    with open(log_path,'r') as f:
        data = f.readlines()
        for line in data:
            # print line
            p = re.compile(r'%s:[0-9]+' % item)
            synch = p.findall(line)
            if synch:
                #print synch
                value = int(re.findall(r'[0-9]+', synch[0])[0])
                if value > 0 and value < 100000:
                    time.append(value)
    #print item
    length = len(time)
    if (length > 0):
        #print "MAX: ", max(time)
        #print "MIN: ", min(time)
        avg = float(sum(time)) / len(time)
        print "AVG:%.2f" % avg,"\tnumber:",length
    return time

if __name__ == '__main__':
    search_item = ("synch_time", "detect_time", "verify_time")
    pl_ = "--------------------------------------------------------------"
    for item in search_item:
        print "\n",pl_
        print "%30s" % item
        print pl_
        for i in range(1,len(sys.argv)):
            log_path = sys.argv[i]
            print "%30s" % log_path,
            ret = synch_time(log_path,item)
            #print len(ret)

