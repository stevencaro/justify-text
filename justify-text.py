from collections import deque
import sys

class LineBuffer():

    def __init__(self, maxwidth=60):
        self.line = []
        self.maxwidth = maxwidth
        self.width = 0

    def calculate_width(self):
        self.width = len(''.join(self.line))

    def clear(self):
        self.line = []
        self.width = 0

    def add(self, word):             # Accepts single words or strings
        for w in word.split():
            if len(w) + self.width > self.maxwidth:
                return None
            else:
                self.line.append(w)
                self.line.append(' ')
                self.calculate_width()
        return self.width

    def strip(self):
        if self.width > 2:
            while self.line[-1] == ' ': # Remove leading and trailing spaces from line
                self.line.pop()
            while self.line[0] == ' ':
                self.line.pop(0)
        self.calculate_width()

    def justify(self):
        self.strip()
        spaces_needed = self.maxwidth - self.width # The number of spaces to add

        index = 0
        while (spaces_needed > 0):
            try:
                space = self.line.index(' ', index) # find spaces starting at index
            except ValueError:
                index = 0                  # if at the end of line, go back to beginning

            self.line.insert(space, ' ')
            spaces_needed -= 1
            index = space + 2              # move forward to find next space in the line

    def show(self):
        line = ''.join(self.line)
        print('-' * self.maxwidth)
        print(line)

class JustifyText():

    def __init__(self, text, width):
        self.text = text
        self.width = width
        self.justified_text = []
        self.fill_deque()
        self.justify()

    def fill_deque(self):
        self.deque = deque()
        for word in self.text.split():
            self.deque.append(word)
            self.deque.append(' ')

    def justify(self):

        linebuffer = LineBuffer(self.width)

        while len(self.deque) > 0:           # Process every word in the deque

            word = self.deque.popleft()      # Take a word from the left of the deque
            res = linebuffer.add(word)

            if res is None:
                self.deque.appendleft(word)  # Put the last word back on the deque

                linebuffer.justify()         # And pad the line so it is justified
                self.justified_text.append(linebuffer.line)
                linebuffer.clear()

        self.justified_text.append(linebuffer.line) # For the last line of the text

    def show(self):
        print('-' * self.width)
        for line in self.justified_text:
            print(''.join(line))
        print('-' * self.width)

    def rejustify(self, new_width):

        self.width = new_width
        self.justified_text = []
        self.fill_deque()
        self.justify()

if __name__ == '__main__':

    textfile =     sys.argv[1]
    width    = int(sys.argv[2])

    with open(textfile, 'r') as f:
        text = f.readlines()
    text = ''.join(text)

    jt = JustifyText(text, width)
    jt.show()
