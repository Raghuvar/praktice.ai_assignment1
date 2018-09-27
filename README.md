
Steps in creating the Bot
===========================

1. I have used **dialogflow** API to create the chatbot.
2. I have used webhook for creating end user API to send the request and get the response. 
3. I have used ngrok to use the created webhook API to the chatbot so that communication can be done 



-------------											-----------------------
|			|											|					   |
| chatbot   |  ---------------------------------------->| Webhook API		   | ------> Send the response to bot
|			|    send the request to webhook end point	|	(endpoint/webhook) |           using ngrok tool and
-------------											------------------------			check the status