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
        sh 'chmod +x -R ./scripts/'
        sh 'cat versionImage | xargs ./scripts/build.sh'
      }
    }

    stage('Run container') {
      steps {
        sh 'docker run --name proyapi -itd --rm -p 80:5000 comando132/proyectoapi:1.1'
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