# Define a function to convert size in megabytes to the number of sectors
def bytes_to_sectors(size_mb):
    """
    Convert size in megabytes to the number of sectors.
    
    :param size_mb: Size in MB.
    :type size_mb: int or float
    :return: The number of sectors.
    :rtype: int
    """
    # 1 MB = 1024 * 1024 bytes; 1 sector = 512 bytes
    # Calculate the total number of sectors and return the result
    return size_mb * 1024 * 1024 // 512

# Define a function to get input from the user and ensure it's an integer
def get_input(prompt_text):
    """
    Get input from the user and ensure it's an integer. If not, prompt again.
    
    :param prompt_text: Text to display when prompting the user.
    :type prompt_text: str
    :return: User's input as an integer.
    :rtype: int
    """
    try:
        # Attempt to convert user input to an integer
        return int(input(prompt_text))
    except ValueError:
        # If the input is not a valid integer, display an error message and prompt again
        print("Invalid input. Enter a number.")
        return get_input(prompt_text)

# Define the main function to orchestrate the program logic
def main():
    """
    Main function to get user input and display partition details.
    """
    # Get user input for the starting sector and partition size
    starting_sector = get_input("Enter the starting sector: ")
    size_mb = get_input("Enter the partition size in MB: ")

    # Convert partition size from MB to sectors using the bytes_to_sectors function
    total_sectors = bytes_to_sectors(size_mb)

    # Display partition details including starting and last sector
    print(f"Starting from sector {starting_sector}, for a partition of {size_mb}MB:")
    print(f"First sector: {starting_sector}")
    print(f"Last sector: {starting_sector + total_sectors - 1}")

# Check if the script is run directly (not imported as a module) and call the main function
if __name__ == "__main__":
    main()
