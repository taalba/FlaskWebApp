pipeline {
  agent none
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Build'
        sh 'docker-compose FlaskWebApp/docker-compose.yml build'
      }
    }
  }
}