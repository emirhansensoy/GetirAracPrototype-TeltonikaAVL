import socket
import json
from AVL import *
import mysql.connector

DATABASE_NAME = "teltonika_avl"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8H*sm4NX2tsV"
)

cursorObject = db.cursor()
sql = "DROP DATABASE IF EXISTS " + DATABASE_NAME
cursorObject.execute(sql)
sql = "CREATE DATABASE " + DATABASE_NAME
cursorObject.execute(sql)
db.commit()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8H*sm4NX2tsV",
    db=DATABASE_NAME
)
cursorObject = db.cursor()


avl_table = """CREATE TABLE IF NOT EXISTS `avl` (
  `IMEI` CHAR(15) NOT NULL,
  `Zero_Bytes` CHAR(8) NOT NULL,
  `Data_Field_Length` CHAR(8) NOT NULL,
  `Codec_ID` CHAR(2) NOT NULL,
  `N_of_Data_1` CHAR(2) NOT NULL,
  `N_of_Data_2` CHAR(2) NOT NULL,
  `CRC_16` CHAR(8) NOT NULL,
  PRIMARY KEY (`IMEI`)
)"""

data_table = """CREATE TABLE IF NOT EXISTS `data_packet` (
  `Data_Packet_ID` VARCHAR(17) NOT NULL,
  `Timestamp` CHAR(16) NOT NULL,
  `Priority` CHAR(2) NOT NULL,
  `Longitude` CHAR(8) NOT NULL,
  `Latitude` CHAR(8) NOT NULL,
  `Altitude` CHAR(8) NOT NULL,
  `Angle` CHAR(4) NOT NULL,
  `Satellites` CHAR(2) NOT NULL,
  `Speed` CHAR(4) NOT NULL,
  `Event_IO_ID` CHAR(2) NOT NULL,
  `N_of_Total_ID` CHAR(2) NOT NULL,
  `N1_of_One_Byte_IO` CHAR(2) NOT NULL,
  `N2_of_Two_Bytes_IO` CHAR(2) NOT NULL,
  `N4_of_Four_Bytes_IO` CHAR(2) NOT NULL,
  `N8_of_Eight_Bytes_IO` CHAR(2) NOT NULL,
  `AVL_IMEI` CHAR(15) DEFAULT NULL,
  PRIMARY KEY (`Data_Packet_ID`),
  KEY `AVL_IMEI_idx` (`AVL_IMEI`),
  CONSTRAINT `IMEI` FOREIGN KEY (`AVL_IMEI`) REFERENCES `avl` (`IMEI`)
)"""

io_desc_table = """CREATE TABLE IF NOT EXISTS `io_desc` (
  `IO_ID` VARCHAR(10) NOT NULL,
  `Property_Name` VARCHAR(200) NOT NULL,
  `Description` VARCHAR(1000) DEFAULT NULL,
  PRIMARY KEY (`IO_ID`)
)"""

io_table = """CREATE TABLE IF NOT EXISTS `io` (
  `Data_ID` VARCHAR(17) NOT NULL,
  `IO_ID` VARCHAR(10) NOT NULL,
  `Value` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`Data_ID`,`IO_ID`),
  KEY `IO_ID_idx` (`IO_ID`),
  CONSTRAINT `DATA_ID` FOREIGN KEY (`Data_ID`) REFERENCES `data_packet` (`Data_Packet_ID`),
  CONSTRAINT `IO_ID` FOREIGN KEY (`IO_ID`) REFERENCES `io_desc` (`IO_ID`)
)"""

cursorObject.execute(avl_table)
cursorObject.execute(data_table)
cursorObject.execute(io_desc_table)
cursorObject.execute(io_table)

db.commit()
imei_list = []
avl_list = []
current_imei = ""

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('172.16.16.221', 1999)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)
while True:
    # Wait for a connection
    connection, client_address = sock.accept()

    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(5000).hex()
            print(data)

            # Checking if the data is an IMEI number
            if data[:5] == "000f3":
                current_imei = data

                if data in imei_list:
                    for i in avl_list:
                        if i.encoded_imei == data:
                            i.parse_imei(data)
                else:
                    imei_list.append(data)
                    avl_list.append(AVL())
                    avl_list[-1].parse_imei(data)

                # Sending back success message
                connection.sendall(format(1, "02x").encode())
            # If data is not an IMEI number then it has to be data
            else:
                temp = ""
                for avl in avl_list:
                    if avl.encoded_imei == current_imei:
                        avl.parse_data(data)
                        temp = str(avl.n_of_data1)

                        cursorObject.execute("SELECT IMEI, COUNT(*) FROM avl WHERE IMEI = %s GROUP BY IMEI", (avl.imei, ))
                        results = cursorObject.fetchall()
                        row_count = cursorObject.rowcount
                        # if table doesnt have the avl then insert it
                        if row_count == 0:
                            cursorObject.execute("INSERT IGNORE INTO avl (IMEI, Zero_Bytes, Data_Field_Length, Codec_ID, N_of_Data_1, N_of_Data_2, CRC_16) VALUES (%s, %s, %s, %s, %s, %s, %s)", (avl.imei, avl.zero_bytes, avl.data_field_length, avl.codec_id, avl.n_of_data1, avl.n_of_data2, avl.crc_16))
                        # avl exits in table. so we need to update it
                        else:
                            cursorObject.execute("UPDATE avl SET IMEI = %s, Zero_Bytes = %s, Data_Field_Length = %s, Codec_ID = %s, N_of_Data_1 = %s, N_of_Data_2 = %s, CRC_16 = %s WHERE IMEI = %s", (avl.imei, avl.zero_bytes, avl.data_field_length, avl.codec_id, avl.n_of_data1, avl.n_of_data2, avl.crc_16, avl.imei))

                        i = 1
                        for data_packet in avl.avl_data_list:
                            cursorObject.execute("SELECT Data_Packet_ID, COUNT(*) FROM data_packet WHERE Data_Packet_ID = %s GROUP BY Data_Packet_ID", (avl.imei + format(i, "02"),))
                            results = cursorObject.fetchall()
                            row_count = cursorObject.rowcount
                            # if table doesnt have the data_packet then insert it
                            if row_count == 0:
                                cursorObject.execute("INSERT IGNORE INTO data_packet (Data_Packet_ID, Timestamp, Priority, Longitude, Latitude, Altitude, Angle, Satellites, Speed, Event_IO_ID, N_of_Total_ID, N1_of_One_Byte_IO, N2_of_Two_Bytes_IO, N4_of_Four_Bytes_IO, N8_of_Eight_Bytes_IO, AVL_IMEI) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (avl.imei + format(i, "02"), data_packet.timestamp, data_packet.priority, data_packet.longitude, data_packet.latitude, data_packet.altitude, data_packet.angle, data_packet.satellites, data_packet.speed, data_packet.event_io_id, data_packet.n_of_total_id, data_packet.n1_of_one_byte_io, data_packet.n2_of_two_bytes_io, data_packet.n4_of_four_bytes_io, data_packet.n8_of_eight_bytes_io, avl.imei))
                            # data_packet exits in table. so we need to update it
                            else:
                                cursorObject.execute("UPDATE data_packet SET Data_Packet_ID = %s, Timestamp = %s, Priority = %s, Longitude = %s, Latitude = %s, Altitude = %s, Angle = %s, Satellites = %s, Speed = %s, Event_IO_ID = %s,N_of_Total_ID = %s, N1_of_One_Byte_IO = %s, N2_of_Two_Bytes_IO = %s, N4_of_Four_Bytes_IO = %s,N8_of_Eight_Bytes_IO = %s, AVL_IMEI = %s WHERE Data_Packet_ID = %s", (avl.imei + format(i, "02"), data_packet.timestamp, data_packet.priority, data_packet.longitude, data_packet.latitude, data_packet.altitude, data_packet.angle, data_packet.satellites, data_packet.speed, data_packet.event_io_id, data_packet.n_of_total_id, data_packet.n1_of_one_byte_io, data_packet.n2_of_two_bytes_io, data_packet.n4_of_four_bytes_io, data_packet.n8_of_eight_bytes_io, avl.imei, avl.imei + format(i, "02")))

                            for io in data_packet.one_byte_io_list:
                                cursorObject.execute("SELECT IO_ID, COUNT(*) FROM io_desc WHERE IO_ID = %s GROUP BY IO_ID", (io,))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount
                                # if table doesnt have the one byte io's then insert it
                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io_desc (IO_ID, Property_Name, Description) VALUES (%s, %s, %s)", (io, data_packet.one_byte_io_list[io]["property_name"], data_packet.one_byte_io_list[io]["description"]))
                                else:
                                    cursorObject.execute("UPDATE io_desc SET IO_ID = %s, Property_Name = %s, Description = %s WHERE IO_ID = %s", (io, data_packet.one_byte_io_list[io]["property_name"], data_packet.one_byte_io_list[io]["description"], io))

                                cursorObject.execute("SELECT IO_ID, Data_ID, COUNT(*) FROM io WHERE IO_ID = %s AND Data_ID = %s GROUP BY IO_ID", (io, avl.imei + format(i, "02")))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io (Data_ID, IO_ID, Value) VALUES (%s, %s, %s)", (avl.imei + format(i, "02"), io, data_packet.one_byte_io_list[io]["value"]))
                                else:
                                    cursorObject.execute("UPDATE io SET IO_ID = %s, Data_ID = %s, Value = %s WHERE IO_ID = %s AND Data_ID = %s", (io, avl.imei + format(i, "02"), data_packet.one_byte_io_list[io]["value"], io, avl.imei + format(i, "02")))

                            for io in data_packet.two_byte_io_list:
                                cursorObject.execute("SELECT IO_ID, COUNT(*) FROM io_desc WHERE IO_ID = %s GROUP BY IO_ID", (io,))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io_desc (IO_ID, Property_Name, Description) VALUES (%s, %s, %s)", (io, data_packet.two_byte_io_list[io]["property_name"], data_packet.two_byte_io_list[io]["description"]))
                                else:
                                    cursorObject.execute("UPDATE io_desc SET IO_ID = %s, Property_Name = %s, Description = %s WHERE IO_ID = %s", (io, data_packet.two_byte_io_list[io]["property_name"], data_packet.two_byte_io_list[io]["description"], io))

                                cursorObject.execute("SELECT IO_ID, Data_ID, COUNT(*) FROM io WHERE IO_ID = %s AND Data_ID = %s GROUP BY IO_ID", (io, avl.imei + format(i, "02")))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io (Data_ID, IO_ID, Value) VALUES (%s, %s, %s)", (avl.imei + format(i, "02"), io, data_packet.two_byte_io_list[io]["value"]))
                                else:
                                    cursorObject.execute("UPDATE io SET IO_ID = %s, Data_ID = %s, Value = %s WHERE IO_ID = %s AND Data_ID = %s", (io, avl.imei + format(i, "02"), data_packet.two_byte_io_list[io]["value"], io, avl.imei + format(i, "02")))

                            for io in data_packet.four_byte_io_list:
                                cursorObject.execute("SELECT IO_ID, COUNT(*) FROM io_desc WHERE IO_ID = %s GROUP BY IO_ID", (io,))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io_desc (IO_ID, Property_Name, Description) VALUES (%s, %s, %s)", (io, data_packet.four_byte_io_list[io]["property_name"], data_packet.four_byte_io_list[io]["description"]))
                                else:
                                    cursorObject.execute("UPDATE io_desc SET IO_ID = %s, Property_Name = %s, Description = %s WHERE IO_ID = %s", (io, data_packet.four_byte_io_list[io]["property_name"], data_packet.four_byte_io_list[io]["description"], io))

                                cursorObject.execute("SELECT IO_ID, Data_ID, COUNT(*) FROM io WHERE IO_ID = %s AND Data_ID = %s GROUP BY IO_ID", (io, avl.imei + format(i, "02")))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io (Data_ID, IO_ID, Value) VALUES (%s, %s, %s)", (avl.imei + format(i, "02"), io, data_packet.four_byte_io_list[io]["value"]))
                                else:
                                    cursorObject.execute("UPDATE io SET IO_ID = %s, Data_ID = %s, Value = %s WHERE IO_ID = %s AND Data_ID = %s", (io, avl.imei + format(i, "02"), data_packet.four_byte_io_list[io]["value"], io, avl.imei + format(i, "02")))

                            for io in data_packet.eight_byte_io_list:
                                cursorObject.execute("SELECT IO_ID, COUNT(*) FROM io_desc WHERE IO_ID = %s GROUP BY IO_ID", (io,))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io_desc (IO_ID, Property_Name, Description) VALUES (%s, %s, %s)", (io, data_packet.eight_byte_io_list[io]["property_name"], data_packet.eight_byte_io_list[io]["description"]))
                                else:
                                    cursorObject.execute("UPDATE io_desc SET IO_ID = %s, Property_Name = %s, Description = %s WHERE IO_ID = %s", (io, data_packet.eight_byte_io_list[io]["property_name"], data_packet.eight_byte_io_list[io]["description"], io))

                                cursorObject.execute("SELECT IO_ID, Data_ID, COUNT(*) FROM io WHERE IO_ID = %s AND Data_ID = %s GROUP BY IO_ID", (io, avl.imei + format(i, "02")))
                                results = cursorObject.fetchall()
                                row_count = cursorObject.rowcount

                                if row_count == 0:
                                    cursorObject.execute("INSERT IGNORE INTO io (Data_ID, IO_ID, Value) VALUES (%s, %s, %s)", (avl.imei + format(i, "02"), io, data_packet.eight_byte_io_list[io]["value"]))
                                else:
                                    cursorObject.execute("UPDATE io SET IO_ID = %s, Data_ID = %s, Value = %s WHERE IO_ID = %s AND Data_ID = %s", (io, avl.imei + format(i, "02"), data_packet.eight_byte_io_list[io]["value"], io, avl.imei + format(i, "02")))

                            i += 1
                            db.commit()

                db.commit()

                # JSON file writing
                with open('file.json', 'w', encoding='utf-8') as json_file:
                    for i in range(len(imei_list)):
                        json.dump(avl_list[i].make_dict(), json_file, indent='\t')
                        avl_list[i].print_avl()

                # Sending back number of data
                print(format(int(hex_to_dec(temp)), "08x").encode())
                connection.sendall(format(int(hex_to_dec(temp)), "08x").encode())

            if data:
                pass
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
        db.close()
