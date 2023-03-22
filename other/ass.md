First of all - I've gotten enough last minute questions that I think it would be wise to do a general extension for this part until Friday. If you already finished, congrats! You can relax :) I'll also spend some of tonight's class going through hints and doing a sort of office hours help session.

With that said, here are some hints and clarifications:

* Writing the SQL injection test: you will need to upload a file to the server for this one. Assuming you have an open file in a variable named f, you can upload the contents of that file using Django's test client with something like client.post("/url", {"param": f}), where "param" is the name of the form field that holds the uploaded data.
* Writing the command injection test: because "echo hello" produces output in the terminal and not in the response the server sends you, you can't just check "hello" is in the response. Instead, you should do something that has a visible side effect, like creating a file. You can do that with "touch foo", and then use "os.path.exists" from Python's "os" module to check if "foo" exists.
* In incmdi.txt, var1 and var2 are just placeholder names - you should write the actual names of the parameters (like "card_supplied" or "card_fname") instead.

* For fixing SQL injection, there are two basic ways: using a parameterized query (i.e., call raw with a placeholders string and put the parameter as a second argument, as in: raw("select ... %s", [param])), or using Django's ORM. I generally recommend using the ORM! In particular, have a look at the filter() method, and the contains keyword: https://docs.djangoproject.com/en/4.1/ref/models/querysets/#std:fieldlookup contains

* For fixing the command injection, we saw in class that it's safer to use subprocess.run (with shell=False). Another thing to consider, though, is whether you really need the user to be able to choose a name for their card! Maybe you can just write the card data to a temporary file using tempfile.NamedTemporaryFile(), and then run the card reader on that file?

Finally, it can be helpful to see what it looks like when your attacks succeed, so here are a couple screenshots:

For the SQL injection attack, you'll be able to see the admin password hash on the page itself:

Use a Card
Found card with data: Card object

For the command injection attack, you should look at the terminal window where "python manage.py runserver" is running. Assuming your command is "echo hello", you should see something like:

[07/Mar/2023 21:46:24] "GET /use.html HTTP/1.1" 200 7920
running: /Users/moyix/git/appsec_hw2/LegacySite/../../bins/giftcardreader_mac.tmp_file

sh: line 1: 11701 Segmentation fault: 11 /Users/moyix/git/appsec_hw2/LegacySite/../../bin/giftcardreader_mac.tmp_file sh: 2: parser.gftcrd: command not found.
b'hi\n'

Internal Server Error: /use.html
Traceback (most recent call last):
File response = get_response(request)
File
response = wrapped_callback(request, *callback_args, **callback_kwargs)
File "/Users/moyix/git/appsec_hw2/LegacySite/views.py", line 211, in use
signature = json.loads(card_data)['records'][0]['signature']

"/Users/moyix/.virtualenvs/appsec_hw2_sp2023/lib/python3.10/site-pac
"/Users/moyix/.virtualenvs/appsec_hw2_sp2023/lib/python3.10/site-pac

File "/usr/local/Cellar/python@3.10/3.10.1_1/Frameworks/Python.framework
return default_decoder.decode(s)

File "/usr/local/Cellar/python@3.10/3.10.1_1/Frameworks/Python.framework