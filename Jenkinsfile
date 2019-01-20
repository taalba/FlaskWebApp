pipeline {
  agent none
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Build'
        sh '/usr/local/bin/docker-compose FlaskWebApp/docker-compose.yml build'
      }
    }
  }
}