Vagrant.configure("2") do |config|
  # Specify the base box
  config.vm.box = "ubuntu/bionic64"

  # Set up port forwarding to access Flask app on the host machine
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # Upload the hello.py file to the VM
  config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"

  # Provision the VM with a shell script to install necessary packages and run the Flask app
  config.vm.provision "shell", inline: <<-SHELL
    # Update package list
    sudo apt-get update

    # Install Python and pip
    sudo apt-get install -y python3 python3-pip

    # Install Flask
    pip3 install Flask

    # Navigate to home directory and run the Flask app
    cd /home/vagrant
    FLASK_APP=hello.py flask run --host=0.0.0.0 &
  SHELL
end
