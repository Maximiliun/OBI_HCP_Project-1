#!/usr/bin/python
# Download R-fMRI, structural, and diffusion for 10 unrelated subjects
# Requires HCP-customized pyxnat:
#   https://github.com/Human-Connectome-Project/pyxnat/tree/hcp-db
#
# Author: Francisco Salido and Kevin A. Archie
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# described in MIT License:
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
# associated documentation files (the "Software"), to deal in the Software without restriction, including without 
# limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the 
# Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  
import sys, getpass
import pyxnat

# List E

unrelated_fem_10 = ['131217', '131419', '131722', '132118', '133019', '134223', '134425', '135528', '135932', '139435']

unrelated_masc_10 = ['145632', '146533', '146836', '147030', '148436', '148941', '149741', '150019', '150625', '151526']

# unrelated_masc_40 = ['100206', '100610', '101309', '101410', '102109',
                '102513', '102715', '103111', '105216', '106319',
                '110613', '112112', '114621', '114924', '116423',
                '116524', '116726', '118225', '118932', '121315',
                '110613', '112112', '114621', '114924', '116423', 
                '116524', '116726', '118225', '118932', '121315',  
                '145632', '146533', '146836', '147030', '148436', 
                '148941', '149741', '150019', '150625', '151526']
  
structural = ['3T_Structural_preproc']
diffusion = ['3T_Diffusion_preproc']
r_fMRI = ['3T_rfMRI_REST1_preproc','3T_rfMRI_REST2_preproc']
  
def main():
    user = sys.argv[1] if 2 <= len(sys.argv) else raw_input('ConnectomeDB user: ')
    password = sys.argv[2] if 3 <= len(sys.argv) else getpass.getpass()
  
    cdb = pyxnat.Interface('https://db.humanconnectome.org', user, password)
  
    cdb.packages.download(unrelated_fem_10, structural + diffusion + r_fMRI)
    
    cdb.packages.download(unrelated_masc_10, structural + diffusion + r_fMRI)

if __name__ == '__main__':
    main()
