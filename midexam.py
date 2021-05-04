win = {
     '찌' : '빠',
     '묵' : '찌',
     '빠'  : '묵'
}
def start(mine,yours):
    result = '0'
    if mine == yours:
        result ='draw'
        return result
    elif win[mine] == yours:
        result = 'win'
        return result
    else :
        result  = 'lost'
        return result

while 1 :
    me = input('찌, 묵, 빠 를 선택하거나 그만하고싶다면 "그만"를 입력하세용>>>>')
    if me =='그만':
        break
    elif (me !='찌')and (me !='묵') and (me !='빠'):
        print('묵 찌 빠를 적으세용.')
        continue
    else:
        import random
        list = ['묵' , '찌', '빠']
        you = random.choice(list)
        print('나 == {} 컴퓨터 == {} >>>   결과:{}'.format(me ,you,start(me,you)))
    print('묵 찌 빠 그마안!')