import os
conf.color_theme=NoTheme()
RESULT=""
p=sniff(iface="ens4d1",count=1,timeout=5)
RESULT=str(p)
f = open('scapyResult.txt','w')
f.write(RESULT)
f.close()
exit()
