#!/usr/bin/env python
from . import Path
import six
if six.PY2:
    FileNotFoundError = OSError

def getimgfiles(stem):
    stem = Path(stem).expanduser()
    path = stem.parent
    name = stem.name
    exts = ['.ppm','.bmp','.png','.jpg']
    for ext in exts:
        pat = name+'.*'+ext
        print('searching {}/{}'.format(path,pat))
        flist = sorted(path.glob(pat))
        if flist:
            break

    if not flist:
        raise FileNotFoundError('no files found under {} with {}'.format(stem,exts))

    print('analyzing {} files {}.*{}'.format(len(flist),stem,ext))

    return flist,ext