console.log(111)

function sendForm(e) {
	const e1 = document.forms.main.param1.value
	const e2 = document.forms.main.param2.value
	const res = document.getElementById('res')
	res.innerHTML = parseInt(e1) + parseInt(e2)
}

const btn = document.forms.main.btn
console.log(btn)
btn.addEventListener('click', sendForm)




<!doctype html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="stylesheet" href="css/style.css" />
		<title>Document</title>
	</head>
	<body>
		<form action="" method="post" name="main" id="main">
			<input type="number" name="param1" id="param1" />
			<input type="number" name="param2" id="param2" />
			<p>
				<button type="button" id="btn" name="btn">Сложить</button>
			</p>
		</form>
		<h1 id="res"></h1>
		<script src="js/test3.js"></script>
	</body>
</html>
