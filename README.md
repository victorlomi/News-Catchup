# News Catchup
A web app to keep up with the latest news. The app makes it easy to check what's going on in the world from different news sources; CNN News, BBC News, and others. The app also shows short descriptions allowing users to quickly decide what they want to read.

**Author: Victor Lominyo**

**Live Link: https://news-catchup-flask.herokuapp.com/**


Technologies Used
=
- Python 
- Flask


Setup Instructions and Installation
=
1. Clone the repository on to your computer

```
$ git clone https://github.com/victorlomi/News-Catchup
```

2. Navigate to the project directory 

```
$ cd News-Catchup
```

3. Create virtual environment and activate it

```
$ python3 -m venv venv
$ . venv/bin/activate
``` 

4. Install packages

```
$ pip install -r requirements.txt
```

5. set environment variables and run

```
$ export FLASK_APP=news_catchup.py
$ export FLASK_ENV=development
$ export API_KEY=<Your api key>
$ flask run
```

You are all set!

Contact
=
**Email:** victorlominyo@gmail.com

License
=
MIT License

Copyright (c) 2020 victorlomi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
