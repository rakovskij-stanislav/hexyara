#!/usr/bin/python3

import sys
import subprocess


def print_hex(file_hndl, pos, length):
    file_hndl.seek(pos)
    for i in range((length//16) + 1):
        b = file_hndl.read(16)
        hex_str = " ".join([f"{i:02x}" for i in b])
        hex_str = hex_str[0:23] + " " + hex_str[23:]
        ascii = "".join([chr(i) if 32 <= i <= 127 else "." for i in b])

        print(f"{(i*16)+pos:08x}  {hex_str} |{ascii}|")


def processor(yara_params, line_multi):
    proc = subprocess.Popen(yara_params, stdout=subprocess.PIPE)
    # путь до файла
    cur_file = None
    # хэндл от этого файла.
    # Нужно помнить, что некоторые рули могут быть без строк, поэтому лишний раз открывать файл не стоит
    cur_file_hndl = None
    while True:
        line = proc.stdout.readline().rstrip()
        if not line:
            break
        #print(">", line.decode())
        if not line.startswith(b"0x"):
            # назначаем теперь другой файл
            cur_file = line.split(maxsplit=2)[1].decode()
            print(cur_file)
            # закроем предыдущий файл
            if cur_file_hndl:
                cur_file_hndl.close()
                cur_file_hndl = None
        else:
            if not cur_file:
                continue
            # теперь можно открыть текущий файл - возникла необходимость
            if not cur_file_hndl:
                cur_file_hndl = open(cur_file, "rb")
            pos, str_name, match_str = line.split(b":", maxsplit=3)

            pos = int(pos.decode(), 16)
            match_str_len = len(match_str) - match_str.count(b"\\x")*4

            print(hex(pos), str_name.decode(), match_str_len, sep=":")
            print_hex(cur_file_hndl, pos, match_str_len+line_multi if line_multi else match_str_len*4)

    # завершаем свою работу
    proc.terminate()
    if cur_file_hndl:
        cur_file_hndl.close()


def help():
    print(f"""\
Hexyara: little enchancement of yara
{sys.argv[0]} [hex_line_count] <yara with params>
    """)
    exit()


if __name__ == "__main__":
    yara_params = sys.argv[1:]
    if not yara_params:
        help()
    try:
        multi = int(yara_params[0], 10)
        yara_params = yara_params[1:]
    except:
        multi = None
    if "-s" not in yara_params:
        yara_params.append("-s")
    processor(yara_params, multi)
    print("Job done!")
