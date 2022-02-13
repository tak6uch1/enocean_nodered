import re
import datetime
import subprocess

passwd = 'PASSWORD\n'.encode()

s = str(input())
s = re.sub('^.*: *', '', s)
s = re.sub(' *}$', '', s)

if int(s) > 0:
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%Y/%m/%d %H:%M:%S')
    out_str = dt_str + "," + s + "\n"
    with open('/home/pi/work/enocean_nodered/button.csv', mode='a') as f:
        f.write(out_str)
        subprocess.run(('sudo', '-S', 'cp', '/home/pi/work/enocean_nodered/button.csv', '/srv/dev-disk-by-uuid-57c7c9da-d3c7-4f6c-82ab-52a5fa017821/nas_user/nas_user/'), input=passwd, check=True)
