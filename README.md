# HACKJKLU
Our project aims to detect phishing websites by analyzing the links present on a webpage. We have created a Google Chrome extension that can be used to fetch all the links from a webpage and then send them to our server for analysis. Our server uses machine learning algorithms to classify the links as either phishing or safe. The extension then displays the results to the user.

How it Works:

When the user clicks on the extension icon, the extension fetches all the links from the webpage that is currently open in the active tab of the browser. It then sends this information to our server for analysis. Our server uses a machine learning algorithm to classify the links as phishing or safe. The algorithm is trained on a known respectively large dataset of known phishing websites and uses various features of the links, such as the domain name, to make the classification.

Once the analysis is complete, the extension displays the results to the user. The user can then take appropriate action based on the results. If a link is flagged as phishing, the user can avoid clicking on it and report it to the relevant authorities.
