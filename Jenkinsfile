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
        sh 'chmod +x -R ./scripts/build.sh'
        sh 'cat versionImage | xargs ./scripts/build.sh'
      }
    }

    stage('Run container') {
      steps {
        sh './run_container.sh'
      }
    }

    stage('test') {
      steps {
        sleep 10
        sh './scripts/test_cont.sh'
      }
    }

  }
}