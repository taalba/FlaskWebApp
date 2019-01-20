pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        step([$class: 'DockerComposeBuilder', dockerComposeFile: 'FlaskWebApp/docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
      }
    }
  }
}