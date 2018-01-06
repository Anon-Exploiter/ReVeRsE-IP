"""
_______________.___.
\______   \__  |   |
 |    |  _//   |   |
 |    |   \\____   |
 |______  // ______|
        \/ \/       
   _____         _______           ________        __________.__         ._____________   __________ 
  /  _  \   ____ \   _  \   ____   \_____  \___  __\______   |  |   ____ |__\__    _______\______   \
 /  /_\  \ /    \/  /_\  \ /    \    _(__  <\  \/  /|     ___|  |  /  _ \|  | |    |_/ __ \|       _/
/    |    |   |  \  \_/   |   |  \  /       \>    < |    |   |  |_(  <_> |  | |    |\  ___/|    |   \
\____|__  |___|  /\_____  |___|  / /______  /__/\_ \|____|   |____/\____/|__| |____| \___  |____|_  /
        \/     \/       \/     \/         \/      \/                                     \/       \/ 

                                ~ Changing Coder Name Wont Make You One :)
                                             ~ An0n 3xPloiTeR :)
"""

from insides import *
from sys     import argv
import requests, json
import optparse
import os, re

################################  Banner   ################################

print(Banner)

################################ Functions ################################

def reverseViaHT(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "http://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=url, website=webs)
    request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
    if len(request) != 5:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                write(var="#", color=g, data=_links)
    else:
        write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")

def reverseViaYGS(website):
    website = addHTTP(website); webs = removeHTTP(website)
    url = "https://domains.yougetsignal.com/domains.php"
    post = {
        'remoteAddress' : webs,
        'key' : ''
    }
    request = requests.post(url, headers=functions._headers, timeout=5, data=post).text.encode('UTF-8')

    grab = json.loads(request)

    Status = grab['status']
    IP = grab['remoteIpAddress']
    Domain = grab['remoteAddress']
    Total_Domains = grab['domainCount']
    Array = grab['domainArray']

    if (Status == 'Fail'):
        write(var="#", color=r, data="Sorry! Reverse Ip Limit Reached.")
    else:
        write(var="$", color=c, data="IP: " + IP + "")
        write(var="$", color=c, data="Domain: " + Domain + "")
        write(var="$", color=c, data="Total Domains: " + Total_Domains + "\n")

        domains = []

        for x, y in Array:
            domains.append(x)

        for res in domains:
            write(var="#", color=b, data=res)

def heading(heading, website, color, afterWebHead):
    space = " " * 15
    var = str(space + heading + " '" + website + "'" + str(afterWebHead) + " ..." + space)
    length = len(var) + 1; print "" # \n
    print("{white}" + "-" * length + "-").format(white=w)
    print("{color}" + var).format(color=color)
    print("{white}" + "-" * length + "-").format(white=w); print "" # \n

################################  Args  ################################ 

_usage      = g + "python " + w + argv[0] + g + " --all hackthissite.org" + w
_version    = w + "[" + c + "~" + w + "] " + g + "Version: " + c + "2.0"
parser      = optparse.OptionParser(usage=_usage, version=_version, conflict_handler="resolve")
general     = optparse.OptionGroup(parser, y + 'Basic Help')
general.add_option( '-h', '--help', action='help', dest='help', help='Shows the help for program.')
general.add_option( '-v', '--version', action='version',
    help='Shows the version of program.')

reverse_ip  = optparse.OptionGroup(parser, g + "Reverse IP")
reverse_ip.add_option( "-s", "--revygs",  action='store_true', dest='yougetsignal', help="For Doing Reverse IP Via You Get Signal's API")
reverse_ip.add_option( "-r", "--revht",  action='store_true', dest='hackertarget', help="For Doing Reverse IP Via Hacker Target's  API")

grouped_scanning = optparse.OptionGroup(parser, c + "Grouped Results")
grouped_scanning.add_option( "-a", "--all",  action='store_true', dest='all', help="All Things at Once!")



parser.add_option_group(general)
parser.add_option_group(reverse_ip)
parser.add_option_group(grouped_scanning)

(options, args) = parser.parse_args()
try: website = addHTTP(args[0])
except: pass

try:
    if  options.yougetsignal:
        heading(heading="Doing Reverse IP", website=website, afterWebHead=" Via YGS <3", color=g)
        reverseViaYGS(website)

    elif options.hackertarget:
        heading(heading="Doing Reverse IP", website=website, afterWebHead=" Via HT <3", color=c)
        reverseViaHT(website)

    elif options.all:
        heading(heading="Doing Reverse IP", website=website, afterWebHead=" Via YGS <3", color=g)
        reverseViaYGS(website)

        heading(heading="Doing Reverse IP", website=website, afterWebHead=" Via HT <3", color=c)
        reverseViaHT(website)

    else:
        write(var="~", color=c, data="Usage: " + g + "python " + w + argv[0] + g + " --all hackthissite.org")

except KeyboardInterrupt:
    write(var="~", color=y, data="Err0r: User Interrupted!")

except Exception, e:
    write(var="#", color=r, data="Err0r: Kindly Report the err0r below to An0n3xPloiTeR :) (If Your Internet's Working ;)\n\"\"\"\n" + str(e) + "\n\"\"\"")

print(Footer)

# ~ See Ya :)
# ~ An0n 3xPloiTeR :)