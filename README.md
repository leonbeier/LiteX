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

# Use the LiteX SoC builder

## Setup
1. Make sure you have Quartus, Git, Make and Python 3.6+ installed  <br/>
Linux: <br/>
```sudo apt-get install make gcc``` <br/>
```sudo apt install git-all``` <br/>
```sudo apt install python3.8``` <br/>
Windows:
- Make sure that the ```Path``` environment variable is set to ```C:\intelFPGA_lite\18.1\quartus\bin64\cygwin\bin``` 
- Install Git here: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Install Python here: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Open the console, go to the directory in that you want to install LiteX and download the setup file using <br/>
```wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py```
- Linux: Execute ```chmod +x litex_setup.py```
3. Install LiteX and Migen using <br/>
Windows: ```python litex_setup.py init install --user``` <br/>
Linux: ```python litex_setup.py init install --user```
4. Execute ```python litex_setup.py gcc``` and add the paths for the RISC-V toolchain to the ```Path``` environment variable <br/>
```C:\Users\[your path]\litex\riscv64-unknown-elf-gcc...\bin``` and <br/>
```C:\Users\[your path]\litex\riscv64-unknown-elf-gcc...\riscv64-unknown-elf\bin``` <br/>
Restart the console after adding the paths
5. Try an SoC design using
```
cd litex-boards\litex_boards\targets
python de10lite.py
```

