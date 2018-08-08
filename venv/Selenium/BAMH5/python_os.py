
import sys
sys.stderr.write('this is stderr text\n')
sys.stderr.flush()
sys.stdout.write('this is stdout text\n')

print(sys.argv)
import urllib.request
import urllib.parse
x = urllib.request.urlopen('http://baidu.com/')
print(x.read())

