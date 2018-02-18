from pathlib import Path

def getimgfiles(stem):
    stem = Path(stem).expanduser()
    path = stem.parent
    name = stem.name
    exts = ['.ppm','.bmp','.png','.jpg']
    for ext in exts:
        pat = f'{name}.*{ext}'
        print(f'searching {path/pat}')
        flist = sorted(path.glob(pat))
        if flist:
            break

    if not flist:
        raise FileNotFoundError(f'no files found under {stem} with {exts}')

    print(f'analyzing {len(flist)} files {stem}.*{ext}')

    return flist
