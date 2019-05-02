# Devel version
node {
//    def registry = "localhost:5000"
    def registry = "${env.TEST_DOCKER_REGISTRY}"
    def imagename = "djangodocker"
    def docker_image = "${registry}/${imagename}:testing"

    stage('Print environment variables') {
	echo sh(returnStdout: true, script: 'env')
    }

    stage('Clone repository') {
        checkout scm
    }

    stage('Build and push Docker image') {
        //docker.build docker_image
        def newImage = docker.build(docker_image, "./django")
        newImage.push()
    }
}
