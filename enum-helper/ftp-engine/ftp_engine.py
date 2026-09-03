import xml.etree.ElementTree as ET


def format_output(file):
    tree = ET.parse(file)
    root = tree.getroot()

    ftp_result = {
        "ip": "",
        "port": "",
        "service": "",
        "anonymous": False,
        "total_files": 0,
        "files": []
    }

    # IP
    ip = root.find('.//address[@addrtype="ipv4"]')
    if ip is not None:
        ftp_result["ip"] = ip.get("addr", "")

    # FTP port
    port = root.find('.//port[@portid="21"]')

    if port is not None:
        ftp_result["port"] = port.get("portid", "")

        # Service belonging specifically to port 21
        service = port.find("service")

        if service is not None:
            service_info = [
                service.get("name"),
                service.get("product"),
                service.get("version")
            ]

            ftp_result["service"] = " ".join(
                value for value in service_info if value
            )

    # Anonymous FTP result
    ftp_anon = root.find('.//script[@id="ftp-anon"]')

    if ftp_anon is not None:
        output = ftp_anon.get("output", "")
        lines = output.splitlines()

        ftp_result["anonymous"] = True

        # Skip the first line:
        # "Anonymous FTP login allowed ..."
        for line in lines[1:]:
            parts = line.split()

            # Skip unexpected / invalid lines
            if len(parts) < 9:
                continue

            writable = "[NSE: writeable]" in line

            # Filename may contain spaces
            name = " ".join(parts[8:])
            name = name.replace(" [NSE: writeable]", "")

            ftp_result["files"].append({
                "permission": parts[0],
                "owner": parts[2],
                "group": parts[3],
                "name": name,
                "writable": writable
            })

        ftp_result["total_files"] = len(ftp_result["files"])

    return ftp_result


def print_ftp_result(data):
    separator = "- - - - - - - - - - - - - - - - - - - - -"

    print(separator)
    print(f"[ IP\t\t] {data['ip']}")
    print(f"[ PORT\t\t] {data['port']}")
    print(f"[ SERVICE\t] {data['service']}")
    print(
        f"[ ANONYMOUS\t] "
        f"{'Allowed' if data['anonymous'] else 'Not allowed'}"
    )
    print(separator)

    if data["total_files"] > 0:
        print(f"[ TOTAL FILES\t] {data['total_files']} file(s) found")

        for i, file in enumerate(data["files"], start=1):
            print(f"- - - - - - - - - [ {i} ] - - - - - - - - -")
            print(
                f"* PERMISSION\t: {file['permission']}\n"
                f"* OWNER\t\t: {file['owner']}\n"
                f"* GROUP\t\t: {file['group']}\n"
                f"* NAME\t\t: {file['name']}\n"
                f"* WRITABLE\t: {file['writable']}"
            )

        print(separator)


output = format_output("ftp_scan_strict.xml")
print_ftp_result(output)