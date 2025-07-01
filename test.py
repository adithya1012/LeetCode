# import unittest
#
#
# def add2No(a, b):
#     return a + b
#
#
# class TestCaseExecution(unittest.TestCase):
#     def test_add2Normal(self):
#         self.assertEqual(add2No(10, 20), 30)
#
#     def test_add2Zero(self):
#         self.assertEqual(add2No(0, 0), 0)
#
#     def test_add2Negetive(self):
#         self.assertEqual(add2No(-10, -20), -30)

# if "__mani__" == __name__:
#     unittest.main()

class Paser():
    def __init__(self, content):
        self.content = content

    def exctract_process(self):
        # with open(self.filename, "r") as content
        logs = []
        for line in self.content:
            log = self._parser(line)
            if log:
                logs.append(log)
        return logs

    def _parser(self, line):
        try:
            if line.startswith("["):
                time, content = line.split("]", 1)
                type, message = content.split(": ", 1)
                log = {
                    "time": time[1:],
                    "type": type,
                    "message": message
                }
                return log
            else:
                return None
        except Exception as e:
            print(e)
            return None


content = [ "[2025-05-18 11:43:05] ERROR: There is a problem",
             "[2025-05-18 11:43:07] INFO: There is a Information",
             "[2025-05-18 11:43:09] WARN: There is a Warning" ]
obj = Paser(content)
logs = obj.exctract_process()
print(logs)