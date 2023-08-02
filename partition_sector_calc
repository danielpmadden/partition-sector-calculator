def bytes_to_sectors(size_mb):
    """
    Convert size in megabytes to the number of sectors.
    
    :param size_mb: Size in MB.
    :type size_mb: int or float
    :return: The number of sectors.
    :rtype: int
    """
    # 1 MB = 1024 * 1024 bytes; 1 sector = 512 bytes
    return size_mb * 1024 * 1024 // 512

def get_input(prompt_text):
    """
    Get input from the user and ensure it's an integer. If not, prompt again.
    
    :param prompt_text: Text to display when prompting the user.
    :type prompt_text: str
    :return: User's input as an integer.
    :rtype: int
    """
    try:
        return int(input(prompt_text))
    except ValueError:
        print("Invalid input. Enter a number.")
        return get_input(prompt_text)

def main():
    """
    Main function to get user input and display partition details.
    """
    starting_sector = get_input("Enter the starting sector: ")
    size_mb = get_input("Enter the partition size in MB: ")

    total_sectors = bytes_to_sectors(size_mb)

    print(f"Starting from sector {starting_sector}, for a partition of {size_mb}MB:")
    print(f"First sector: {starting_sector}")
    print(f"Last sector: {starting_sector + total_sectors - 1}")

if __name__ == "__main__":
    main()
