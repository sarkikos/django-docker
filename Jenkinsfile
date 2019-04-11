node {
//    def registry = ${env.TEST_DOCKER_REGISTRY}
    def registry = "localhost:5000"
    def imagename = "djangodocker"
    def docker_image = "${registry}/${imagename}:testing"

    stage('Clone repository') {
        checkout scm
    }

    stage('Build and push Docker image') {
        //docker.build docker_image
        def newImage = docker.build(docker_image, "./django")
        newImage.push()
    }
}
