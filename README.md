# Program with Migen in the VHDPlus IDE

## Setup
1. Follow the first step of the LiteX setup below. If you want to use LiteX as well, you don't have to install migen separately.
2. Clone or download and extract this repository http://github.com/m-labs/migen
3. Open the console and go to the directory of the repository
```cd [directory]```
4. Install Migen using ```python setup.py develop --user``` or ```python3 ./setup.py develop --user``` for linux

## Program
1. Clone or download and extract this repository
2. Open ```Migen_Tests\Test_Default\Test_Default.vhdpproj``` with the VHDPlus IDE
3. Open the Test.py file to program with Migen <br/>
Here more information: <br/>
http://blog.lambdaconcept.com/doku.php?id=migen:tutorial<br/>
https://m-labs.hk/migen/manual/ <br/>
https://github.com/m-labs/migen/tree/master/examples/basic
4. After you finished coding, open ```Terminal/New Terminal``` in the IDE and convert the python file using ```python [filename].py``` 
(Check if `Extras/Settings/Detect external` file changes is enabled)
5. The file Test.v created after running the python file
6. Now make sure your file with the ```Main``` component uses the new updated and click on ```Compile```

# Use the LiteX SoC builder

## Setup
#### Windows:
1. Make sure you have Quartus, Git and Python 3.6+ installed  <br/>
- Make sure that the ```Path``` environment variable is set to ```C:\intelFPGA_lite\18.1\quartus\bin64\cygwin\bin```  and ```C:\intelFPGA_lite\18.1\quartus\bin64```
- Install Git here: https://git-scm.com/download/win
- Install Python here: https://www.python.org/downloads/
2. Open the console, go to the directory in that you want to install LiteX and download the setup file using <br/>
```wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py```
3. Install LiteX and Migen using ```python litex_setup.py init install --user```
4. Download and extract the RISC-V toolchain using ```python litex_setup.py gcc```
5. Add the paths for the RISC-V toolchain to the ```Path``` environment variable using <br/>
```set PATH=%PATH%;$PWD\riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-w64-mingw32\bin``` and <br/>
```set PATH=%PATH%;$PWD\riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-w64-mingw32\riscv64-unknown-elf\bin```
5. Try an SoC design using
```
cd litex-boards\litex_boards\targets
python de10lite.py
```

#### Linux:
1. Make sure you have Quartus, Git, Make and Python 3.6+ installed  <br/>
```sudo apt-get install make gcc``` <br/>
```sudo apt install git-all``` <br/>
```sudo apt install python3.8``` <br/>
2. Open the console, go to the directory in that you want to install LiteX and download the setup file using <br/>
```wget https://raw.githubusercontent.com/enjoy-digital/litex/master/litex_setup.py```
- Execute ```chmod +x litex_setup.py```
3. Install LiteX and Migen using  ```./litex_setup.py init install --user``` and ```export PATH=$PATH:~/.local/bin```
4. Download and extract the RISC-V toolchain using ```./litex_setup.py gcc``` 
5. Add the paths for the RISC-V toolchain to the ```Path``` environment variable using <br/>
```export PATH=$PATH:$PWD/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14/bin/``` and <br/>
```export PATH=$PATH:$PWD/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14/riscv64-unknown-elf/bin/```
5. Try an SoC design using
```
cd litex-boards\litex_boards\targets
./de10lite.py
```

## Add the VHDPlus Core (CR00010)

1. Clone or download and extract this repository: https://github.com/micro-FPGA/litex-boards

#### Windows:
2. Find the Python user site using ```python -m site``` and copy the path after ```USER_SITE: ```
3. Execute ```python setup.py install --prefix=[your path]Python38\\site-packages``` in the folder with the repository
4. Try the CR00010 SoC design using (you maybe have to edit the file depending on your hardware configuration)
```
cd litex_boards\partner\targets
python cr00010.py
```

#### Linux:
2. Execute ```sudo ./setup.py install``` in the folder with the repository
3. Try the CR00010 SoC design using (you maybe have to edit the file depending on your hardware configuration))
```
cd litex_boards\partner\targets
./cr00010.py
```
