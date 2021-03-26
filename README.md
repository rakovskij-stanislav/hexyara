# hexyara - hex output for yara searches

It works as preloader for your selected yara engine and add `-s` paramenet if it is obedient.

### How to install
```bash
chmod +x hexyara.py
sudo cp hexyara.py /usr/bin/
```

In Windows - Just drop it to any folder in $PATH. For example:
```cmd
>where python
C:\Program Files\Python37\python.exe
>cp hexyara.py C:\Program Files\Python37\python.exe
```

### How to use
```bash
hexyara.py yara <count_of_extra_symbols> <your_yara_command>
```
### Examples:
In this example I will use compiled the newest version as a demonstration of use non-system yara. You can use any yara.
```bash
> hexyara.py ./yara-4.0.5/yara ./pyinstaller_rule.yar -r ./pyinstaller_matches/
./pyinstaller_matches//1
0x22240:$zip:25
00022240  25 73 25 63 62 61 73 65  5f 6c 69 62 72 61 72 79 |%s%cbase_library|
00022250  2e 7a 69 70 25 63 25 73  00 00 00 00 00 00 00 00 |.zip%c%s........|
00022260  73 79 73 2e 70 61 74 68  20 28 62 61 73 65 64 20 |sys.path (based |
00022270  6f 6e 20 25 73 29 20 65  78 63 65 65 64 73 20 62 |on %s) exceeds b|
00022280  75 66 66 65 72 5b 25 64  5d 20 73 70 61 63 65 0a |uffer[%d] space.|
00022290  00 00 00 00 00 00 00 00  46 61 69 6c 65 64 20 74 |........Failed t|
000222a0  6f 20 63 6f 6e 76 65 72  74 20 70 79 70 61 74 68 |o convert pypath|
0x224e8:$tmpdir:19
000224e8  70 79 69 2d 72 75 6e 74  69 6d 65 2d 74 6d 70 64 |pyi-runtime-tmpd|
000224f8  69 72 00 00 00 00 00 00  49 4e 54 45 52 4e 41 4c |ir......INTERNAL|
00022508  20 45 52 52 4f 52 3a 20  63 61 6e 6e 6f 74 20 63 | ERROR: cannot c|
00022518  72 65 61 74 65 20 74 65  6d 70 6f 72 61 72 79 20 |reate temporary |
00022528  64 69 72 65 63 74 6f 72  79 21 0a 00 2e 00 00 00 |directory!......|
./pyinstaller_matches/2
0x20484:$zip:25
00020484  25 73 25 63 62 61 73 65  5f 6c 69 62 72 61 72 79 |%s%cbase_library|
00020494  2e 7a 69 70 25 63 25 73  00 00 00 00 73 79 73 2e |.zip%c%s....sys.|
000204a4  70 61 74 68 20 28 62 61  73 65 64 20 6f 6e 20 25 |path (based on %|
000204b4  73 29 20 65 78 63 65 65  64 73 20 62 75 66 66 65 |s) exceeds buffe|
000204c4  72 5b 25 64 5d 20 73 70  61 63 65 0a 00 00 00 00 |r[%d] space.....|
000204d4  46 61 69 6c 65 64 20 74  6f 20 63 6f 6e 76 65 72 |Failed to conver|
000204e4  74 20 70 79 70 61 74 68  20 74 6f 20 77 63 68 61 |t pypath to wcha|
0x205f8:$tmpdir:19
000205f8  70 79 69 2d 72 75 6e 74  69 6d 65 2d 74 6d 70 64 |pyi-runtime-tmpd|
00020608  69 72 00 00 49 4e 54 45  52 4e 41 4c 20 45 52 52 |ir..INTERNAL ERR|
00020618  4f 52 3a 20 63 61 6e 6e  6f 74 20 63 72 65 61 74 |OR: cannot creat|
00020628  65 20 74 65 6d 70 6f 72  61 72 79 20 64 69 72 65 |e temporary dire|
00020638  63 74 6f 72 79 21 0a 00  2e 00 00 00 2e 00 2e 00 |ctory!..........|
./pyinstaller_matches/3
0x20768:$tmpdir:19
00020768  70 79 69 2d 72 75 6e 74  69 6d 65 2d 74 6d 70 64 |pyi-runtime-tmpd|
00020778  69 72 00 00 49 4e 54 45  52 4e 41 4c 20 45 52 52 |ir..INTERNAL ERR|
00020788  4f 52 3a 20 63 61 6e 6e  6f 74 20 63 72 65 61 74 |OR: cannot creat|
00020798  65 20 74 65 6d 70 6f 72  61 72 79 20 64 69 72 65 |e temporary dire|
000207a8  63 74 6f 72 79 21 0a 00  2e 00 00 00 2e 00 2e 00 |ctory!..........|
```

```bash
> hexyara.py 128 ./yara-4.0.5/yara ./pyinstaller_rule.yar -r ./pyinstaller_matches/
./pyinstaller_matches//1
0x20484:$zip:25
00020484  25 73 25 63 62 61 73 65  5f 6c 69 62 72 61 72 79 |%s%cbase_library|
00020494  2e 7a 69 70 25 63 25 73  00 00 00 00 73 79 73 2e |.zip%c%s....sys.|
000204a4  70 61 74 68 20 28 62 61  73 65 64 20 6f 6e 20 25 |path (based on %|
000204b4  73 29 20 65 78 63 65 65  64 73 20 62 75 66 66 65 |s) exceeds buffe|
000204c4  72 5b 25 64 5d 20 73 70  61 63 65 0a 00 00 00 00 |r[%d] space.....|
000204d4  46 61 69 6c 65 64 20 74  6f 20 63 6f 6e 76 65 72 |Failed to conver|
000204e4  74 20 70 79 70 61 74 68  20 74 6f 20 77 63 68 61 |t pypath to wcha|
000204f4  72 5f 74 0a 00 00 00 00  45 72 72 6f 72 20 64 65 |r_t.....Error de|
00020504  74 65 63 74 65 64 20 73  74 61 72 74 69 6e 67 20 |tected starting |
00020514  50 79 74 68 6f 6e 20 56  4d 2e 00 00 73 74 72 69 |Python VM...stri|
0x205f8:$tmpdir:19
000205f8  70 79 69 2d 72 75 6e 74  69 6d 65 2d 74 6d 70 64 |pyi-runtime-tmpd|
00020608  69 72 00 00 49 4e 54 45  52 4e 41 4c 20 45 52 52 |ir..INTERNAL ERR|
00020618  4f 52 3a 20 63 61 6e 6e  6f 74 20 63 72 65 61 74 |OR: cannot creat|
00020628  65 20 74 65 6d 70 6f 72  61 72 79 20 64 69 72 65 |e temporary dire|
00020638  63 74 6f 72 79 21 0a 00  2e 00 00 00 2e 00 2e 00 |ctory!..........|
00020648  00 00 00 00 5c 00 00 00  2a 00 00 00 57 41 52 4e |....\...*...WARN|
00020658  49 4e 47 3a 20 66 69 6c  65 20 61 6c 72 65 61 64 |ING: file alread|
00020668  79 20 65 78 69 73 74 73  20 62 75 74 20 73 68 6f |y exists but sho|
00020678  75 6c 64 20 6e 6f 74 3a  20 25 73 0a 00 00 00 00 |uld not: %s.....|
00020688  77 62 00 00 45 72 72 6f  72 20 63 72 65 61 74 69 |wb..Error creati|
./pyinstaller_matches//2
0x22240:$zip:25
00022240  25 73 25 63 62 61 73 65  5f 6c 69 62 72 61 72 79 |%s%cbase_library|
00022250  2e 7a 69 70 25 63 25 73  00 00 00 00 00 00 00 00 |.zip%c%s........|
00022260  73 79 73 2e 70 61 74 68  20 28 62 61 73 65 64 20 |sys.path (based |
00022270  6f 6e 20 25 73 29 20 65  78 63 65 65 64 73 20 62 |on %s) exceeds b|
00022280  75 66 66 65 72 5b 25 64  5d 20 73 70 61 63 65 0a |uffer[%d] space.|
00022290  00 00 00 00 00 00 00 00  46 61 69 6c 65 64 20 74 |........Failed t|
000222a0  6f 20 63 6f 6e 76 65 72  74 20 70 79 70 61 74 68 |o convert pypath|
000222b0  20 74 6f 20 77 63 68 61  72 5f 74 0a 00 00 00 00 | to wchar_t.....|
000222c0  45 72 72 6f 72 20 64 65  74 65 63 74 65 64 20 73 |Error detected s|
000222d0  74 61 72 74 69 6e 67 20  50 79 74 68 6f 6e 20 56 |tarting Python V|
0x224e8:$tmpdir:19
000224e8  70 79 69 2d 72 75 6e 74  69 6d 65 2d 74 6d 70 64 |pyi-runtime-tmpd|
000224f8  69 72 00 00 00 00 00 00  49 4e 54 45 52 4e 41 4c |ir......INTERNAL|
00022508  20 45 52 52 4f 52 3a 20  63 61 6e 6e 6f 74 20 63 | ERROR: cannot c|
00022518  72 65 61 74 65 20 74 65  6d 70 6f 72 61 72 79 20 |reate temporary |
00022528  64 69 72 65 63 74 6f 72  79 21 0a 00 2e 00 00 00 |directory!......|
00022538  2e 00 2e 00 00 00 00 00  5c 00 00 00 2a 00 00 00 |........\...*...|
00022548  57 41 52 4e 49 4e 47 3a  20 66 69 6c 65 20 61 6c |WARNING: file al|
00022558  72 65 61 64 79 20 65 78  69 73 74 73 20 62 75 74 |ready exists but|
00022568  20 73 68 6f 75 6c 64 20  6e 6f 74 3a 20 25 73 0a | should not: %s.|
00022578  00 00 00 00 77 62 00 00  45 72 72 6f 72 20 63 72 |....wb..Error cr|
./pyinstaller_matches//3
0x20768:$tmpdir:19
00020768  70 79 69 2d 72 75 6e 74  69 6d 65 2d 74 6d 70 64 |pyi-runtime-tmpd|
00020778  69 72 00 00 49 4e 54 45  52 4e 41 4c 20 45 52 52 |ir..INTERNAL ERR|
00020788  4f 52 3a 20 63 61 6e 6e  6f 74 20 63 72 65 61 74 |OR: cannot creat|
00020798  65 20 74 65 6d 70 6f 72  61 72 79 20 64 69 72 65 |e temporary dire|
000207a8  63 74 6f 72 79 21 0a 00  2e 00 00 00 2e 00 2e 00 |ctory!..........|
000207b8  00 00 00 00 5c 00 00 00  2a 00 00 00 57 41 52 4e |....\...*...WARN|
000207c8  49 4e 47 3a 20 66 69 6c  65 20 61 6c 72 65 61 64 |ING: file alread|
000207d8  79 20 65 78 69 73 74 73  20 62 75 74 20 73 68 6f |y exists but sho|
000207e8  75 6c 64 20 6e 6f 74 3a  20 25 73 0a 00 00 00 00 |uld not: %s.....|
000207f8  77 62 00 00 45 72 72 6f  72 20 63 72 65 61 74 69 |wb..Error creati|
```
