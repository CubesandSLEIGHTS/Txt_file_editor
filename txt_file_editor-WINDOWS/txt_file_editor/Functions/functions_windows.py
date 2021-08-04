from os import chdir, name, system, path, makedirs, chdir
def cs():
    _ = system('cls') if name == 'nt'else system('clear')

def valid_input(inp):
    validity_error = 'Invalid mode! Enter create, add, write, read or stop!'
    try:
        ret = str(inp)
        ret = ret.lower()
        if not (ret == 'create' or ret == 'add' or ret == 'write' or ret == 'read' or ret == 'stop'):
            print(validity_error)
            return None
        return ret
    except:
        print(validity_error)

def fix_fn(fn):
    for i in range(len(fn)):
        if fn[i] == ' ':
            fn[i] = '_'
    return fn

def write_txt(fn):
    lst = []
    txt = ''
    print('What do you want to write? Enter END to stop:')
    while True:
        if txt.upper() == 'END':break
        else:
            lst.append('\n' +txt)
            txt = input()
    with open(fn, 'w') as f:
        f.writelines(lst)

def create_txt():
    fn = input('What do you want the file to be called? (Use underscores [ _ ] instead of spaces) ')
    fn = fix_fn(fn)
    print(f'New File name: {fn}')
    fn += '.txt'
    a = open(fn, 'w')
    a.close()
    write_txt(fn)

def add_to_txt(fn):
    lst = []
    txt = ''
    print('What do you want to add to the txt .file? Enter END to stop:')
    while True:
        if txt.upper() == 'END':break
        else:
            lst.append('\n' + txt)
            txt = input()
    with open(fn, 'a') as f:
        f.writelines(lst)

def read_txt(fn):
    with open(fn, 'r') as f:
        a = f.read()
        print(a)
        input('______________________________________________________________________________\nPress ENTER to continue ')

def mode():
    while True:
        cs()
        while True:
            mode_ = valid_input(input('What mode do you want to go into? Create, add, write, read or stop: '))
            if mode_:break
        mode_ = mode_.lower()
        if mode_ == 'create':
            cs()
            create_txt()
        elif mode_ == 'add':
            cs()
            fn = input('What is the txt file name? ')
            fn += '.txt'
            cs()
            add_to_txt(fn)
        elif mode_ == 'write':
            cs()
            fn = input('What is the txt file name? ')
            fn += '.txt'
            cs()
            write_txt(fn)
        elif mode_ == 'read':
            cs()
            fn = input('What is the txt file name? ')
            fn += '.txt'
            cs()
            read_txt(fn)
        else:
            break


def main():
    newpath = r'C:\\txt-files\\txts' if name == 'nt' else r'/txt-files/txts'
    if not path.exists(newpath):
        makedirs(newpath)
    chdir(newpath)
    mode()