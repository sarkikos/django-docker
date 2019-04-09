node {
    def registry = "localhost:5000"
    def imagename = "djangodocker"
    def docker_image = "${registry}/${imagename}:testing"

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        docker.build docker_image
    }
}