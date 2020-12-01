pipeline {
  agent any
  stages {
    stage('inicio') {
      steps {
        echo 'Iniciando construccion de proyecto'
        sh 'env'
      }
    }

    stage('docker env') {
      steps {
        sh 'docker -v'
      }
    }

    stage('build') {
      steps {
        sh 'docker'
      }
    }

  }
}