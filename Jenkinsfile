pipeline {
  agent any

  environment {
    VENV = ".venv"
  }

  options {
    ansiColor('xterm')
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh '''
          python3 -m venv ${VENV}
          . ${VENV}/bin/activate
          pip install -U pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Syntax / Lint / Types') {
      steps {
        sh '''
          . ${VENV}/bin/activate
          ruff check .
          ruff format --check .
          mypy app.py
          python -m py_compile app.py
        '''
      }
    }

    stage('Unit Tests') {
      steps { 
        sh ". ${VENV}/bin/activate && pytest -m unit -q --cov=."
      }
    }

    stage('Integration Tests') {
      steps {
        sh ". ${VENV}/bin/activate && pytest -m integration -q"
      }
    }

    stage('Deploy to Staging') {
      when { branch 'main' }
      steps {
        echo 'Deploying to staging (placeholder)...'
      }
    }

    stage('Manual Approval for Prod (4-eyes)') {
      when { branch 'main' }
      steps {
        script {
          input message: 'Promote to PROD?',
                ok: 'Approve',
                submitter: 'approver'   // create this user in Jenkins
        }
      }
    }

    stage('Deploy to Prod') {
      when { branch 'main' }
      steps {
        echo 'Deploying to prod (placeholder)...'
      }
    }
  }

  post {
    always {
      cleanWs()
    }
  }
}
