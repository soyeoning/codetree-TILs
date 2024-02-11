n = int(input())

dict = {'book':3000, 'mask':1000}

if n >= dict['book'] and n >= dict['mask']:
    if n >= dict['book']:
        print('book')
    elif dict['mask'] <= n < dict['book']:
        print('mask')
else:
    print('no')