from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

session = session = WolframLanguageSession('/Applications/Wolfram Desktop.app/Contents/MacOS/WolframKernel')
#while True:
#   myInput = input("Question: ")
session.evaluate(wl.WolframAlpha("number of moons of Saturn", "Result"))
session.terminate()
