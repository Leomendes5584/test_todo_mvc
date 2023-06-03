from behave import fixture, use_fixture
from selenium import webdriver

class TestTodoMVC:
    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        if self.driver:
            self.driver.quit()

@fixture
def test_class(context):
    context.test = TestTodoMVC()
    context.test.setup()
    yield context.test
    context.test.teardown()

def before_all(context):
    use_fixture(test_class, context)

if __name__ == "__main__":
    from behave import __main__ as behave_main
    behave_main.main("features")