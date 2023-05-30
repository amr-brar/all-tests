import dropbox

def save_shared_links_to_file(folder_path, output_file):
    # Dropbox API access token
    access_token = "sl.BfVDarpnKDdyNBySnVCPYKDwt4QFlEMVRoiV1jJ7C_TfmhJQz2_a0pBOzXg_9nH__JM2r0McgbLHQdkhJxlSOqEQ9YQ2XdrBCBKWDLfbuG5B5xNtUIytOEI0lYZlUBa9a284TUpCFohe"

    # Create a Dropbox client
    dbx = dropbox.Dropbox(access_token)

    # List files in the folder
    files = dbx.files_list_folder(folder_path).entries

    # Save shared links to a file
    with open(output_file, "w") as file:
        for file_entry in files:
            # Get the shared link for the file
            shared_link_metadata = dbx.sharing_create_shared_link(file_entry.path_lower)
            shared_link = shared_link_metadata.url

            # Write the shared link to the file
            file.write(shared_link + "\n")

    print("Shared links saved to", output_file)

def generate_direct_download_links(input_file):
    direct_download_links = []

    with open(input_file, "r") as file:
        shared_links = file.read().splitlines()

        for shared_link in shared_links:
            # Convert shared link to direct download link
            direct_download_link = shared_link.replace("www.dropbox.com", "dl.dropboxusercontent.com") + "?dl=1"

            # Add the direct download link to the list
            direct_download_links.append(direct_download_link)

    return direct_download_links

# Example usage
folder_path = "/Mega/PICS-ONLYFANS/hicshehe"
output_file = "links.txt"

# Save shared links to a file
save_shared_links_to_file(folder_path, output_file)

# Generate direct download links from the saved links
direct_download_links = generate_direct_download_links(output_file)

# Print the direct download links
for link in direct_download_links:
    print(link)

    

