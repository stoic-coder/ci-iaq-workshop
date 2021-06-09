pipeline {
    agent any

    environment {
      HCLOUD_TOKEN = credentials('hcloud-token')
    }

    stages {
        stage('Start Test VM') {
            steps {
              dir('ci-test-vm') {
                sh 'terraform init'
<<<<<<< HEAD
                  sh 'terraform apply -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"'
=======
                // hier soll die VM gestartet werden
                sh 'terraform apply -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"'
>>>>>>> exercise-01
              }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
              sh 'ansible-galaxy collection install -r requirements.yml'
<<<<<<< HEAD
              sh 'ansible-playbook -i inventory/test.hcloud.yml install-hero-app.yml'
            }
        }

        stage('Run Testinfra Tests') {
            steps {
              sh "py.test --connection=ansible --ansible-inventory inventory/test.hcloud.yml --hosts='ansible://ansible-test-instance' --force-ansible -v test/*.py" // hostnamen anpassen
=======
              // hier sollen die Playbooks laufen
              sh 'ansible-playbook -i inventory/test.hcloud.yml install-hero-app.yml'
>>>>>>> exercise-01
            }
        }
    }
    post {
        always {
          dir('ci-test-vm') {
<<<<<<< HEAD
            sh 'terraform destroy -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"'
=======
             // hier soll die VM gelöscht werden
             sh 'terraform destroy -auto-approve -var="hcloud_token=${HCLOUD_TOKEN}"'
>>>>>>> exercise-01
          }
         }
    }
}
