import requests
import os

# Create helper class
class Helpers:
    # Define a function to print a blank line
    def space():
        print('\n')
        print('\n')

    # Define a function to download a file
    def download_file(url, file):
        # Define the directory where you want to save the file
        directory = "data/"

        # Create the directory if it does not exist
        os.makedirs(directory, exist_ok=True)

        # Test if the file is already in the directory; if not, download it
        if not os.path.isfile(os.path.join(directory, file)):
            print(f"Downloading {url}...")

            # Send an HTTP GET request to the URL
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open the file in binary write mode and write the contents of the response
                with open(os.path.join(directory, file), "wb") as f:
                    f.write(response.content)
                print("File downloaded successfully.")
            else:
                print(f"Failed to download the file. Status code: {response.status_code}")
