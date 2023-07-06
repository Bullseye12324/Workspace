import cProfile
import FloydA
import testexamples as t
cProfile.run("FloydA.floydA(t.input_8)")
cProfile.run("FloydA.floydAIterative(t.input_8)")
