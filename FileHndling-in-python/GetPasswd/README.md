<h2 style="text-align: center" > GetPass MoDule In Python</h2>
<p><strong>getpass()</strong> is used to Prompts password without echoing or without showing password when entering. its also called blind password.</p>

## **Getpass provides two functions **
1. getpass()
2. getuser()

###**getpass()**
<p>It provides hiden password without echoing when Prompts
The getpass() function is used to prompt to users using the string prompt and reads the input from the user as Password.The input read defaults to “Password: ” is returned to the caller as a string.<p>
####Format

`getpass.getpass(Prompts="password": Stream=None)`

###**Example**

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

####OUTPUT

```
Password: 
Password Entered =  castorichy
```
