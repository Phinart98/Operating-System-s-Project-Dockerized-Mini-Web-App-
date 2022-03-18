## How to Run this Dockerized Application

1. In your command prompt, make sure you are in the project directory(RAID_WebApp) and run the following command:
`docker build --tag web_app .`'web_app' can be changed to anything as it is the desired name of the docker image to be 
created.

2. Run the docker image with the following command: `docker run -p 5000:5000 web_app`

3. Do not click on the IP address that appears in the command prompt if you are using Windows. Instead, go to your local 
host at http://127.0.0.1:5000/ or http://localhost:5000/

4. Follow the instructions on the homepage of the web app to test the permissions and parity APIs

