total=input()
lista=total.split()
euros=int(lista[0])
cent=int(lista[1])
bill500=euros//500
bill200=(euros-500*bill500)//200
bill100=(euros-200*bill200-500*bill500)//100
bill50=(euros-100*bill100-200*bill200-500*bill500)//50
bill20=(euros-100*bill100-200*bill200-500*bill500-bill50*50)//20
bill10=(euros-100*bill100-200*bill200-500*bill500-bill50*50-bill20*20)//10
bill5=(euros-100*bill100-200*bill200-500*bill500-bill50*50-bill20*20-bill10*10)//5
mon2e=(euros-100*bill100-200*bill200-500*bill500-bill50*50-bill20*20-bill10*10-bill5*5)//2
mon1e=euros-100*bill100-200*bill200-500*bill500-bill50*50-bill20*20-bill10*10-bill5*5-mon2e*2
mon50c=cent//50
mon20c=(cent-mon50c*50)//20
mon10c=(cent-mon50c*50-mon20c*20)//10
mon5c=(cent-mon50c*50-mon20c*20-mon10c*10)//5
mon2c=(cent-mon50c*50-mon20c*20-mon10c*10-mon5c*5)//2
mon1c=cent-mon50c*50-mon20c*20-mon10c*10-mon5c*5-mon2c*2
print(f"""Banknotes of 500 euros: {bill500}
Banknotes of 200 euros: {bill200}
Banknotes of 100 euros: {bill100}
Banknotes of 50 euros: {bill50}
Banknotes of 20 euros: {bill20}
Banknotes of 10 euros: {bill10}
Banknotes of 5 euros: {bill5}
Coins of 2 euros: {mon2e}
Coins of 1 euro: {mon1e}
Coins of 50 cents: {mon50c}
Coins of 20 cents: {mon20c}
Coins of 10 cents: {mon10c}
Coins of 5 cents: {mon5c}
Coins of 2 cents: {mon2c}
Coins of 1 cent: {mon1c}""")