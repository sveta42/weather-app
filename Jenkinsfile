pipeline {
    agent none
    environment {
		ECR_CREDENTIALS=credentials('aws-ecr')
	}

    stages {
        stage('Start') {
            agent { label 'agent' }
            steps {
                echo 'starting the build .... '
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
                sh 'aws ecr --region eu-central-1 | echo $ECR_CREDENTIALS_PSW | docker login -u $ECR_CREDENTIALS_USR --password-stdin 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
                echo 'successfully logged in'
                sh 'docker tag sveta296/weatherapp:latest 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
                echo 'successfully tagged image'
            }
        }

        stage('Push') {
            agent { label 'agent' }
            steps {
                sh 'docker push 983612380489.dkr.ecr.eu-central-1.amazonaws.com/weather_app'
                echo 'successfully pushed the image to ECR'
            }
        }

        stage('Login to agent 1') {
            agent { label 'agent2' }
            steps {
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal'
                echo 'successfully logged in to agent 1'
            }
        }
        stage('deploy app in eks') {
            agent { label 'agent2' }
            steps {
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal kubectl apply -f /home/ubuntu/jenkins/workspace/weather_app/deploy-leumi.yaml'
                echo 'success deploying app'
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal sleep 6'
                echo 'copy the EXTERNAL IP to go to the app'
                sh 'ssh -i ~/agent1 ubuntu@ip-172-31-41-254.eu-central-1.compute.internal kubectl get service/weatherapp-service'
            }
        }
    }
}
