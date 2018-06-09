from mocker import Mocker


mocker = Mocker()
obj = mocker.mock()


obj.hello()
mocker.result("Hi!")


class SampleTest(MockerTestCase):
    def test_hello(self):
        obj = self.mocker.mock()
        obj.hello()
        self.mocker.result("Hi!")
        self.mocker.replay()
        self.assertEquals(obj.hello(), "Hi!")