{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0f40263c-fd44-4ba6-b466-c6d88178eeef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2026-02-06 15:03:30.183507] Status: 200\n",
      "Links found on page:\n",
      "https://lovable.dev/projects/caeda0b6-ecd4-4861-9b64-1843abddfae4?utm_source=lovable-badge\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import datetime\n",
    "\n",
    "# Target webpage\n",
    "url = \"https://bharath-bakery.lovable.app/\"\n",
    "\n",
    "def scan_page(url):\n",
    "    print(f\"\\n--- Scan started at {datetime.datetime.now()} ---\")\n",
    "    try:\n",
    "        response = requests.get(url, timeout=10)\n",
    "        status = response.status_code\n",
    "        print(f\"Website status: {status}\")\n",
    "\n",
    "        if status == 200:\n",
    "            soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "            links = [a['href'] for a in soup.find_all('a', href=True)]\n",
    "            print(f\"Found {len(links)} links on the page.\")\n",
    "\n",
    "            # Check each link\n",
    "            for link in links:\n",
    "                if link.startswith(\"http\"):\n",
    "                    try:\n",
    "                        r = requests.get(link, timeout=5)\n",
    "                        if r.status_code == 200:\n",
    "                            print(f\"[OK] {link}\")\n",
    "                        else:\n",
    "                            print(f\"[BROKEN] {link} (status {r.status_code})\")\n",
    "                    except Exception as e:\n",
    "                        print(f\"[ERROR] {link} ({e})\")\n",
    "                else:\n",
    "                    print(f\"[SKIP] {link} (relative link)\")\n",
    "        else:\n",
    "            print(\"Website might be down or unreachable.\")\n",
    "    except Exception as e:\n",
    "        print(f\"Error scanning page: {e}\")\n",
    "\n",
    "scan_page(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14b05716-b6c5-40b1-8824-9282adfbc24d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:ANACONDA]",
   "language": "python",
   "name": "conda-env-ANACONDA-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
