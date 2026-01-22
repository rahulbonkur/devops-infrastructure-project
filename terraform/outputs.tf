output "docker_host_public_ip" {
  description = "Public IP of Docker Host EC2"
  value       = aws_instance.docker_host.public_ip
}

output "ansible_slave_public_ip" {
  description = "Public IP of Ansible Slave EC2"
  value       = aws_instance.ansible_slave.public_ip
}
