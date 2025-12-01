pipeline {
    agent {
        docker {
            image 'python:3.12'
            args '-u'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    pip install --upgrade pip
                    if [ -f "requirements.txt" ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    if [ -d "tests" ]; then
                        pytest
                    else
                        echo "No hay carpeta tests, saltando tests"
                    fi
                '''
            }
        }
    }
}
