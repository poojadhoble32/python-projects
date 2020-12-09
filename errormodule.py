import logging

#log msg to file ignoring less severe than ERROR

#logging.basicConfig(filename='myprogram.log',level=logging.WARNING)
logging.basicConfig(filename='program.log',level=logging.ERROR)

#these msg should appear in our file

logging.error("the washing machine is leaking")
logging.critical("the house is on fire")

#but these ones wont

logging.warning("we r almost out of milk")
logging.info("its sunny today")
logging.debug("i had eggs for breakfast")
