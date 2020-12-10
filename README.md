# Program with Migen in the VHDPlus IDE

## Setup
1. Install Python 3.6+
2. Clone or download and extract this repository [http://github.com/m-labs/migen](http://github.com/m-labs/migen)
3. Open the console and go to the directory of the repository
```cd [directory]```
4. Install Migen using ```python setup.py develop --user``` or ```python3 ./setup.py develop --user``` for linux

## Program
1. Clone or download and extract this repository
2. Open ```Migen_Tests\Test_Default\Test_Default.vhdpproj``` with the VHDPlus IDE
3. Open the Test.py file to program with Migen <br/>
Here more information: <br/>
[http://blog.lambdaconcept.com/doku.php?id=migen:tutorial](http://blog.lambdaconcept.com/doku.php?id=migen:tutorial)<br/>
[https://m-labs.hk/migen/manual/](https://m-labs.hk/migen/manual/)
4. After you finished coding, open ```Terminal/New Terminal``` in the IDE and convert the python file using ```python [filename].py```
5. In the folder ```build```, you can find the generated top.v file. Add the pins of the module to the Top.qsys.vhdp file so you can use your design together with your vhdp and vhdl files.
6. Now make sure your file with the ```Main``` component uses the new ```Top``` component and click on ```Compile```
