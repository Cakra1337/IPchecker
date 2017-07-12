import ipaddress
import socket

print '----- Python IP Checker -----'
def main():
        print '1.Check My Local IP'
        print '2.Coming soon.'
        choose = raw_input('Choose : ')
        if choose == '1':
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect_ex(('8.8.8.8',80))
                localIP = s.getsockname()[0]
                ip = ipaddress.ip_address(unicode(localIP))
                print '----local IP : ',localIP
                print '----IP Version : ',ip.version
                s.close()

        elif choose == '2' :
                print 'Coming soon.'
                main()

main()
