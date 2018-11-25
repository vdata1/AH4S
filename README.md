# AH4S
Python implementation for my paper: AH4S: an algorithm of text in text steganography using the structure of omega network.

Abstract: 
This work introduces a new technique to hide text-in-text messages. The proposed mechanism uses the structure of omega 
network to hide and extract secret messages. The generation of secret message is made as follows, take every letter from 
the original message, use the omega network to generate two related letters from the selected letter, and finally search 
the dictionary for a suitable English cover word to hide the generated two letters. In order to increase the chance of 
find a suitable words, the generated two letters need not to be adjacent in the cover word. As a result, the white-space 
steganography is used in order to hide the position of the two letters in the selected cover word. The experiments show 
that the proposed mechanism gives a better execution time and better cover words than the current similar mechanisms 
especially when we are trying to hide long text messages.


For More Info, Please read the full article:  
https://onlinelibrary.wiley.com/doi/pdf/10.1002/sec.1752
