import os

inp_len = sum(1 for line in open("TweetsAirlines_Test.csv"))
prev_airline = ""
prev_sent = ""
prev = ""

with open("TweetsAirlines_Test.csv") as inp:
    
    for i in range(0, inp_len):
        l = inp.readline()
        print("Just read line: %s" % (l))

        if i == 0:
            # This is the header
            continue
        
        line = l.rstrip()
        fields = line.split(";", 2)
        print("Fields are: %s" % (fields))

        if i == 1:
            # If it is line no. 1, save it in buffers and continue
            prev = fields[2]
            prev_sent = fields[0]
            prev_airline = fields[1]
            continue
            
        # If its any other line, write the previous if its the start of a new review, or buffer it if its plain text
        if fields[0] == "neutral" or fields[0] == "positive" or fields[0] == "negative":
            print("Writing down previous line %d on folder '%s/%s': %s" % (i, prev_airline, prev_sent, prev))

            if not os.path.exists("test/%s/%s" % (prev_airline, prev_sent)):
                print("Creating dir %s/%s" % (prev_airline, prev_sent))
                os.makedirs("test/%s/%s" % (prev_airline, prev_sent))

            with open("test/%s/%s/%d.txt" % (prev_airline, prev_sent, i), 'w+') as out:
                out.write(prev + "\n")
            
            prev = fields[2]
            prev_sent = fields[0]
            prev_airline = fields[1]

        else:
            prev += line
            
print("Writing down previous line %d on folder '%s/%s': %s" % (inp_len, prev_airline, prev_sent, prev))
with open("test/%s/%s/%d.txt" % (prev_airline, prev_sent, inp_len), 'w+') as out:
    out.write(prev + "\n")