pipeline {
    agent none
    environment {
		ECR_CREDENTIALS=credentials('aws-ecr')
	}

    stages {
        stage('Start') {
            agent { label 'agent' }
            steps {
                echo 'finish pulling from git - success'
            }
        }
        stage('Kill') {
            agent { label 'agent' }
            steps {
                sh 'sudo docker rm -f weatherapp'
                echo 'finish pulling from git - success'
            }
        }
        stage('Build') {
            agent { label 'agent' }
            steps {
                sh 'sudo docker build -t sveta296/weatherapp:latest .'
                echo 'success building the image'
            }
        }
        stage('Login') {
            agent { label 'agent' }
			steps {
                sh 'sudo chmod 666 /var/run/docker.sock'
//                 sh 'docker login --username AWS -p $(aws ecr get-login-password --region eu-central-1) 983612380489.dkr.ecr.eu-central-1.amazonaws.com'
                sh 'aws ecr --region eu-central-1 | echo $ECR_CREDENTIALS_PSW | docker login -u $ECR_CREDENTIALS_USR --password-stdin 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
//                 sh 'aws ecr --region eu-central-1 | docker login -u AWS -p eyJwYXlsb2FkIjoicVp2SHVXdFJCRFF5ZThEQ20yZUt4eUt6TSsrUmhHelFFQlRyQ05kSk5iV1YwemFYUU9nRThYeXRwVXF5SS8zTW0xWElRdE8xajNteit4M05tQkN4MzZSaEw2N3RIeXNqVG9mTmoxZ1REWU9zSkM4QjFINnFVNEpLZW13VHpnTEdFVDRnZUZ3RnVHdkNVSUxQVyswNGpyRGNNQ2VNbGtIQ3JMUjcrV21TZGNjS3B4Y3ZlWkd2dVFJZ05RajJpK1F3UWJ3bkFvRDlWV0g3alRQZDhrWXMzWHRpak9ZbXM5MjlRZUMvaFo1TUNyQ0lxbXF0dSt2MjN4cEtQc1A3SndnV1ZPNERiT1g3ZlZOdUY4RWFpQlQ3Z0RQc1FVdXpCa1ZjVUVuNDVDbk1xNWM3ZjJBQ0Roc3BEc3dYVEhEVm1UOEVGY2xEWFpWdmJCQTBjeU55N3lFQzhaMUwzdTl1SmRDSnlVMUppZ0FIdHJ2alRyVU55R0cxTDF4M29sckpxMzBRUzJYVHNTa1l3TW5VSkgzS0x6OTVyam03emdwYkJMMjV0U1E0TE9RK1BuSnE2L0x2MGlzbUN2Yy84Qko0QXJEdDE3MDhsbTZoRklOZEd2K2wrb2N2Y3ZlS1Irc2xTQjJsZko0Q292WTk3UjZOT25xOGY2RVJ0WUkvcE5jVmJxL0hBckhKNmJuZEIyRENIbkswNjRhK3pVNGIrZ1Z2SGhDL2JvQk5xQTEzSERFbHQ5bVZVWi9TUUtUelNXVU1MYk4xekpnU2RXbzRXS0NTM1RITWpETkpwRHNUY2VJcTNqNkFYQjNDNm1GODlOeEg1ZWlYcTlZcmp5UXNETUlrcXM4RWtNS1krbE4xdlNMVWxlbHBvQjd6N0dzQXBCakhFVUZWUWljSzl5NURQWnBXQ3huU0x6RVBjaGZ3UmtvczBOeDluOVZYMnBBVERoRTFMQ1g5ZjEwcjNQV3FvQ1NKSHdPWk93bER5eEJwamF6cFJDcTBDbDRTQy9qVGxxUkJvZzdBcXZDUWdRbjJZUkdYOTlJTlhacTRhMS9GWTdmTVhIYnZNb3NHcmY5RDZIVkVkSmMrS1lBM3JrUkVLRjd3eWNTL3dDM1NCU2U2SDQvQTUybmtiSXh6N1NLYWZrS2t6MkJRU2lDamxPSHBheURqOTFKYkVYMjdLMEoyZEpKN0NPYTBiVFdpRmg0ZC9tcS9aRm9FODMvQk4rc1IrcEs3WVpYbVFwQUwyUGpNR09jbUU1cCtnWWwwQkVuMHJ2d2VNN3oxbjFQMXNDdllTK0hxSmtJM1p1N3hlQjV2anFmbXBDYTdVTGxSU3NTMnZKVGU2RkZWeWk2UUpaRjhKdW5BQng3MGJpVVhlU1FVWjg5Q1ZrMFRBUkhEbjNpVWpXeG0iLCJkYXRha2V5IjoiQVFFQkFIaDN6WU9kdHBCQlNWdy9ZMmFuOEJYSUQ0a3dMUWZub1RqNXp3WnRHSlpvWlFBQUFINHdmQVlKS29aSWh2Y05BUWNHb0c4d2JRSUJBREJvQmdrcWhraUc5dzBCQndFd0hnWUpZSVpJQVdVREJBRXVNQkVFRE1FYTFlYXdvUk5HQWd1dXlnSUJFSUE3dGV1TWF6NHlVSXl2cVFDODZTN2NoZHhJZEM4RjFoMVhqZVE0S0plL2VkQUEvSU05TTBlNmpWTjBaZUFZUXVMNUZrWW9rK1MzcVI3ckJNcz0iLCJ2ZXJzaW9uIjoiMiIsInR5cGUiOiJEQVRBX0tFWSIsImV4cGlyYXRpb24iOjE2NjEyOTc2NzR9 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
                echo 'successfully logged in'
                sh 'docker tag sveta296/weatherapp:latest 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
                echo 'successfully tagged image1'
            }
        }

        stage('Push') {
            agent { label 'agent' }
            steps {
                sh 'docker push 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
                echo 'successfully pushed the image to ECR'
            }
        }
// 		stage('Log out') {
//
// 			steps {
// 				sh 'sudo docker logout'
// 				echo 'success logged out'
// 			}
// 		}
        stage('Login to agent 1') {
            agent { label 'agent2' }
            steps {
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal'
                echo 'successfully logged in to agent'
            }
        }
        stage('deploy app in eks') {
            agent { label 'agent2' }
            steps {
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal kubectl apply -f /home/ubuntu/jenkins/workspace/weather_app/deploy-leumi.yaml'
                echo 'success deploying app'
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal sleep 8'
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal kubectl get svc'
                echo 'copy the EXTERNAL IP to go to the app'
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal kubectl get service/weatherapp-service'
            }
        }
    }
}
