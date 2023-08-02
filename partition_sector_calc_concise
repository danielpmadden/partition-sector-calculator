def bytes_to_sectors(size_mb):
    return size_mb * 2 * 1024

def main():
    try:
        starting_sector = int(input("Enter the starting sector: "))
        size_mb = int(input("Enter the partition size in MB: "))
        
        total_sectors = bytes_to_sectors(size_mb)
        
        print(f"From sector {starting_sector} for {size_mb}MB -> Last sector: {starting_sector + total_sectors - 1}")
    except ValueError:
        print("Invalid input. Enter a number.")

if __name__ == "__main__":
    main()
