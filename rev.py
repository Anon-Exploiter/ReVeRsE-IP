from colorama import init,Fore,Back,Style
import requests, re
import json
import os

__header__ = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

##########################   Some Colors We Need :P #########################

if os.name == "posix":
    # colors foreground text:
    fc = "\033[0;96m"
    fg = "\033[0;92m"
    fw = "\033[0;97m"
    fr = "\033[0;91m"
    fb = "\033[0;94m"
    fy = "\033[0;33m"
    fm = "\033[0;35m"

    # colors background text:
    bc = "\033[46m"
    bg = "\033[42m"
    bw = "\033[47m"
    br = "\033[41m"
    bb = "\033[44m"
    by = "\033[43m"
    bm = "\033[45m"

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT
else:
    ## ----------------------------------------------------------------------------------------------------------------------  ##
    init(autoreset=True)
    # colors foreground text:
    fc = Fore.CYAN
    fg = Fore.GREEN
    fw = Fore.WHITE
    fr = Fore.RED
    fb = Fore.BLUE
    fy = Fore.YELLOW
    fm = Fore.MAGENTA
    

    # colors background text:
    bc = Back.CYAN
    bg = Back.GREEN
    bw = Back.WHITE
    br = Back.RED
    bb = Back.BLUE
    by = Fore.YELLOW
    bm = Fore.MAGENTA

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT
    ## ----------------------------------------------------------------------------------------------------------------------  ##

def main():

    banner = '''
%s%s__________     ____   ____    __________       ___________  ._____________ 
%s%s\\______   \\ ___\\   \\ /   /____\\______   \\ _____\\_   _____/  |   \______   \\
%s%s |       _// __ \   Y   // __ \|       _//  ___/|    __)_   |   ||     ___/
%s%s |    |   \  ___/\     /\  ___/|    |   \\\\___ \ |        \  |   ||    |    
%s%s |____|_  /\___  >\___/  \___  >____|_  /____  >_______  /  |___||____|  ~ %s%sBy %s%sAn0n 3xPloiTeR :)
%s%s        \/     \/            \/       \/     \/        \/                  
    ''' % (fc,sb, fc,sb, fc,sb, fb,sb, fb,sb, fr,sb ,fc,sb, fb,sb )

    footer = "\n  %s%s[%s%s$%s%s] %s%sThanks For Using :D\n\t%s%s~%s%s %s%sAn0n 3xPloiTeR%s%s :)\n" % (
            fw, sb,
            fg, sb,
            fw, sb,
            fc, sb,
            fb, sb,
            fw, sb,
            fr, sb,
            fw, sb
        )

    web = "https://domains.yougetsignal.com/domains.php"

    print banner

    dom = raw_input(""+fw+sb+"["+fc+sb+"$"+fw+sb+"] "+fc+sb+"Please Enter Website: "+fc+sb)
    print ""

    post = {
        'remoteAddress' : dom,
        'key' : ''
    }

    try:

        req = requests.post(web, headers=__header__, data=post).content

    except requests.exceptions.ConnectionError:
        print "\nErr0r: Sorry! You Entered A Wrong Website 0r Website Is 0ff."

    grab = json.loads(req)

    if (grab['status'] == 'Fail'):
        print fw+sb+"["+fc+sb+"@"+fw+sb+"] " + "Err0r ~ " + "Sorry! Reverse Ip Limit Reached."

    # elif (re.match("Invalid remote address", grab['message'])):
    #     print fw+sb+"["+fc+sb+"@"+fw+sb+"] " + "Err0r ~ " + "Wrong Website Given :')"

    else:

        print fw+sb+"["+fc+sb+"$"+fw+sb+"] "+fg+sb+"IP: " + grab['remoteIpAddress']
        print fw+sb+"["+fc+sb+"$"+fw+sb+"] "+fg+sb+"Domain: " + grab['remoteAddress']
        print fw+sb+"["+fc+sb+"$"+fw+sb+"] "+fg+sb+"Total Domains: " + grab['domainCount'] + "\n"

        domains = []

        for x, y in grab['domainArray']:
            domains.append(x)

        for res in domains:
            print fw+sb+"["+fb+sb+"~"+fw+sb+"] " + fr+sb+res

    print footer

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\n"+fw+sb+"["+fc+sb+"$"+fw+sb+"] "+fr+sb+"Err0r: "+fc+sb+"User Interrupted :')"
