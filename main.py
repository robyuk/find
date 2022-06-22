from pathlib import Path

rootdir=Path('.')

for path in rootdir.rglob('*14*'):
  print(path.absolute())