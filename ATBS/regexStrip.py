#! python3
# regexStrip.py - regex version of the strip() function

import re

def regexStrip(strIn, stripChar=' '):

    myRegex = r'[^' + stripChar + r'].*[^' + stripChar + r']'
    myMatchObj = re.search(myRegex, strIn)
    if myMatchObj == None:
        return 'Bad String'
    else:
        print(myMatchObj.group())

regexStrip('   Hey I am Jack    ')
regexStrip('So   Hey I am Jack    ')
regexStrip('So   Hey I am Jack    So')
regexStrip('Hey I am Jack    ')
regexStrip('     Hey I am Jack')
regexStrip('xxxxx     Testxxx    xxxxxx', 'x')
