# Cancer Cell Data Analysis

The .DAT files are generated from cancer cell detection system with fix format and large number of count.

These files are feed to Python processor script `dat_file_processor.py` to calcualte the desired output.

Trigger the script with below way on comand line- 

### In case of single input file 
>>> python dat_file_processor.py <file_name>.dat

### In case of multiple files 
```
>>> listOfFiles = ['A1.dat', 'B1.dat', 'C1.dat', 'D1.dat', 'E1.dat', 'F1.dat', 'G1.dat', 'H1.dat']

>>> for inCaseOfMultipleFiles in listOfFiles:
...      python dat_file_processor.py inCaseOfMultipleFiles
```
![cancer](https://user-images.githubusercontent.com/31859032/44418693-b2e79900-a596-11e8-80b6-68217acfe6a7.jpg)
