# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:48:53 2023

@author: blake.bavington
"""

import os
path = 'S:\Data & Analytics\Primary Care Analytics\Accreditation'
for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith('.csv') or file.endswith('.xlsx') or file.endswith('.xlsm'):
            print(os.path.join(root,file))