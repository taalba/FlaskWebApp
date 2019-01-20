pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        sh 'docker-compose FlaskWepApp/docker-compose.yml build'
        sh 'docker-compose FlaskWepApp/docker-compose.yml up'
      }
    }
  }
}