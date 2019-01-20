pipeline {
  agent none
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Build'
        sh 'docker --version'
      }
    }
  }
}