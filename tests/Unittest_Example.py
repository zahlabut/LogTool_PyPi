from zahlabut.LogTool import *
import os
from configparser import SafeConfigParser
from datetime import datetime
import unittest

conf_file = 'conf_unittest.ini'
class NginxTestCases(unittest.TestCase):
    def setUp(self):
        test_start_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        parser = SafeConfigParser()
        parser.read('conf_unittest.ini')
        parser.set('Settings', 'time_grep', test_start_time)
        parser.set('Settings', 'log_tool_result_file', 'Test_Restart_Errors.log')
        with open(conf_file, 'w') as configfile:
            parser.write(configfile)

    def test_restart_nginx(self):
        for x in range(0, 5):
            # os.system('nginx stop')
            os.system('nginx')

    def tearDown(self):
        load_conf_file(conf_file)
        result = start_analyzing()
