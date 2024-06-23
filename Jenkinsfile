pipeline {
    agent any

    stages {
        stage('git checkout') {
            steps {
                git(
                    url: 'https://github.com/MaTaN19910/world_of_games.git'
                    branch: "${master}"
                    )
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t world_of_games .'
            }
        }
        stage('run') {
            steps {
                sh 'docker run -d -p 8777:8777 world_of_games'
            }
        }
    }
}