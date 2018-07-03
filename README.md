# Logs Analysis

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

Using that information, This project will answer questions about the site's user activity.
It connects that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Requirements:

### To use this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

### 1- Install the Virtual Machine

you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

  #### Use a terminal
    
  You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system,         your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the     Git software. If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads).

  #### Install VirtualBox
  
  VirtualBox is the software that actually runs the virtual machine. You can download it from
  [virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your       operating system. You do not   need the extension pack or the SDK. You do not need to launch VirtualBox after installing     it; Vagrant will do that.
  
  **Ubuntu users:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a     reported bug, installing VirtualBox from the site may uninstall other software you need.
  
  #### Install Vagrant
  
  Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.   [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

  **Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure   to allow this.
  
  #### Download the VM configuration
  
  There are a couple of different ways you can download the VM configuration:

  1. You can download and unzip this file: [FSND-Virtual-Machine.zip](https://goo.gl/ujE6Wb) This will give you a directory     called **FSND-Virtual-Machine**. It may be located inside your **Downloads** folder.

  2. Alternately, you can use Github to fork and clone the repository <https://github.com/udacity/fullstack-nanodegree-vm>.

  Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with     `cd`. Inside, you will find another directory called vagrant. Change directory to the vagrant directory.

  #### Start the virtual machine
  
  From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the   Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet         connection is.

  When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log   in to your newly installed Linux VM!
  
  #### Logged in!
  
  If you are now looking at a shell prompt that starts with the word vagrant, congratulations — you've gotten logged into       your Linux VM.
  
  #### Logging out and in
  
  If you type `exit` (or `Ctrl-D`) at the shell prompt inside the VM, you will be logged out, and put back into your host         computer's shell. To log back in, make sure you're in the same directory and type `vagrant ssh` again.

  If you reboot your computer, you will need to run `vagrant up` to restart the VM.
  
### 2- Download the data:

[Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database.

To load the data, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

Here's what this command does:
`psql` — the PostgreSQL command line program
`-d news` — connect to the database named news which has been set up for you
`-f newsdata.sql` — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### 3- Download and install python 2.7 from [here](https://www.python.org/downloads/) .

### 4- Download all files from [logs-analyasis](https://github.com/DoaaMakhlouf/logs-analysis).
