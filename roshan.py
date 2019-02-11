import serial
import csv
serial_port="/dev/ttyACM0"
baud_rate=9600
write_to_file_path="out.xml"
file2_name=open("anku.csv","w+")
csv_writer=csv.writer(file2_name)
ser=serial.Serial(serial_port,baud_rate)
while True:
    line=ser.readline();
    line = line.decode("utf-8")  # ser.readline returns a binary, convert to string
    # print(line);
    csv_writer.writerow(line)

