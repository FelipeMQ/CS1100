try: val = int('-63')
except ValueError: pass

if isinstance(val,int):
    print(True)