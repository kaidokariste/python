import requests
import datetime


def post_im(message):
    requests.post("<MS Teams hook>", json={"text": message})


def modify_file(action, write_message="EMPTY"):
    if action == "READ":
        f = open("pereujumine.txt", "r")
        status = f.read()
        f.close()
        return status
    elif action == "WRITE":
        f = open("pereujumine.txt", "w")
        f.write(write_message)
        f.close()
        return write_message


def pereujumine_bron():
    date = datetime.date.today()
    # We are interested not current week  but 1 weeks ahead.
    week_number = date.isocalendar()[1] + 1
    current_week = f"W{week_number}"
    last_checked = modify_file("READ")
    print(current_week + ' lc ' + last_checked)
    if current_week != last_checked:
        url = f"https://client.bronn.ee/book_groups/week/186/{week_number}/2023"
        result = requests.get(url)
        large_text = str(result.text)
        if "Laupäev" in large_text or "Pühapäev" in large_text:
            message = f"Beebysport registreerimine avatud.\n{url}"
            post_im(message)
            modify_file('WRITE', f"W{week_number}")


if __name__ == '__main__':
    pereujumine_bron()
