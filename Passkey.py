try:
    import webbrowser
    Key = open('passkey.html', 'w')
    html_template = """
    <html lang='en'>
        <head>
        <meta charset='utf-8'>
        <meta name="view-port" content='width=device-width, initial_scale='1.0''>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>form Element</title>
        </head>
        <body>
            <div id='wrapper' style='background-color: red;'>
            <form  action='' method=''>
            <input type='text' placeholder='Enter your fisrt name'>
            <input type='password' placeholder='Password here;'>
            <button type='submit'>Sign In</button>
            </form>
            </div>
        </body>
    </html>"""
    Key.write(html_template)
    Key.close()
    webbrowser.open('passkey.html')
except Exception as Error:
    print(Error)