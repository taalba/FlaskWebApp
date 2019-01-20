pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build'
        sh '''step([$class: \'DockerComposeBuilder\', dockerComposeFile: \'FlaskWebApp/docker-compose.yml\', option: [$class: \'StartService\', scale: 1, service: \'neo4jdb\'], useCustomDockerComposeFile: true])
'''
      }
    }
  }
}