import zipfile
import optparse
from threading import Thread

def execFile(zipName,password):
    try:
        zipName.extractall(pwd=password)
        print password
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f',dest='zname',type='string',help='specifu dictionary file')
    parser.add_option('-d',dest='dname',type='string',help='specifu dictionary file')
    (options,args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=execFile,args=(zFile,password))
        t.start()

if __name__ == '__main__':
    main()




