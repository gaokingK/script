import random
import time
import os
import csv


def gen_timestamp():
    timestp=int(time.time()) - 31*24*3600
    n=0
    while n<30*24*3600:
        n+=1
        timestp += 1
        yield timestp

def gen_csv():
    os.chdir(os.path.dirname(__file__))
    filename = "kpi.res_20240521.csv"

    # Write data to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Writing the data into the file
        csvwriter.writerow(["timestamp","value"])
        for t in gen_timestamp():
            csvwriter.writerow([t, random.randint(60,80)])


    print(f"CSV file '{filename}' created successfully.")




if __name__ == "__main__":
    # g=gen_timestamp()
    # for i in g:
    #     print(i)
    # Define the CSV file name
    gen_csv()
