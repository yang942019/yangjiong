pipeline{
    agent any
    stage{
        stage(){
            steps{
                bat '''workon jupyter
                       python run.py'''
            }
        }
    }
    post {
      always {
        // One or more steps need to be included within each condition's block.

      }
    }

}