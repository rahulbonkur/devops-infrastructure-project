DOCKER_IP = sh(
  script: "terraform output -raw docker_host_public_ip",
  returnStdout: true
).trim()

ANSIBLE_IP = sh(
  script: "terraform output -raw ansible_slave_public_ip",
  returnStdout: true
).trim()
