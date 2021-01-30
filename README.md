# Test Broken Hash Serve

A testing suite for the Broken Hash Serve application as part of the JumpCloud SDET Engineer Assignment. These tests were built on Mac OSX 10.14.6 using the pytest python module. 


## Setup

 1. Clone the Github Repo onto your local machine.
 2. Run the following command to install the dependencies used:
	> Pip Install -r requirements.txt
 3. Add the following ENV variables to your .bash_profile:
	>export PORT=8088
		 export BROKEN_HASH=/absolute/path/to/app

## Interacting With The Application
The following is a postman collection that you can use to execute the 4 requests you can use to interact with the hashing application: 
>https://www.getpostman.com/collections/dc918ee57b2cbf4cc0f2

You can use this link to import the enter collection into your postman account. 

## Running The Tests
To run the tests you will need to run them each individually. Currently, running all of the tests together will cause some errors related to opening and shutting down the application. Here is an example of how to run an individual test file: 
		
    pytest test_example_file.py

## User Stories

 1. When launched, the application should wait for http connections.
 2. It should answer on the ​PORT​ specified in the ​PORT​ environment variable.
 3. It should support three endpoints:
	 - A ​POST​ to ​/hash​ should accept a password. It should return a job identifier immediately. It should then wait 5 seconds and compute the password hash. The hashing algorithm should be SHA512.
	 - A ​GET​ to ​/hash​ should accept a job identifier. It should return the base64 encoded password hash for the corresponding POST request.
	 - A ​GET​ to ​/stats​ should accept no data. It should return a JSON data structure for the total hash requests since the server started and the average time of a hash request in milliseconds.
 4. The software should be able to process multiple connections simultaneously.
 5. The software should support a graceful shutdown request. Meaning, it should allow any in-flight password hashing to complete, reject any new requests, respond with a ​200​ and shutdown.
 6. No additional password requests should be allowed when shutdown is pending.

## Limitations
Unfortunately I was not able to fully test all of the user stories outlined above. Below are the 3  areas where I did not finish testing the functionality. 

 1. *It[POST to /hash] should then wait 5 seconds and compute the password hash. The hashing algorithm should be SHA512*.
While testing the behavior of the application I noticed that the application did wait 5 seconds before returning a response, however that response was the hash identifier and not the computed password hash. I was unsure if it was intended that the application was supposed to send an additional response after the identifier, and subsequently how to test that. 
 3. *It[shutdown request] should allow any in-flight password hashing to complete, reject any new requests, respond with a ​200​ and shutdown*.
 In this case, I understand that to test this I needed to setup a special case of sequential requests to check if the application is able to reject requests after it's been shutdown. I was not able to implement this functionality in this iteration. 
 4. *Running a singular test suite*.
As mentioned above in the **Running the Tests** section, I was not able to reconcile all of the tests to run together in a single suite. The primary reason for this was the helper function that I created to open the application caused some overlapping requests to to conflict with the startup and shutdown of the application. One potential solution would be to use a module that would order the tests in a sequential order, thus executing them in an order that would not cause the overlap. 
