import dropbox

class TransferData:
    def __init__ (self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'rRrVv750ISsAAAAAAAAAAYF9dCK-xENplEyDVQmH2nJK2PN2lSue4YD4g9HCYqWn'
    transferData = TransferData(access_token)
    file_from = input("Write the name of the file to transfer: ")
    file_to = input("Enter the full path including file name to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()