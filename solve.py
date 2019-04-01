from datetime import datetime as dt

def convert_date(x):
    return dt.strptime(x,'[%d/%b/%Y:%H:%M:%S')

def read(file_name):
    global data
    data = []
    with open(file_name) as file:
        file.readline() # 첫줄 제거
        data = list(map(lambda x:x.strip().split(','),file.readlines()))
  
def sort(option):
    global data
    methods = {
        '-t'    : lambda x : convert_date(x[1]),
        '-ip'   : lambda x : (x[0],convert_date(x[1]))
    }
    data.sort(key = methods[option])
    
def print_data():
    for d in data:
        print(d[0])
        print('\tTime:',d[1][1:])
        print('\tURL:',d[2])
        print('\tStatus:',d[3])
        print()

if __name__ == '__main__':
    
    funcs = {
        'read'  : read,
        'sort'  : sort,
        'print' : print_data
    }
    
    while True:
        cmd = input('$ ').split()
        try:
            funcs[cmd[0]](*cmd[1:])
        except Exception as e:
            print(e)
        
        
