import os
base = r'C:\Users\ВАЛЕРИЯ 2004\OneDrive\Рабочий стол\терчис'
files = ['учебник_пункт1.html','учебник_пункт2.html','учебник_пункт3.html','учебник_пункт4.html','учебник_пункт5.html','учебник_пункт6.html','пункт7.html','пункт8.html','пункт9.html','пункт10.html','пункт11.html']
for f in files:
    c = open(os.path.join(base,f),encoding='utf-8').read()
    body_idx = c.find('<body>')
    after_body = c[body_idx:body_idx+200]
    topnav_first = after_body.find('<div class="top-nav"')
    container_first = after_body.find('<div class="container"')
    ok = topnav_first != -1 and topnav_first < container_first
    print(f + ': ' + ('OK' if ok else 'WRONG'))