pipeline {
  agent none
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        sh 'docker-compose FlaskWepApp/docker-compose.yml'
      }
    }
  }
}