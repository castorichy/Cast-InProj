<h2 style="text-align: center" > GetPass MoDule In Python</h2>
<p><strong>getpass()</strong> is used to Prompts password without echoing or without showing password when entering. its also called blind password.</p>

<h3>Getpass provides two functions</h3>
<li> getpass()</li>
<li>getuser()</li>

<h3>getpass()</h3>
<p>It provides hiden password without echoing when Prompts
The getpass() function is used to prompt to users using the string prompt and reads the input from the user as Password.The input read defaults to “Password: ” is returned to the caller as a string.</p>
<h3>Format</h3>

`getpass.getpass(Prompts="password": Stream=None)`
<p>Here no prompt is provided by the user insteed it uses default prompt `password`</p>

<h5>Example</h5>

```
import getpass as gp
"""This module hides password Prompts echoes"""

def easyLog():
    try:
        paswd = gp.getpass()
    except Exception as Error:
        print("Error: ", Error)
    else:
        print("Password Entered = ", paswd)

easyLog()
```

<h5>OUTPUT</h5>

```
Password: 
Password Entered =  castorichy
```
<p> In case of security pass,words one can ask for security quastions like Whats your fevorite color?<br> Here we user prompt to display the security quastions but the input doesnt prompt as you type.</p>

<h5>Example</h5>
<p> Click this <a href="https://github.com/castorichy/Cast-InProj/blob/main/GetPasswd/getuser_prompt.py" alt="getpass">here</a> to get the code and test it your self</p>
<h3> getuser() </h3>
<p>The getuser() function displays the login name of the user. This function checks the environment variables `LOGNAME, USER, LNAME and USERNAME`, in order, and returns the value of the first non-empty string. </p>
<h5>Example</h5>
<p>click <a href="" alt="getuser()">here</a> to get the souce code and try it yourself </p>

