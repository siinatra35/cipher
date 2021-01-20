# cipher

This is a example of the union route cipher. This cipher encrypts using a path i.e clockwise, up and down and many more. It writes to a grid or matrix using the path. Then decrypts using the same path type to recreate the default matrix containing the text.

<br>
This program uses the same method as the union route cipher. Taking user input to gather the path type, text, and route size.
Then determining the grid size and creating the default matrix. And we read the grid using the selected path type.
<hr></hr>

<b>Example</b> <br>

```
text = "hello world"
routesize = 3
pathtype = clockwise

```

We write the text to a 3x4 grid and read the grid in a clockwise pattern.

|h |e |l|
|--|--|--|   
|l |o |w
|o |r |l
|d |- |-

`Result: lwl--dolheor`

<hr></hr>

<b>References</b>

[crypto corner route cipher](https://crypto.interactive-maths.com/route-cipher.html#:~:text=The%20Route%20Cipher%20is%20a,off%20following%20the%20route%20chosen)


[dcode route cipher](https://www.dcode.fr/route-cipher)

[crypto-it](http://www.crypto-it.net/eng/simple/route-cipher.html)