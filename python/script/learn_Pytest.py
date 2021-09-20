# To: pytest的日志为什么会输出两遍?
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def setup():
    logger.info("this is setup")


def teardown():
    logger.info("this is teardown")


def test_step_001():
    logger.info("this is step 001")
    print("call")


def test_step_002():
    logger.info("this is step 002")


# if __name__ == '__main__':
#     logger.info("start")
