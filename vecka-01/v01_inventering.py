# Racket, en enhet per rad. Byt ut mot era faktiska enheter.
device_1 = "Switch0"
model_1 = "WS-CSWitch-PT"
role_1 = "Switch, access"
device_2 = "router0"
model_2 = "Cisco C7200"
role_2 = "Router, lager 3"
# Rubrikrad, och en linje under den.
print("UTRUSTNINGSLISTA")
print("-" * 52)
# Varje rad far samma bredd, sa att kolumnerna hamnar under varandra.
print(f"{device_1:<16}{model_1:<20}{role_1}")
print(f"{device_2:<16}{model_2:<20}{role_2}")
print("-" * 52)
print("Antal enheter: 2")