import sys, re, subprocess, shlex, urllib.request, urllib.parse
from colorama import Fore

songs = []


def download_the_damn_song():
    while(True):
        searchx = input(Fore.MAGENTA + 'Song name?: ')
        query = searchx.split(',')
        for search in query:
            if search is "Q" or search is "q":
                print(Fore.RED + "Have fun being broke")
                quit()
            songs.append(input)
            search += " official lyric"
            query_string = urllib.parse.urlencode({"search_query" : search})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            search_result = "http://www.youtube.com/watch?v=" + search_results[0]
            print(Fore.GREEN + '{} song found'.format(search))
            run_command(Fore.CYAN, "youtube-dl --restrict-filenames --ignore-errors -x --audio-format mp3 " + search_result)

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
    print(Fore.BLUE + "Welcome to F*CK Spotify! (press Q and enter to quit)")
    download_the_damn_song()

if __name__ == '__main__':
    main()