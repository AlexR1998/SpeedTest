Automated SpeedTest command program

This program allows you to test internet download, upload and ping status using speedtest-cli library
The utility of the program is that, this saves the test on a record.csv file and contains an ps1 script for powershell
that allows to automate the process of passing the test each certain time on a day


Usage:
You can change the execution values on test_automation.ps1 and execute it on a powershell console
*$each_time= refers to the time on minutes between each test
*$test_per_time=refers to the number of test executed each n minutes


Deeper Features:
You can edit the executor.py to change the recording file specification, such as name and directory.
By default, the record file is nameed as "record.csv" and saved on the root folder of the program.

ConsoleApp.py is a console application that contains a list of useful tools for pass test and analyze results.
automatic_test corresponds to the PowerShell automatic execution that allows to execute n test each cenrtain minutes automatically.

The program execution want to be done from windows PowerShell accesing to the folder and executing "python ConsoleApp.py" or "automatic_test.ps1".