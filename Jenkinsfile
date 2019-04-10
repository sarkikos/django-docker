node {
    def registry = "localhost:5000"
    def imagename = "djangodocker"
    def docker_image = "${registry}/${imagename}:testing"

    stage('Clone repository') {
        checkout scm
    }

    stage('Build Docker image') {
        //docker.build docker_image
        docker.build(docker_image, "./django")
    }

    stage('Push Docker image') {
        docker.push(docker_image)
    }
}