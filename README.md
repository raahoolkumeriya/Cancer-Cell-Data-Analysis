# Cancer Cell Data Analysis

The .DAT files are generated from cancer cell detection system with fix format and large number of count.

These files are feed to Python processor script (dat_file_processor.py) to calcualte the desired output.

Trigger the script with below way on comand line- 

- ( in case of single input file )
>>> python dat_file_processor.py <file_name>.dat

- ( in case of multiple files )
>>> for multiple_input_files in [ list of input files ]:
...      python dat_file_processor.py multiple_input_files
