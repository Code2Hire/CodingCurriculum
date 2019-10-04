# Welcome to my "final" project!

## Prerequisites

1. Install Docker: 
	Windows/Mac	https://docs.docker.com/install/
2. Or for Linux run the following commands:
	1. sudo yum install docker-engine -y
	2. sudo service docker start

## Running this project

Special note: Make sure you have nothing using port 3306, 8080, or 80.
3306 is commonly used by msql databases.

1. Clone the repo
2. Create your own .env file based off of .env.example
3. Navigate to your installation folder via cli
4. Run 'docker-compose build'
5. Run 'docker-compose up'
6. Navigate to 0.0.0.0 in your browser
7. When finished, run 'docker-compose down'





