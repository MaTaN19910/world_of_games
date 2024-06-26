pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('matandevops-dockerhub')
    }

    stages {
        stage('git checkout') {
            steps {
                git(
                    url: 'https://github.com/MaTaN19910/world_of_games.git',
                    branch: "master"
                )
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t world_of_games .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:8777 world_of_games'
            }
        }
        stage('Test') {
            steps {
                sh  '''
                    pip install selenium
                    cd tests/
                    python3 e2e.py
                '''
            }
        }
        stage('Finalize'){
            steps {
                sh '''
                    docker container stop world_of_games
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    docker push matandevops/world_of_games
                    docker logout
                '''
            }
        }
    }
}