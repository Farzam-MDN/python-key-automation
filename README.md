# python-key-automation


# ![Pythonmation Logo](https://i.imgur.com/wyITnRp.png)


python-key-automation (also known as 'Pythonmation') is a keyboard recorder tool that allows you to replay your recordings. It can be used to automate keyboard activities.
Currently the tool does not provide mouse automation.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need the following in order to run the application as intended on your machine:

```
Python 3 or above
Pip package installer for python
```

### Installing and Running the application


**Step1 - Application setup**
First clone this repository or download it manually to a working directory on your computer.
Thereafter, open terminal/cmd inside the 'python-key-automation' directory on your computer.
Now Run the following command in your terminal/cmd:

```
pip install -r requirements.txt
```
Open cmd/terminal in the 'python-key-automation' directory. Thereafter, run the command below in the cmd/terminal.

```
py python-key-automation.py
```

The application is now running in your cmd/terminal.
Now the application should display a welcome message and prompt you to provide an input.


**Step2 - Create a new recording** 
You will create a new recording. Type '2' (without the quotation marks) in the cmd/terminal and press enter.


The application should prompt you to name the session, Before you name the session. You need to do what you will do in the session. In this demo you are supposed to open the notepad or any other text editor (when the recording has started) and type 'I love python' without the quotaion marks. 

Since it is a good practice to name your session something related to the task you will be doing, type 'I love python' (without quotaion marks) in the cmd and press enter.

You will see a countdown of 5 seconds in the cmd/terminal.
After 5 seconds the recording of keyboard starts.
When the recording starts, open notepad or any other text editor that you have. Inside the notepad/text-editor type 'I love python' (without the quotation marks).
Press 'F1' Key. Now the recrdoing has paused. Now open the cmd/terminal that the app is running inside it and press enter. The application will unpause. Open notepad/text-editor again and type 'Goodbye' (without the quotation marks). Now press the 'F2' key. The application has now stopped.

**Step3- Replay the recording**
Go to the 'python-key-automation' directory. You can see a new text file has been added to files. The name of the file includes 'I love python' somewhere in the beginning of it. This file contains all of the information about the 'I love python' recording.
copy the full name of this text file (copy the name of the file as well as the .txt extension).
Open terminal/cmd in the 'python-key-automation' directory.
Run the following command in the terminal/cmd.
```
py python-key-automation.py
```
The application is now running in your cmd/terminal.
Now the application should display a welcome message and prompt you to provide an input.

You will replay a new recording. Type '1' (without the quotation marks) in the cmd/terminal and press enter.

Now the application asks for the full name of the recording file. Paste the text you previously copied to your clipboard in the cmd/terminal and press enter.

The application asks you how many times you want to play the recording. Type '1' (without the quotation marks) in the cmd/terminal and press enter.

The application will countdown from 10 to 1 and then it will replay the recording.



**Extra: Replay your recordings using the replay history**
Open replayhistory.txt in 'python-key-automation' directory.
In case in the full name of your recording file is not in this file, paste the full name of the recording on a new line at the end of the file (the recording name should include the .txt extension). 
Open terminal/cmd in the 'python-key-automation' directory.
Run the following command in the terminal/cmd.
```
py python-key-automation.py
```
The application is now running in your cmd/terminal.
Now the application should display a welcome message and prompt you to provide an input.

You will replay a new recording. Type '1' (without the quotation marks) in the cmd/terminal and press enter.

You will see a list of recordings in the cmd/terminal. You should be able to see the name of your recording in this list. In case you found the name in the list, you will also see a reference code before the name (for example 'num0'). type the reference code in the cmd/terminal and press enter.
Now type a number indicating how many times you want the recording to replay.
The recording will replay when the countdown ends!


## Contributing

Feel free to fork and expand this project! Send a pull request if you would like to add your code to the project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Farzam-MDN/JustShareKeys/releases). 

## Authors

* **Farzam Madani** - *Creation of the core application* - [Farzam-MDN](https://github.com/Farzam-MDN)

See also the list of [contributors](https://github.com/Farzam-MDN/JustShareKeys/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Farzam-MDN/JustShareKeys/blob/master/LICENSE) file for details

## Acknowledgments

* Big thanks to anyone whose library was used in this project!
