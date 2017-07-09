# ifsc-code

[![Join the chat at https://gitter.im/ifsc-code/Lobby](https://badges.gitter.im/ifsc-code/Lobby.svg)](https://gitter.im/ifsc-code/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Script for downloading and generating bank IFSC code data in multiple formats ( Excel, JSON etc)

## Installation  
    pip install ifsccode    

## Example 
```python
from ifsccode.ifsc_code import get_ifsc_code
get_ifsc_code(out_dir, file_type, verbose)
```
> out_dir, is path to output directory where files will be placed (Mandatory)

> file_type, type of the ouput file e.g EXCEL/JSON (Optional)

> verbose, to increase the verbosity of program e.g True or False (Optional)
    
