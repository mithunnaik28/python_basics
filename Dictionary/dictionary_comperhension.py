cp={
    "murdeshawer":150,
    "bailure":98,
    "doddabalase":56,
    "bhatkal":200
}
bc={key:value for key,value in cp.items() if value>100 }

print(bc)

# {'murdeshawer': 150, 'bhatkal': 200}
