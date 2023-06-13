from mega import Mega
email = "6ptd2@loptagt.com"
password = "xLxVdi.!pFs_n4p"
# mega_file_url = "https://mega.nz/file/M0pG0RJY#4SP_YNn4_N8aku90jK2lK8aDwEe55r5GtmvwJdsCmno"
# api_url = "https://api.gofile.io/uploadFile"

mega = Mega()
m = mega.login(email, password)
files = m.get_files()
# Specify the filename you want to download
filename = "hwpSlRjC"

# Find the file using the filename
file = m.find(filename)

# Download the file
m.download(file)
