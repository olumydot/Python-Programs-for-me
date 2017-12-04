
import logging
from math import sqrt

LOG_FORMAT = "%(levelname)s  %(asctime)s  - %(message)s"
logging.basicConfig(filename="C:\\Users\\OluE\\Desktop\loggerfile1.log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()  # we can provide a name for a logger eg getLogger(olu)


def quad_eq(a,b,c):
        """Returns solutions to a quadratic equation ax^2 +bx + c"""
        logger.info("quadratic_formula({0},{1},{2})".format(a,b,c))

        # compute the discriminant
        logger.debug("computing the discriminant")
        disc = b**2 - 4*a*c

        # calculate the roots
        logger.debug("Calculate the roots")
        root1 = (-b+sqrt(disc))/(2*a)
        root2 = (-b-sqrt(disc))/(2*a)

        # return the two roots as a tuple
        logger.debug("return the roots as a tuple")
        logger.info("the roots are {},{}".format(root1, root2))
        return root1, root2


x,y = quad_eq(1,4,4)
print(x)
print(y)
