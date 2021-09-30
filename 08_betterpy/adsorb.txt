# ** Team Name: Naomi Naranjo, Zhao Yu Lin, Gavin McGinley **
## SoftDev
## K08 -- Looking over the different methods the class used to read, organize, and weight the CSV data.
## 2021-09-30

**Questions:**
*How much quicker is it to use an imported library rather than math or hard coding?


**Comments:**
*CSV readers will automatically split by commas, so manual splitting isn’t necessary
*There is already a function (random.choices) that does weighted randomization 
*A lot of people just treated 99.8 as 998, and multiplied percentages by 10, to use integer randomization instead of working with floats
*csv.reader used most often for reading input
*Comments make code easier to understand, but commenting more code is pointless clutter, and usually just the result of a person forgetting to delete the code they left as a comment
*Division of process over multiple functions was common
*It's definitely helpful to store the contents of the CSV file after you read it in, so the file doesn’t need to be repeatedly opened and copied

**Concerns:**
*Is it a good practice to close files after reading? How much does this help?
