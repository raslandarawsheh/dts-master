import os
conf.color_theme=NoTheme()
RESULT=""
p = sniff(iface="ens4", count=2)
RESULT = p[1].summary()
f = open('scapyResult.txt','w')
f.write(RESULT)
f.close()
exit()
