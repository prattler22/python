#! python3

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{2,3}|\(\d{3}\))?        # area code
    (\s|-|\.)?                  # separator
    (\d{3,4})                   # first 3 or 4 digits
    (\s|-|\.)                   # separator
    (\d{4})                     # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)


# TODO : create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9._%+-]+           # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE)
    

# TODO : find matches in clipboard text
text = str(pyperclip.paste())

# 전화번호의 지역번호가 없는 전국번호 1544 같은 번호 추출 방법이 필
matches = []
#for groups in phoneRegex.findall(text):
#    matches.append(groups[0])
#    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#    if groups[8] != '':
#        phoneNum += ' x' + groups[8]
#        matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO : copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('클립보드에 복사가 되었습니다 : ')
    print('\n'.join(matches))
else:
    print('이메일 주소를 찾지 못 했습니다')
