Steps to execute and verify the task

Step1) git clone https://github.com/venkatgurijala/movie-code.git
Step2)  cd movie-code
Step3) docker build -t movie-code:latest .
Step4) docker run -itd movie-code:latest
Step5) docker ps
Step6) docker exec -it container_id bash 
Step7) cd /venkat	
Step8) python test.py batman


Docker Work :

Step1)created new image from the Centos 7 as date image
step2)created a working directory(venkat) in centos.
Step3)copied the python script(test.py) into working direcory(venkat).
step4)installed the python,pip and request module in centos.
Step5)to keep contianer always up and running i used the ENTRYPOINT ["top", "-b"] 
 
Python script work :

Step1)imported the request and json modules to interact and parse the REST API.
Step2)Capturing the command line arguments into single string in this case movie name is command line argument.
Step3)validating the movie name
Step4)caling the REST API by using the request module
Step5)process the reposne of REST API by using the Json module.
Step6)display the results in useful way on command line.
 

 