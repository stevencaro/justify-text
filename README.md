# justify-text.py
A command line tool to justify a text at a specified width.

## Usage
```
> justify-text.py lorem-ipsum.txt 60
------------------------------------------------------------
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
do  eiusmod  tempor  incididunt  ut  labore  et dolore magna
aliqua.  Ut  enim ad minim veniam, quis nostrud exercitation
ullamco  laboris  nisi  ut  aliquip ex ea commodo consequat.
Duis  aute  irure  dolor in reprehenderit in voluptate velit
esse  cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat  cupidatat  non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum.
------------------------------------------------------------
```
## Reference: class definitions

### LineBuffer() methods
<dl>
  <dt>__init__</dt>
  <dd>Initializes the instance variables line, width, and maxwidth.</dd>
  <dt>calculate_width</dt>
  <dd>Calculates the width of the buffer.</dd>
  <dt>clear</dt>
  <dd>Empties the buffer and sets the width to zero.</dd>
  <dt>add</dt>
  <dd>Adds a word or string of words to the buffer. Returns:</dd>
  <dd> * None if the buffer is full and the word could not be added.</dd>
  <dd> * The new width of the buffer if the word was added successfully.</dd>
  <dt>strip</dt>
  <dd>Removes leading and trailing whitespace from the buffer.</dd>
  <dt>justify</dt>
  <dd>Fills the buffer with spaces until it reaches width in size.</dd>
  <dt>show</dt>
  <dd>Shows the buffer. Useful for debugging.</dd>
</dl>

### JustifyText() methods
<dl>
  <dt>__init__</dt>
  <dd>Initilizes the instance variables text, width, and justified text. Runs the methods fill_deque and justify.</dd>

  <dt>fill_deque</dt>
  <dd>Fills the double ended queue with the text sumbitted by the user of the class.</dd>
  <dt>justify</dt>
  <dd>Creates a LineBuffer and submits words to it until its full. When it is justified, adds the line to the justified_text instance variable.</dd>
  <dt>show</dt>
  <dd>Displays the justified line buffer to the user.</dd>
  <dt>rejustify</dt>
  <dd>Given a new width, rejustified the text to that width. Useful interactively.</dd>
</dl>

### Interactive Ipython session
```
In [1]: with open('samharris.txt') as f:
   ...:     text = f.read()
   ...:

In [2]: p (text)
But the moment we admit that information processing is the source of intelligence;
that some appropriate computational system is what the basis of intelligence is. . .
and we admit that we will improve these systems continuously; and we admit that
the horizon of cognition very likely far exceeds what we currently know, then
we have to admit that we're in the process of building some sort of god.  Now
would be a good time to make sure its a god we can live with.


In [3]: run -n justify-text.py

In [4]: justify = JustifyText(text, 70)

In [5]: justify.show()
----------------------------------------------------------------------
But  the  moment we admit that information processing is the source of
intelligence;  that  some appropriate computational system is what the
basis  of intelligence is. . . and we admit that we will improve these
systems  continuously; and we admit that the horizon of cognition very
likely  far exceeds what we currently know, then we have to admit that
we're in the process of building some sort of god. Now would be a good
time to make sure its a god we can live with.
----------------------------------------------------------------------
```
