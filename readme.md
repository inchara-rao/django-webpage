## Django webpage project
A web-app satisfying the below criteria:

1- A webpage  that has a form that contains one input which takes a  URL and  sends a POST request to another webpage ( https://localhost:8000/result ) upon submitting.

2- Upon landing on https://localhost:8000/result ,It processes the URL received from https://localhost:8000/frequency and then the backend visits and extracts the text present on the URL’s Webpage and  processes the text (Not the Html markup,only the rendered text) and displays the top 10 most frequent words along with their respective frequency in descending order.

3- The common words  like is,are, the etc are ignored before processing.

4- The results are stored in  a local MySQL Database using the django database API.

5- Whenever a new URL is encountered,the results are stored to the Database and if the encountered URL was processed before and its data is already available in the database, then it is not processed and instead the stored data from the database is displayed.

6-On https://localhost:8000/result , it is also shown whether the displayed data is coming from the database or it was freshly processed.
