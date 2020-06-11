#!/bin/python3
import requests, time

def urlRecon(ip):
    try:
        urlList = []
        c = False
        while c == False:
            port = input('Enter Port: ')
            port = str(port)
            if port != '80' and port != '8080' and port != '443':
                print('Wrong input...')
                c = False
            else:
                c = True
                print('Thank you. Checking port {}'.format(str(port)))
                http = 'http://'
                https = 'https://'
                ip = http + ip
                count = 0
                link = open('directoryListSmall.txt', 'r')
                try:
                    for l in link:
                        l = l.strip()
                        fullURL = ip + ':' + port + '/' + str(l) + '.html'
                        print('Trying: {}'.format(str(fullURL)))
                        theRequest = requests.get(fullURL)
                        if theRequest.status_code == 200:
                            print('Found Link:' + str(fullURL))
                            time.sleep(4)
                            urlList.append(fullURL)
                        else:
                            print('....')
                        fullURL = ip + ':' + port + '/' + str(l) + '.php'
                        print('Trying: {}'.format(str(fullURL)))
                        theRequest2 = requests.get(fullURL)
                        if theRequest2.status_code == 200:
                            print('Found Link:' + str(fullURL))
                            time.sleep(4)
                            urlList.append(fullURL)
                        else:
                            print('....')
                        fullURL = ip + ':' + port + '/' + str(l) + '/'
                        print('Trying: {}'.format(str(fullURL)))
                        theRequest3 = requests.get(fullURL)
                        if theRequest3.status_code == 200:
                            print('Found Link:' + str(fullURL))
                            time.sleep(4)
                            urlList.append(fullURL)
                        else:
                            print('....')

                    toC = input('Would you like to try another port? (y or n): ')
                    toC = toC.lower()
                    if toC == 'y':
                        c = False
                    if toC == 'n':
                        c = True
                except KeyboardInterrupt:
                    print('Sorry, failed to run')
                    toC = input('Would you like to try another port? (y or n): ')
                    toC = toC.lower()
                    if toC == 'y':
                        c = False
                    if toC == 'n':
                        c = True
                        return urlList
                    print('........')
                except:
                    toC = input('Would you like to try another port? (y or n): ')
                    toC = toC.lower()
                    if toC == 'y':
                        c = False
                    if toC == 'n':
                        c = True
                        return urlList
                    print('......')

        return urlList
    except KeyboardInterrupt:
        print('Program Stopped')
        print('URL List: ' + str(urlList))
        return urlList
    except:
        print('Error continuing. Ending here and saving data obtained so far. The site may be protected via brute-force attempts')
        return urlList





