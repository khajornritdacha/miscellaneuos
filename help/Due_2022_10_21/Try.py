import csv 

# encoding with utf-8 to read Thai alphabets
with open("in1.txt", encoding="utf-8") as f1, open("in2.txt", encoding="utf-8") as f2:
    rawData = [x.strip().split() for x in f1.readlines()]
    myDict = {x[0]: [x[1]] for x in rawData}

    try:
        # Prepare Data
        rawData2 = [x.strip().split() for x in f2.readlines()]
        for x in rawData2:
            myDict[x[0]].append(x[1])

        # Output .txt file
        with open("out.txt", "w", encoding="utf-8")  as outF:
            for key, val in myDict.items():
                if (len(val) == 1):
                    val.append('-')
                res = key + " " + " ".join(val) + "\n"
                outF.write(res)
        
        # Output .csv file
        with open("out.csv", "w", encoding="utf-8", newline="") as outF:
            writer = csv.writer(outF)
            for key, val in myDict.items():
                res = [key] + val
                writer.writerow(res)
         
    except:
        print("Error Occured")
    


