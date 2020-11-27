pipeline {
  agent any
  stages {
    stage('inicio') {
      steps {
        echo 'Iniciando construccion de proyecto'
        sh 'env'
      }
    }

    stage('instalar') {
      steps {
        sh 'gcc -v'
      }
    }

    stage('compilar') {
      steps {
        sh '''gcc programa.c -o mi_programa
ls -lrt'''
        sh './mi_programa'
      }
    }

    stage('limpiar') {
      steps {
        sh 'rm mi_programa'
      }
    }

  }
}