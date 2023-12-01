try:
    import webbrowser
    form = open('Table.html', 'w')
    html_template = """
    <html lang='en'>
        <head>
        <meta charset='utf-8'>
        <meta name="view-port" content='width=device-width, initial_scale='1.0''>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Time Table</title>
        </head>
        <table border="1" cellspacing="3" cellpadding="20">
            <caption>PROGRAMMING CLASS TIME TABLE</caption>
            <thead>
                <tr>
                    <th>Days/time</th>
                    <th>9:00 - 10:00</th>
                    <th>10:00 - 11:00</th>
                    <th>11:00 - 12:00</th>
                    <th>1:00 - 2:00</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th>Mon</th>
                    <td>Web Development</td>
                    <td>Basic html</td>
                    <td rowspan="3" class='break'>Break</td>
                    <td>CSS</td>
                </tr>
                <tr>
                    <th>Tue</th>
                    <td colspan="2">Cyber Security</td>
                    <td>CSS</td>
                </tr>
                <tr>
                    <th>Wed</th>
                    <td>Data Analysis</td>
                    <td>UI/UX</td>
                    <td>Web Design</td>
                </tr>
                <tr>
                    <th>Thu</th>
                    <td>UI/UX</td>
                    <td>Break</td>
                    <td colspan="2">Web  Design</td>
                </tr>
                <tr>
                    <th>Fri</th>
                    <td colspan="2">Web Development</td>
                    <td>Break</td>
                    <td>Project Defense</td>
                </tr>
            </tbody>
        </table>
    </html>"""
    form.write(html_template)
    form.close()
    webbrowser.open('Table.html')
except Exception as Error:
    print(Error)