properties([pipelineTriggers([pollSCM('* * * * *')])])
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                bat 'C:\Users\yaniv\AppData\Local\Programs\Python\Python39\python.exe print.py'
            }
        }
    }
}
