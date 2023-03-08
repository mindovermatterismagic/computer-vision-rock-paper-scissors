# Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera. 

## Milestone 1 

- Creates a remote github repository for this project to version control the software.

- Connects the remote repository to a local clone using the command line.

```bash
git clone git clone https://github.com/d4min/computer-vision-rock-paper-scissors.git
```

## Milestone 2

- Created and trained a deep learning model using Teachable Machine to recognise images of users gesturing rock, paper, scissors or nothing through the webcam. 

## Milestone 3

- Used conda to create and install the dependencies required for the project.

- First created a new virtual environment with conda where the dependencies would be installed. 

```bash
conda create --name computer_vision python
```
It is important to use an environment seperate from base becasue virtual environments let you have a stable, reproducible, and portable environment. You are in control of which packages versions are installed and when they are upgraded. You can have as many environments as you want and this reduces the likelihood of dependencies between projects clashing and causing errors. 

```bash
conda install pip
conda install tensorflow opencv ipykernel
```
- I also exported the conda environment packages to a text file which is kept with the code to allow for other users to be able to install the required dependencies to work with the project.

```bash
conda list --explicit > requirements.txt
```


