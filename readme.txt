Automated SpeedTest command program

This program allows to test internet download, upload and ping status using speedtest-cli library
The utility of the program is that, this saves the test on a record.csv file and contains an ps1 script for powershell
that allows to automate the process of passing the test each certain time on a day


Usage:
You can change the execution values on test_automation.ps1 and execute it on a powershell console
*$each_time= refers to the time on minutes between each test
*$test_per_time=refers to the number of test executed each n minutes


Deeper Features:
You can edit the executor.py to change the recording file specification, such as name and directory.
By default, the record file is nameed as "record.csv" and saved on the root folder of the program.

Executing on Windows Init:
You can allow Windows to execute automatically the test_automation.ps1 script creting a file named "startup.cmd" on the path:
*C:\Users\<user name>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
And adding the content:
*PowerShell -Command "Set-ExecutionPolicy Unrestricted" >> "%TEMP%\StartupLog.txt" 2>&1
*PowerShell <parth to the test_automation.ps1 file> >> "%TEMP%\StartupLog.txt" 2>&1