@echo off

if not exist venv (
    echo Creating virtual environment...
    py -3.11 -m venv venv
)


echo Activating virtual environment...
call venv\Scripts\activate
git pull origin master
if not exist venv\Lib\site-packages\installed (
    if exist requirements.txt (
		echo installing wheel for faster installing
		pip install wheel
        echo Installing dependencies...
        pip install -r requirements.txt
        echo. > venv\Lib\site-packages\installed
    ) else (
        echo requirements.txt not found, skipping dependency installation.
    )
) else (
    pip install -r requirements.txt
    echo Dependencies already installed, skipping installation.
)

echo Starting the bot...
python main.py -a 1


echo done
pause
