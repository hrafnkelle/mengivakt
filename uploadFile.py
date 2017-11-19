#!/usr/bin/env python3

import sys
import dropbox
import os
import uploadConfig as cfg


#dbx=dropbox.Dropbox(cfg.access_token)

filename=sys.argv[1][:-1]
f=open(filename,'rb')
#dbx.files_upload(f.read(),path='/mengivakt/{}'.format(os.path.basename(filename)),mute=True,autorename=True)
f.close()
os.remove(filename)
