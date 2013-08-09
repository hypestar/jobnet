__author__ = "Jacob Dueholm"

def __getCredentialsFromFile():
    f = open('.credentials')
    lines = f.readlines()
    f.close()
    if (len(lines) >= 2):
        username = lines[0]
        username = __trim(username)
        password = password = lines[1]
        password = __trim(password)
        return {'Username': username,'Password': password}

def __trim(untrimmed):    
    untrimmed = untrimmed.replace(" ", "")
    return untrimmed.rstrip('\n')

if __name__ == "__main__":
    __getCredentialsFromFile()
