# Student-Utility-App

## To get started after clonning the repository:

# 1. we need to install all the packages to run the scripts so head over to terminal directed to this current directory and type the following:
  
  > ## i = use virtual environment(Recommended) to install it:  
  > ### pip install virtualenv


```python
      if i == True:         
          bash:
            virtualenv <venv name>
            source <venv name>/Scripts/activate
            pip install -r requiremts.txt

          cmd:
            virtualenv <venv name>
            <venv name>\Scripts\activate

      else:
        pip install -r requirements.txt
```

# 2. Inside the app.py script head over to  "Default images and music used && CONSTANTS" section (this is the first section) and read the commented function and do as instructed

# 3. As there is already an .exe build of the script you can head over to app.spec and find "-*- file location below to be changed with your path -*-" and do as instructed

# 4 To build the exe file yourself

	go to pyinstaller docs and do as instructed (Recommended)
  
   or
   
	inside in venv type: pyinstaller --onefile --noconsole app.py (the simplest way)
  

# AND DONOT FORGET TO UPADTE YOUR .spec FILE AS in MENTIONED IN POINT 3
