import funcs.judge

if __name__=='__main__':
    print('Cocoro :','何しにきた')

    while(True):
        argSen = input()
        if(argSen=='つかれた'):
            break
        print('Cocoro :',funcs.judge.judge(argSen))
    print('Cocoro :''さよなら')



