# Second Draft Transciption.
# export to .csv
# Purpose: Takes all .cha files from a directory and parse through the files
#          which has special characters. Output them all to a seperate new csv ile
# Date: 2/9/21
# Made by: Spencer Ha

import csv
import os
from string import digits

#goes through the entire directory and takes all cha files. change the listdir
#to your dir with the cha files
def main():
    path = "cha_files/"
    filelist = os.listdir(path)

    #change the path to the folder directory where you want your csv files to go to
    write_path = "csv_files"

    writer_txt = open('transcribed_file.txt', 'w')
    for i in filelist:
        counter = 0
        writer_csv = open(os.path.join(write_path, i + '.csv'), 'w')
        csv_writer = csv.writer(writer_csv, delimiter=',')
        if i.endswith(".cha"):
            with open(path + i, 'r') as file:
                print(path + i)
                # if you want a header line saying which file is being transcribed  uncomment the next line
                # writer_txt.write("**** File being transcribed is " + str(i) +" ****" + "\n")
                for line in file:
                #    if line.startswith('@') or line.startswith('\t') or line.startswith('%'):
                #        continue
                    #probably could make the next 3 lines more modualar, but need it to creater the speaker_ID variable before deletion
                    #removes all characters after the '%'. Can change if needed
                    if line[0] == '*':
                    
                        sep = '%'
                        line = line.split(sep, -1)[0]
                        line = line.translate({ord(z): None for z in '⌈⌋⌊⌉_-_().*≈><\t?,∆°↗⇘∬↘⁇↑Ã≤='})
                        if (line[0:2] == 'SP'):
                            speaker_ID = line[0:3]
                        #Deletes all remaining special characters and digits
                        line = line_manipulation(line)
                        print(line)
                        if len(line) < 2: 
                            continue 
                        else:
                            writer_txt.writelines(line)
                            counter = counter + 1
                            csv_writer.writerow([counter,speaker_ID,line])

def line_manipulation(line):
    remove_digits = str.maketrans('', '', digits)

    line = line.translate(remove_digits)
    line = line.replace("SP:", "")
    line = line.strip()
    # removes all whitespace around the line (important to do this BEFORE adding the \n, after removing overlaps)                    
    line = line + "\n"
    #removes all ⌈⌋⌊⌉().*
    line = line.replace(":", "")
    line = line.replace("  ", " ")
    line = line.replace("Mhmm", "mhm")
    line = line.replace("uhm", "um")
    return line

main() 
