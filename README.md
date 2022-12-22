# Grep_PDF
_Grep_PDF looks through many PDF at the same time to find anything you want.Regular expressions can be used when the word is not known._

```
 _______                          ______ ______  _______ 
(_______)                        (_____ (______)(_______)
 _   ___  ____ _____ ____         _____) )     _ _____   
| | (_  |/ ___) ___ |  _ \       |  ____/ |   | |  ___)  
| |___) | |   | ____| |_| |______| |    | |__/ /| |      
 \_____/|_|   |_____)  __(_______)_|    |_____/ |_|      
                    |_|                                  
```

### SUMMARY
Grep_PDF grabs PDF from a folder you choose and then look through all of them to find a word (string) you defined.<br />
The soft allows you to use Regular Expressions in case you do not know what exactly you are looking for.<br />

### SCREENSHOTS

![Screenshot](https://github.com/gelndjj/Grep_PDF/blob/main/img/grep_pdf_main.png)

![Screenshot](https://github.com/gelndjj/Grep_PDF/blob/main/img/grep_pdf_main_dark.png)

### HOW IT WORKS 
1. Open a folder containing PDF files by clicking on Open a folder.
2. Below the Open button,in the white field,type in the word you look for and type Enter or click on Go ahead.
3. The result will be displayed on the right window if the word is found inside the PDF files. If not, the right window will remain white.

* The result will display in which PDF file the word has been found and how many times it appears. 

### USE REGULAR EXPRESSIONS TO FIND ANYTHING YOU WANT

The soft contains instructions to get familiar with RE; toogle the button close to 'Instructions' to display them.<br />
Then we can use them the same way we look for a word we already know.<br />

![Screenshot](https://github.com/gelndjj/Grep_PDF/blob/main/img/grep_pdf_ins.png)

* Here is an example using RE to find any address with its postcode ; so we look for 5 digits in a row followed by the city's name (which will more than one character).<br /> 
* A digit is represented by this expression \d , so for 5 digts in a row we will type \d\d\d\d\d or \d{5}.<br />
* A white space is represented by this one -> \s .<br />
* An alphabet character uses this expression [a-z] or [a-zA-Z] to have capital letters as well as the small ones.<br />
* As we don't know the length of the city name, we must add this expression '+' to indicate that we look for a letter (upper or lower) that occurs once or more. So in our case we will type [a-zA-Z]+ .<br />

* Let's see what looks like the pattern at final: \d{5} for 5 digits in a row, \s for a white space and [a-zA-Z]+ for a word that contains one or more letters.<br />
* We type \d{5}\s[a-zA-Z]+ in the field then type enter.<br />

![Screenshot](https://github.com/gelndjj/Grep_PDF/blob/main/img/grep_pdf_reg.png)

Regular Expression is a powerful tool and can do much more.

### FEATURES

The frame _Options_ allows you to look for any informations inside the white window above as well as get the size and the amount of PDF from the folder we just selected.<br /> 
1. Typing a word in the Find field will look for it in the window above.
2. Checking off the Get/number size button will display the amount of PDF and the size of them in the horizontal field.

![Screenshot](https://github.com/gelndjj/Grep_PDF/blob/main/img/grep_pdf_getsize.png)

