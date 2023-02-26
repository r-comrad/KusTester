from KusTester import *

from pathlib import Path
testPaths = list(Path("./tests").rglob("*.test"))

for i in testPaths:
    file = open(i, "r", encoding="utf8")
    url = file.readline()
    answer = file.read()

    jsonAnswer = json.loads(answer)
    tester = KusTester(driver_path=r"D:/projects/Other/kus-testing/chromedriver.exe", url="http://127.0.0.1:18080")
    tester.Add(url, jsonAnswer)
    tester.Test()