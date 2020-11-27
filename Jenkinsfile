pipeline {
  agent any
  stages {
    stage('inicio') {
      steps {
        echo 'Iniciando construccion de proyecto'
        sh 'env'
      }
    }

    stage('instalacion') {
      steps {
        sh 'gcc -v'
      }
    }

  }
}