import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# DEBUG, INFO, WARNING, ERROR, CRITICAL

# logging.basicConfig(filename='./logFile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# 파일 용량이 커질 것을 대비해 RotatingFileHandler 사용

# logging.disable()         #loggin 비활성화

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')