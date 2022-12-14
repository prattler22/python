#! python3

import pyperclip, re

# TODO : create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9._%+-]+           # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE)
    

# TODO : find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO : copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('클립보드에 복사가 되었습니다 : ')
    print('\n'.join(matches))
else:
    print('이메일 주소를 찾지 못 했습니다')
