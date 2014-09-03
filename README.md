This is a simple webscraper for Nike.com releases.
This scraper grabs the title of the release and displays it to the console/IDE.

Urllib and Regular Expressions are exclusively used to parse the url and to find the desired tags that contain the titles, both respectively.

Currently, I have it set to loop through 64 times, this means it will detect/display up to 64 releases from the release page (http://help-en-us.nike.com/app/answers/detail/a_id/41986/p/3897)
This number can be adjusted accordingly. 
When the end of the page/releases has occurred, a vague exception will be thrown stating that the program out of bounds. This is just so the user can blatantly see the number and know 
that they can fiddle with it as desired.

Also, some funny <br> tags may show, these are due to a small description/blurb about the release on the webpage. 


For an easy execution, open run.bat and type: "python NDC_release.py"
Follow me on twitter @zweed4u
	
