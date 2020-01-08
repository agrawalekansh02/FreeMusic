import sys
import urllib.request
import urllib.parse
import re
import subprocess
import shlex
from colorama import Fore


def download_the_damn_song():
    while(True):
        search = input(Fore.MAGENTA + 'Song name?: ')
        if search is "Q" or search is "q":
            print(Fore.RED + "Have fun being broke")
            break
        search += " official lyric"
        query_string = urllib.parse.urlencode({"search_query" : search})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        search_result = "http://www.youtube.com/watch?v=" + search_results[0]
        print(Fore.GREEN + '{} song found'.format(search))
        run_command(Fore.CYAN, "youtube-dl --restrict-filenames --ignore-errors -x --audio-format mp3 " + search_result)

#def clean_up():
    #run_command(Fore.LIGHTGREEN_EX, "python3 brainztag.py")

def run_command(color, command):
    process = subprocess.Popen(shlex.split(command), stdout = subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(color + str(output.strip()))
    rc = process.poll()


def main():
    print(Fore.BLUE + "Welcome to F*CK Spotify! (press Q to quit)")
    download_the_damn_song()   
    #clean_up()


if __name__ == '__main__':
    main()