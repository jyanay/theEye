## Building "The Eye"
### Questions and Assumptions
 As it's the weekend when I undertook this test, I didn't want to bother you with questions, or even assume that I would get a response. As such, I've written the questions I would have asked, along with what I assume to be the answer.
1. When you talk about "applications" are you using them in the Django sense of the word, or are all these completely separate systems?
	*Assumption* : They are separate systems, living in separate projects
2. Will the applications send every event to the "The Eye" or am I expected to pull data out of the requests themselves?
	*Because of Assumption one, I exclude middleware for this task and assume every event is sent directly via POST request*
3. Will the format of the request remain the same going forward with just "data" changing based on "category" and "name"?
	*Assumption*: Yes the only thing that will change is inside the "data" key
4. Can I authenticate "trust" based on IP? Or do we need a token system?
	*Assumption*: You can verify application IPs via Middleware
5. Could this scale well past ~100 events/second?
	*Assumption*: Yes it definitely could.
	
	
	### Explanation
	- Validation:
		- Without much to go off on types of validation, I've placed validation in the serializers.py and used field validators, if there were lots of types of validation, I'd move it import them as needed
		- I'm basically using DRF serializers to validate the data, but creating the objects elsewhere instead of allowing the serializer.save() to handle it, since celery doesn't play nice with objects.
	- Tech Decisions
		- Django/Python obviously
		- Redis and Celery because I'm assuming we could go beyond ~100 events/second easily and wanted to be able to scale.
		- PostGresSql -- Just my preferred DB
	- Testing
		- I've written a few tests, but there is not full coverage as I've ran into the soft time limit
	- Logging
		- Coverage again is not what I'd like due to time constraints
	- TODO:
		- Accept Get requests and provide nested json in the format: Session--> All related Events, Category --> All related events, Time Range --> All related events
		- Django Admin Panel to browse about information
	
	
	### Conclusion
	
	Obviously not a finished product, but functional, and an interesting project.
	
	
	### The (Barebone) Docs
	
	This project is dockerized:
	
	Run:
	`
	docker compose up
	`
	
	This will start redis, celery, postgres, django
	
	By default django is exposed at 0.0.0.0:8000
	
	Use a rest api client to send a POST request to 
	
	`
	0.0.0.0:8000/post/create
	`
	
	Post request should contain json body of the following format:
	
	`
	{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
   },
   "timestamp": "2021-01-01 09:15:27.243860"
   }
	`
	
	
	
	
	
	
	
	



