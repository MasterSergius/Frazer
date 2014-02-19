# Frazer
# Shows random fun phrases via Tkinter window with set time intervals
#
# Version 2.1
# Author: Serhii Buniak

# Standard modules
import os
import sys
import time
import subprocess
import ConfigParser
import random

# Non-standard modules, need to install
import chardet

# Self modules
import mydaemon

class Frazer(mydaemon.Daemon):
    def __init__(self, *args, **kwargs):
        """ Initializes class """
        super(Frazer, self).__init__(*args, **kwargs)
        self._get_config()

    def _get_config(self):
        """ Gets config """
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(os.environ['PRODROOT'],'etc/frazer.cfg'))
        self.path_to_files = self.config.get('general', 'path_to_files')
        self.sleep = int(self.config.get('general','timeout'))

    def _get_file_list(self):
        """ Gets list of files from self.path_to_files """
        filelist = [item for item in os.listdir(self.path_to_files)
                    if os.path.isfile(os.path.join(self.path_to_files, item))]
        return filelist

    def get_phrase(self):
        """ Gets random phrase from file """
        filelist = self._get_file_list()
        path_to_file =  os.path.join( self.path_to_files,
                             random.choice(filelist) )
        with open(path_to_file) as f:
            lines = f.readlines()
        phrase = random.choice(lines)
        with open(path_to_file) as f:
            phrase_encoding = chardet.detect(f.read())['encoding']
        return phrase.decode(phrase_encoding).strip()

    def show_phrase(self, phrase):
        """ Shows phrase via tkinter window """
        path_to_tkinter_message_script = os.path.join(os.environ['PRODROOT'], 'src/show_tkinter_message.py')
        phrase = "%s" % (phrase.replace('"','\\"'),)
        subprocess.call('python %s "%s"' % (path_to_tkinter_message_script, phrase.encode('utf-8')), shell=True)

    def run(self):
        """ Always runs until stop daemon """
        while True:
            phrase = self.get_phrase()
            self.show_phrase(phrase)
            time.sleep(self.sleep)

if __name__ == '__main__':
    daemon = Frazer('/tmp/frazer_daemon.pid', stderr='/tmp/frazer_error.log')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print 'Unknown command'
            sys.exit(2)
        sys.exit(0)
    else:
        print 'usage: %s start|stop|restart' % sys.argv[0]
        sys.exit(2)
