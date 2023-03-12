def finally_volume(x, unit_summ, y):
	if x == 'Км^3' and y == 'М^3':
		unit_result = float(unit_summ) * 10**9
		return(unit_result)
	elif x == 'Км^3' and y == 'Дм^3':
		unit_result = float(unit_summ) * 10**12
		return(unit_result)
	elif x == 'Км^3' and y == 'См^3':
		unit_result = float(unit_summ) * 10**15
		return(unit_result)
	elif x == 'Км^3' and y == 'Мм^3':
		unit_result = float(unit_summ) * 10**18
		return(unit_result)
	elif x == 'Км^3' and y == 'Км^3':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'М^3' and y == 'Км^3':
		unit_result = float(unit_summ) / 10**9
		return(unit_result)
	elif x == 'М^3' and y == 'Дм^3':
		unit_result = float(unit_summ) * 10**3
		return(unit_result)
	elif x == 'М^3' and y == 'См^3':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'М^3' and y == 'Мм^3':
		unit_result = float(unit_summ) * 10**9
		return(unit_result)
	elif x == 'М^3' and y == 'М^3':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Дм^3' and y == 'Км^3':
		unit_result = float(unit_summ) / 10**12
		return(unit_result)
	elif x == 'Дм^3' and y == 'М^3':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'Дм^3' and y == 'См^3':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'Дм^3' and y == 'Мм^3':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'Дм^3' and y == 'Дм^3':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'См^3' and y == 'Км^3':
		unit_result = float(unit_summ) / 10**15
		return(unit_result)
	elif x == 'См^3' and y == 'М^3':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'См^3' and y == 'Дм^3':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'См^3' and y == 'Мм^3':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'См^3' and y == 'См^3':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Мм^3' and y == 'Км^3':
		unit_result = float(unit_summ) / 10**18
		return(unit_result)
	elif x == 'Мм^3' and y == 'М^3':
		unit_result = float(unit_summ) / 10**9
		return(unit_result)
	elif x == 'Мм^3' and y == 'Дм^3':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'Мм^3' and y == 'См^3':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'Мм^3' and y == 'Мм^3':
		unit_result = float(unit_summ) * 1
		return(unit_result)












def finally_square(x, unit_summ, y):
	if x == 'Км^2' and y == 'М^2':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'Км^2' and y == 'Дм^2':
		unit_result = float(unit_summ) * 10**8
		return(unit_result)
	elif x == 'Км^2' and y == 'См^2':
		unit_result = float(unit_summ) * 10**10
		return(unit_result)
	elif x == 'Км^2' and y == 'Мм^2':
		unit_result = float(unit_summ) * 10**12
		return(unit_result)
	elif x == 'Км^2' and y == 'Км^2':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'М^2' and y == 'Км^2':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'М^2' and y == 'Дм^2':
		unit_result = float(unit_summ) * 100
		return(unit_result)
	elif x == 'М^2' and y == 'См^2':
		unit_result = float(unit_summ) * 10**4
		return(unit_result)
	elif x == 'М^2' and y == 'Мм^2':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'М^2' and y == 'М^2':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Дм^2' and y == 'Км^2':
		unit_result = float(unit_summ) / 10**8
		return(unit_result)
	elif x == 'Дм^2' and y == 'М^2':
		unit_result = float(unit_summ) / 100
		return(unit_result)
	elif x == 'Дм^2' and y == 'См^2':
		unit_result = float(unit_summ) * 100
		return(unit_result)
	elif x == 'Дм^2' and y == 'Мм^2':
		unit_result = float(unit_summ) * 10**4
		return(unit_result)
	elif x == 'Дм^2' and y == 'Дм^2':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'См^2' and y == 'Км^2':
		unit_result = float(unit_summ) / 10**10
		return(unit_result)
	elif x == 'См^2' and y == 'М^2':
		unit_result = float(unit_summ) / 10**4
		return(unit_result)
	elif x == 'См^2' and y == 'Дм^2':
		unit_result = float(unit_summ) / 100
		return(unit_result)
	elif x == 'См^2' and y == 'Мм^2':
		unit_result = float(unit_summ) * 100
		return(unit_result)
	elif x == 'См^2' and y == 'См^2':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Мм^2' and y == 'Км^2':
		unit_result = float(unit_summ) / 10**12
		return(unit_result)
	elif x == 'Мм^2' and y == 'М^2':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'Мм^2' and y == 'Дм^2':
		unit_result = float(unit_summ) / 10**4
		return(unit_result)
	elif x == 'Мм^2' and y == 'См^2':
		unit_result = float(unit_summ) / 100
		return(unit_result)
	elif x == 'Мм^2' and y == 'Мм^2':
		unit_result = float(unit_summ) * 1
		return(unit_result)











def finally_weight(x, unit_summ, y):
	if x == 'Т' and y == 'Ц':
		unit_result = float(unit_summ) * 10
		return(unit_result)
	elif x == 'Т' and y == 'Кг':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'Т' and y == 'Г':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'Т' and y == 'Мг':
		unit_result = float(unit_summ) * 10**9
		return(unit_result)
	elif x == 'Т' and y == 'Т':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Ц' and y == 'Т':
		unit_result = float(unit_summ) / 10
		return(unit_result)
	elif x == 'Ц' and y == 'Кг':
		unit_result = float(unit_summ) * 100
		return(unit_result)
	elif x == 'Ц' and y == 'Г':
		unit_result = float(unit_summ) * 10**5
		return(unit_result)
	elif x == 'Ц' and y == 'Мг':
		unit_result = float(unit_summ) * 10**8
		return(unit_result)
	elif x == 'Ц' and y == 'Ц':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Кг' and y == 'Т':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'Кг' and y == 'Ц':
		unit_result = float(unit_summ) / 100
		return(unit_result)
	elif x == 'Кг' and y == 'Г':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'Кг' and y == 'Мг':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'Кг' and y == 'Кг':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Г' and y == 'Т':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'Г' and y == 'Ц':
		unit_result = float(unit_summ) / 10**5
		return(unit_result)
	elif x == 'Г' and y == 'Кг':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'Г' and y == 'Мг':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'Г' and y == 'Г':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Мг' and y == 'Т':
		unit_result = float(unit_summ) / 10**9
		return(unit_result)
	elif x == 'Мг' and y == 'Ц':
		unit_result = float(unit_summ) / 10**8
		return(unit_result)
	elif x == 'Мг' and y == 'Кг':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'Мг' and y == 'Г':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'Мг' and y == 'Мг':
		unit_result = float(unit_summ) * 1
		return(unit_result)









def finally_length(x, unit_summ, y):
	if x == 'Км' and y == 'М':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'Км' and y == 'Дм':
		unit_result = float(unit_summ) * 10**4
		return(unit_result)
	elif x == 'Км' and y == 'См':
		unit_result = float(unit_summ) * 10**5
		return(unit_result)
	elif x == 'Км' and y == 'Мм':
		unit_result = float(unit_summ) * 10**6
		return(unit_result)
	elif x == 'Км' and y == 'Км':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'М' and y == 'Км':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'М' and y == 'Дм':
		unit_result = float(unit_summ) * 10
		return(unit_result)
	elif x == 'М' and y == 'См':
		unit_result = float(unit_summ) * 100
		return(unit_result)
	elif x == 'М' and y == 'Мм':
		unit_result = float(unit_summ) * 1000
		return(unit_result)
	elif x == 'М' and y == 'М':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Дм' and y == 'Км':
		unit_result = float(unit_summ) / 10**5
		return(unit_result)
	elif x == 'Дм' and y == 'М':
		unit_result = float(unit_summ) / 10
		return(unit_result)
	elif x == 'Дм' and y == 'См':
		unit_result = float(unit_summ) * 10
		return(unit_result)
	elif x == 'Дм' and y == 'Мм':
		unit_result = float(unit_summ) * 100
		return(unit_result)
	elif x == 'Дм' and y == 'Дм':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'См' and y == 'Км':
		unit_result = float(unit_summ) / 10**5
		return(unit_result)
	elif x == 'См' and y == 'М':
		unit_result = float(unit_summ) / 100
		return(unit_result)
	elif x == 'См' and y == 'Дм':
		unit_result = float(unit_summ) / 10
		return(unit_result)
	elif x == 'См' and y == 'Мм':
		unit_result = float(unit_summ) * 10
		return(unit_result)
	elif x == 'См' and y == 'См':
		unit_result = float(unit_summ) * 1
		return(unit_result)

	elif x == 'Мм' and y == 'Км':
		unit_result = float(unit_summ) / 10**6
		return(unit_result)
	elif x == 'Мм' and y == 'М':
		unit_result = float(unit_summ) / 1000
		return(unit_result)
	elif x == 'Мм' and y == 'Дм':
		unit_result = float(unit_summ) / 100
		return(unit_result)
	elif x == 'Мм' and y == 'См':
		unit_result = float(unit_summ) / 10
		return(unit_result)
	elif x == 'Мм' and y == 'Мм':
		unit_result = float(unit_summ) * 1
		return(unit_result)