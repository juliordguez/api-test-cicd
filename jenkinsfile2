pipeline {

    agent { label 'windows-agent' }

    options {
        skipDefaultCheckout()   // No hacer checkout automático
    }

    stages {

        stage('Validar rama') {
            when {
                expression { env.BRANCH_NAME == 'dev' }
            }
            steps {
                echo "Ejecutando pipeline porque la rama es: ${env.BRANCH_NAME}"
            }
        }

        stage('Checkout') {
            when {
                expression { env.BRANCH_NAME == 'dev' }
            }
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            when {
                expression { env.BRANCH_NAME == 'dev' }
            }
            steps {
                bat '''
                    echo ===== VERSION DE PYTHON =====
                    python --version

                    echo ===== CREAR ENTORNO VIRTUAL =====
                    python -m venv venv

                    echo ===== ACTIVAR ENTORNO VIRTUAL =====
                    call venv\\Scripts\\activate.bat

                    echo ===== ACTUALIZAR PIP =====
                    pip install --upgrade pip

                    echo ===== INSTALAR REQUIREMENTS =====
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            when {
                expression { env.BRANCH_NAME == 'dev' }
            }
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    pytest
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado."
        }
    }
}
