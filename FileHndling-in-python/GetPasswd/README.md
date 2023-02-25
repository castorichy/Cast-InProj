<h2 style="text-align: center" > GetPass MoDule In Python</h2>
<p><strong>getpass()</strong> is used to Prompts password without echoing or without showing password when entering. its also called blind password.</p>

<h3>Getpass provides two functions</h3>
1. getpass()
2. getuser()

<h5>getpass()</h5>
<p>It provides hiden password without echoing when Prompts
The getpass() function is used to prompt to users using the string prompt and reads the input from the user as Password.The input read defaults to “Password: ” is returned to the caller as a string.<p>
<h3>Format<h3>

`getpass.getpass(Prompts="password": Stream=None)`

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
