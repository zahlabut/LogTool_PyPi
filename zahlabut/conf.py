[Settings]
# All "Error BLocks" happened before this time will be skipped.
time_grep = 2018-01-01 00:00:00

# List of directories to analyze (os.walk is used to get all *log files recursively).
log_root_dir = ['/var/log']

# Options are ERROR or WARNING
string_for_grep = ERROR

# If 'yes' logTool result file will be created (to disable set to 'no').
create_logtool_result_file=yes

# File name that will be used to generate LogTool result file.
log_tool_result_file = ResultFile.log

# All these strings are used to detect "problematical" blocks in logs.
magic_words = ['error','traceback','stderr','failed','critical','fatal',"\|err\|",'trace','http error', 'failure']

# These strings are used to ignore "Error Blocks", once detected "Error Block" will be skipped (won't be exported)
ignore_strings = ['completed with no errors','program: Errors behavior:','No error reported.','--exit-command-arg error'
                 ,'Use errors="ignore" instead of skip.','Errors:None','errors, 0','errlog_type error ',
                 'errorlevel = ','Total errors: 0','0 errors,','python-traceback2-','"Error": ""','perl-Errno-',
                 'libgpg-error-','libcom_err-','= CRITICAL ','"Error": ",','stderr F',
                 'fatal_exception_format_errors','failed=0','--log-level error']

# Folowing log paths will be skipped
logs_to_ignore = ['/var/lib/containers/storage/overlay']

# List of all standard Python exceptions, used to detect "Error Blocks"
python_exceptions = ['StopIteration','StopAsyncIteration','ArithmeticError','FloatingPointError',
                   'OverflowError','ZeroDivisionError','AssertionError','AttributeError','BufferError',
                   'EOFError','ImportError','ModuleNotFoundError','LookupError','IndexError','KeyError',
                   'MemoryError','NameError','UnboundLocalError','OSError','BlockingIOError',
                   'ChildProcessError','ConnectionError','BrokenPipeError','ConnectionAbortedError',
                   'ConnectionRefusedError','ConnectionResetError','FileExistsError','FileNotFoundError',
                   'InterruptedError','IsADirectoryError','NotADirectoryError','PermissionError',
                   'ProcessLookupError','TimeoutError','ReferenceError','RuntimeError','NotImplementedError',
                   'RecursionError','SyntaxError','IndentationError','TabError','SystemError','TypeError',
                   'ValueError','UnicodeError','UnicodeDecodeError','UnicodeEncodeError','UnicodeTranslateError']

# All these logs will be enforced to be analyzed as not standard.
# Sometimes messages that supposed to be logged as ERROR are being logged as INFO for example,
# so that is why LogTool will analyze such logs including "magic_strings" without line limitation
# Debug level is in first 60 characters
analyze_log_as_not_standard=['heat_api_cfn.log', 'ansible.log', 'overcloud_deployment','install-undercloud']

# If 'save_standard_logs_raw_data_file' is empty, won't be created
save_standard_logs_raw_data_file='Standard_Logs_Output.log'

# If 'save_not_standard_logs_raw_data_file' is empty, won't be created
save_not_standard_logs_raw_data_file='Not_Standard_Logs_Output.log'
