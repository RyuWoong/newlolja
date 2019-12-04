import logging,os
from logging import handlers


#logger instance
logger = logging.getLogger("LOLJA")

#logger instance로 log 찍기
logger.setLevel(level=logging.INFO)

#formatter
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')

#handler
streamHandler = logging.StreamHandler()
fileHandler = handlers.TimedRotatingFileHandler(filename=os.path.dirname( os.path.abspath( __file__ ) )+"/log/server.log",when='midnight',interval=1,encoding='utf-8')

#각 instance에 farmatter 설정
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
fileHandler.suffix = "%Y%m%d"

#logger instance에 handler 설정
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

