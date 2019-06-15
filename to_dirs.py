inp_len = sum(1 for line in open("TweetsAirlines_Train.csv"))
prev_sent = ""
prev = ""

with open("TweetsAirlines_Train.csv") as inp:
    
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
            continue
            
        # If its any other line, write the previous if its the start of a new review, or buffer it if its plain text
        if fields[0] == "neutral" or fields[0] == "positive" or fields[0] == "negative":
            print("Writing down previous line %d on folder '%s': %s" % (i, prev_sent, prev))

            with open("train/%s/%d.txt" % (prev_sent, i), 'w+') as out:
                out.write(prev + "\n")
            
            prev = fields[2]
            prev_sent = fields[0]

        else:
            prev += line
            
print("Writing down previous line %d on folder '%s': %s" % (inp_len, prev_sent, prev))
with open("train/%s/%d.txt" % (prev_sent, inp_len), 'w+') as out:
    out.write(prev + "\n")