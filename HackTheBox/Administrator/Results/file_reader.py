import struct

def read_psafe3_file(file_path):
    with open(file_path, 'rb') as file:
        # Read the file header
        header = file.read(16)
        print("Header:", header.hex())

        # Read the file size
        file_size = struct.unpack('>I', file.read(4))[0]
        print("File Size:", file_size)

        # Read the file data
        data = file.read(file_size)
        print("Data:", data.hex())

# Replace 'your_file.psafe3' with the path to your file
read_psafe3_file('Backup.psafe3')
