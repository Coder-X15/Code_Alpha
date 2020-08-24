# Code_Alpha #
Cryptography API for Python
____________________________
This is a simple cryptography service for Python. I created this during a mental ability class I was attending then.
Basically, we all love to send messages that are really private that you don't want anyone else to see. So was it when the Germans working under the Nazi regime used the Enigma Machine to send coded stuff across the seas (unfortuantely, Alan J Turing broke into their secrets !). What if such a service is made available ?  

This is where Code_Alpha comes in . This is basically a coding - decoding mechanism crafted in Python using simple logic (one that even the greatest fool may understand). So, as a part of trying to be honest, here's how the code goes:

1) Take a word (eg: HELLO).
2) Write the position values of each letter in the word, i.e., for H it is 1, for E it is 2, etc.

 So what you'll get now is :
 ```
 H  E  L  L  O
 1  2  3  4  5
 ```
 3) Subtract 1 from each number. This will give you the index of the word in a Python array.
 ```
 H  E  L  L  O
 0  1  2  3  4
 ```
 4) With each index, transform the letter into a number using the formula :
 ``` 
 26 * (the index you take) + (value of the letter in the series of alphabets in order)
 ```
 5) Transcribe the word using the letters you get.
 
 Thus, HELLO is transformed into  8-31-64-90-119 . 
 
 This is how the code works. Interesting, right ?
 If you input a sentence, each word in the sentence is transformed into the corresponding numeric code.
 
 # '20-34-53-92-115- 25-41-73-' 
 code for "Thank you"
 ________________
 
 PS : There are a few things to be noted :
 1) Symbol transcription hasn't been made
 2) Contributers are welcome to make any change to the API to enhance its performance, its abilities, etc.
 3) Please put up the updates you made in this README file; also create a new release for this, in case you edit the API as a part of perfromance enhacement .
 
 #NEW !#
 _________
 
 Decoding function added...... use ```decode(nstring)``` (```nstring``` - the numeric string code to be decoded) to decode the codes you get ! 
