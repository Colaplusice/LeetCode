def is_ip():
    try:

        ip = input()
        ip_list = ip.split(".")
        start_list = ["10", "172", "192"]
        if not len(ip_list) == 4:
            return False

        if not ip_list[0] in start_list:
            return False

        if ip_list[0] == start_list[0]:
            for each in ip_list[1:]:
                if 0 <= int(each) <= 255:
                    return True
            return False
        if ip_list[0] == start_list[1]:
            if 0 <= int(ip_list[1]) < 32:
                for each in ip_list[2:]:
                    if 0 <= int(each) <= 255:
                        return True
            return False
        if ip_list[0] == start_list[2]:
            if ip_list[1] == "168":
                for each in ip_list[2:]:
                    if 0 <= int(each) <= 255:
                        return True
            return False
    except:
        return False

    return False


print(is_ip())
