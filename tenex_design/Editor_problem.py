import unittest


class Editor:
    def __init__(self):
        self.cursor_line = -1
        self.cursor_index = -1
        self.block = []
        self.last_word = ""
    def handleKey(self, ch):
        if self.cursor_index == -1:
            if ch == "\n":
                if self.last_word:
                    self.block.append(self.last_word)
                    self.last_word = ""
            elif ch == "BACKSPACE":
                if self.last_word:
                    self.last_word = self.last_word[:-1]
                else:
                    if self.block:
                        self.last_word = self.block.pop()
                    else:
                        print("No elements entered")
            else:
                self.last_word += ch
        else:
            if ch == "\n":
                # if self.cursor_index >= len(self.block[self.cursor_line])-1:
                #     return
                word = self.block[self.cursor_line]
                self.block[self.cursor_line] = word[:self.cursor_index]
                self.block.insert(self.cursor_line+1, word[self.cursor_index:])
                self.cursor_line += 1
                self.cursor_index = 0
            elif ch == "BACKSPACE":
                if self.cursor_index == 0:
                    self.block[self.cursor_line-1] += self.block[self.cursor_line]
                    self.block.pop(self.cursor_line)
                    self.cursor_line -= 1
                    self.cursor_index = len(self.block[self.cursor_line])-1
                else:
                    word = self.block[self.cursor_line]
                    new_word = word[:self.cursor_index-1] + word[self.cursor_index:]
                    self.cursor_index -= 1
                    self.block[self.cursor_line] = new_word
            else:
                word = self.block[self.cursor_line]
                new_word = word[:self.cursor_index] + ch + word[self.cursor_index:]
                self.block[self.cursor_line] = new_word
                self.cursor_index += len(ch)



    def outputContent(self):
        if self.last_word:
            res = "\n".join(self.block+[self.last_word])
        else:
            res = "\n".join(self.block)
        return res

    def moveCursor(self, line_no, index):
        # TODO: Validation
        if self.last_word:
            self.block.append(self.last_word)
            self.last_word = ""
        self.cursor_line = line_no
        self.cursor_index = index


class EditorTests(unittest.TestCase):
    def setUp(self):
        self.editor = Editor()

    def testHandleKeyCharacters(self):
        self.editor.handleKey("a")
        self.editor.handleKey("b")
        self.editor.handleKey("c")
        self.editor.handleKey("\n")
        self.editor.handleKey("d")
        self.assertEqual(self.editor.outputContent(), "abc\nd")

    def testHandleBackspace(self):
        self.editor.handleKey("d")
        self.editor.handleKey("e")
        self.editor.handleKey("f")
        self.editor.handleKey("BACKSPACE")
        self.assertEqual(self.editor.outputContent(), "de")
    #
    def testHandleBackspaceAcrossLines(self):
        self.editor.handleKey("abc")
        self.editor.handleKey("\n")
        self.editor.handleKey("BACKSPACE")
        self.assertEqual(self.editor.outputContent(), "abc")
        self.editor.handleKey("d")
        self.assertEqual(self.editor.outputContent(), "abcd")

    def testCursorWithoutBackspace(self):
        self.editor.handleKey("a")
        self.editor.handleKey("b")
        self.editor.handleKey("c")
        self.editor.handleKey("\n")
        self.editor.handleKey("d")
        self.editor.moveCursor(0, 1)  # Cursor between 'a' and 'b'
        self.editor.handleKey("\n")
        self.assertEqual(self.editor.outputContent(), "a\nbc\nd")

    def testCursorWithBackspace(self):
        self.editor.handleKey('a')
        self.editor.handleKey('b')
        self.editor.handleKey('c')
        self.editor.handleKey('\n')
        self.editor.handleKey('d')
        self.editor.moveCursor(0, 1)  # Cursor between 'a' and 'b'
        self.editor.handleKey('BACKSPACE')  # Deletes 'a'
        self.assertEqual(self.editor.outputContent(), "bc\nd")

    def testCursorMergeLinesWithBackspace(self):
        self.editor.handleKey('abc')
        self.editor.handleKey('\n')
        self.editor.handleKey('def')
        self.editor.moveCursor(1, 0)  # Cursor at start of 'def'
        self.editor.handleKey('BACKSPACE')  # Merges with previous line
        self.assertEqual(self.editor.outputContent(), "abcdef")
        self.assertEqual(self.editor.cursor_line, 0)
        self.assertEqual(self.editor.cursor_index, 3)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)