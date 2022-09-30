def generateHTMLReport(filename, response_data):

    file = open(filename + ".html", "w")

    file.write("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>IP to MAC Address Report</title>
        <link rel="stylesheet" href="css\styles.css">
    </head>
    <body>
    """)

    for key in response_data.keys():  # For every key (valid query) in response_data in main.py
        file.write(f"""
        <table>
            <thead>
                <th colspan="2">{key}</th>
            </thead>
            <tbody>
        """)

        for value in response_data[key]:
            value = value.split("|")  # [0] = IP Addr, [1] = MAC Addr
            file.write(f"""
            <tr>
                <td>{value[0]}</td>
                <td>{value[1]}</td>  
            </tr>
            """)

        file.write("""
        </table>
        """)  # Close the <table>

    file.write(f"""
    </body>
    </html>
    """)

    return True
