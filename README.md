# webcrawler

Web Crawler/Scrapper using Python with GUI
#Author: Mitesh Goplani

1.Install all the modules

2.Set the path for the text file and database file to be created

Verify: if os.path.isfile(sqlite_file)==True:
(inside __init__ of main class)

3.Run the program for the first time(Crawlers table will be created ) in database
(Created is printed in python console)

4.Before you execute the code the second and later times,
 change the following:
if os.path.isfile(sqlite_file)==False:
(inside __init__ of main class)

If step 4 is not executed, an error message displaying table already exists will be displayed , then the user has to delete the sqlite fie before progressing with the run.

5.The crawled website links are stored automatically in DB, "Save in Database" button is used to just display the database entries into a text format.

6.To store the top 10 links in .txt file , click on save to file button.
