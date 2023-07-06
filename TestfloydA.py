import unittest
import testexamples as t
import FloydA
class TestfloydA(unittest.TestCase):
    def testfloyd1(self):
        floyaAOutput = t.input_1
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_1
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_1 Failed")

    def testfloyd2(self):
        floyaAOutput = t.input_2
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_2
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_2 Failed")

    def testfloyd3(self):
        floyaAOutput = t.input_3
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_3
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_3 Failed")

    def testfloyd4(self):
        floyaAOutput = t.input_4
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_4
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_4 Failed")

    def testfloyd5(self):
        floyaAOutput = t.input_5
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_5
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_5 Failed")

    def testfloyd6(self):
        floyaAOutput = t.input_6
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_6
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_6 Failed")

    def testfloyd7(self):
        floyaAOutput = t.input_7
        floyaAOutput = FloydA.floydA(floyaAOutput)
        memoOutput = t.output_7
        self.assertEqual(floyaAOutput,memoOutput,"Test on Input_7 Failed")

if __name__ == '__main__':
    unittest.main()
