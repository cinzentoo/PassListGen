FBI_open_up="""
      _                     _              _ _ _      _   _                           _              __
     | |                   | |            | (_) |    | | | |                         | |        _   / /
   __| | ___    _ __   ___ | |_    ___  __| |_| |_   | |_| |__   ___     ___ ___   __| | ___   (_) | | 
  / _` |/ _ \  | '_ \ / _ \| __|  / _ \/ _` | | __|  | __| '_ \ / _ \   / __/ _ \ / _` |/ _ \      | | 
 | (_| | (_) | | | | | (_) | |_  |  __/ (_| | | |_   | |_| | | |  __/  | (_| (_) | (_| |  __/   _  | | 
  \__,_|\___/  |_| |_|\___/ \__|  \___|\__,_|_|\__|   \__|_| |_|\___|   \___\___/ \__,_|\___|  (_) | | 
   ____               _     _                _                                                      \_\
  / __ \             | |   | |              | |                                                        
 | |  | |_ __    __ _| |_  | | ___  __ _ ___| |_                                                       
 | |  | | '__|  / _` | __| | |/ _ \/ _` / __| __|                                                      
 | |__| | |    | (_| | |_  | |  __/ (_| \__ \ |_                                                       
  \____/|_|     \__,_|\__| |_|\___|\__,_|___/\__|     _                               _                
     | |                    | |        | |    | |    | |                             | |               
   __| | ___     _ __   ___ | |_     __| | ___| | ___| |_ ___     _ __ ___  _   _    | |_ __ _  __ _   
  / _` |/ _ \   | '_ \ / _ \| __|   / _` |/ _ \ |/ _ \ __/ _ \   | '_ ` _ \| | | |   | __/ _` |/ _` |  
 | (_| | (_) |  | | | | (_) | |_   | (_| |  __/ |  __/ ||  __/   | | | | | | |_| |   | || (_| | (_| |  
  \__,_|\___/   |_| |_|\___/ \__|   \__,_|\___|_|\___|\__\___|   |_| |_| |_|\__, |    \__\__,_|\__, |  
                                                                             __/ |              __/ |  
                                                                            |___/              |___/   
'donot edit thecode  or at least do not delete mt tag'
                                    I AM cinzentoo_   =))                                                  """



#? so lets start coding :)
megdar=0
#================================== import ha 
import os
import sys
import time
import string
import argparse
import itertools
#==================================tabe ha
def createWordList(chrs, min_length, max_length, output):
    if min_length > max_length:
        print ("[!]>> Please `min_length` must smaller or same as with `max_length`")
        sys.exit()
        
    

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))
        

    print ('[+]>> Creating wordlist at `%s`...' % output)
    print ('[i]>> Start time was: %s' % time.strftime('%H:%M:%S'))

    output = open(output, 'w')

    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()
    output.close()

    print ('\n[i]>> End time: %s' % time.strftime('%H:%M:%S'))

def app():
    print ("""
┬ ┬┌─┐┬─┐┌┬┐  ╦  ┬┌─┐╔╦╗  ┌┬┐┌─┐┬┌─┌─┐┬─┐
││││ │├┬┘ ││  ║  │└─┐ ║   │││├─┤├┴┐├┤ ├┬┘
└┴┘└─┘┴└──┴┘  ╩═╝┴└─┘ ╩   ┴ ┴┴ ┴┴ ┴└─┘┴└─
               BY: Cinzentoo_ ==> Insta & Github
               """)
def main_menu():
    global what_to_do
    press=input (""" hey !
       plese run the app like this again :
            +--------------------------------======== In Linux ========--------------------------------+
            | > python3 passGen.py -chr=xxxxxx -min=x -max=x -out=output/x.txt                         |
            +------------------------------------------------------------------------------------------+
            | or use the full command like this :                                                      |
            | > python3 passGen.py --chars=xxxxxx --min_length=x --max_length=x --output=output/x.txt  |
            +------------------------------------------------------------------------------------------+
            |                                                                                          |
            +-------------------------------======== In Windows ========-------------------------------+
            | > py "the path of file"/passGen.py -chr=xxxxxx -min=x -max=x -out=output/x.txt           |
            +------------------------------------------------------------------------------------------+
            | > py "path"/passGen.py --chars=xxxxxx --min_length=x --max_length=x --output=output/x.txt|
            +------------------------------------------------------------------------------------------+
            |                        ===>> follow me on instagram: Cinzentoo_                          |
            +------------------------------------------------------------------------------------------+""")



#! only for TEST: py C:\Users\Ali\Desktop\pass_Gen\passGen.py -chr=qwert -min=4 -max=5 -out=ForTest/test.txt
#============================================barname asli 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Python Wordlist Generator')
    parser.add_argument(
        '-chr', '--chars',
        default=None, help='characters to iterate')
    parser.add_argument(
        '-min', '--min_length', type=int,
        default=1, help='minimum length of characters')
    parser.add_argument(
        '-max', '--max_length', type=int,
        default=2, help='maximum length of characters')
    parser.add_argument(
        '-out', '--output',
        default='output/wordlist.txt', help='output of wordlist file.')

    args = parser.parse_args()
    if args.chars is None:
        args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    createWordList(args.chars, args.min_length, args.max_length, args.output)
app()
main_menu()