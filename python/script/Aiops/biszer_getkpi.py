import requests

url = "http://10.251.4.18:8083/api/kpi/simplified"

headers = {
    "Cookie": "UA=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJkdXJhdGlvbiI6MzYwMDAwMCwibGFzdExvZ2luIjoxNzAzMjI0MjY0NzQwLCJuYW1lcyI6IltcImpheFwiLFwibG9nQW5hbHlzaXNcIixcImxvZ1NwZWVkXCJdIiwic2luZ2xlU2lnbk9uIjpmYWxzZSwid2l0aFNlcnZpY2VBdXRoIjoie1wiamF4XCI6dHJ1ZSxcImdhdWdlXCI6dHJ1ZSxcInZpc2lvblwiOnRydWUsXCJkYXRhTW9kZXJuaXphdGlvblwiOnRydWUsXCJkZWFsQW5hbHlzaXNcIjp0cnVlLFwiY21kYlwiOnRydWUsXCJsb2dBbmFseXNpc1wiOnRydWUsXCJsb2dTcGVlZFwiOnRydWUsXCJyZWZpbmVyXCI6dHJ1ZSxcIkFJT3BzXCI6dHJ1ZX0iLCJzZXNzaW9uSWQiOjUwNTI0MTQ4NDQ2MDEzNDQsInVzZXJOYW1lIjoiYWRtaW4iLCJ1c2VySWQiOiJKc3FpbkkxdjJwcFY4dXIxK0NTbUxITHQ1ano2WGlHVVRPWHNteTdhUkdFTWxQdG51S1Q0QlpUQ3VlMGw5SVdpVU1EMnd1dklVZmFnZ0JxRjFHaGVQTnRlNUVhbXRKa3pwNjcxTEMrVEZBYmEvUlUzcEhObllUeE5GaVBPMXFweStvQjU3UWcwU01Mb2hlM0s4Ulg3T1ZXakNVa3Rhb2FXcUM0b0R1d3podk09IiwicHJvZHVjdHMiOiJ7fSJ9.d2Luik1xJEtQDO6gR-ukMwGa1YJPWb2J-c5BNCCPXDZohDxmU__qu7_yQxbs6IboC0xGLtRCMf2nANv6BYDuKA",
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJmdWxsX25hbWUiOiJzdXBlcmFkbWluIiwiZXhwIjoxNzA2NzY5MTE5LCJ1c2VybmFtZSI6ImFpb3BzIiwicm9sZXMiOltdfQ.skbuAuUNN4vNLWruxJxEIhzievfyG_Q7kmr6-sUq5mJJh7iwFHiPloC0CUmis4ACSb4gVTil0FIeSAEmUBdAFQ"
}

response = requests.request("GET", url, headers=headers)

print(response.text)