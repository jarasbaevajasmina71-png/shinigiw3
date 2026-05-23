# try:
#     suw=0
#     if suw == 0
#     raise Exception('suw joq')

# print=('shay demlendi')
# except Exception as qate:
# print = (f"problema: {qate}")

while True:
    a = input('san jazin')
    b = input('san jazin')
    try:
        a=int(a)
        b=int(b)
        s=a+b
        print(s)  
        break
    except ValueError:
        print('duris magliwmat kiritin')
    finally:
        print(f'juwmaqlandi')
      