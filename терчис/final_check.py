import os
base = r'C:\Users\ВАЛЕРИЯ 2004\OneDrive\Рабочий стол\терчис'
files = ['учебник_пункт1.html','учебник_пункт2.html','учебник_пункт3.html','учебник_пункт4.html','учебник_пункт5.html','учебник_пункт6.html','пункт7.html','пункт8.html','пункт9.html','пункт10.html','пункт11.html']
for f in files:
    try:
        c = open(os.path.join(base,f),encoding='utf-8').read()
        has_emoji_theory = '\U0001F4D6' in c
        has_emoji_tasks = '\u270F\uFE0F' in c
        has_reset = '\U0001F504' in c
        print(f + ': theory=' + ('OK' if has_emoji_theory else 'NO') + ' tasks=' + ('OK' if has_emoji_tasks else 'NO') + ' reset=' + ('OK' if has_reset else 'NO'))
    except:
        print(f + ': ERROR')