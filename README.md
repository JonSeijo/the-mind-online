# The Mind Online

This is a clone of the card game The Mind. You can play it online at https://jonseijo.com/themind

You need at least 2 players in the same lobby to play.

Note that there are some features missing, like the throwing star cards

---


The server is implemented in python3, using [pyre](https://pyre-check.org/) for type checking. The API is written with Flask and Socket.io (see https://flask-socketio.readthedocs.io/en/latest/)

The frontend is written with [React](https://reactjs.org/)


---

## Server

### INSTALL:

I assume python3.7 for the guide, it probably works in previous versions but I didn't test it. Replace 3.7 in the commands for the version you use.

Install python3.7 headers:
```sudo apt-get install python3.7-dev```

Install venv for python3.7:
```sudo apt-get install python3.7-venv```

Step into the-mind-online:
```cd the-mind-online```

Create a virtual enviroment to install required python libraries:
```python3.7 -m venv the-mind-venv```

Activate the virtual enviroment:
```source the-mind-venv/bin/activate```

You should see "(the-mind-venv)" in the command prompt

Go to 'the-mind' directory and install the requirements. Important, the virtual enviroment MUST be activated!

```pip install -r requirements.txt```


## RUN

You should activate the virtual enviroment every time you want to run the server:

```source the-mind-venv/bin/activate```

Run tests:
```./test.sh```

Run tests with type checking (pyre is needed):
```./test.sh all```

Start the server:
```./serve.sh```

The server runs by default on localhost:5000


-----------------------------

## Client

### INSTALL

I used yarn but it can probably be replaced with just npm.

Install [yarn](https://classic.yarnpkg.com/en/docs/install/#debian-stable)

(you also need ```nodejs``` if is not installed automatically)

In ```the-mind-react``` directory, install the dependencies specified in package.json: ``` yarn install```


### RUN

In ```the-mind-react```:

``` yarn start```

You can access the client from localhost:3000
