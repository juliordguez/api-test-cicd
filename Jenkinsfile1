pipeline {
    agent { label 'windows-agent' }

    options {
        skipDefaultCheckout()
    }

    stages {
        stage('Debug vars') {
            steps {
                echo "BRANCH_NAME = '${env.BRANCH_NAME}'"
                echo "GIT_BRANCH  = '${env.GIT_BRANCH}'"
            }
        }

        // lo demás igual...
    }

    post {
        always {
            echo "Pipeline finalizado."
        }
    }
}
