# Salary-Predictor-on-top-of-Docker-Container

Deploying Machine Learning code on Docker Technology

what is docker
docker is a containerization technology that helps to deploy the various applications

Steps To Deploy Machine Learning Code On Docker
1. install docker on the top of RHEL8
   Command To Install Docker "yum install docker-ce"


2. Pull The Docker Container Image Of Centos Image From DockerHub
   Command to Pull The Image From DockerHub "docker pull centos:latest"

3. Launch One Container
   Command To Launch The Container "docker run -it — name <file name> centos:latest"

4. Install The Python Software On the Top of The Container Created i.e TASK1
   Command to Install The Python Software "yum install python3"

5. Installing Required Libraries To Run The Program
   Command To Install The Library is "pip3 install pandas" 
                                      "pip3 install numpy" and all required libraries.

6. From The Base Red Hat Operating System Copy The Mchine Learning Code To The Container.
   Command To Copy The Code is "docker cp <filename.py> <container id>:/<filename.py>"
   Copy The Data File From Base Red Hat Operating System To Container
   
7. runs python file successfully.


   




