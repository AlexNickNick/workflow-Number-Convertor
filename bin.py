# -*- coding:utf-8 -*-
import json,sys,NumberUtils
from commands import getoutput
from workflow import Workflow

reload(sys)
sys.setdefaultencoding('utf-8')

class item:
    def __init__(self, title, subtitle, arg):
        self.title = title
        self.subtitle = subtitle
        self.arg = arg


def get_item(value,type):
    title = ''
    subtitle = ''  
    if(2 == type):
        bin = str(value)
        title = 'bin : '+ bin
        subtitle = '二进制 : '+ bin
        return item(title=title, subtitle=subtitle, arg=bin)
    elif (8 == type):
        oct = str(NumberUtils.bin_2_oct(value))
        title = 'oct : '+ oct
        subtitle = '八进制 : '+ oct
        return item(title=title, subtitle=subtitle, arg=oct)
    elif (10 == type):
        dec = str(NumberUtils.bin_2_dec(value))
        title = 'dec : '+ dec
        subtitle = '十进制 : '+ dec
        return item(title=title, subtitle=subtitle, arg=dec)
    elif (16 == type):
        hex = str(NumberUtils.bin_2_hex(value))
        title = 'hex : '+ hex
        subtitle = '十六进制 : '+ hex
        return item(title=title, subtitle=subtitle, arg=hex)
    else :
        return item(title='二进制转换',subtitle='二进制转换',arg='')
    


def main(wf):
    value = (wf.args[0] if len(wf.args) else '').strip()
    try:
        if(value):
            bin_item = get_item(value,2)
            wf.add_item(title=bin_item.title, subtitle=bin_item.subtitle, arg=bin_item.arg, valid=True)

            oct_item = get_item(value,8)
            wf.add_item(title=oct_item.title, subtitle=oct_item.subtitle, arg=oct_item.arg, valid=True)

            dec_item = get_item(value,10)
            wf.add_item(title=dec_item.title, subtitle=dec_item.subtitle, arg=dec_item.arg, valid=True)

            hex_item = get_item(value,16)
            wf.add_item(title=hex_item.title, subtitle=hex_item.subtitle, arg=hex_item.arg, valid=True)
        else : 
            wf.add_item(title='二进制转换',subtitle='二进制转换',arg='',valid=True)
    except:
        return
    
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
